# Exp 38.2: Explore network, HIV and STI parameters for the four settings, lower HIV ranges

**Question.** Which of 13 network, HIV and STI parameters move HIV prevalence at ages
15-49 in 2026 and the year HIV incidence peaks, and what fraction of each country's draws
lands in each setting's cell? This repeats
[38.1_explore_parameters](../38.1_explore_parameters/README.md) with lower HIV
transmission and seeding ranges. Its [pilot](../38.1_explore_parameters/SUMMARY.md) put
no Zimbabwe draw below 18.9% HIV prevalence at 15-49 in 2026 and no draw in either
expanding cell.

Cells and phase are defined in the
[settings decision](../../../docs/pages/settings-prevalence-by-phase.md): Eswatini's
setup fills the two high cells (25% within 3 points), Zimbabwe's the two medium cells
(15% within 3 points).

**Plan.** Everything matches 38.1 except two ranges:

- HIV `beta_m2f` 0.003-0.025, down from 0.0086-0.033
- HIV `rel_init_prev` 0.01-1.5, down from 0.1-1.5, drawn on a log scale

The other 11 ranges, the resampling rule, the country setups, the SOC arm, 10,000 agents
and the recorded outcomes are 38.1's.

The run has two stages, appended to one results file. A local pilot of 60 draws (30 per
country) measures the landing fraction *p* per cell on the new ranges. The large batch,
on Coiled, is sized so the hardest cell gets about 30 landing draws (*N* ≈ 30 / *p* per
country).

**Success criteria.** Each cell's landing fraction is known with about 30 landing draws in
the hardest one. For both 2026 prevalence and the peak year, the parameters that move them
are identified (rank correlation over all draws, and which ranges the landing draws
occupy). The landing draws' STI prevalence is reported beside the measured values. A cell
that fills with far fewer than 30 draws at the batch size, or landing draws whose
incidence curves cannot be told apart by phase, means these ranges cannot produce that
setting either.
