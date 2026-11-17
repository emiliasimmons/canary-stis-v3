---
type: entry
title: "hivsim_eswatini: STIsim HIV model of Eswatini"
description: Starsim/STIsim HIV-only model of Eswatini with age-by-sex ART coverage from SHIMS surveys, PHIA viral suppression re-targeted on the treated stock, four HIV testing streams, and a history-matching calibration to survey prevalence, SHIMS incidence and UNAIDS deaths.
author: Adam Akullian (maintainer), with Daniel Citron
resource: https://github.com/starsimhub/hivsim_eswatini
local: raw/hivsim_eswatini
tags: [hiv, modeling, care-seeking, prep]
updated: 2026-11-17 13:51
---

An agent-based HIV model of Eswatini built on Starsim and STIsim, from 1985 to 2031 in
monthly steps with 10,000 agents scaled to the national population. It carries HIV
alone, with no curable STIs. Its research question is the relative value of scaling up
long-acting PrEP against closing the treatment cascade, and where prevention still
matters once viral suppression is high. Read at commit `ab632d5` (2026-09-07), model tag
`model-v1.3` on stisim 1.5.11 and starsim 3.5.2. The README still describes an older
Optuna workflow and an `n_art.csv` ART input, so the experiment folders and
`interventions.py` are the current record.

## Architecture

`run_sims.make_sim()` builds every simulation: a `StructuredSexual` network with three
risk groups plus a maternal network, `sti.HIV`, the interventions from
`interventions.make_interventions()`, and the `hiv_epi` analyzer. Model changes live in
the repo as subclasses or separate interventions, because edits to the editable stisim
checkout were lost on upgrade once (the VMMC patch, exp 015). Each experiment under
`experiments/NNN_*` has a README written before it runs and a SUMMARY after, and
`experiments/log.md` covers only 001 to 007.

## Components

**ART coverage.** `sti.ART(coverage=data/art_coverage.csv)` takes the proportion of all
people living with HIV on ART, by sex and four age bands (15-24, 25-34, 35-44, 45+), at
2004 (zero, before the programme), 2011, 2016 and 2021. The 2021 values run from 0.650
(men 25-34) to 0.970 (women 35-44), mean 0.870. stisim forward-fills from the last row,
so coverage stays at its 2021 values to the end of the run (`scenarios.py:141-147`).
Each step `sti.ART` adds or removes agents to bring each age-sex stratum to its target.
Upstream stisim first summed the strata and allocated globally by CD4 priority, and exp
002 patched it locally (`experiments/002_art_strata_fix/github_issue.md`). By stisim
1.6.1 the correction works per stratum (`notes/stisim_pr_and_issues.md:78`). The file
codes sex 0 = female, 1 = male, the opposite of `calibration_data/prevalence_by_age_sex.csv`,
and a swap between the two cost exp 018 one of its results.

`art_coverage_construction.py` documents the table's provenance. The 2011 and 2016 45+
cells copy the 35-44 value, because neither SHIMS1 nor SHIMS2 publishes an older band.
The 2021 45+ cells come from SHIMS3 Table 9.1.A's 50+ band (women 0.966, men 0.953). The
2016 men 15-24 cell was corrected from 0.360 to 0.556, the biomarker-basis value derived
from SHIMS2 Table 10.3.B as diagnosed times on-ART-among-diagnosed. Ages under 15 are
outside the table.

**Viral suppression.** `vls_construction.py` transcribes suppression among people on ART
(adults 15+, biomarker-adjusted ART status) from the PHIA reports: 2016 men 0.905, women
0.918 (SHIMS2 Table 10.3.B), 2021 men 0.967, women 0.959 (SHIMS3 Table 9.1.B). It has no
age dimension: derived by age, suppression among the treated varied by only 0.3 to 0.8
points across 15-44 in 2016, so the age gradient in population suppression is a coverage
gradient. The series is held at the 2016 value back to 1985 and at the 2021 value after
it. It enters twice. `sti.ART(vls_coverage=...)` sets suppression at ART start, and
`VLSStockTarget` (`vls_stock_target.py`), run after ART, re-targets the whole treated
stock each step by sex. It ranks agents on ART by a persistent random propensity and
marks the top `target × n` suppressed, so a rising target adds people to the suppressed
pool in a stable order. Without it, an agent keeps the status drawn at initiation for
life, and in exp 021 realised suppression among the treated lagged its input (0.956
against 0.967 in 2021). With it, exp 022 tracked the input to four decimals at 2021 and
left prevalence fit unchanged (mean absolute error 0.0584 to 0.0586). stisim's default
`vls_coverage=None` suppresses everyone on ART, which exp 021 measured as overstating
population suppression by 8.8 points in 2016. Treated but unsuppressed agents transmit
with `nonsupp_art_efficacy` 0.35 against `effective_art_efficacy` 0.99. The stock target
has been proposed upstream on stisim branch `feat/vls-stock-target-and-cascade-results`.

**HIV testing.** Four `sti.HIVTest` streams (`interventions.py:12-76`). Probabilities
ramp linearly from 0 in 1990 to the 2020 value, then to the 2040 value:

- FSW not yet diagnosed or on ART: 0.75 by 2020, 0.85 by 2040.
- Everyone else not diagnosed or on ART: 0.5, then 0.6.
- Undiagnosed agents with CD4 below 200: 0.85, then 0.95.
- Antenatal: undiagnosed women in the first trimester at a constant 0.9, unscaled by
  timestep (`dt_scale=False`) and with no time profile, so it runs from 1985.

