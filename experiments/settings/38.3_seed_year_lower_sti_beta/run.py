"""
Exp 38.3: Latin hypercube draws over the 14 explored parameters, one run each, per
country, appended to outputs/results.jsonl as each finishes. Each result carries
the draw's 2026 network summary.

    uv run python experiments/settings/38.3_seed_year_lower_sti_beta/run.py --stage batch --workers 80
    uv run python experiments/settings/38.3_seed_year_lower_sti_beta/run.py --plot-only

A stage's draws are fixed by its name, so rerunning a stage skips the draws
already in the results and runs the rest.
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
from scipy.stats import qmc

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2]))

from src.settings import setting_pars, summarize  # noqa: E402
from src.sim import build_sim, sim_pars  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
RESULTS = HERE / "outputs" / "results.jsonl"
FAILURES = HERE / "outputs" / "failures.jsonl"
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
        dict(draw_id=f"{stage}-{country}-{i:04d}", stage=stage, country=country,
             rand_seed=stage_seed(stage, country, str(i)), draw=draw)
        for i, draw in enumerate(kept)
    ]


def run_draw(job):
    # a failing draw is recorded and the stage carries on, so one bad corner of
    # the box doesn't stop a batch
    try:
        return simulate(job)
    except Exception as exc:
        return dict(draw_id=job["draw_id"], error=f"{type(exc).__name__}: {exc}")


def simulate(job):
    t0 = time.perf_counter()
    pars = setting_pars(job["draw"], job["country"],
                        sim=dict(n_agents=CONFIG["n_agents"], rand_seed=job["rand_seed"]))
    sim = build_sim(pars)
    sim.run(verbose=0)
    return dict(
        draw_id=job["draw_id"], stage=job["stage"], country=job["country"],
        rand_seed=job["rand_seed"], **job["draw"], **summarize(sim),
        run_time_s=time.perf_counter() - t0,
    )


def done_ids():
    if not RESULTS.exists():
        return set()
    return {json.loads(line)["draw_id"] for line in RESULTS.read_text().splitlines() if line}


def run(stage, sizes, workers):
    jobs = [job for country, n in sizes.items() for job in draws(stage, country, n)]
    done = done_ids()
    jobs = [job for job in jobs if job["draw_id"] not in done]
    print(f"{len(jobs)} simulations to run on {workers} workers ({len(done)} already in results)")
    RESULTS.parent.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    with Pool(workers) as pool:
        for i, row in enumerate(pool.imap_unordered(run_draw, jobs), 1):
            if "error" in row:
                with FAILURES.open("a") as f:
                    f.write(json.dumps(row) + "\n")
                print(f"{i}/{len(jobs)} {row['draw_id']} failed: {row['error']}", flush=True)
                continue
            with RESULTS.open("a") as f:
                f.write(json.dumps(row) + "\n")
            print(f"{i}/{len(jobs)} {row['draw_id']} prevalence {row['hiv_prevalence_2026']:.3f} "
                  f"in {row['run_time_s']:.0f} s ({time.perf_counter() - t0:.0f} s elapsed)", flush=True)


def load():
    return pd.read_json(RESULTS, lines=True)


def plot(df):
    FIGURES.mkdir(exist_ok=True)
    countries, tol = CONFIG["countries"], CONFIG["tolerance"]

    fig, axes = plt.subplots(1, len(countries), figsize=(10, 3.5), sharey=True)
    for ax, (country, spec) in zip(axes, countries.items()):
        prev = df[df.country == country].hiv_prevalence_2026 * 100
        ax.hist(prev, bins=np.arange(0, 51, 2), color="0.5")
        ax.axvspan(100 * (spec["target"] - tol), 100 * (spec["target"] + tol), color="tab:blue", alpha=0.2)
        ax.set_title(f"{country.title()} (n = {len(prev)})")
        ax.set_xlabel("HIV prevalence at 15-49 in 2026 (%)")
    axes[0].set_ylabel("Draws")
    fig.tight_layout()
    fig.savefig(FIGURES / "prevalence_2026.png", dpi=150)
    plt.close(fig)

    plot_curves(df, "hiv_incidence_all", 1, "HIV incidence at 15-49 per 100 PY", "incidence_curves.png")
    plot_curves(df, "hiv_prevalence", 100, "HIV prevalence at 15-49 (%)", "prevalence_curves.png", band=True)
    plot_beta_prevalence(df)
    plot_sti_bands(df)
    plot_seed_peak(df)
    for country in countries:
        plot_network(df, country)


def landing(df, country):
    """A country's draws and whether each lands in its cell."""
    spec, tol = CONFIG["countries"][country], CONFIG["tolerance"]
    sub = df[df.country == country]
    return sub, ((sub.hiv_prevalence_2026 - spec["target"]).abs() <= tol).to_numpy()


