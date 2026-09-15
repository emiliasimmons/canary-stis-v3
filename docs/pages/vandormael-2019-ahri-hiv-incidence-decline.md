---
type: entry
title: Declines in HIV incidence among men and women in a South African population-based cohort
description: AHRI KwaZulu-Natal repeat-testing cohort, 2005-2017; sex-specific HIV incidence rates and a 43% overall decline over 2012-2017.
author: Vandormael et al.
published: 2019-12
resource: https://doi.org/10.1038/s41467-019-13473-y
local: raw/10.1038/s41467-019-13473-y
tags: [hiv]
updated: 2026-09-10 00:23
---

Source: [vandormael-2019](https://doi.org/10.1038/s41467-019-13473-y)

Prospective HIV incidence estimates from the Africa Health Research Institute (AHRI)
population-based surveillance platform in the Hlabisa sub-district of KwaZulu-Natal, South
Africa: roughly 90,000 residents in 11,000 households across 438 km², surveyed two to three
times a year with annual dried-blood-spot HIV testing. The incidence cohort is 22,239
repeat testers (9,630 men aged 15-54, 12,609 women aged 15-49) contributing 92,877 person-
years between 2005 and 2017.

## Relevance to project

A comparator and a sanity bound on HIV incidence levels and trend, not a calibration target
for canary-stis: the site is rural KwaZulu-Natal, not Rakai, and the study measures no STIs.
Its use here is threefold.

First, it fixes the order of magnitude the model's HIV module must reproduce in a
hyperendemic generalized epidemic. Female incidence sat near 4.3 per 100 person-years across
2005-2013 and fell to 3.06 (95% CI 2.38-3.94) by 2017; male incidence peaked at 2.49
(1.83-3.37) in 2012 and fell to 1.01 (0.58-1.76) in 2017. A simulated 15-49 population with
female incidence far outside 3-5 per 100 person-years in the pre-decline era is
mis-parameterized. The paper itself notes the Rakai cohort reported a 42% decline over
2012-2016, closely matching the 43% here over 2012-2017, so the trend magnitude transfers to
the planned calibration site even though the levels need not.

Second, the sex asymmetry is the counterfactual any STI-diagnostics impact estimate has to
sit against. Between 2012 and 2017, background ART and circumcision scale-up alone cut
incidence 59% in men and 37% in women, with the female decline lagging the male one by two
years. Any incidence reduction attributed to a POC STI panel is an increment on top of a
background trend of that size, which sets the scale at which a POC-versus-SOC difference is
detectable.

Third, the circumcision stratification bounds a competing prevention pathway. Self-reported
circumcision coverage rose from 3.0% to 32.9% between 2009 and 2016; the incidence rate among
circumcised men was 1.24 (0.57-2.69) per 100 person-years in 2012 falling to 0.5 (0.16-1.57)
in 2016, against 3.01 (2.16-4.18) falling to 1.73 (1.01-2.97) among uncircumcised men. If the
model carries a circumcision covariate, these are usable stratum levels for a generalized
epidemic setting.

What it cannot supply: no STI prevalence, no syndromic or etiological care-seeking data, and
no partnership-level network structure. Its ART coverage numbers are the percentage of
HIV-positive participants on treatment (women 2.1% in 2005 to 50.6% in 2017; men 1.5% to
38.4%) and are underestimates, since ~40% of HIV-positive participants were never linked to
local clinic records.

## Key points

Declines in each sex's incidence appeared only after opposite-sex ART coverage passed roughly
35%: for men that threshold was crossed in 2012, for women in 2014. The authors read this as
a population treatment threshold rather than a smooth dose-response, though the adjusted
incidence rate ratios (Model 1) do decline monotonically across coverage bands: for women
against male ART coverage, 0.99 (10-24%), 0.87 (25-34%), 0.68 (35-55%) relative to 0-9%.

HIV prevalence rose throughout the same period, from 14% to 20% in men and 25% to 41% in
women aged 15-54, and reached 59% among women aged 30-49 by 2017. Falling incidence alongside
rising prevalence is survival on treatment, and a model calibrated to prevalence alone would
miss the incidence trend entirely.

Population prevalence of detectable viremia (threshold 1,550 copies/mL) among HIV-positive
participants fell from 72.8% in 2011 to 55.3% in 2014 in women, and only 77.8% to 67.2% in
men over the same years.

Self-reported condom use was flat from 2012 onward, around 64% reported by women for their
male partners and around 70% among men, so behavioral change does not explain the decline.

Peak acquisition risk was in men aged 25-29 and women aged 20-24, relative to 15-19-year-olds.

## Methodology

Incidence was estimated by single random-point imputation of the seroconversion date within
the censoring interval between the last negative and first positive test, with 300 imputed
datasets combined by Rubin's rules, followed by Poisson regression for rate ratios. Median
censoring interval was 3 years. Only 41% of contacted participants tested in an average year,
and 76% of eligible HIV-negative participants entered the incidence cohort; inverse
probability weights for follow-up and dropout were applied in the adjusted models. The
authors argue elsewhere that single random-point imputation stays robust at testing rates as
low as 40% and censoring intervals as wide as four years, which is what makes these estimates
usable despite the participation rates.

## Limitations

Circumcision status and condom use are self-reported and subject to social desirability bias.
ART coverage is underestimated because ~40% of HIV-positive participants were unlinked to
local clinic records; the authors argue this biases the ART-coverage association toward the
null. The association between ART coverage and incidence is observational and ecological
(opposite-sex coverage in the surrounding community), so it cannot be read as a causal
treatment effect at the individual level.
