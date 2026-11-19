"""
Exp 43: one batch per setting over 40.1's ranges, the high-incidence cells with HIV and
its programmes delayed by a drawn hiv_delay, and each cell's ensemble taken as its first
landing draws by index, all intervened in 2027.

    uv run python experiments/settings/43_delayed_epidemic_ensembles/run.py --workers 80
    uv run python experiments/settings/43_delayed_epidemic_ensembles/run.py --plot-only

Rerunning skips the simulations already in the results and runs the rest.
"""

import argparse
import json
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

from src.settings import PARAMETERS, SELECTION_YEAR, setting_pars, summarize  # noqa: E402
from src.sim import build_sim  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
OUTPUTS = HERE / "outputs"
RESULTS = OUTPUTS / "results.jsonl"
FAILURES = OUTPUTS / "failures.jsonl"
ENSEMBLES = HERE / "ensembles.json"
FIGURES = HERE / "figures"


def stage_seed(*parts):
    # the experiment number keeps these draws apart from 40.x's, which share draw names
    return zlib.crc32("-".join(("43", *parts)).encode())


def valid(draw):
    lo = CONFIG["min_middle_group"]
    return (1 - draw["prop_f0"] - draw["prop_f2"] >= lo) and (1 - draw["prop_m0"] - draw["prop_m2"] >= lo)


def draws(cell, spec):
    """spec['n'] Latin hypercube draws for one cell, invalid ones replaced."""
    ranges = {**CONFIG["ranges"], **CONFIG["country_ranges"][spec["country"]]}
    if "hiv_delay" in spec:
        ranges["hiv_delay"] = spec["hiv_delay"]
    names = list(ranges)
    lo, hi = np.array(list(ranges.values()), dtype=float).T
    logged = np.isin(names, CONFIG.get("log_ranges", []))
    lo, hi = np.where(logged, np.log(lo), lo), np.where(logged, np.log(hi), hi)
    sampler = qmc.LatinHypercube(d=len(names), seed=stage_seed(cell))
    n, kept = spec["n"], []
    # each batch is a full hypercube, so the kept draws stay close to stratified
    while len(kept) < n:
        scaled = qmc.scale(sampler.random(n), lo, hi)
        scaled[:, logged] = np.exp(scaled[:, logged])
        for row in scaled:
            draw = dict(zip(names, row.tolist()))
            if valid(draw) and len(kept) < n:
                kept.append(draw)
    return [
        dict(sim_id=f"{cell}-{i:04d}", cell=cell, country=spec["country"],
             rand_seed=stage_seed(cell, str(i)), draw=draw)
        for i, draw in enumerate(kept)
    ]


def peak_ratio(incidence):
    """Selection-year incidence as a proportion of the curve's peak."""
    incidence = np.asarray(incidence)
    return float(incidence[-1] / incidence.max()) if incidence.max() > 0 else 0.0


def lands(df):
    target = df.country.map({c: s["target"] for c, s in CONFIG["countries"].items()})
    return (df.hiv_prevalence_2026 - target).abs() <= CONFIG["tolerance"]


def run_job(job):
    # a failing simulation is recorded and the batch carries on
    try:
        return simulate(job)
    except Exception as exc:
        return dict(sim_id=job["sim_id"], error=f"{type(exc).__name__}: {exc}")


def simulate(job):
    t0 = time.perf_counter()
    pars = setting_pars(job["draw"], job["country"],
                        sim=dict(n_agents=CONFIG["n_agents"], rand_seed=job["rand_seed"]),
                        network_summary=dict(year=None))
    sim = build_sim(pars)
    sim.run(verbose=0)
    out = summarize(sim)
    out.pop("network")
    return dict(sim_id=job["sim_id"], cell=job["cell"], country=job["country"],
                rand_seed=job["rand_seed"], **job["draw"], **out, run_time_s=time.perf_counter() - t0)


def done_ids():
    if not RESULTS.exists():
        return set()
    return {json.loads(line)["sim_id"] for line in RESULTS.read_text().splitlines() if line}


