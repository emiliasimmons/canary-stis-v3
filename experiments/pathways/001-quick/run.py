"""
Exp 001: the eight pathway arms on the six Zimbabwe draws closest to 15% HIV
prevalence, with annual HIV and STI trajectories over the whole run.

    uv run python experiments/pathways/001-quick/run.py
    uv run python experiments/pathways/001-quick/run.py --plot-only

Rerunning skips the simulations already in outputs/results.jsonl.
"""

import argparse
import json
import os
import sys
import time
from multiprocessing import Pool
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
import yaml

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2]))

from src.settings import PARAMETERS, setting_pars  # noqa: E402
from src.sim import build_sim  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
OUTPUTS = HERE / "outputs"
RESULTS = OUTPUTS / "results.jsonl"
FAILURES = OUTPUTS / "failures.jsonl"
FIGURES = HERE / "figures"

STIS = ("ng", "ct", "tv", "syph")
NAMES = dict(hiv="HIV", ng="Gonorrhoea", ct="Chlamydia", tv="Trichomoniasis", syph="Syphilis")
TREATMENT = dict(ng="ng_tx", ct="ct_tx", tv="metronidazole", syph="syph_tx")
# stisim's age bands that together make up ages 15-49
BANDS_15_49 = ("15_20", "20_25", "25_30", "30_35", "35_50")


def selected_draws():
    df = pd.read_json((HERE / CONFIG["draws"]["source"]).resolve(), lines=True)
    df = df[df.country == CONFIG["country"]]
    gap = (df.hiv_prevalence_2026 - CONFIG["draws"]["target"]).abs()
    return df.loc[gap.sort_values().index[:CONFIG["draws"]["n"]]]


def jobs():
    out = []
    for _, row in selected_draws().iterrows():
        draw = {name: row[name] for name in PARAMETERS if name in row and pd.notna(row[name])}
        for arm in CONFIG["arms"]:
            out.append(dict(sim_id=f"{row.draw_id}-{arm}", draw_id=row.draw_id, arm=arm,
                            rand_seed=int(row.rand_seed), draw=draw))
    return out


def annual(sim, monthly, how):
    year = np.floor(sim.t.yearvec).astype(int)
    years = np.unique(year)
    monthly = np.asarray(monthly, dtype=float)
    return [float(getattr(monthly[year == y], how)()) for y in years]


def sti_trajectories(sim, prev):
    """Annual new infections, incidence per 100 person-years and prevalence at 15-49, by sex.

    The incidence denominator is all person-time at 15-49, infected or not, the one
    STIPrevalence1549 records.
    """
    out = {}
    for d in STIS:
        res = sim.results[d]
        out[d] = {}
        for sex, tag in (("all", ""), ("female", "f_"), ("male", "m_")):
            new = sum(np.asarray(res[f"new_infections_{tag}{band}"]) for band in BANDS_15_49)
            p = prev[(prev.disease == d) & (prev.sex == sex)].sort_values("year")
            new_annual = np.array(annual(sim, new, "sum"))
            out[d][sex] = dict(
                new_infections=new_annual.tolist(),
                incidence=(100 * new_annual / p.person_years.to_numpy()).tolist(),
                prevalence=p.prevalence.tolist(),
            )
    return out