**VMMC and PrEP.** `sti.VMMC` takes circumcision prevalence targets by 5-year band
(`data/vmmc_coverage.csv`: a 1990 anchor, SDHS 2007, SHIMS2 2016, SHIMS3 2021 Table
12.5). The calibration baseline has no PrEP: `sti.Prep()` without `coverage` applies a
built-in programme reaching 80% of FSW by 2025 from 2004, and every experiment from 001
to 017 ran with it unnoticed. `scenarios.py` adds lenacapavir (efficacy 0.95, 6-month
duration) as an explicit coverage target from 2026, and notes that `sti.Prep` fills
coverage within the eligible group by a random `willingness` score, so users carry the
group's average risk.

## Calibration

History matching through IDM's `historymatching` 2.0.1 with the `bayes_linear` emulator
(`hm_shim.py` stubs TensorFlow, which has no Python 3.14 wheels), replacing the earlier
1000-trial Optuna fit. Wave 1 (exp 024) opened seven parameters, chosen by sensitivity in
exp 023: `beta_m2f` 0.0096-0.025 and `rel_beta_f2m` 0.15-0.60 (per-act transmission),
`s_f_young` 0.8-3.0 (susceptibility of women 15-24), `age_gap_shift` −2 to +3 years and
`age_gap_sd_mult` 0.6-1.8 (partner age mixing), and `prop_f0` 0.45-0.85 and `prop_m0`
0.40-0.80 (low-risk group shares). `rel_init_prev` (0.2) and `conc_mult` (1.0) are fixed.
The design was 1000 Latin hypercube points, one replicate each, 10,000 agents, 456 s on
120 cores.

Targets, fitted on the 2007, 2011 and 2016 surveys with 2021 held out for validation:

- Prevalence by age, sex and year from SDHS 2007, SHIMS1 2011 and SHIMS2 2016, with σ
  from the published 95% intervals as (upper − lower)/3.92 (0.0043-0.0066 on 15-49
  prevalence by sex), plus a declared model-discrepancy σ of 0.02.
- Peak UNAIDS AIDS deaths, given σ = 2000 because the model reaches about 7,069 against
  UNAIDS's 11,000.
- The UNAIDS 1985 age distribution.
- SHIMS incidence at adult aggregates only: SHIMS1 cohort 2011, ages 18-49 (women 3.14,
  men 1.65 per 100 person-years), and SHIMS2 2016 Table 5.3.B, ages 15-49 (women 1.73,
  men 0.85). The age-banded rows are kept but unfitted, because the female profile is
  flat in a way the authors attribute to false recency in the recency assay, which
  inflates incidence most where prevalence is highest.

ART coverage, suppression and VMMC are inputs and never fitted. The 48 registered
targets are tiered: A (overall prevalence 15-49 and peak deaths), B (sex and age ratios,
incidence) and C (24 prevalence cells by age, sex and year). Wave 1 emulated only overall
15-49 prevalence averaged over the three survey years, with implausibility threshold 4.
The emulator reached R² 0.923, and 87.2% of the box survived, cut along one composite
transmission direction. One draw (design row 868: `beta_m2f` 0.0142, `rel_beta_f2m`
0.310, `s_f_young` 2.22) lands within 3σ on all 48 targets. The model's 2016 female
incidence is right in total and wrong by age: 2.05 per 100 person-years at 15-24 against
1.67 measured, and 0.35 at 35-49 against 2.09. Wave 2 (exp 025, σ_disc 0.01, adding
incidence and the female young-to-old prevalence ratio behind a synthetic-data
re-identification gate) is designed and was blocked on compute at 2026-09-07. There is
no posterior, and the scenario runs in exp 026 use row 868 alone.

## Extension points

`make_sim()` accepts `art_coverage` (a replacement ART table, the scenario axis for
cascade arms), `art_vls_coverage`, `vls_stock_target`, `hiv_class` and `vmmc_class`
(subclass injection), and `extra_interventions`, which run after the defaults so
anything re-targeting a stock wins. `scenarios._ramp_long` extends a long-format coverage
table past its last year and only raises strata below the target, since a flat ramp to
0.95 would pull three of eight ART strata down.

## Relevance to project

The project's ART follows this model. `sti.ART` runs with an age-by-sex coverage table
measured from surveys and held flat after the last data year, suppression comes from
PHIA through `vls_coverage` plus a `VLSStockTarget` re-targeting the treated stock each
step, and the four testing streams (FSW, general population, low CD4, antenatal) are
taken from here. The [partner notification implementation](partner-notification-implementation.md)
decision relies on this design: a partner diagnosed with HIV joins the same
coverage-targeted ART, so a diagnosis adds people on ART only in strata whose diagnosed
pool is too small to fill the target. The repo is also a worked comparator for
calibration choices (survey σ from confidence intervals, an explicit discrepancy term,
deaths down-weighted through σ, incidence fitted at aggregates) and a list of stisim
defaults that silently add programmes.

It supplies no STI parameters, and its HIV transmission values (`beta_m2f`,
`rel_beta_f2m`, `s_f_young`) are fitted to Eswatini by one unreplicated draw. They can
bound a prior.

## Limitations

The 2021 rows of the ART coverage source are back-derived from SHIMS3 suppression
divided by the national suppression rate (0.7935 × 0.959 reproduces SHIMS3's women 15-24
suppression exactly), so they embed the suppression input supplied separately (exp 021
SUMMARY). The 2011 and 2016 45+ coverage cells are copies. Suppression before 2016 is an
assumption. stisim treats a stratum missing from a stratified coverage table as 100%
covered (`notes/stisim_pr_and_issues.md:155`). The wave-1 prior ensemble's 5-95% envelope
misses women 35-49's 2016 incidence and men 15-24's 2007 and 2011 prevalence, and the
authors suspect partner age mixing.
Results hold for this model version only, and the authors record each experiment's model
tag for that reason.
