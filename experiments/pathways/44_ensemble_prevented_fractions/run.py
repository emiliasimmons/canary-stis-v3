"""
Exp 44: the eight pathway arms on every member of the four settings' ensembles, and each
setting's prevented fractions of HIV infections against SOC.

    uv run python experiments/pathways/44_ensemble_prevented_fractions/run.py --workers 80
    uv run python experiments/pathways/44_ensemble_prevented_fractions/run.py --plot-only

Rerunning skips the simulations already in outputs/results.jsonl.
"""

import argparse
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

from src.settings import setting_pars  # noqa: E402
from src.sim import build_sim  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
OUTPUTS = HERE / "outputs"
RESULTS = OUTPUTS / "results.jsonl"
FAILURES = OUTPUTS / "failures.jsonl"
FIGURES = HERE / "figures"

STIS = ("ng", "ct", "tv", "syph")
TREATMENT = dict(ng="ng_tx", ct="ct_tx", tv="metronidazole", syph="syph_tx")
# stisim's age bands that together make up ages 15-49
BANDS_15_49 = ("15_20", "20_25", "25_30", "30_35", "35_50")


def member_seed(sim_id):
    cell, index = sim_id.rsplit("-", 1)
    return zlib.crc32(f"{CONFIG['seed_prefix']}-{cell}-{int(index)}".encode())


def jobs():
    ensembles = json.loads((HERE / CONFIG["ensembles"]).resolve().read_text())
    out = []
    for cell in CONFIG["cells"]:
        for member in ensembles[cell]:
            for arm in CONFIG["arms"]:
                out.append(dict(sim_id=f"{member['sim_id']}-{arm}", member=member["sim_id"], cell=cell,
                                country=member["country"], arm=arm, rand_seed=member_seed(member["sim_id"]),
                                draw=member["draw"]))
    return out


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
    pars = setting_pars(job["draw"], job["country"],
                        sim=dict(n_agents=CONFIG["n_agents"], rand_seed=job["rand_seed"], stop=CONFIG["stop"]),
                        network_summary=dict(year=None), **CONFIG["arms"][job["arm"]])
    sim = build_sim(pars)
    sim.run(verbose=0)
    prev = sim.analyzers.sti_prevalence_15_49.annual()
    return dict(sim_id=job["sim_id"], member=job["member"], cell=job["cell"], arm=job["arm"],
                rand_seed=job["rand_seed"], years=np.unique(np.floor(sim.t.yearvec).astype(int)).tolist(),
                hiv=hiv_trajectories(sim), **sti_trajectories(sim, prev),
                treated=treatments(sim), prep=prep(sim), run_time_s=time.perf_counter() - t0)


def run_job(job):
    # a failing simulation is recorded and the run carries on
    try:
        return simulate(job)
    except Exception as exc:
        return dict(sim_id=job["sim_id"], error=f"{type(exc).__name__}: {exc}")


def run(workers):
    done = set()
    if RESULTS.exists():
        done = {json.loads(line)["sim_id"] for line in RESULTS.read_text().splitlines() if line}
    todo = [job for job in jobs() if job["sim_id"] not in done]
    print(f"{len(todo)} simulations to run on {workers} workers ({len(done)} already in results)")
    OUTPUTS.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    with Pool(workers) as pool:
        for i, row in enumerate(pool.imap_unordered(run_job, todo), 1):
            path = FAILURES if "error" in row else RESULTS
            with path.open("a") as f:
                f.write(json.dumps(row) + "\n")
            status = f"failed: {row['error']}" if "error" in row else f"in {row['run_time_s']:.0f} s"
            print(f"{i}/{len(todo)} {row['sim_id']} {status} ({time.perf_counter() - t0:.0f} s elapsed)", flush=True)


def infections(df, years):
    """Members x arms: HIV infections at 15-49 over the horizon, in agents."""
    lo, hi = CONFIG["horizon"]
    window = (years >= lo) & (years <= hi)
    n = df.hiv.map(lambda t: np.asarray(t["all"]["new_infections"])[window].sum())
    return df.assign(n=n).pivot(index="member", columns="arm", values="n")


def against_comparator(totals):
    """Members x arms, as (prevented fraction, infections averted in agents)."""
    # arms still to run in a later stage are left out
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


def plot_cell(n, name, cell, arms, comp, xlim, xlabel, measure):
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
    bottom.set_xlim(xlim)
    fig.suptitle(f"Fig {n}: {CONFIG['cells'][cell]}, {measure} against SOC over {len(arms)} ensemble members")
    fig.savefig(FIGURES / f"fig{n}_{name}_{cell}.png", dpi=150)
    plt.close(fig)


def shared_xlim(tables):
    """One x range covering every table, so the settings' figures read on the same axis."""
    lo = min(t.min().min() for t in tables)
    hi = max(t.max().max() for t in tables)
    pad = 0.03 * (hi - lo)
    return lo - pad, hi + pad


def plot():
    FIGURES.mkdir(exist_ok=True)
    df = pd.read_json(RESULTS, lines=True)
    years = np.asarray(df.years.iloc[0])
    lo, hi = CONFIG["horizon"]
    cells = [c for c in CONFIG["cells"] if (df.cell == c).any()]
    tables = {}
    for cell in cells:
        pf, averted = against_comparator(infections(df[df.cell == cell], years))
        tables[cell] = dict(pf=(100 * pf, components(100 * pf)), averted=(averted, components(averted)))
        pf.to_csv(OUTPUTS / f"prevented_fractions_{cell}.csv")
        components(pf).to_csv(OUTPUTS / f"pathway_components_{cell}.csv")
        averted.to_csv(OUTPUTS / f"infections_averted_{cell}.csv")
        components(averted).to_csv(OUTPUTS / f"pathway_components_averted_{cell}.csv")
        print(f"\n{CONFIG['cells'][cell]}")
        for table in tables[cell]["pf"]:
            print(table.describe().loc[["50%", "25%", "75%", "min", "max"]].T.round(1).to_string())
    figures = [
        ("pf", 1, "prevented", f"HIV infections at 15-49 prevented, {lo}-{hi} (% of SOC's)",
         "prevented fraction"),
        ("averted", 1 + len(CONFIG["cells"]), "averted",
         f"HIV infections at 15-49 averted, {lo}-{hi} (agents, of {CONFIG['n_agents']:,} at the 1985 start)",
         "HIV infections averted"),
    ]
    for key, first, name, xlabel, measure in figures:
        xlim = shared_xlim([t for cell in cells for t in tables[cell][key]])
        for n, cell in enumerate(CONFIG["cells"], first):
            if cell in tables:
                plot_cell(n, name, cell, *tables[cell][key], xlim, xlabel, measure)


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