def plot_seed_peak(df):
    """HIV incidence peak year against seed_year, landing draws in blue."""
    countries = CONFIG["countries"]
    fig, axes = plt.subplots(1, len(countries), figsize=(10, 4), sharey=True, layout="constrained")
    for ax, country in zip(axes, countries):
        sub, lands = landing(df, country)
        ax.scatter(sub.seed_year[~lands], sub.peak_year[~lands], s=10, color="0.6")
        ax.scatter(sub.seed_year[lands], sub.peak_year[lands], s=18, color="tab:blue")
        ax.set_title(f"{country.title()}: {lands.sum()} landing of {len(sub)} draws")
        ax.set_xlim(*CONFIG["ranges"]["seed_year"])
        ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
        ax.set_xlabel("HIV seed_year")
    axes[0].set_ylabel("Year HIV incidence at 15-49 peaks")
    fig.savefig(FIGURES / "seed_year_peak_year.png", dpi=150)
    plt.close(fig)


def plot_network(df, country, n_draws=3):
    """Network summary of up to n_draws landing draws, with the condom use the model takes as input."""
    sub, lands = landing(df, country)
    shown = sub[lands].sort_values("draw_id").head(n_draws)
    sexes = dict(female="tab:red", male="tab:blue")
    styles = ["-", "--", ":"]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8), layout="constrained")
    (ax_life, ax_new, ax_debut), (ax_rg, ax_gap, ax_condom) = axes

    for (_, row), ls in zip(shown.iterrows(), styles):
        net = row.network
        for sex, color in sexes.items():
            for ax, key in ((ax_life, "lifetime_partners"), (ax_new, "new_partners_last_year")):
                counts = np.asarray(net[key][sex], dtype=float)
                ax.plot(np.arange(len(counts)), 100 * counts / counts.sum(), ls=ls, marker="o", ms=3,
                        color=color, label=f"{sex}, {row.draw_id}")
    for ax, key, title in ((ax_life, "lifetime_partners", "Lifetime partners"),
                           (ax_new, "new_partners_last_year", "New partners in the last year")):
        if shown.empty:
            continue
        n_bins = len(shown.iloc[0].network[key]["female"])
        ax.set_xticks(range(n_bins), [*map(str, range(n_bins - 1)), f"{n_bins - 1}+"], fontsize=7)
        ax.set_title(title)
        ax.set_ylabel("People 15-49 (%)")
    ax_new.set_yscale("log")
    if not shown.empty:
        ax_life.legend(fontsize=7)

    def quantile_box(ax, x, q, color):
        ax.plot([x, x], [q[0], q[-1]], color=color, lw=1)
        ax.plot([x, x], [q[1], q[-2]], color=color, lw=6, alpha=0.5)
        ax.plot(x, q[len(q) // 2], "o", color=color, ms=4)

    labels = []
    for i, (_, row) in enumerate(shown.iterrows()):
        for j, (sex, color) in enumerate(sexes.items()):
            x = 2 * i + j
            q = row.network["debut_age_quantiles"][sex]
            if q is not None:
                quantile_box(ax_debut, x, q, color)
            bottom = 0
            for g, prop in enumerate(row.network["risk_group"][sex]):
                ax_rg.bar(x, 100 * (prop or 0), bottom=bottom, color=color, alpha=(0.3, 0.6, 1.0)[g])
                bottom += 100 * (prop or 0)
            labels.append(f"{sex[0].upper()}\n{row.draw_id[-4:]}")
    for ax in (ax_debut, ax_rg):
        ax.set_xticks(range(len(labels)), labels, fontsize=7)
    ax_debut.set_title("Age at sexual debut, 10/25/50/75/90th centiles", fontsize=10)
    ax_debut.set_ylabel("Age")
    ax_rg.set_title("Risk groups 0, 1, 2, light to dark")
    ax_rg.set_ylabel("People 15-49 (%)")

    groups = dict(f15_20="15-19", f20_25="20-24", f25_50="25-49")
    for i, (_, row) in enumerate(shown.iterrows()):
        for k, key in enumerate(groups):
            gap = row.network["age_gap"][key]
            x = k + (i - 1) * 0.25
            if gap["quantiles"] is not None:
                quantile_box(ax_gap, x, gap["quantiles"], "0.3")
                ax_gap.annotate(f"n={gap['n']}", (x, gap["quantiles"][-1]), ha="center", va="bottom", fontsize=6)
    ax_gap.set_xticks(range(len(groups)), [f"Women {g}" for g in groups.values()])
    ax_gap.axhline(0, color="0.8", lw=0.8)
    ax_gap.set_title("Partner age gap, man minus woman, 5/25/50/75/95th centiles", fontsize=10)
    ax_gap.set_ylabel("Years")

    condom = sim_pars().network.condom_data
    names = ["sex work" if pair == ("fsw", "client") else f"M{pair[0]}-F{pair[1]}" for pair in condom]
    use = [100 * np.interp(2026, data["year"], data["val"]) for data in condom.values()]
    ax_condom.bar(range(len(use)), use, color="0.5")
    ax_condom.set_xticks(range(len(use)), names, fontsize=7, rotation=45)
    ax_condom.set_title("Condom use in 2026 by partners' risk groups (model input)", fontsize=10)
    ax_condom.set_ylabel("Acts with a condom (%)")

    if shown.empty:
        for ax in axes.flat[:-1]:
            ax.text(0.5, 0.5, "No landing draws", transform=ax.transAxes, ha="center", va="center")
    fig.suptitle(f"{country.title()}: {len(shown)} of {lands.sum()} landing draws, 2026, ages 15-49")
    fig.savefig(FIGURES / f"network_{country}.png", dpi=150)
    plt.close(fig)


def plot_sti_bands(df):
    """2026 STI prevalence per draw with HIV at 1% or more, STIPS band shaded, landing draws in blue."""
    countries, tol, bands = CONFIG["countries"], CONFIG["tolerance"], CONFIG["sti_bands"]
    labels = dict(ct="Chlamydia", ng="Gonorrhoea", tv="Trichomoniasis", syph_rpr="Syphilis, RPR+")
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(1, len(countries), figsize=(13, 4.5), sharey=True, layout="constrained")
    for ax, (country, spec) in zip(axes, countries.items()):
        sub = df[(df.country == country) & (df.hiv_prevalence_2026 >= 0.01)]
        lands = ((sub.hiv_prevalence_2026 - spec["target"]).abs() <= tol).to_numpy()
        ticks = []
        for i, (key, (lo, hi)) in enumerate(bands.items()):
            ax.fill_between([i - 0.4, i + 0.4], lo, hi, color="0.85", zorder=0)
            prev = sub[f"{key}_prevalence_2026"] * 100
            x = i + rng.uniform(-0.25, 0.25, len(prev))
            ax.scatter(x[~lands], prev[~lands], s=8, color="0.6", zorder=1)
            ax.scatter(x[lands], prev[lands], s=16, color="tab:blue", zorder=2)
            inside = prev[lands].between(lo, hi).sum()
            ticks.append(f"{labels[key]}\n{inside}/{lands.sum()} in band")
        ax.set_xticks(range(len(bands)), ticks, fontsize=9)
        ax.set_title(f"{country.title()}: {lands.sum()} landing of {len(sub)} draws with HIV ≥ 1%")
    axes[0].set_ylabel("Prevalence at 15-49 in 2026 (%)")
    fig.savefig(FIGURES / "sti_prevalence_vs_stips.png", dpi=150)
    plt.close(fig)


def plot_beta_prevalence(df):
    """2026 prevalence against HIV beta_m2f, coloured by seeding since the seed decides take-off."""
    countries, tol = CONFIG["countries"], CONFIG["tolerance"]
    norm = matplotlib.colors.LogNorm(*CONFIG["ranges"]["rel_init_prev"])
    fig, axes = plt.subplots(1, len(countries), figsize=(11, 4), sharey=True, layout="constrained")
    for ax, (country, spec) in zip(axes, countries.items()):
        sub = df[df.country == country]
        sc = ax.scatter(sub.hiv_beta_m2f, sub.hiv_prevalence_2026 * 100, c=sub.rel_init_prev,
                        norm=norm, cmap="viridis", s=12)
        ax.axhspan(100 * (spec["target"] - tol), 100 * (spec["target"] + tol), color="tab:blue", alpha=0.15)
        ax.set_title(f"{country.title()} (n = {len(sub)})")
        ax.set_xlabel("HIV beta_m2f")
    axes[0].set_ylabel("HIV prevalence at 15-49 in 2026 (%)")
    fig.colorbar(sc, ax=axes, label="rel_init_prev")
    fig.savefig(FIGURES / "beta_prevalence_2026.png", dpi=150)
    plt.close(fig)


def plot_curves(df, column, scale, ylabel, name, band=False):
    """Annual curves per country, landing draws in blue, the target band shaded if band."""
    countries, tol = CONFIG["countries"], CONFIG["tolerance"]
    fig, axes = plt.subplots(1, len(countries), figsize=(10, 3.5), sharey=True)
    for ax, (country, spec) in zip(axes, countries.items()):
        sub = df[df.country == country]
        for _, row in sub.iterrows():
            lands = abs(row.hiv_prevalence_2026 - spec["target"]) <= tol
            ax.plot(row.years, np.asarray(row[column]) * scale, lw=1.2 if lands else 0.5,
                    color="tab:blue" if lands else "0.75", zorder=2 if lands else 1)
        if band:
            ax.axhspan(100 * (spec["target"] - tol), 100 * (spec["target"] + tol), color="tab:blue", alpha=0.15)
        ax.set_title(f"{country.title()}: landing draws in blue")
        ax.set_xlabel("Year")
    axes[0].set_ylabel(ylabel)
    fig.tight_layout()
    fig.savefig(FIGURES / name, dpi=150)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", help="name fixing the stage's draws, e.g. pilot")
    parser.add_argument("--n", type=int, help="draws per country, overriding the stage's sizes in config.yaml")
    parser.add_argument("--workers", type=int, default=os.cpu_count())
    parser.add_argument("--plot-only", action="store_true")
    args = parser.parse_args()
    if not args.plot_only:
        if args.stage is None:
            parser.error("--stage is required unless --plot-only")
        if args.n is not None:
            sizes = dict.fromkeys(CONFIG["countries"], args.n)
        elif args.stage in CONFIG["stages"]:
            sizes = CONFIG["stages"][args.stage]
        else:
            parser.error(f"stage {args.stage!r} has no sizes in config.yaml; pass --n")
        run(args.stage, sizes, args.workers)
    plot(load())


if __name__ == "__main__":
    main()
