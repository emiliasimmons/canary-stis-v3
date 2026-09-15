---
type: entry
title: "Comparing modelled HIV incidence estimates with empirical HIV incidence observations in high-burden HIV African epidemic settings: systematic review and meta-regression"
description: 3560 empirical incidence observations from 179 studies matched to UNAIDS modelled estimates by area, sex, age and year; population-representative studies match the models, cohort incidence in adults 15-49 fell 75-90% over 2010-2023, and the epidemic is aging faster than Spectrum assumes
author: Stevens et al.
published: 2026-02-05
resource: https://doi.org/10.64898/2026.02.05.26345548
local: raw/10.64898/2026.02.05.26345548
tags: [hiv, modeling, rakai, sexual-networks]
updated: 2026-09-10 00:14
---

Source: [stevens-2026](https://doi.org/10.64898/2026.02.05.26345548)

A systematic review pooling directly observed adult HIV incidence across sub-Saharan Africa, matched observation by observation to UNAIDS modelled incidence for the same subnational area, sex, five-year age group and year, then regressed to ask whether the models sit at the right level and decline at the right rate. The review extends Joshi et al. (published 2010-2019) with literature published July 2019 to February 2024, and adds PHIA survey microdata, seven population cohorts, four universal-test-and-treat trials, and key-population meta-analyses. Yield: 3560 observations from 179 studies in 21 countries, 23,000 seroconversions over 3.1 million person-years, median study year 2014 (IQR 2006-2016).

Modelled estimates are UNAIDS Global HIV Epidemic Estimates published July 2024 (EPP-Spectrum, Thembisa v4.7 for South African provinces). Regression is Bayesian mixed-effect Poisson with log person-years offset and log modelled incidence as offset, fitted in R-INLA.

## Relevance to project

Sets the incidence level and trend the HIV side of the model has to reproduce at the Rakai calibration site, and bounds how much of an incidence decline any intervention arm can plausibly add on top of what treatment scale-up already delivered.

Concretely usable here:

- Calibration target shape for Rakai: adult 15-49 incidence flat from 2000 to about 2010, then a 75-90% decline between 2010 and 2023 across all seven population cohorts including RCCS. Rakai is one of the cohorts whose modelled and observed trends agreed.
- Age split of new infections, a target the paper argues most models get wrong: in 2017-2022, adults 15-24 carried a median 25% of new infections (range 24-44%) across uMkhanyakude, Siaya, Kyamulibwa and Rakai, and the share was falling. UNAIDS modelled estimates put 40-50% of infections in 15-24. Incidence fell 7%/year in 15-24 (aRR 0.93, 95% CI 0.90-0.96) against 3%/year in 25-49 (interaction aRR 0.96/year, 95% CI 0.94-0.98). If the STIsim network is built to a constant age pattern, it will place too much incidence in the youngest band.
- Sex split: women were a median 72% of new infections (range 69-74%) in population cohorts over 2017-2022, and incidence fell faster in men (interaction aRR 0.96/year, 95% CI 0.95-0.97). Latest cohort data show the female:male ratio of new infections rising toward 4:1 in Kyamulibwa, against the roughly 1.5:1 that national models assumed for 1995-2008.
- A bound on comparator arms. Because the model runs an SOC arm against a POC arm at the same care-seeking door, the trial-arm literature is the natural external benchmark, and this paper shows those benchmarks are inflated relative to the general population: control arms of non-UTT clinical trials ran 2.91x matched modelled incidence (95% CI 1.80-4.69), pregnant and post-partum women 2.44x (1.47-4.06), FSW 6.46x (4.18-10.00), MSM 44.02x (27.35-70.87). Trials recruited on risk criteria, sometimes an explicit minimum number of sex acts, and participants reported high prevalence of transactional sex and STIs. An incidence target lifted from a prevention trial's control arm would be roughly three times too high for a population-representative model.
- Justification for calibrating to population-representative data rather than to UNAIDS output alone: the two agree. Population cohorts and UTT control clusters 0.95x modelled (95% CI 0.49-1.86), nationally-representative household surveys 1.01x (0.64-1.59), other household surveys 1.25x (0.79-1.96), with no year trend in the ratio (0.99, 95% CI 0.98-1.01). Log-scale correlation of observed against matched modelled incidence R = 0.83; PHIA against national modelled R = 0.90.

What it does not supply: no absolute incidence rate per 100 person-years for Rakai by year (the trend figures are normalised to 2010 and the underlying numbers live in the Zenodo dataset at https://zenodo.org/records/18482588), no STI covariate, and no partnership or network structure. Risk-based recruitment, including studies of people with STIs and serodiscordant couples, was excluded from the pooled dataset by design, so this source says nothing about the STI-HIV cofactor the project is built around. Its one relevant remark is descriptive: high self-reported STI prevalence is part of why prevention-trial control arms sit three times above population incidence.

## Key points

The models pass on level and on rate of decline, and fail on composition. EPP-Spectrum infers 15-49 incidence from cross-sectional prevalence trends and ART data, then apportions it across sex and five-year age groups using incidence rate ratios, and 58 of 74 sub-Saharan African Spectrum files in the 2024 round specified a constant age pattern over time. That assumption is what breaks: the cohorts show a sustained shift of infection to older ages that a fixed apportionment cannot express.

PHIA agreement weakened between rounds. Correlation of log incidence with modelled estimates was R = 0.94 in round 1 (2015-2019, n = 14 surveys) and R = 0.56 in round 2 (2020-2022, n = 9). Survey 95% CIs contained the modelled estimate for 17 of 23 surveys; Zimbabwe and Tanzania modelled incidence sat below the second survey.

uMkhanyakude is the one cohort where modelled and observed trends diverge: the modelled decline starts earlier than the data show.

## Limitations

Subnational incidence estimates existed only for 2023 and were extrapolated back to 1970-2023 parallel to matched national or provincial Spectrum trajectories, so true subnational history may differ, and this uncertainty is not carried into the regression. Study sites may be selected for urban or rural locations away from the area average the modelled estimate represents. Coverage is skewed: 131 of 179 studies come from five countries (South Africa 51, Kenya 35, Uganda 17, Tanzania and Zimbabwe 14 each), and only 26 studies are from West and Central Africa, of which 7 are total-population. Person-years were imputed for observations that did not report them.

The preprint's own numbers are inconsistent between the abstract and Table 1. The abstract reports IRR 1.07 (0.68, 1.67) for nationally-representative household surveys and 0.98 (0.51, 1.89) for population-representative populations; Table 1 reports 1.01 (0.64, 1.59) and 0.95 (0.49, 1.86). The figures quoted above are Table 1. Not peer reviewed.
