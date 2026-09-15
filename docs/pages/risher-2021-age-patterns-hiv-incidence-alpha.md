---
type: entry
title: "Age patterns of HIV incidence in eastern and southern Africa: a modelling analysis of observational population-based cohort studies"
description: Bayesian reconstruction of age-specific HIV incidence 2000-17 in six ALPHA cohorts including Rakai, giving mean age at infection, age distribution of new infections, and birth-cohort lifetime risk.
author: Risher et al.
published: 2021-07
resource: 10.1016/S2352-3018(21)00069-2
local: ../raw/10.1016/s2352-3018(21)00069-2
tags: [hiv, rakai, modeling]
updated: 2026-09-10 00:30
---

Source: [risher-2021](https://doi.org/10.1016/S2352-3018(21)00069-2)

Lancet HIV analysis from the ALPHA network of six population-based HIV cohorts in Malawi
(Karonga), South Africa (uMkhanyakude), Tanzania (Kisesa), Uganda (Masaka, Rakai) and Zimbabwe
(Manicaland). A Bayesian model jointly reconstructs age-specific HIV incidence and mortality from
repeated serostatus observations plus vital status, so participants who were HIV-positive at
enrolment or tested only once still inform the incidence estimate, rather than only the
seroconverter cohort.

## Relevance to project

Calibration targets for the HIV arm at the Rakai site, resolved by age and sex, which is
finer than the aggregate incidence figures the model would otherwise be fit to.

The usable Rakai numbers, all for ages 15-54 and standardised to the enumerated resident
population:

- Mean age at infection in 2017: 29.2 years in men (95% CrI 27.5-31.0), 25.5 years in women
  (24.2-27.2). Change since 2000: +0.7 years in men, -0.2 years in women. Rakai is the one
  cohort where the female mean age at infection did not drift older.
- Share of new infections in women aged 15-24: 60% (52-69). Share in men aged 20-29: 52%
  (43-61). Both are at the high end across the six cohorts (women 38-63%, men 30-63%).
- Narrowest age band holding 75% of new infections in 2017: 15.0-29.2 years for women,
  18.4-35.8 years for men.
- Cumulative incidence between ages 15 and 49 for the birth cohort turning 50 in 2020: 40%
  of women (32-51). This is a lifetime-risk quantity, not a prevalence, and is far above the
  14-26% prevalence measured at ages 45-54.
- Rakai peaked incidence age pattern persisted through the study period, unlike Karonga,
  Kisesa, Manicaland and Masaka where the age profile flattened.

The shape here bears directly on the risk-structured network. An incidence peak at 20-24 in
women and 25-29 in men, with a roughly 4-year sex gap in mean age at infection that stays
constant over 17 years, is the signature the model's age-mixing and partnership formation
have to reproduce before any POC-versus-SOC contrast is meaningful. If the simulated age
profile is flat where Rakai's is peaked, the arms will differ for the wrong reason, because
prevention targeting lands on the wrong ages.

The cohort spread (women 15-24 carrying 38% of infections in Karonga against 63% in
uMkhanyakude) is a bound on how far a Rakai-calibrated model can be read as representing
eastern and southern Africa generally.

Nothing here touches STIs, diagnostics, or care-seeking. Use it for the HIV target, not for
anything about the intervention.

## Key points

Age-specific incidence declined at every age across all six cohorts, with timing and
magnitude varying. Mean age at infection was consistently higher in men (cohort means
27.8-34.6 years) than women (24.8-29.6), and increased slightly between 2000 and 2017 (men
+0.5 to +2.8 years, women -0.2 to +2.5). Cohorts with lower current incidence and earlier
declines show flatter age profiles and older mean age at infection, which the authors read
as the classic force-of-infection-versus-age-at-infection relation.

The headline caution: 40-60% of infections in women fall outside 15-24, so an
adolescent-girls-and-young-women-only prevention strategy of the DREAMS type misses roughly
half the burden even in the cohorts where the concentration is highest.

Lifetime risk fell for successive birth cohorts everywhere. uMkhanyakude is the outlier at
70% (67-72) of women in the cohort turning 50 in 2020 ever infected, projected to peak at
79% (77-81) for the 2029 cohort.

## Methodology

Incidence hazard is a generalised additive model in time and age, log λ(t,a) = f(t) + f(a) +
f(t,a), each term a penalised B-spline with knots every 5 years. Non-HIV mortality is
additive in time and age with no interaction. Survival after seroconversion is Weibull in
age at infection and duration, scaled in the ART era by an estimated ratio h_ART(t). Fitted
in Stan with NUTS, 4 chains of 500 iterations, last 250 retained. Discretised to 0.2-year
steps. A hypothetical pre-epidemic serosurvey of 451 all-negative adults aged 15-60 anchors
prevalence at zero before HIV arrived.

Rakai contributes 61,887 individuals, 289,135 person-years, 17 serosurveys from 1994, 14% of
tests HIV-positive, ART from 2004.

## Limitations

Rural, geographically localised cohorts originally chosen because they were heavily
HIV-affected, so generalisation to urban populations is not supported. No systematic testing
below age 15 and sparse testing above 54, so results are reported only for 15-54; Rakai in
particular has largely not tested above 49, which is why its 45-54 age band is absent from
the incidence figure. Age bands above 49 are unavailable for the Rakai calibration.

Birth-cohort projections rest on two stylised futures (incidence frozen at the most recent
estimate, or continuing the past 5 years' decline with sex-specific rates converging in
2022), which the authors flag as a place mechanistic modelling would do better.

The analysis estimates acquisition only, not transmission, so it says who gets infected and
at what age but nothing about who infects them. For a model whose premise is finding
high-transmission positions in the network, that is the half of the picture this source does
not supply.
