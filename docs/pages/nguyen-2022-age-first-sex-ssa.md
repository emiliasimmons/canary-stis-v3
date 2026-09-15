---
type: entry
title: Trends and country-level variation in age at first sex in sub-Saharan Africa among birth cohorts entering adulthood between 1985 and 2020
description: Bias-adjusted Bayesian estimates of the full age-at-first-sex distribution by sex, country, and birth cohort across 42 sub-Saharan African countries.
author: Nguyen and Eaton
published: 2022-05-28
resource: 10.1186/s12889-022-13451-y
local: raw/10.1186/s12889-022-13451-y
tags: [sexual-networks, hiv, modeling]
updated: 2026-09-10 00:24
---

Source: [nguyen-2022](https://doi.org/10.1186/s12889-022-13451-y)

Nguyen and Eaton pooled individual records from 253 nationally representative household
surveys (DHS, MICS, AIS, PMA, PHIA and others) covering 3,088,315 respondents aged 15-55
at interview, born 1950-2005, in 42 sub-Saharan African countries. They fit a Bayesian
spatio-temporal survival model with a three-parameter log-skew-logistic time-to-event
distribution, giving the sexual debut hazard by sex, age, country, and birth cohort rather
than a single median. Because the same birth cohort reports its age at first sex (AFS) in
successive survey rounds roughly five years apart, the differences between those reports
identify a reporting bias term as a function of age at interview, estimated separately by
sex and country and pooled hierarchically for countries with only one survey.

## Relevance to project

This supplies the entry process into the sexual network: the age at which agents become
sexually active, and how fast a cohort transitions from never-active to active. The
model's debut is an age-varying rate, so the useful output here is the full distribution,
not the median. For the birth cohort turning 15 in 2015, the interquartile range of the
AFS distribution averaged 4.0 years across countries (range 2.2 years for Liberian women
to 9.6 for Sudanese men), and was shorter for women than men in 37 of 40 countries. That
gives a directly usable shape for a debut hazard: a peaked transition around a median, with
25% to 75% of women crossing in about four years and men in about five.

For Rakai the relevant slice is Uganda, whose country-level median AFS is in the country
map (Fig. 1) and Supplemental Table S2 rather than the article text, so the exact Ugandan
figure has to be pulled from the supplement before it is used as a number. Two qualitative
Uganda-relevant results are in the text: Uganda is named among the countries whose trend
fluctuated non-monotonically over the period, and eastern Africa as a region shows an
average increase of only 0.31 years in median AFS across 1985-2020. That supports holding
debut age fixed over the simulated calibration period rather than giving it a time trend,
which removes one moving part from the network model.

The male-female gap is also usable as a network input. In eastern and southern Africa the
gap is under two years and stable, so the age-mixing structure the model needs for Rakai
does not require the wide cross-generational offset implied by Sahel-region estimates,
where the gap exceeds two years and has widened.

What it cannot do: it gives no partnership formation rates, no partner counts, no
concurrency, and no link between debut age and later risk behaviour. It is the age gate on
network entry and nothing beyond it. It also carries no HIV or STI outcome, so it cannot
serve as a calibration target.

## Key points

- Median AFS in the 2015 cohort ranged from 15.8 years (Angolan women, IQR 15.5-16.2) to
  25.3 (Nigerien men, 24.5-26.1). Women debuted earlier than men in 37 of 40 countries;
  the exceptions were Lesotho, South Africa, and Comoros.
- Change over 1985-2020 was small: mean 0.84 years for women (IQR 0.11-1.55) and 0.79 for
  men (IQR -0.23-1.97), increasing in 60 of 82 country-sex series. Eastern Africa averaged
  +0.31 years, southern Africa +0.12.
- Percentage ever having had sex by age 18 in the 2015 cohort ranged from 4.4% (Nigerien
  men, 3.2-6.0%) to 86.1% (Liberian women, 82.8-88.9%). By age 15 the highest was 37.7%
  (Angolan men). In 37 of 82 country-sex series, under 10% had debuted by age 15.
- Reporting bias runs in opposite directions by sex among the young: female teenagers
  report a higher AFS than the same cohort reports in its late twenties (under-reporting
  early activity), male teenagers report a lower one. Both sexes report progressively
  higher AFS as they age past 30, consistent with recall error.
- The authors' conclusion is that behavioural programmes aimed at delaying debut had modest
  effect, and services should be timed to the local debut distribution instead.

## Limitations

- No gold standard for which reporting age is truthful. The bias adjustment fixes only
  relative differences across ages at interview; the authors anchor all reported estimates
  to age 23 as reference, chosen because it is above the average female age at marriage and
  not a digit-preference age. Every AFS number in the paper inherits that choice.
- The shape of the distribution and the reporting bias are allowed to vary by country but
  not over time within a country. Only the median moves across cohorts, so any change in
  the spread of debut ages over the period is absorbed elsewhere.
- Estimates are national. Rakai is a rural southern-Uganda setting and the paper's own
  discussion flags that subnational estimates would differ and would need to handle
  urban-rural migration, since respondents may not live where they debuted.
- Confounders that plausibly separate Ugandan subpopulations, religion in particular, were
  not modelled.
- Survey weights were used in a pseudo-likelihood, but stratified clustered sampling design
  was not modelled, so uncertainty intervals are likely too narrow.
- Data screening removed reports of AFS under 7 years (0.01-1.67% of observations per
  dataset), 32 datasets missing over 10% of the AFS variable, and 6 with over 10%
  non-response on age among those reporting ever having had sex.