def run(workers):
    jobs = [job for cell, spec in CONFIG["cells"].items() for job in draws(cell, spec)]
    done = done_ids()
    jobs = [job for job in jobs if job["sim_id"] not in done]
    print(f"{len(jobs)} simulations to run on {workers} workers ({len(done)} already in results)")
    OUTPUTS.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    with Pool(workers) as pool:
        for i, row in enumerate(pool.imap_unordered(run_job, jobs), 1):
            if "error" in row:
                with FAILURES.open("a") as f:
                    f.write(json.dumps(row) + "\n")
                print(f"{i}/{len(jobs)} {row['sim_id']} failed: {row['error']}", flush=True)
                continue
            with RESULTS.open("a") as f:
                f.write(json.dumps(row) + "\n")
            print(f"{i}/{len(jobs)} {row['sim_id']} prevalence {row['hiv_prevalence_2026']:.3f} "
                  f"in {row['run_time_s']:.0f} s ({time.perf_counter() - t0:.0f} s elapsed)", flush=True)


def ensembles(df):
    """Each cell's first ensemble_size landing draws by draw index, as sim_pars-ready draws."""
    members = (df[lands(df)].sort_values("sim_id").groupby("cell", sort=False)
               .head(CONFIG["ensemble_size"]))
    return {
        cell: [dict(sim_id=row.sim_id, country=row.country, intv_year=CONFIG["intv_year"],
                    draw={name: float(row[name]) for name in PARAMETERS if name in row and pd.notna(row[name])})
               for _, row in sub.iterrows()]
        for cell, sub in members.groupby("cell", sort=False)
    }


def save(fig, n, name, title):
    """Number a figure in its title and file name, so a figure seen alone says which one it is."""
    fig.suptitle(f"Fig {n}: {title}")
    fig.savefig(FIGURES / f"fig{n}_{name}.png", dpi=150)
    plt.close(fig)


def plot_prevalence(df):
    cells, tol = CONFIG["cells"], CONFIG["tolerance"]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex="col", layout="constrained")
    for ax, (cell, spec) in zip(axes.T.flat, cells.items()):
        sub = df[df.cell == cell]
        hit = lands(sub)
        target = CONFIG["countries"][spec["country"]]["target"]
        ax.scatter(sub.hiv_beta_m2f[~hit], 100 * sub.hiv_prevalence_2026[~hit], s=10, color="0.6")
        ax.scatter(sub.hiv_beta_m2f[hit], 100 * sub.hiv_prevalence_2026[hit], s=14, color="tab:blue")
        ax.axhspan(100 * (target - tol), 100 * (target + tol), color="tab:blue", alpha=0.15)
        ax.set_title(f"{cell}: {hit.sum()} landing of {len(sub)}")
        ax.set_ylabel(f"HIV prevalence at 15-49 in {SELECTION_YEAR} (%)")
    for ax in axes[-1]:
        ax.set_xlabel("HIV beta_m2f")
    save(fig, 1, "prevalence_2026", "2026 HIV prevalence against HIV beta_m2f per cell, landing draws in blue")


def plot_incidence(df, ens):
    cells = CONFIG["cells"]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True, layout="constrained")
    for ax, cell in zip(axes.T.flat, cells):
        ids = {m["sim_id"] for m in ens.get(cell, [])}
        sub = df[df.sim_id.isin(ids)]
        if sub.empty:
            ax.set_title(f"{cell}: no ensemble members")
            continue
        curves = np.stack(sub.hiv_incidence_all.map(np.asarray))
        years = np.asarray(sub.years.iloc[0])
        lo, mid, hi = np.percentile(curves, [10, 50, 90], axis=0)
        ax.fill_between(years, lo, hi, color="tab:blue", alpha=0.25, label="10th-90th percentile")
        ax.plot(years, mid, color="tab:blue", label="median")
        ratio = np.median([peak_ratio(c) for c in curves])
        ax.set_title(f"{cell}: {len(sub)} members, median 2026/peak {ratio:.2f}")
        ax.set_ylabel("HIV incidence at 15-49 per 100 PY")
    axes[0, 0].legend(fontsize=8)
    for ax in axes[-1]:
        ax.set_xlabel("Year")
    save(fig, 2, "ensemble_incidence", "HIV incidence at 15-49 of each cell's ensemble members")


def plot():
    if not RESULTS.exists():
        return
    FIGURES.mkdir(exist_ok=True)
    df = pd.read_json(RESULTS, lines=True)
    ens = ensembles(df)
    plot_prevalence(df)
    plot_incidence(df, ens)
    ENSEMBLES.write_text(json.dumps(ens, indent=1) + "\n")
    for cell in CONFIG["cells"]:
        sub = df[df.cell == cell]
        print(f"{cell}: {lands(sub).sum()} landing of {len(sub)}, {len(ens.get(cell, []))} in the ensemble")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--plot-only", action="store_true")
    args = parser.parse_args()
    if not args.plot_only:
        run(args.workers)
    plot()


if __name__ == "__main__":
    main()
