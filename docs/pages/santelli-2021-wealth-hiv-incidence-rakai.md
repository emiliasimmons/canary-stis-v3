---
type: entry
title: Household wealth and HIV incidence over time, rural Uganda, 1994-2018
description: RCCS HIV incidence by round, sex, age, and household wealth quartile across 17 rounds, 1994-2018.
author: Santelli et al.
published: 2021-09-01
resource: 10.1097/QAD.0000000000002989
local: raw/10.1097/qad.0000000000002989
tags: [rakai, hiv]
updated: 2026-09-10 00:36
---

Analysis of the Rakai Community Cohort Study (RCCS) linking household socioeconomic status
(SES) to HIV incidence over 24 years. It uses 28 communities followed continuously from
round 1 (February 1994) through round 18 (ending May 2018), averaging 5387 households and
8622 individuals aged 15-49 per round; the incidence analysis covers 21 143 unique
individuals contributing 76 071 person-round observations, restricted to people with at
least two HIV tests and a prior negative. Fishing communities (introduced in round 15) and
mobile households are excluded. SES is a nine-asset index (radio, bicycle, motorcycle, car,
latrine, electricity, modern roof, floor, wall) reduced by principal components analysis to
a first component explaining 26% of variance, then cut into quartiles. Incidence rate ratios
come from GEE Poisson regression with an exchangeable correlation structure. Extracted text
sits in `raw/10.1097/qad.0000000000002989`.

## Relevance to project

The usable content here is the HIV incidence time series for the project's first calibration
site, stratified in exactly the dimensions the model tracks. Overall incidence in the 28
continuously followed RCCS communities falls from 1.45 per 100 person-years at round 2
(August 1995 - April 1996) to 0.40 per 100 person-years at round 18 (October 2016 - May
2018), IRR 0.39 (95% CI 0.32-0.47). Table 3 of the source gives per-round incidence for
every round from R02 to R18 by sex and by age band (15-24, 25-34, 35-49), and the by-sex,
by-age cells: for men, 1.97 at R04 declining to 0.35 at R18; for women, 1.64 at R04 to 0.44
at R18. Those are direct calibration targets for the HIV module's incidence trajectory and
for the sex ratio in incidence, which women carry at IRR 1.42 (95% CI 1.00-2.02) relative to
men after adjustment.

The age pattern constrains the age mixing in the network. Among men, incidence peaks at
25-34 (IRR 2.21, 95% CI 1.77-2.76, versus 15-24); among women there is no such peak, with
25-34 flat against 15-24 (IRR 0.97) and 35-49 lower (IRR 0.62, 95% CI 0.51-0.76). A model
that reproduces the aggregate decline but puts the male incidence peak in the youngest band
is wrong on a feature this cohort measures directly.

The wealth gradient is context, not a target: the model has no SES dimension. It matters
because the decline is not uniform across the population. Incidence in the highest wealth
quartile fell by IRR 0.36 (95% CI 0.23-0.54) between rounds 2 and 18, while the lowest
quartile showed no significant change (IRR 0.70, 95% CI 0.43-1.13, P = 0.148). Adjusted for
round, sex, and age, highest versus lowest quartile carries IRR 0.55 (95% CI 0.45-0.66).
Residual incidence late in the cohort is therefore concentrated in a subgroup the model
represents only through whatever heterogeneity the risk-structured network supplies, which
bears on how much headroom a targeted POC diagnostic arm can plausibly claim.

The paper supplies no STI data, no diagnostic performance, and no care-seeking measures.
Its denominators are person-rounds of the 15-49 population resident in non-mobile,
non-fishing households, so incidence here is lower than RCCS estimates that include the
Lake Victoria fishing communities.

## Key points

- Asset ownership rose steeply over the period: modern wall construction 36% to 93%,
  modern flooring 28% to 75%, electricity 3% to 48%. Bicycle ownership was the one asset
  that fell. By round 18, 50% of households sat in the highest SES quartile against 14% at
  round 1, and only 4% in the lowest, which makes the lowest quartile a shrinking and
  increasingly selected group late in the series.
- The wealth-HIV association reverses over the epidemic. Incidence was flat across SES
  categories in 1994-1997 and the protective gradient emerged only later, consistent with
  the shift other sub-Saharan African studies report around 1996.
- Time and sex interact (IRR 1.027 per round for women, P = 0.032): men's incidence fell
  faster than women's.
- Educational attainment, used as an alternative SES measure in sensitivity analysis, gave
  the same pattern as the asset index.

## Limitations

- Roughly 25% of censused residents are absent at each round (work, school, travel), and
  incidence is measured only among those with repeat tests. Absent and mobile people are
  plausibly at different risk, so the incidence levels are conditional on a residentially
  stable subsample.
- 12% of households were dropped for missing asset data.
- The analysis does not adjust for or measure use of prevention services, so the
  differential decline by wealth cannot be attributed to ART or circumcision access
  from this paper.
- Household assets ignore transfers between related households, which are common when a
  household faces an HIV-related crisis.
