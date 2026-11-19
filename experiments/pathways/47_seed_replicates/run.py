"""
Exp 47: 45's 30 HPrev mature members and twelve arms on 10 new seeds each, and how much of
the spread in each arm's prevented fraction across members is seed noise.

Each member and seed is one set: its twelve arms continue from one simulation stopped at
the start of snapshot_year, which reproduces running each arm from 1985.

    uv run python experiments/pathways/47_seed_replicates/run.py --workers 80
    uv run python experiments/pathways/47_seed_replicates/run.py --plot-only

Rerunning skips the sets already in outputs/results.jsonl.
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

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2]))

from src.settings import SELECTION_YEAR, setting_pars  # noqa: E402
from src.sim import _deep_update  # noqa: E402
from src.snapshots import continue_as, snapshot  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
MEMBERS = json.loads((HERE / "members.json").read_text())
OUTPUTS = HERE / "outputs"
RESULTS = OUTPUTS / "results.jsonl"
FAILURES = OUTPUTS / "failures.jsonl"
FIGURES = HERE / "figures"

STIS = ("ng", "ct", "tv", "syph")
TREATMENT = dict(ng="ng_tx", ct="ct_tx", tv="metronidazole", syph="syph_tx")
# stisim's age bands that together make up ages 15-49
BANDS_15_49 = ("15_20", "20_25", "25_30", "30_35", "35_50")


def sets():
    return [dict(set_id=f"{m['member']}-s{k:02d}", member=m["member"], seed=k, draw=m["draw"],
                 rand_seed=zlib.crc32(f"{CONFIG['seed_prefix']}-{m['member']}-{k}".encode()))
            for m in MEMBERS for k in range(1, CONFIG["n_seeds"] + 1)]


def arm_pars(job, arm):
    overrides = _deep_update(copy.deepcopy(CONFIG["baseline"]), copy.deepcopy(CONFIG["arms"][arm]))
    return setting_pars(job["draw"], CONFIG["country"],
                        sim=dict(n_agents=CONFIG["n_agents"], rand_seed=job["rand_seed"], stop=CONFIG["stop"]),
                        network_summary=dict(year=None), **overrides)


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


def summarize(job, arm, sim, snapshot_s, run_s):
    prev = sim.analyzers.sti_prevalence_15_49.annual()
    years = np.unique(np.floor(sim.t.yearvec).astype(int))
    hiv = hiv_trajectories(sim)
    return dict(sim_id=f"{job['set_id']}-{arm}", set_id=job["set_id"], member=job["member"], seed=job["seed"],
                arm=arm, rand_seed=job["rand_seed"], draw=job["draw"], years=years.tolist(),
                hiv_prevalence_2026=hiv["all"]["prevalence"][int(np.flatnonzero(years == SELECTION_YEAR)[0])],
                hiv=hiv, **sti_trajectories(sim, prev), treated=treatments(sim), prep=prep(sim),
                snapshot_time_s=snapshot_s, run_time_s=run_s)


def run_set(job):
    """Every arm of one member and seed, from one snapshot; a failing set is recorded and the run carries on."""
    try:
        t0 = time.perf_counter()
        arms = {arm: arm_pars(job, arm) for arm in CONFIG["arms"]}
        snap = snapshot(arms.values(), CONFIG["snapshot_year"])
        snapshot_s = time.perf_counter() - t0
        rows = []
        for arm, pars in arms.items():
            t1 = time.perf_counter()
            sim = continue_as(snap, pars).run(verbose=0)
            rows.append(summarize(job, arm, sim, snapshot_s, time.perf_counter() - t1))
        return rows
    except Exception as exc:
        return dict(set_id=job["set_id"], error=f"{type(exc).__name__}: {exc}")


def results():
    if not RESULTS.exists():
        return pd.DataFrame(columns=["sim_id", "set_id", "member", "seed", "arm"])
    return pd.read_json(RESULTS, lines=True)


def run(workers):
    jobs = sets()
    # a set's rows are written together, so any row of a set means the whole set is done
    done = set(results().set_id)
    todo = [j for j in jobs if j["set_id"] not in done]
    print(f"{len(todo)} sets of {len(CONFIG['arms'])} arms to run on {workers} workers "
          f"({len(jobs) - len(todo)} already in results)")
    OUTPUTS.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    with Pool(workers) as pool:
        for i, out in enumerate(pool.imap_unordered(run_set, todo), 1):
            if isinstance(out, dict):
                with FAILURES.open("a") as f:
                    f.write(json.dumps(out) + "\n")
                status = f"{out['set_id']} failed: {out['error']}"
            else:
                with RESULTS.open("a") as f:
                    f.writelines(json.dumps(row) + "\n" for row in out)
                soc = next(r for r in out if r["arm"] == CONFIG["comparator"])
                status = (f"{out[0]['set_id']} prevalence {soc['hiv_prevalence_2026']:.3f}, snapshot "
                          f"{out[0]['snapshot_time_s']:.0f} s, arms {sum(r['run_time_s'] for r in out):.0f} s")
            print(f"{i}/{len(todo)} {status} ({time.perf_counter() - t0:.0f} s elapsed)", flush=True)


def infections(df):
    """(member, seed) x arms: HIV infections at 15-49 over the horizon, in agents."""
    lo, hi = CONFIG["horizon"]
    years = np.asarray(df.years.iloc[0])
    window = (years >= lo) & (years <= hi)
    n = df.hiv.map(lambda t: np.asarray(t["all"]["new_infections"])[window].sum())
    return df.assign(n=n).pivot(index=["member", "seed"], columns="arm", values="n")


def arms_of(totals):
    return [a for a in CONFIG["labels"] if a in totals]


def per_seed(totals):
    """(member, seed) x arms: prevented fraction against the comparator on the same seed."""
    return 1 - totals[arms_of(totals)].div(totals[CONFIG["comparator"]], axis=0)


def per_member(totals):
    """Members x arms, as (prevented fraction of infections summed over seeds, mean infections averted in agents)."""
    sums = totals.groupby(level="member").sum()
    soc = totals[CONFIG["comparator"]]
    averted = -totals[arms_of(totals)].sub(soc, axis=0)
    return 1 - sums[arms_of(totals)].div(sums[CONFIG["comparator"]], axis=0), averted.groupby(level="member").mean()


def components(table):
    """Rows x pathway contributions, in the units of table."""
    return pd.DataFrame({label: sum(c * table[arm] for arm, c in coefs.items())
                         for label, coefs in CONFIG["components"] if set(coefs) <= set(table)})


def seed_noise(seed_table, member_table):
    """Per column, in the units of the tables: standard deviation across seeds within a member (pooled over
    members), across members of the over-seeds values, and across members of seed 1 alone (45's design)."""
    within = np.sqrt(seed_table.groupby(level="member").var().mean())
    return pd.DataFrame(dict(within_member_across_seeds=within,
                             across_members_over_seeds=member_table.std(),
                             across_members_seed_1=seed_table.xs(1, level="seed").std()))


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


def plot_prevalence(df):
    soc = df[df.arm == CONFIG["comparator"]]
    members = sorted(soc.member.unique())
    target, tol = CONFIG["target"], CONFIG["tolerance"]
    fig, ax = plt.subplots(figsize=(7, 2 + 0.22 * len(members)), layout="constrained")
    for i, member in enumerate(members):
        ax.scatter(100 * soc[soc.member == member].hiv_prevalence_2026, np.full((soc.member == member).sum(), i),
                   s=10, color="tab:blue", alpha=0.6)
    ax.axvspan(100 * (target - tol), 100 * (target + tol), color="tab:blue", alpha=0.15)
    ax.set_yticks(range(len(members)), members, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel(f"SOC's HIV prevalence at 15-49 in {SELECTION_YEAR} (%)")
    inside = (soc.hiv_prevalence_2026 - target).abs() <= tol
    ax.set_title(f"{inside.sum()} of {len(soc)} member-seeds inside 45's selection band (shaded)")
    save(fig, 1, "prevalence_2026", f"{CONFIG['cell_label']}, 2026 HIV prevalence of each member on each seed")


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
    save(fig, n, name, f"{CONFIG['cell_label']}, {measure} against SOC over {len(arms)} ensemble members, "
                       f"{CONFIG['n_seeds']} seeds each")


def plot_noise(noise):
    labels = [CONFIG["labels"].get(row, row) for row in noise.index]
    y = np.arange(len(noise))
    fig, ax = plt.subplots(figsize=(11, 2 + 0.36 * len(noise)), layout="constrained")
    for offset, col, label in ((-0.2, "within_member_across_seeds", "Across seeds, within a member"),
                               (0.0, "across_members_seed_1", "Across members, one seed each (45's design)"),
                               (0.2, "across_members_over_seeds", f"Across members, {CONFIG['n_seeds']} seeds pooled")):
        ax.barh(y + offset, noise[col], height=0.2, label=label)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlabel("Standard deviation of the prevented fraction or contribution (percentage points)")
    fig.legend(loc="outside lower center", ncols=3)
    save(fig, 4, "seed_noise", f"{CONFIG['cell_label']}, seed noise against spread across members")


def plot():
    df = results()
    if df.empty:
        return
    FIGURES.mkdir(exist_ok=True)
    plot_prevalence(df)
    lo, hi = CONFIG["horizon"]
    totals = infections(df)
    seed_pf = per_seed(totals)
    pf, averted = per_member(totals)
    noise = pd.concat([seed_noise(100 * seed_pf, 100 * pf),
                       seed_noise(components(100 * seed_pf), components(100 * pf))])
    seed_pf.to_csv(OUTPUTS / "prevented_fractions_per_seed.csv")
    pf.to_csv(OUTPUTS / "prevented_fractions.csv")
    components(pf).to_csv(OUTPUTS / "pathway_components.csv")
    averted.to_csv(OUTPUTS / "infections_averted.csv")
    components(averted).to_csv(OUTPUTS / "pathway_components_averted.csv")
    noise.to_csv(OUTPUTS / "seed_noise.csv")
    for table in (100 * pf, components(100 * pf)):
        print(table.describe().loc[["50%", "25%", "75%", "min", "max"]].T.round(1).to_string())
    print(noise.round(2).to_string())
    plot_arms(2, "prevented", 100 * pf, components(100 * pf),
              f"HIV infections at 15-49 prevented, {lo}-{hi} (% of SOC's, summed over seeds)", "prevented fraction")
    plot_arms(3, "averted", averted, components(averted),
              f"HIV infections at 15-49 averted, {lo}-{hi} (agents, of {CONFIG['n_agents']:,} at the 1985 start, "
              "mean over seeds)", "HIV infections averted")
    plot_noise(noise)


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
