"""
Exp 45: the HPrev mature setting redrawn under Barker 2022's acquisition cofactors with ANC
testing off, then the pathway arms, the ANC arms and the Magic arms on its 30 members,
and each arm's prevented fraction of HIV infections against SOC.

Stage 1 runs SOC to 2041 on every draw; the members are the first ensemble_size draws by
index whose 2026 HIV prevalence at 15-49 lands within tolerance of the target, and their
stage 1 runs are their SOC arm. Stage 2 runs the other arms on each member's seed.

    uv run python experiments/pathways/45_barker_cofactors_anc_arms/run.py --workers 80
    uv run python experiments/pathways/45_barker_cofactors_anc_arms/run.py --plot-only

Rerunning skips the simulations already in outputs/results.jsonl.
"""

import argparse
import copy
import json
import os
import sys
import time
import zlib
from multiprocessing import Pool
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
import yaml
from scipy.stats import qmc

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2]))

from src.settings import SELECTION_YEAR, setting_pars  # noqa: E402
from src.sim import _deep_update, build_sim  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
OUTPUTS = HERE / "outputs"
RESULTS = OUTPUTS / "results.jsonl"
FAILURES = OUTPUTS / "failures.jsonl"
ENSEMBLE = OUTPUTS / "ensemble.json"
FIGURES = HERE / "figures"

STIS = ("ng", "ct", "tv", "syph")
TREATMENT = dict(ng="ng_tx", ct="ct_tx", tv="metronidazole", syph="syph_tx")
# stisim's age bands that together make up ages 15-49
BANDS_15_49 = ("15_20", "20_25", "25_30", "30_35", "35_50")


def seed(*parts):
    return zlib.crc32("-".join((CONFIG["seed_prefix"], *parts)).encode())


def valid(draw):
    lo = CONFIG["min_middle_group"]
    return (1 - draw["prop_f0"] - draw["prop_f2"] >= lo) and (1 - draw["prop_m0"] - draw["prop_m2"] >= lo)


def draws():
    """n_draws Latin hypercube draws, invalid ones replaced, as 43 draws a cell."""
    cell, ranges = CONFIG["cell"], CONFIG["ranges"]
    names = list(ranges)
    lo, hi = np.array(list(ranges.values()), dtype=float).T
    logged = np.isin(names, CONFIG["log_ranges"])
    lo, hi = np.where(logged, np.log(lo), lo), np.where(logged, np.log(hi), hi)
    sampler = qmc.LatinHypercube(d=len(names), seed=seed(cell))
    n, accepted = CONFIG["n_draws"], []
    # each batch is a full hypercube, so the accepted draws stay close to stratified
    while len(accepted) < n:
        scaled = qmc.scale(sampler.random(n), lo, hi)
        scaled[:, logged] = np.exp(scaled[:, logged])
        for row in scaled:
            draw = dict(zip(names, row.tolist()))
            if valid(draw) and len(accepted) < n:
                accepted.append(draw)
    return [dict(member=f"{cell}-{i:04d}", rand_seed=seed(cell, str(i)), draw=draw)
            for i, draw in enumerate(accepted)]


def job(member, arm):
    return dict(sim_id=f"{member['member']}-{arm}", arm=arm, **member)


def annual(sim, monthly, how):
    year = np.floor(sim.t.yearvec).astype(int)
    monthly = np.asarray(monthly, dtype=float)
    return [float(getattr(monthly[year == y], how)()) for y in np.unique(year)]


def sti_trajectories(sim, prev):
    """Annual new infections in agents, incidence per 100 person-years and prevalence at 15-49, by sex."""
    # stisim scales STI counts to the country population; person-years are in agents
    scale = sim.pars.pop_scale
    out = {}
    for d in STIS:
        res = sim.results[d]
        out[d] = {}
        for sex, tag in (("all", ""), ("female", "f_"), ("male", "m_")):
            new = sum(np.asarray(res[f"new_infections_{tag}{band}"]) for band in BANDS_15_49)
            p = prev[(prev.disease == d) & (prev.sex == sex)].sort_values("year")
            new_annual = np.array(annual(sim, new, "sum")) / scale
            out[d][sex] = dict(
                new_infections=new_annual.tolist(),
                incidence=(100 * new_annual / p.person_years.to_numpy()).tolist(),
                prevalence=p.prevalence.tolist(),
            )
    return out


def hiv_trajectories(sim):
    inc = sim.analyzers.hiv_incidence_15_49.annual()
    out = {}
    for sex in ("all", "female", "male"):
        s = inc[inc.sex == sex].sort_values("year")
        out[sex] = dict(new_infections=s.new_infections.astype(float).tolist(), incidence=s.incidence.tolist())
    out["all"]["prevalence"] = annual(sim, sim.results.hiv["prevalence_15_49"], "mean")
    return out


