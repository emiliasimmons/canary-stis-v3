"""
Exp 40.1: an Eswatini batch over 38.3's ranges with a higher HIV beta_m2f range,
then seed replicates of each country's landing draws closest to its target, and
the ensembles kept from them, each draw with a mature and an expanding cell.

    uv run python experiments/settings/40.1_peak_year_ensembles/run.py --stage batch
    uv run python experiments/settings/40.1_peak_year_ensembles/run.py --stage replicates
    uv run python experiments/settings/40.1_peak_year_ensembles/run.py --plot-only

Rerunning a stage skips the simulations already in its results and runs the rest.
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

from src.settings import PARAMETERS, setting_pars, summarize  # noqa: E402
from src.sim import build_sim  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
OUTPUTS = HERE / "outputs"
RESULTS = dict(batch=OUTPUTS / "results.jsonl", replicates=OUTPUTS / "replicates.jsonl")
FAILURES = OUTPUTS / "failures.jsonl"
ENSEMBLES = HERE / "ensembles.json"
FIGURES = HERE / "figures"


def stage_seed(*parts):
    return zlib.crc32("-".join(parts).encode())


def valid(draw):
    lo = CONFIG["min_middle_group"]
    return (1 - draw["prop_f0"] - draw["prop_f2"] >= lo) and (1 - draw["prop_m0"] - draw["prop_m2"] >= lo)


def draws(stage, country, n):
    """n Latin hypercube draws for one stage and country, invalid ones replaced."""
    names = list(CONFIG["ranges"])
    lo, hi = np.array(list(CONFIG["ranges"].values())).T
    logged = np.isin(names, CONFIG.get("log_ranges", []))
    lo, hi = np.where(logged, np.log(lo), lo), np.where(logged, np.log(hi), hi)
    sampler = qmc.LatinHypercube(d=len(names), seed=stage_seed(stage, country))
    kept = []
    # each batch is a full hypercube, so the kept draws stay close to stratified
    while len(kept) < n:
        scaled = qmc.scale(sampler.random(n), lo, hi)
        scaled[:, logged] = np.exp(scaled[:, logged])
        for row in scaled:
            draw = dict(zip(names, row.tolist()))
            if valid(draw) and len(kept) < n:
                kept.append(draw)
    return [
        dict(sim_id=f"{stage}-{country}-{i:04d}", draw_id=f"{stage}-{country}-{i:04d}",
             country=country, rand_seed=stage_seed(stage, country, str(i)), draw=draw)
        for i, draw in enumerate(kept)
    ]


def landing(df, country):
    spec = CONFIG["countries"][country]
    sub = df[df.country == country]
    return sub[(sub.hiv_prevalence_2026 - spec["target"]).abs() <= CONFIG["tolerance"]]


def candidates(country):
    """The country's landing draws closest to its target, from its source in config.yaml."""
    source = CONFIG["candidates"][country]
    path = RESULTS["batch"] if source == "batch" else (HERE / source).resolve()
    df = landing(pd.read_json(path, lines=True), country)
    gap = (df.hiv_prevalence_2026 - CONFIG["countries"][country]["target"]).abs()
    return df.loc[gap.sort_values().index[:CONFIG["replicates"]["draws_per_country"]]]


def replicate_jobs():
    jobs = []
    for country in CONFIG["countries"]:
        for _, row in candidates(country).iterrows():
            draw = {name: row[name] for name in PARAMETERS if name in row and pd.notna(row[name])}
            for k in range(CONFIG["replicates"]["seeds"]):
                jobs.append(dict(sim_id=f"{row.draw_id}-r{k:02d}", draw_id=row.draw_id, country=country,
                                 rand_seed=stage_seed("replicates", row.draw_id, str(k)), draw=draw))
    return jobs


def run_job(job):
    # a failing simulation is recorded and the stage carries on
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
    return dict(sim_id=job["sim_id"], draw_id=job["draw_id"], country=job["country"],
                rand_seed=job["rand_seed"], **job["draw"], **out, run_time_s=time.perf_counter() - t0)


def done_ids(path):
    if not path.exists():
        return set()
    return {json.loads(line)["sim_id"] for line in path.read_text().splitlines() if line}


def run(stage, workers):
    if stage == "batch":
        jobs = [job for country, n in CONFIG["stages"]["batch"].items() for job in draws(stage, country, n)]
    else:
        jobs = replicate_jobs()
    path = RESULTS[stage]
    done = done_ids(path)
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
            with path.open("a") as f:
                f.write(json.dumps(row) + "\n")
            print(f"{i}/{len(jobs)} {row['sim_id']} prevalence {row['hiv_prevalence_2026']:.3f} "
                  f"in {row['run_time_s']:.0f} s ({time.perf_counter() - t0:.0f} s elapsed)", flush=True)