def hiv_trajectories(sim):
    inc = sim.analyzers.hiv_incidence_15_49.annual()
    out = {}
    for sex, key in (("all", "prevalence_15_49"), ("female", None), ("male", None)):
        s = inc[inc.sex == sex].sort_values("year")
        out[sex] = dict(new_infections=s.new_infections.astype(float).tolist(), incidence=s.incidence.tolist())
        if key is not None:
            out[sex]["prevalence"] = annual(sim, sim.results.hiv[key], "mean")
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
    overrides = dict(CONFIG["arms"][job["arm"]])
    pars = setting_pars(job["draw"], CONFIG["country"],
                        sim=dict(n_agents=CONFIG["n_agents"], rand_seed=job["rand_seed"], stop=CONFIG["stop"]),
                        network_summary=dict(year=None), **overrides)
    sim = build_sim(pars)
    sim.run(verbose=0)
    prev = sim.analyzers.sti_prevalence_15_49.annual()
    return dict(sim_id=job["sim_id"], draw_id=job["draw_id"], arm=job["arm"], rand_seed=job["rand_seed"],
                years=np.unique(np.floor(sim.t.yearvec).astype(int)).tolist(),
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


def save(fig, n, name, title):
    """Number a figure in its title and file name, so a figure seen alone says which one it is."""
    fig.suptitle(f"Fig {n}: {title}")
    fig.savefig(FIGURES / f"fig{n}_{name}.png", dpi=150)
    plt.close(fig)


def series(df, disease, measure, sex="all"):
    """Draws x years array of one trajectory, per arm."""
    return {arm: np.stack(sub[disease].map(lambda t: np.asarray(t[sex][measure], dtype=float)))
            for arm, sub in df.groupby("arm")}


def plot_trajectories(df, years, n, name, measure, ylabel, scale):
    diseases = ("hiv", *STIS)
    # the stop year holds a single month
    whole = years < CONFIG["stop"]
    fig, axes = plt.subplots(1, len(diseases), figsize=(20, 4), layout="constrained")
    for ax, d in zip(axes, diseases):
        for arm, values in sorted(series(df, d, measure).items()):
            ax.plot(years[whole], scale * values.mean(axis=0)[whole], lw=1.2, label=arm)
        ax.axvline(CONFIG["intv_year"], color="k", lw=0.8, ls=":")
        ax.set_title(NAMES[d])
        ax.set_xlabel("Year")
    axes[0].set_ylabel(ylabel)
    axes[-1].legend(fontsize=7, loc="upper right")
    save(fig, n, name, f"{ylabel} at 15-49 by arm, mean of {df.draw_id.nunique()} draws")


def prevented_fractions(df, years):
    """Per contrast and draw: 1 - HIV infections at 15-49 in the arm / in its comparator, over the horizon."""
    lo, hi = CONFIG["horizon"]
    window = (years >= lo) & (years <= hi)
    infections = df.hiv.map(lambda t: np.asarray(t["all"]["new_infections"])[window].sum())
    totals = df.assign(n=infections).pivot(index="draw_id", columns="arm", values="n")
    return pd.concat([
        pd.DataFrame(dict(contrast=label, draw_id=totals.index,
                          prevented_fraction=1 - totals[arm] / totals[comp]))
        for arm, comp, label in CONFIG["contrasts"]
    ], ignore_index=True)


def plot_prevented(pf):
    labels = [c[2] for c in CONFIG["contrasts"]]
    lo, hi = CONFIG["horizon"]
    fig, ax = plt.subplots(figsize=(7, 4.5), layout="constrained")
    for i, label in enumerate(labels):
        values = 100 * pf[pf.contrast == label].prevented_fraction
        ax.scatter(values, np.full(len(values), i), s=14, color="0.5")
        ax.scatter(values.mean(), i, marker="|", s=300, color="tab:blue")
    ax.axvline(0, color="k", lw=0.8)
    ax.set_yticks(range(len(labels)), labels)
    ax.invert_yaxis()
    ax.set_xlabel(f"HIV infections at 15-49 prevented, {lo}-{hi} (% of comparator)")
    save(fig, 4, "prevented_fractions", "Prevented fraction per draw (dots) and mean (bar)")


def plot():
    FIGURES.mkdir(exist_ok=True)
    df = pd.read_json(RESULTS, lines=True)
    years = np.asarray(df.years.iloc[0])
    plot_trajectories(df, years, 1, "prevalence", "prevalence", "Prevalence (%)", 100)
    plot_trajectories(df, years, 2, "incidence", "incidence", "Incidence per 100 PY", 1)
    plot_trajectories(df, years, 3, "new_infections", "new_infections", "New infections per year", 1)
    pf = prevented_fractions(df, years)
    plot_prevented(pf)
    pf.to_csv(OUTPUTS / "prevented_fractions.csv", index=False)
    print(pf.groupby("contrast", sort=False).prevented_fraction.describe()[["mean", "min", "max"]].to_string())


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