def treatments(sim):
    """Annual STI infections treated, by disease and whether the person had symptoms of it."""
    log = sim.interventions.treatment_log.to_df()
    years = np.unique(np.floor(sim.t.yearvec).astype(int))
    log["year"] = np.floor(log.year.astype(float)).astype(int)
    out = {}
    for d in STIS:
        hit = log[(log.drug == TREATMENT[d]) & log[d].astype(bool)]
        sym = hit[d + "_symptomatic"].astype(bool)
        for label, sub in (("symptomatic", hit[sym]), ("asymptomatic", hit[~sym])):
            out[f"{d}_{label}"] = sub.groupby("year").size().reindex(years, fill_value=0).astype(int).tolist()
    return out


def prep(sim):
    if "prep" not in sim.interventions:
        return None
    res = sim.interventions.prep.results
    return dict(new=annual(sim, res.new_prep, "sum"), on=annual(sim, res.n_on_prep, "mean"))


def simulate(job):
    t0 = time.perf_counter()
    overrides = _deep_update(copy.deepcopy(CONFIG["baseline"]), copy.deepcopy(CONFIG["arms"][job["arm"]]))
    pars = setting_pars(job["draw"], CONFIG["country"],
                        sim=dict(n_agents=CONFIG["n_agents"], rand_seed=job["rand_seed"], stop=CONFIG["stop"]),
                        network_summary=dict(year=None), **overrides)
    sim = build_sim(pars)
    sim.run(verbose=0)
    prev = sim.analyzers.sti_prevalence_15_49.annual()
    years = np.unique(np.floor(sim.t.yearvec).astype(int))
    hiv = hiv_trajectories(sim)
    return dict(sim_id=job["sim_id"], member=job["member"], arm=job["arm"], rand_seed=job["rand_seed"],
                draw=job["draw"], years=years.tolist(),
                hiv_prevalence_2026=hiv["all"]["prevalence"][int(np.flatnonzero(years == SELECTION_YEAR)[0])],
                hiv=hiv, **sti_trajectories(sim, prev),
                treated=treatments(sim), prep=prep(sim), run_time_s=time.perf_counter() - t0)


def run_job(job):
    # a failing simulation is recorded and the run carries on
    try:
        return simulate(job)
    except Exception as exc:
        return dict(sim_id=job["sim_id"], error=f"{type(exc).__name__}: {exc}")


def results():
    if not RESULTS.exists():
        return pd.DataFrame(columns=["sim_id", "member", "arm"])
    return pd.read_json(RESULTS, lines=True)


def run_stage(stage, jobs, workers):
    done = set(results().sim_id)
    todo = [j for j in jobs if j["sim_id"] not in done]
    print(f"stage {stage}: {len(todo)} simulations to run on {workers} workers "
          f"({len(jobs) - len(todo)} already in results)")
    OUTPUTS.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    with Pool(workers) as pool:
        for i, row in enumerate(pool.imap_unordered(run_job, todo), 1):
            path = FAILURES if "error" in row else RESULTS
            with path.open("a") as f:
                f.write(json.dumps(row) + "\n")
            status = (f"failed: {row['error']}" if "error" in row
                      else f"prevalence {row['hiv_prevalence_2026']:.3f} in {row['run_time_s']:.0f} s")
            print(f"{i}/{len(todo)} {row['sim_id']} {status} ({time.perf_counter() - t0:.0f} s elapsed)",
                  flush=True)


def lands(stage_1):
    return (stage_1.hiv_prevalence_2026 - CONFIG["target"]).abs() <= CONFIG["tolerance"]


def stage_1_runs(df):
    return df[df.arm == CONFIG["comparator"]]


def ensemble(df):
    """The first ensemble_size landing draws by index, with their seeds and draws."""
    stage_1 = stage_1_runs(df)
    members = stage_1[lands(stage_1)].sort_values("member").head(CONFIG["ensemble_size"])
    return [dict(member=row.member, rand_seed=int(row.rand_seed), draw=row.draw) for row in members.itertuples()]


def run(workers):
    stage_1 = draws()
    run_stage(1, [job(m, CONFIG["comparator"]) for m in stage_1], workers)
    members = ensemble(results())
    ENSEMBLE.write_text(json.dumps(members, indent=1) + "\n")
    landing = lands(stage_1_runs(results())).sum()
    print(f"{landing} of {len(stage_1)} draws land, {len(members)} members")
    if len(members) < CONFIG["min_members"]:
        print(f"fewer than {CONFIG['min_members']} members: stage 2 not run")
        return
    arms = [a for a in CONFIG["arms"] if a != CONFIG["comparator"]]
    run_stage(2, [job(m, arm) for m in members for arm in arms], workers)


def infections(df, years):
    """Members x arms: HIV infections at 15-49 over the horizon, in agents."""
    lo, hi = CONFIG["horizon"]
    window = (years >= lo) & (years <= hi)
    n = df.hiv.map(lambda t: np.asarray(t["all"]["new_infections"])[window].sum())
    return df.assign(n=n).pivot(index="member", columns="arm", values="n")


