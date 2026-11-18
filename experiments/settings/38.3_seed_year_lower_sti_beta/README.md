# Exp 38.3: Explore network, HIV and STI parameters for the four settings, later HIV seeding and lower STI ranges

**Question.** Which of 14 network, HIV and STI parameters move HIV prevalence at ages
15-49 in 2026 and the year HIV incidence peaks, what fraction of each country's draws
lands in each setting's cell, and how does the landing draws' 2026 curable-STI prevalence
compare with measured bands? The exploration is answered when the landing fraction per
cell is known, the parameters driving 2026 prevalence and the peak year are identified,
and the landing draws' 2026 gonorrhoea, chlamydia, trichomoniasis and syphilis prevalence
is set against sourced bands.

[38.2](../38.2_lower_hiv_beta_and_seed/SUMMARY.md) filled both mature cells but no
expanding cell: every landing draw's incidence peaked by 2017, 50 of 51 by 2011, with HIV
seeded in 1985. Only gonorrhoea fell inside its band. The landing draws' median 2026
prevalence was about 23% for chlamydia, 37% for trichomoniasis and 29% for RPR-positive
syphilis. Zimbabwe landed only at HIV `beta_m2f` 0.004-0.0075.

Cells are defined in the [settings decision](../../../docs/pages/settings-prevalence-by-phase.md),
which shares HIV and STI biology across the four settings, so both countries draw from the
same ranges. Phase is judged from each landing draw's incidence curve, with no fixed
peak-year cut-off.

**Plan.** 38.2's draws with one added parameter and five changed ranges:

- HIV `seed_year` 1993-2000, the year HIV is first seeded, 8-15 years after 38.2's 1985.
  Seeding is unchanged apart from its year: the risk-group table scaled by
  `rel_init_prev`.
- HIV `rel_init_prev` 0.3-1.5 on a log scale, up from 0.01-1.5. None of 38.2's 150 draws
  at 0.3-1.5 had 2026 HIV prevalence at 15-49 under 1%, against 78 of 109 at 0.01-0.03,
  so the timing rests on `seed_year`.
- HIV `beta_m2f` 0.003-0.012, down from 0.003-0.025. In 38.2, Eswatini landed at
  0.006-0.021 and Zimbabwe at 0.004-0.0075.
- chlamydia `beta_m2f` 0.03-0.16, down from 0.046-0.54. 38.2's 20 draws inside the band
  had 0.061-0.154.
- trichomoniasis `beta_m2f` 0.005-0.08, down from 0.019-0.66. 38.2's 11 draws inside the
  band had 0.025-0.051.
- syphilis `beta_m2f` 0.01-0.12, down from 0.097-0.38. No 38.2 draw reached the band, and
  draws at 0.097-0.163 had a median 2026 RPR-positive prevalence at 15-49 of 25%.

Gonorrhoea `beta_m2f` stays at 0.019-0.33, where 156 of 38.2's 353 draws with HIV
prevalence of at least 1% fell inside the band. The network ranges, the resampling rule,
the country setups, the SOC arm and 10,000 agents are 38.2's.

Each draw also records a network summary in 2026: lifetime partners by sex, new partners
in the last year by sex, age at sexual debut by sex, risk-group composition by sex, and
the age gap between partners by female age group. Condom use by partnership type is an
input and comes from the parameters. A model-features figure per country shows these for
a few landing draws.

One zebra batch runs 300 draws per country. At 38.2's batch landing fractions (21 landing
of 110 Eswatini draws, 19 landing of 300 Zimbabwe draws) that gives about 57 Eswatini and 19 Zimbabwe landing
draws, and the proportion of Zimbabwe draws inside its 38.2 landing HIV `beta_m2f` values of
0.004-0.0075 rises from about 16% under 38.2's range of 0.003-0.025 to about 39% under
this one of 0.003-0.012.

The STI band for each infection is the span of the 95% confidence intervals across the
two communities in [STIPS](../../../docs/pages/grabowski-2022-stips-sti-burden-rakai.md),
adults 18-49 in Rakai in 2019: chlamydia 7.9-12.0%, gonorrhoea 3.8-10.5%, trichomoniasis
7.7-14.5%, and for the model's RPR-positive syphilis, STIPS's high-titre syphilis (RPR at
least 1:8) at 0.8-11.5%. Any positive treponemal serology (7.1% and 24.2% in the two
communities) is an upper bound for the model's syphilis at any stage, since it also counts
cured infection. The model reports ages 15-49.

**Success criteria.** Success is landing draws in all four cells: in each country, some
landing draws whose HIV incidence at 15-49 is still rising or only recently past its peak
in 2026, and some long past it. A `seed_year` within 1993-2000 gives expanding epidemics
in both countries, and that year is kept. For each of the four infections, some landing
draws have 2026 prevalence inside its STIPS band.

Two failures are possible. Eswatini draws seeded in 1993-2000 may stay below 22% HIV
prevalence at 15-49 in 2026, the lower edge of Eswatini's cell, at HIV `beta_m2f` up to
0.012, as 38.2's latest-starting epidemics
did. Then a high-prevalence expanding epidemic cannot share Zimbabwe's HIV
transmission. Syphilis may stay above its band even at syphilis `beta_m2f` 0.01, the bottom of its range. Then
syphilis prevalence comes from how long infection lasts or how it is treated in the
model, and that is what changes next.
