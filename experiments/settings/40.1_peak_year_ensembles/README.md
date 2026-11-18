# Exp 40.1: Ensembles for the four settings, with the expanding cells intervened at the incidence peak

**Question.** Which simulations make up each of the four settings, when each expanding
cell is stood in for by intervening at its simulations' HIV incidence peak?
[38.3](../38.3_seed_year_lower_sti_beta/SUMMARY.md) filled both mature cells (154 of 400
Zimbabwe draws at 12-18% HIV prevalence at 15-49 in 2026, 10 of 400 Eswatini draws at
22-28%) and gave no expanding epidemic: every landing draw's incidence peaked by 2013.
Until a slower epidemic is found, each country's ensemble serves two cells: the mature
cell with `intv_year` 2027, and the expanding cell with `intv_year` set to each
simulation's own peak year. The expanding cells then differ from the mature ones in ART
coverage as well as phase, since ART in both country tables starts at 0 in 2004 and
reaches about 0.8-0.9 of women aged 25-34 with HIV by 2020-2021.

The [settings decision](../../../docs/pages/settings-prevalence-by-phase.md) judges phase
from the incidence curve to 2026, intervenes in 2027 in every cell, and shares HIV
biology across settings. This experiment departs from all three as an interim
arrangement. Eswatini landed only at HIV `beta_m2f` 0.0102-0.0117, the top of 38.3's
shared range, so it gets its own range.

**Plan.** Two stages, both run locally.

1. Eswatini batch: 200 draws over 38.3's ranges with HIV `beta_m2f` 0.010-0.020 in place
   of 0.003-0.012. In 38.3 Eswatini's median 2026 prevalence rose by about 1-1.5
   percentage points per 0.001 of `beta_m2f`, reaching a median of 18.8% at HIV
   `beta_m2f` 0.010-0.012, so a median of 25% needs roughly HIV `beta_m2f` of
   0.016-0.018. `seed_year` stays drawn over 1993-2000, matching the Zimbabwe draws
   carried over from 38.3.
2. Replicates: the 5 landing draws per country closest to the target (Zimbabwe from
   38.3's 154, Eswatini from the batch), 10 seeds each, SOC arm, 10,000 agents, run
   to the end of 2026. A draw is kept when its replicate-averaged 2026 prevalence at
   15-49 is within 3 points of the target (25% Eswatini, 15% Zimbabwe). Its peak year is
   the year its replicate-averaged incidence at 15-49 is highest.

At about 200 s per simulation on 16 workers, the Eswatini batch takes about 40 minutes and
the replicates stage about 20 minutes. The result is a table of kept draws, each written as `sim_pars`
overrides with `intv_year` 2027 for the mature cell and its peak year for the expanding
cell.

**Success criteria.** At least 3 kept draws per country, and a seed-to-seed standard
deviation of 2026 prevalence well inside the 3-point tolerance (under about 1.5 points).
If fewer than 3 Eswatini batch draws land at HIV `beta_m2f` up to 0.020, high prevalence
needs a change other than HIV transmission, most likely the network ranges. A wider
seed-to-seed spread, from late take-off or extinction, calls for more agents rather
than more seeds.
