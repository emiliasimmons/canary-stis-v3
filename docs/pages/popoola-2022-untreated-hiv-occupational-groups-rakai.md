---
type: entry
title: "Prevalence of untreated HIV and HIV incidence among occupational groups in Rakai, Uganda: a population-based longitudinal study, 1999-2016"
description: RCCS untreated-HIV prevalence and HIV incidence per 100 person-years broken out by self-reported primary occupation and sex, identifying female bar and restaurant workers and male transport workers as the groups where incidence did not fall
author: Popoola et al.
published: 2022-06-22
resource: https://doi.org/10.1101/2022.06.21.22276714
local: raw/10.1101/2022.06.21.22276714
tags: [hiv, rakai, care-seeking]
updated: 2026-09-10 11:18
---

medRxiv preprint, not peer reviewed at the time of posting, re-analysing the same 12 Rakai Community Cohort Study rounds and the same 30 continuously surveyed communities as the 1999-2016 incidence analysis, this time stratified by self-reported primary occupation. 33,866 participants, 19,113 (56%) women, contributed 102,759 person-visits. The incidence cohort is 17,840 women contributing 57,912 person-years and 14,244 men contributing 49,403 person-years. Fishing communities are excluded, since RCCS surveys there started only in 2011. Extracted content in [raw/10.1101/2022.06.21.22276714/](../raw/10.1101/2022.06.21.22276714/).

## Relevance to project

This is the structural input for risk-group definition at the Rakai site. It gives observed HIV incidence and untreated-HIV prevalence for occupational subgroups that the model's risk strata are meant to stand in for, with denominators, and it fixes how much heterogeneity a plausible network has to generate. In the mature-intervention period (2011-2016) female bar and restaurant workers had 2.88 times the HIV incidence of women in agriculture (95% CI 1.51-5.49) and male transport workers 2.75 times that of men in agriculture (1.37-5.50), while students of both sexes sat well below agriculture. A risk-structured network that produces a flat incidence gradient across strata is inconsistent with this.

It is also a secondary calibration target. Occupation-specific incidence rates per 100 person-years are reported for three calendar periods with numerator and person-year denominator, so the model can be scored against subgroup levels rather than just the population average.

The care-seeking content is ART uptake among HIV-positive people by occupation, which shows treatment access varying by group in the same direction as risk. That is a plausible template for making the STI care-seeking rate differ across strata, though the source measures HIV treatment uptake and not symptomatic STI presentation, so the transfer is an analogy and not a parameter.

No STI is measured. The source cannot inform STI prevalence, coinfection, or any part of the diagnostic pathway. Sex work is absent as a category: no participant of either sex reported it as a primary occupation across all 12 rounds, which is a reporting artefact of criminalisation rather than a finding, so the model's highest-activity stratum has no direct observation here.

## Key points

Population HIV incidence per 100 person-years by period, all occupations pooled. Women: 1.1 (146/12,781) in 1999-2004, 1.0 (257/24,958) in 2004-2011, 0.7 (147/20,173) in 2011-2016, adjusted IRR for late against pre 0.66 (0.53-0.83). Men: 1.1 (109/9,821), 0.9 (186/21,498), 0.5 (86/18,085), adjusted IRR 0.44 (0.33-0.59).

Occupations where incidence did not fall. Female bar and restaurant workers went 1.1 (4/365) to 2.1 (17/813) to 2.0 (12/605) per 100 person-years, adjusted IRR late against pre 2.79 (0.85-9.19), the point estimate rising on very small counts. Female local crafts workers went 1.3 (5/387) to 2.3 (12/518) to 1.6 (5/308). Male transport workers went 1.4 (4/287) to 1.8 (21/1181) to 1.2 (12/964), adjusted IRR 1.10 (0.35-3.50).

Occupations where it did fall. Men in agriculture: 1.4 (53/3894) to 0.8 to 0.4 (25/5834), adjusted IRR 0.33 (0.21-0.54). Women in agriculture: 1.1 (97/8490) to 0.9 to 0.7 (62/9515), adjusted IRR 0.62 (0.45-0.86). Male construction: adjusted IRR 0.35 (0.15-0.83).

