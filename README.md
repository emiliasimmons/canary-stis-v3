# canary-stis

Pathway analysis and calibration harness for quantifying the population-level HIV prevention impact of point-of-care STI diagnostics. The scientific question: how much of the reduction in HIV incidence from POC STI diagnostics comes from direct treatment, prevention targeting, or network identification?

The model is a Starsim/STIsim agent-based model with 10,000 agents, 1990–2030 at monthly timestep, co-circulating HIV and four curable bacterial STIs (gonorrhea, chlamydia, syphilis, trichomoniasis) on a shared risk-structured sexual network. The first planned calibration site is the Rakai Community Cohort Study (rural Uganda).

## Setup

Requires Python ≥ 3.13 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

All simulation dependencies (starsim, stisim, parsimmon) are pulled from private git sources; SSH access to those repositories is required.

## Running

Run an experiment script directly:

```bash
uv run python experiments/canary/01_model_port/run.py
```

On a remote VM (requires SSH access to the target):

```bash
scripts/mirror zebra canary/01_model_port -j 80
```

Pull results back:

```bash
scripts/mirror-pull zebra canary/01_model_port
```

`mirror` enforces git soundness before syncing: no uncommitted changes in experiment, src, or deps; branch must have an upstream with no unpushed commits. After launch it prints the tmux attach and log-tail commands for monitoring.

## Project structure

```
src/              simulation library (sim.py, interventions.py, diagnostics.py, connectors.py, analyzers.py)
experiments/      experiment tracks (canary/, rakai/)
docs/             knowledge base and decision records
scripts/          remote execution utilities (mirror, mirror-pull)
data/             calibration data (not yet in repo)
```

`experiments/canary/` is the default track for pathway exploration. `experiments/rakai/` is for Rakai calibration work. Each track numbers experiments independently (`01_slug`, `02_slug`, …). Every experiment folder contains a `README.md` (pre-registered intent), a `run.py`, and a `SUMMARY.md` after it closes.

`src/sim.py` defines `sim_pars()` and `build_sim()`, the [parsimmon](https://github.com/emiliasimmons/parsimmon) fn-hash boundary. The diagnostic arm is selected by `pars.intv_year`: `None` runs syndromic standard-of-care for the whole simulation, a year switches the NG/CT/TV and syphilis pathways to the POC etiological arm at that year. `src/interventions.py` holds the classes with no stisim equivalent (a gonorrhea-treatment seeding fix, magic cure, and the care-seeking / bundled-prevention / FSW-outreach levers); PrEP runs through stisim's `sti.Prep`, configured in `build_sim`; `src/diagnostics.py` the care-seeking eligibility, arm gating, and syphilis testing chain; `src/connectors.py` the HIV-STI coinfection connectors. `src/analyzers.py` has eight analyzers covering the diagnostic and transmission cascade.

Demand-side levers are off at their identity or zero value, never behind a boolean flag: `care_seek_mult=1.0`, `bundled_prevention=None`, `fsw_outreach.rate=0.0`, `prep.eligibility='none'`, `magic_cure.year=None`.

The `docs/` knowledge base is managed with [canonize](https://github.com/emiliasimmons/canonize). Decision records live in `docs/decisions/`; findings from closed experiments go in `docs/findings/<workspace>/`.

## AI assistant plugins

This project uses two assistant plugins:

- [canonize](https://github.com/emiliasimmons/skills-ensemble) — knowledge base and evidence-trail management
- [calib-plugin](https://github.com/InstituteforDiseaseModeling/calib-plugin) — calibration workflow skills

See `CLAUDE.md` / `AGENTS.md` for behavioral instructions given to AI assistants working in this repo.