def against_comparator(totals):
    """Members x arms, as (prevented fraction, infections averted in agents)."""
    arms = [a for a in CONFIG["labels"] if a in totals]
    soc = totals[CONFIG["comparator"]]
    return 1 - totals[arms].div(soc, axis=0), -totals[arms].sub(soc, axis=0)


def components(table):
    """Members x pathway contributions, in the units of table."""
    return pd.DataFrame({label: sum(c * table[arm] for arm, c in coefs.items())
                         for label, coefs in CONFIG["components"] if set(coefs) <= set(table)})


def boxes(ax, table, rng):
    values = [table[col].dropna() for col in table]
    ax.boxplot(values, positions=range(len(values)), orientation="horizontal", widths=0.6,
               showfliers=False, medianprops=dict(color="tab:blue", lw=1.5))
    for i, v in enumerate(values):
        ax.scatter(v, i + rng.uniform(-0.15, 0.15, len(v)), s=8, color="0.45", alpha=0.6, zorder=3)
    ax.axvline(0, color="k", lw=0.8)
    ax.invert_yaxis()


def save(fig, n, name, title):
    """Number a figure in its title and file name, so a figure seen alone says which one it is."""
    fig.suptitle(f"Fig {n}: {title}")
    fig.savefig(FIGURES / f"fig{n}_{name}.png", dpi=150)
    plt.close(fig)


def plot_landing(df):
    stage_1 = stage_1_runs(df)
    beta = stage_1.draw.map(lambda d: d["hiv_beta_m2f"])
    hit = lands(stage_1)
    target, tol = CONFIG["target"], CONFIG["tolerance"]
    fig, ax = plt.subplots(figsize=(7, 4.5), layout="constrained")
    ax.scatter(beta[~hit], 100 * stage_1.hiv_prevalence_2026[~hit], s=10, color="0.6")
    ax.scatter(beta[hit], 100 * stage_1.hiv_prevalence_2026[hit], s=14, color="tab:blue")
    ax.axhspan(100 * (target - tol), 100 * (target + tol), color="tab:blue", alpha=0.15)
    ax.set_xlabel("HIV beta_m2f")
    ax.set_ylabel(f"HIV prevalence at 15-49 in {SELECTION_YEAR} (%)")
    ax.set_title(f"{hit.sum()} of {len(stage_1)} draws land, landing draws in blue")
    save(fig, 1, "prevalence_2026", f"{CONFIG['cell_label']}, 2026 HIV prevalence against HIV beta_m2f")


def plot_arms(n, name, arms, comp, xlabel, measure):
    rng = np.random.default_rng(0)
    rows = len(arms.columns) + len(comp.columns)
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(11, 2 + 0.36 * rows), sharex=True, layout="constrained",
                                      gridspec_kw=dict(height_ratios=[len(arms.columns), len(comp.columns)]))
    boxes(top, arms, rng)
    top.set_yticks(range(len(arms.columns)), [CONFIG["labels"][a] for a in arms])
    top.set_title("Each arm against SOC")
    boxes(bottom, comp, rng)
    bottom.set_yticks(range(len(comp.columns)), comp.columns)
    bottom.set_title("Pathway contributions: differences between the arms above")
    bottom.set_xlabel(xlabel)
    save(fig, n, name, f"{CONFIG['cell_label']}, {measure} against SOC over {len(arms)} ensemble members")


def plot():
    df = results()
    if df.empty:
        return
    FIGURES.mkdir(exist_ok=True)
    plot_landing(df)
    members = {m["member"] for m in ensemble(df)}
    df = df[df.member.isin(members)]
    if set(df.arm) == {CONFIG["comparator"]}:
        return
    lo, hi = CONFIG["horizon"]
    pf, averted = against_comparator(infections(df, np.asarray(df.years.iloc[0])))
    pf.to_csv(OUTPUTS / "prevented_fractions.csv")
    components(pf).to_csv(OUTPUTS / "pathway_components.csv")
    averted.to_csv(OUTPUTS / "infections_averted.csv")
    components(averted).to_csv(OUTPUTS / "pathway_components_averted.csv")
    for table in (100 * pf, components(100 * pf)):
        print(table.describe().loc[["50%", "25%", "75%", "min", "max"]].T.round(1).to_string())
    plot_arms(2, "prevented", 100 * pf, components(100 * pf),
              f"HIV infections at 15-49 prevented, {lo}-{hi} (% of SOC's)", "prevented fraction")
    plot_arms(3, "averted", averted, components(averted),
              f"HIV infections at 15-49 averted, {lo}-{hi} (agents, of {CONFIG['n_agents']:,} at the 1985 start)",
              "HIV infections averted")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=os.cpu_count())
    parser.add_argument("--plot-only", action="store_true")
    args = parser.parse_args()
    if not args.plot_only:
        run(args.workers)
    plot()


if __name__ == "__main__":
    main()
