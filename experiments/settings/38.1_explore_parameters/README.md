# Exp 38: Explore network, HIV and STI parameters for the four settings

**Question.** Which of 13 network, HIV and STI parameters move HIV prevalence at ages
15-49 in 2026 and the year HIV incidence peaks, and what fraction of each country's draws
lands in each setting's cell? The experiment also counts the Zimbabwe draws that overshoot
into high HIV prevalence, and reports each landing draw's 2026 prevalence of gonorrhoea,
chlamydia, trichomoniasis and syphilis so it can be compared with STI prevalence measured
in real populations, starting from
[STIPS](../../../docs/pages/grabowski-2022-stips-sti-burden-rakai.md) in Rakai.

This is the first experiment on the settings track. Cells and phase are defined in the
[settings decision](../../../docs/pages/settings-prevalence-by-phase.md): Eswatini's
setup fills the two high cells (25% within 3 points), Zimbabwe's the two medium cells
(15% within 3 points). The next experiment picks the shared HIV and STI transmission
values from the landing draws.

**Plan.** Each draw runs once, at 10,000 agents, from 1985 to the end of 2026, under the
SOC arm. Each country gets its own Latin hypercube draws over the 13 ranges below, taken
from today's defaults, Eswatini's best draw and sti_notification's kept draws, widened by
about 10% at each end:

- `prop_f0` 0.40-0.94, `prop_m0` 0.36-0.88
- `prop_f2` 0.009-0.11, `prop_m2` 0.018-0.22
- `f1_conc` 0.009-0.17, `f2_conc` 0.09-0.28, `m1_conc` 0.13-0.22
- HIV `beta_m2f` 0.0086-0.033
- HIV `rel_init_prev` 0.1-1.5, scaling the reference models' risk-group seeding table
  (`init_prev_hiv.csv`)
- STI `beta_m2f`: syphilis 0.097-0.38, gonorrhoea 0.019-0.33, chlamydia 0.046-0.54,
  trichomoniasis 0.019-0.66

Draws with `prop_f0 + prop_f2` (or `prop_m0 + prop_m2`) too close to 1 to leave a middle
risk group are resampled. `m2_conc` stays at 0.5, condom use and HIV `rel_beta_f2m` (0.5)
at today's values, every other parameter at its default. Each simulation records HIV
prevalence at 15-49 in 2026, annual HIV incidence at 15-49 (pooled and by sex), the
incidence peak year, the prevalence-to-incidence ratio in 2026, the four STIs' 2026
prevalence, and run time.

The run has two stages, appended to one results file. A local pilot of 60 draws (30 per
country) measures run time per simulation and the landing fraction *p* per cell. The
large batch, on Coiled, is sized so the hardest cell gets about 30 landing draws
(*N* ≈ 30 / *p* per country).

**Success criteria.** Each cell's landing fraction is known with about 30 landing draws in
the hardest one. For both 2026 prevalence and the peak year, the parameters that move them
are identified (rank correlation over all draws, and which ranges the landing draws
occupy). The landing draws' STI prevalence is reported beside the measured values. A cell that fills
with far fewer than 30 draws at the batch size, or landing draws whose incidence curves
cannot be told apart by phase, means the ranges cannot produce that setting and the next
experiment widens or moves them before issue 39 fixes any value.