def ensembles(reps):
    """Per draw: replicate-averaged 2026 prevalence and its seed spread, and the peak year of
    the replicate-averaged incidence curve. Kept draws carry both cells' intv_year."""
    rows = []
    for draw_id, sub in reps.groupby("draw_id"):
        country = sub.country.iloc[0]
        years = np.asarray(sub.years.iloc[0])
        mean_inc = np.mean(np.stack(sub.hiv_incidence_all.map(np.asarray)), axis=0)
        prev = sub.hiv_prevalence_2026
        peak = int(years[np.argmax(mean_inc)])
        rows.append(dict(
            draw_id=draw_id, country=country, n_seeds=len(sub),
            prevalence_2026_mean=float(prev.mean()), prevalence_2026_sd=float(prev.std()),
            peak_year=peak,
            kept=bool(abs(prev.mean() - CONFIG["countries"][country]["target"]) <= CONFIG["tolerance"]),
            draw={name: float(sub[name].iloc[0]) for name in PARAMETERS if name in sub},
            intv_year=dict(mature=CONFIG["mature_intv_year"], expanding=peak),
            years=years.tolist(), incidence_mean=mean_inc.tolist(),
        ))
    return pd.DataFrame(rows)


def save(fig, n, name, title):
    """Number a figure in its title and file name, so a figure seen alone says which one it is."""
    fig.suptitle(f"Fig {n}: {title}")
    fig.savefig(FIGURES / f"fig{n}_{name}.png", dpi=150)
    plt.close(fig)


def plot_batch(df):
    spec, tol = CONFIG["countries"]["eswatini"], CONFIG["tolerance"]
    lands = (df.hiv_prevalence_2026 - spec["target"]).abs() <= tol
    fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
    ax.scatter(df.hiv_beta_m2f[~lands], df.hiv_prevalence_2026[~lands] * 100, s=12, color="0.6")
    ax.scatter(df.hiv_beta_m2f[lands], df.hiv_prevalence_2026[lands] * 100, s=16, color="tab:blue")
    ax.axhspan(100 * (spec["target"] - tol), 100 * (spec["target"] + tol), color="tab:blue", alpha=0.15)
    ax.set_xlabel("HIV beta_m2f")
    ax.set_ylabel("HIV prevalence at 15-49 in 2026 (%)")
    ax.set_title(f"{lands.sum()} landing of {len(df)} draws")
    save(fig, 1, "eswatini_batch", "Eswatini batch, 2026 HIV prevalence against HIV beta_m2f, landing draws in blue")


def plot_replicates(reps, ens):
    countries, tol = CONFIG["countries"], CONFIG["tolerance"]
    fig, axes = plt.subplots(1, len(countries), figsize=(11, 4), sharey=True, layout="constrained")
    for ax, (country, spec) in zip(axes, countries.items()):
        sub = ens[ens.country == country].sort_values("prevalence_2026_mean").reset_index(drop=True)
        for i, row in sub.iterrows():
            prev = reps[reps.draw_id == row.draw_id].hiv_prevalence_2026 * 100
            color = "tab:blue" if row.kept else "0.5"
            ax.scatter(np.full(len(prev), i), prev, s=10, color=color, alpha=0.6)
            ax.scatter(i, row.prevalence_2026_mean * 100, marker="_", s=300, color=color)
        ax.axhspan(100 * (spec["target"] - tol), 100 * (spec["target"] + tol), color="tab:blue", alpha=0.15)
        ax.set_xticks(range(len(sub)), sub.draw_id, rotation=45, ha="right", fontsize=8)
        ax.set_title(f"{country.title()}: {sub.kept.sum()} kept of {len(sub)}")
    axes[0].set_ylabel("HIV prevalence at 15-49 in 2026 (%)")
    save(fig, 2, "replicate_prevalence", "2026 HIV prevalence per seed (dots) and mean (bar), kept draws in blue")


def plot_peaks(ens):
    countries = CONFIG["countries"]
    fig, axes = plt.subplots(1, len(countries), figsize=(11, 4), sharey=True, layout="constrained")
    for ax, country in zip(axes, countries):
        for _, row in ens[(ens.country == country) & ens.kept].iterrows():
            line, = ax.plot(row.years, np.asarray(row.incidence_mean), lw=1.2)
            ax.axvline(row.peak_year, color=line.get_color(), ls=":", lw=1)
        ax.axvline(CONFIG["mature_intv_year"], color="k", lw=1)
        ax.set_title(f"{country.title()}: kept draws, peak year dotted, 2027 solid")
        ax.set_xlabel("Year")
    axes[0].set_ylabel("HIV incidence at 15-49 per 100 PY, seed mean")
    save(fig, 3, "peak_years", "Seed-averaged HIV incidence at 15-49 of kept draws, with each draw's intervention years")


def plot():
    FIGURES.mkdir(exist_ok=True)
    if RESULTS["batch"].exists():
        plot_batch(pd.read_json(RESULTS["batch"], lines=True))
    if RESULTS["replicates"].exists():
        reps = pd.read_json(RESULTS["replicates"], lines=True)
        ens = ensembles(reps)
        plot_replicates(reps, ens)
        plot_peaks(ens)
        kept = ens[ens.kept].drop(columns=["years", "incidence_mean", "kept"])
        ENSEMBLES.write_text(json.dumps(kept.to_dict(orient="records"), indent=1) + "\n")
        print(ens[["draw_id", "prevalence_2026_mean", "prevalence_2026_sd", "peak_year", "kept"]]
              .to_string(index=False))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=list(RESULTS))
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--plot-only", action="store_true")
    args = parser.parse_args()
    if not args.plot_only:
        if args.stage is None:
            parser.error("--stage is required unless --plot-only")
        run(args.stage, args.workers)
    plot()


if __name__ == "__main__":
    main()
