# Exp 38.3: Explore network, HIV and STI parameters for the four settings, lower STI ranges

**Question.** Which of 13 network, HIV and STI parameters move HIV prevalence at ages
15-49 in 2026 and the year HIV incidence peaks, what fraction of each country's draws
lands in each setting's cell, and how does the landing draws' 2026 curable-STI prevalence
compare with measured bands? This repeats
[38.2_lower_hiv_beta_and_seed](../38.2_lower_hiv_beta_and_seed/README.md) with lower STI
transmission ranges and a narrower HIV range. In [38.2](../38.2_lower_hiv_beta_and_seed/SUMMARY.md)
only gonorrhoea fell inside its band: the landing draws' median 2026 prevalence was about
23% for chlamydia, 37% for trichomoniasis and 29% for RPR-positive syphilis. Zimbabwe
landed only at HIV `beta_m2f` 0.004-0.0075, and above 0.008 every Zimbabwe draw
overshot its cell.

Cells and phase are defined in the
[settings decision](../../../docs/pages/settings-prevalence-by-phase.md), which shares HIV
and STI biology across the four settings, so both countries draw from the same ranges.

**Plan.** Everything matches 38.2 except five ranges:

- chlamydia `beta_m2f` 0.03-0.16, down from 0.046-0.54. 38.2's 20 draws inside the band
  had 0.061-0.154.
- trichomoniasis `beta_m2f` 0.005-0.08, down from 0.019-0.66. 38.2's 11 draws inside the
  band had 0.025-0.051.
- syphilis `beta_m2f` 0.01-0.12, down from 0.097-0.38. No 38.2 draw reached the band, and
  draws at 0.097-0.163 had a median 2026 RPR-positive prevalence at 15-49 of 25%.
- HIV `beta_m2f` 0.003-0.012, down from 0.003-0.025. Eswatini landed at 0.006-0.021 and
  Zimbabwe at 0.004-0.0075 in 38.2.
- HIV `rel_init_prev` 0.1-1.5 on a log scale, up from 0.01-1.5. At 0.01-0.03, 78 of 109
  38.2 draws had 2026 HIV prevalence at 15-49 under 1%, and with HIV seeded in 1985 a small seed only delays the
  epidemic. Late epidemics are left to the next experiment's `seed_year`.

Gonorrhoea `beta_m2f` stays at 0.019-0.33, where 156 of 38.2's 353 draws with HIV
prevalence of at least 1% fell inside the band. The network ranges, the resampling rule,
the country setups, the SOC arm, 10,000 agents and the recorded outcomes are 38.2's. A
local pilot of 60 draws (30 per country) sizes a zebra batch so the hardest mature cell
gets about 30 landing draws.

The STI band for each infection is the span of the 95% confidence intervals across the
two communities in [STIPS](../../../docs/pages/grabowski-2022-stips-sti-burden-rakai.md),
adults 18-49 in Rakai in 2019: chlamydia 7.9-12.0%, gonorrhoea 3.8-10.5%, trichomoniasis
7.7-14.5%, and for the model's RPR-positive syphilis, STIPS's high-titre syphilis (RPR at
least 1:8) at 0.8-11.5%. Any positive treponemal serology (7.1% and 24.2% in the two
communities) is an upper bound for the model's syphilis at any stage, since it also counts
cured infection. The model reports ages 15-49.

**Success criteria.** Each mature cell has about 30 landing draws, and for each infection
some landing draws fall inside the band, with the STI `beta_m2f` values they occupy
reported as the starting point for fixing the shared STI parameters. The SUMMARY states
the landing fraction per cell, the parameters driving 2026 HIV prevalence and the peak
year, and the landing draws' STI prevalence against the bands, which closes the
exploration. If syphilis stays above its band at `beta_m2f` 0.01, syphilis prevalence is
set by its natural history or care in the model, and lowering transmission cannot fix it.