Untreated HIV prevalence, defined as HIV infection in a person not self-reporting ART use, comparing survey 1 (1999-2000) to survey 12 (2015-2016). All occupations: women 15.6% (543/3474) to 4.4% (294/6647), adjusted prevalence risk ratio 0.27 (0.24-0.31); men 10.5% (265/2518) to 3.4% (180/5358), adjusted PRR 0.29 (0.24-0.35). Female bar and restaurant workers started highest at 34.7% (50/144) and ended at 12.0% (32/267), three times the 4.0% (106/2669) among women in agriculture at the final visit. Take the adjusted PRR for that decline from Table 3, 0.21 (0.14-0.31), not from the running text, which gives 0.38 (0.25-0.58). The two disagree, and the text also reports 0.27 (0.22-0.34) for women in agriculture where the table gives 0.22 (0.18-0.27), the 0.27 being the value in the men's column of the same row. Male transport workers went 8.2% (4/49) to 7.1% (18/252), adjusted PRR 0.90 (0.30-2.73), the only male group with no decline and the highest male untreated prevalence at the end.

Occupational composition shifted over the period. Agriculture as primary occupation fell from 61% to 40% among women and from 39% to 29% among men. Among men, transport rose from 1.9% to 4.7% and mechanic work from 2.5% to 5.6%. Among women, trading rose from 9.4% to 16% and student from 7.3% to 14%. A model with fixed stratum sizes over 1999-2016 does not reproduce this drift.

ART uptake among HIV-positive people rose in every occupational group. In the mature period it was lowest among female students and, relative to women in agriculture, significantly lower among female traders (adjusted PRR 0.91, 0.83-0.98) and female bar and restaurant workers (0.87, 0.78-0.97). Among men it was lowest in trading (0.91, 0.83-0.98) and among students (0.59, 0.41-0.84).

## Limitations

Not peer reviewed. Occupation and ART use are self-reported, with ART self-report validated in this population at 99% specificity and 77% sensitivity, so untreated prevalence is likely overstated somewhat.

The subgroup incidence estimates rest on few events. Female bar and restaurant workers contributed 4, 17 and 12 infections across the three periods, and male transport workers 4, 21 and 12, which is why intervals on the period comparisons span an order of magnitude and cross one. The cross-sectional contrast against agriculture in the mature period is the better-supported claim; the within-group trend over time is not.

Sex work is criminalised in Uganda and was almost certainly underreported. Bar and restaurant work is functioning here as a partial proxy for it, and the authors say as much.

Key-population programming in the region began in 2017 and universal test-and-treat and PrEP came in 2017 and 2018, all after the analysis window, so none of these figures reflect them.

The excluded fishing communities are the highest-prevalence setting in Rakai, so the occupational gradient measured here is the agrarian and trading gradient only.

## Methodology

Untreated HIV prevalence and ART use are cross-sectional at each of the 12 rounds; incidence uses person-years between consecutive rounds with one missed round permitted and infections placed at the interval midpoint. Prevalence risk ratios come from log-binomial models and incidence rate ratios from Poisson models, both adjusted for age and marital status only, which is a thinner adjustment set than the whole-population incidence analysis used, so the occupational contrasts still carry age and partnership structure that a model would need to reproduce separately.

Occupation is the participant's self-reported primary activity at that visit, from 41 free-text and coded responses collapsed into 15 subgroups. Only subgroups with a median of at least 50 observations per round were analysed, 8 among men and 9 among women. People change occupation between rounds, so a subgroup is a time-varying attribute of person-visits rather than a fixed cohort, and the incidence rate for a subgroup is an average over whoever reported it during that interval.

The three periods are pre-intervention 1999-2004, early scale-up 2005-2011, and mature 2011-2016. Table headings label the middle period 2004-2011; the text uses 2005-2011.
