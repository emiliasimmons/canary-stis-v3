"""
Exp 38.3: Latin hypercube draws over the 14 explored parameters, one run each, per
country, appended to outputs/results.jsonl as each finishes. Each result carries
the draw's 2026 network summary. --network reruns landing draws on their batch seeds
with the current network summary, for the model-features figures.

    uv run python experiments/settings/38.3_seed_year_lower_sti_beta/run.py --stage batch --workers 80
    uv run python experiments/settings/38.3_seed_year_lower_sti_beta/run.py --plot-only
    uv run python experiments/settings/38.3_seed_year_lower_sti_beta/run.py --network 10

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
NETWORK = HERE / "outputs" / "network.jsonl"
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

    fig, axes = plt.subplots(1, len(countries), figsize=(10, 3.8), sharey=True, layout="constrained")
    for ax, (country, spec) in zip(axes, countries.items()):
        prev = df[df.country == country].hiv_prevalence_2026 * 100
        ax.hist(prev, bins=np.arange(0, 51, 2), color="0.5")
        ax.axvspan(100 * (spec["target"] - tol), 100 * (spec["target"] + tol), color="tab:blue", alpha=0.2)
        ax.set_title(f"{country.title()} (n = {len(prev)})")
        ax.set_xlabel("HIV prevalence at 15-49 in 2026 (%)")
    axes[0].set_ylabel("Draws")
    save(fig, 3, "prevalence_2026", "HIV prevalence at 15-49 in 2026, each country's cell shaded")

    plot_curves(df, "hiv_incidence_all", 1, "HIV incidence at 15-49 per 100 PY", 1, "incidence_curves",
                "HIV incidence at 15-49 by year, landing draws in blue")
    plot_seed_peak(df)
    plot_beta_prevalence(df)
    plot_sti_bands(df)
    for n, country in enumerate(countries, 6):
        plot_model_features(country, n)
    plot_curves(df, "hiv_prevalence", 100, "HIV prevalence at 15-49 (%)", 8, "prevalence_curves",
                "HIV prevalence at 15-49 by year, landing draws in blue, cell shaded", band=True)


def save(fig, n, name, title):
    """Number a figure in its title and file name, so a figure seen alone says which one it is."""
    fig.suptitle(f"Fig {n}: {title}")
    fig.savefig(FIGURES / f"fig{n}_{name}.png", dpi=150)
    plt.close(fig)


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
    save(fig, 2, "seed_year_peak_year", "Year HIV incidence peaks against seed_year, landing draws in blue")


def rerun_network(df, n_draws):
    """Rerun up to n_draws landing draws per country on their batch seeds, appending each network summary."""
    jobs = {job["draw_id"]: job for country, n in CONFIG["stages"]["batch"].items()
            for job in draws("batch", country, n)}
    done = set(pd.read_json(NETWORK, lines=True).draw_id) if NETWORK.exists() else set()
    todo = []
    for country in CONFIG["countries"]:
        sub, lands = landing(df, country)
        todo += [jobs[i] for i in sub[lands].draw_id.sort_values()[:n_draws] if i not in done]
    print(f"{len(todo)} landing draws to rerun for their network summary")
    batch_prev = df.set_index("draw_id").hiv_prevalence_2026
    with Pool(min(len(todo), os.cpu_count()) or 1) as pool:
        for row in pool.imap_unordered(run_draw, todo):
            if "error" in row:
                print(f"{row['draw_id']} failed: {row['error']}", flush=True)
                continue
            # the batch seed must reproduce the batch run, or the figure describes a different epidemic
            match = np.isclose(row["hiv_prevalence_2026"], batch_prev[row["draw_id"]])
            with NETWORK.open("a") as f:
                f.write(json.dumps(dict(draw_id=row["draw_id"], country=row["country"],
                                        reproduces_batch=bool(match), network=row["network"])) + "\n")
            print(f"{row['draw_id']} reproduces batch: {match}", flush=True)


def pooled_quantiles(counts, qs=(0.25, 0.5, 0.75)):
    """Quantiles of an integer histogram, bin index as value."""
    cum = np.cumsum(counts) / np.sum(counts)
    return [int(np.searchsorted(cum, q)) for q in qs]


def plot_model_features(country, n):
    """Six model features pooled over the landing draws rerun for their network summary."""
    rows = pd.read_json(NETWORK, lines=True) if NETWORK.exists() else pd.DataFrame(columns=["country", "network"])
    if "reproduces_batch" in rows:
        rows = rows[rows.reproduces_batch]
    nets = list(rows[rows.country == country].network)
    sexes = dict(female="#d6604d", male="#4393c3")
    fig, axes = plt.subplots(2, 3, figsize=(16, 9), layout="constrained")
    (ax_debut, ax_rg, ax_condom), (ax_pair, ax_life, ax_new) = axes

    def pool(key, sex):
        return np.sum([net[key][sex] for net in nets], axis=0)

    if nets:
        for sex, color in sexes.items():
            counts = pool("debut_age", sex)
            ages = np.arange(len(counts)) + 10
            cdf = np.cumsum(counts) / counts.sum()
            median = np.interp(0.5, cdf, ages + 1)
            ax_debut.step(ages + 1, cdf, where="post", color=color, label=f"{sex.title()} (median {median:.1f})")
        ax_debut.legend(frameon=False)

        cats = dict(low=("Low", "#4daf4a"), medium=("Medium", "#ff7f00"), high=("High", "#e41a1c"),
                    sex_work=("FSW / client", "#984ea3"))
        for x, sex in enumerate(sexes):
            bottom = 0
            for key, (label, color) in cats.items():
                share = 100 * np.mean([net["risk_group"][sex][key] for net in nets])
                ax_rg.bar(x, share, bottom=bottom, color=color, label=label if x == 0 else None)
                if share >= 3:
                    ax_rg.text(x, bottom + share / 2, f"{share:.0f}%", ha="center", va="center", color="white",
                               fontweight="bold")
                bottom += share
        ax_rg.set_xticks([0, 1], ["Female", "Male"])
        ax_rg.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.06))

        cells = np.concatenate([np.asarray(net["age_pairing"]) for net in nets])
        grid = np.zeros((80, 80))
        np.add.at(grid, (cells[:, 1], cells[:, 0]), cells[:, 2])
        edges = np.arange(81)
        mesh = ax_pair.pcolormesh(edges, edges, np.ma.masked_equal(grid, 0), cmap="viridis",
                                  norm=matplotlib.colors.LogNorm())
        fig.colorbar(mesh, ax=ax_pair, label="Partnerships (log)")
        ax_pair.plot([15, 65], [15, 65], "w--", lw=1, label="y = x")
        gaps = []
        for lo, hi in ((15, 25), (25, 35), (35, 50)):
            sel = (cells[:, 0] >= lo) & (cells[:, 0] < hi)
            gap = cells[sel, 1] - cells[sel, 0]
            order = np.argsort(gap)
            q = np.interp([0.25, 0.5, 0.75], np.cumsum(cells[sel, 2][order]) / cells[sel, 2].sum(), gap[order])
            gaps.append(f"F {lo}-{hi - 1}: Δ = {q[1]:+.1f} [{q[0]:+.1f}, {q[2]:+.1f}]")
        ax_pair.text(0.03, 0.97, "\n".join(gaps), transform=ax_pair.transAxes, va="top", fontsize=9,
                     bbox=dict(facecolor="0.4", alpha=0.8, edgecolor="none"), color="white")
        ax_pair.set_xlim(15, 65)
        ax_pair.set_ylim(15, 80)

        for ax, key in ((ax_life, "lifetime_partners"), (ax_new, "new_partners_last_year")):
            legend = []
            for i, (sex, color) in enumerate(sexes.items()):
                counts = pool(key, sex)
                x = np.arange(len(counts))
                ax.bar(x + (i - 0.5) * 0.4, counts / counts.sum(), 0.4, color=color, alpha=0.8)
                q = pooled_quantiles(counts)
                legend.append(f"{sex.title()}  {q[1]} [{q[0]}-{q[2]}]")
            ax.legend(legend, title="median [IQR]", frameon=True, fontsize=9)
            n_bins = len(counts)
            ticks = list(range(0, n_bins, 5 if n_bins > 15 else 2))
            ax.set_xticks(ticks, [f"{t}+" if t == n_bins - 1 else str(t) for t in ticks])
    else:
        for ax in (ax_debut, ax_rg, ax_pair, ax_life, ax_new):
            ax.text(0.5, 0.5, "No network summaries", transform=ax.transAxes, ha="center", va="center")

    groups = {(0, 0): ("Low-Low", "#4daf4a"), (1, 1): ("Med-Med", "#ff7f00"), (2, 2): ("High-High", "#e41a1c"),
              ("fsw", "client"): ("FSW-client", "#984ea3")}
    condom, years = sim_pars().network.condom_data, np.arange(1985, 2027)
    for pair, (label, color) in groups.items():
        ax_condom.plot(years, np.interp(years, condom[pair]["year"], condom[pair]["val"]), color=color,
                       label=label)
    ax_condom.legend(frameon=False)

    titles = [(ax_debut, "(A) Age at sexual debut", "Age (years)", "Cumulative proportion"),
              (ax_rg, "(B) Risk-group composition, 2026", None, "Proportion (%)"),
              (ax_condom, "(C) Condom use by partnership", "Year", "Condom use probability"),
              (ax_pair, "(D) Age-pairing density, 2026", "Female age (years)", "Male partner age (years)"),
              (ax_life, "(E) Lifetime partners (capped at 30)", "Number of lifetime partners", "Proportion"),
              (ax_new, "(F) New partners in last year, 2026", "New partners in prior 12 months", "Proportion")]
    for ax, title, xlabel, ylabel in titles:
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    ax_condom.set_ylim(0, 1)
    save(fig, n, f"model_features_{country}",
         f"{country.title()} model features, ages 15-49, pooled over {len(nets)} landing draws")


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
    save(fig, 5, "sti_prevalence_vs_stips", "STI prevalence at 15-49 in 2026 against the STIPS bands (grey)")


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
    save(fig, 4, "beta_prevalence_2026", "HIV prevalence at 15-49 in 2026 against HIV beta_m2f")


def plot_curves(df, column, scale, ylabel, n, name, title, band=False):
    """Annual curves per country, landing draws in blue, the target band shaded if band."""
    countries, tol = CONFIG["countries"], CONFIG["tolerance"]
    fig, axes = plt.subplots(1, len(countries), figsize=(10, 3.8), sharey=True, layout="constrained")
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
    save(fig, n, name, title)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", help="name fixing the stage's draws, e.g. pilot")
    parser.add_argument("--n", type=int, help="draws per country, overriding the stage's sizes in config.yaml")
    parser.add_argument("--workers", type=int, default=os.cpu_count())
    parser.add_argument("--plot-only", action="store_true")
    parser.add_argument("--network", type=int, metavar="N",
                        help="rerun up to N landing draws per country for the model-features figures, then plot")
    args = parser.parse_args()
    if args.network is not None:
        rerun_network(load(), args.network)
    elif not args.plot_only:
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
