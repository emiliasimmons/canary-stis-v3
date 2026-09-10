---
type: entry
title: Large age shifts in HIV-1 incidence patterns in KwaZulu-Natal, South Africa
description: 16-year AHRI cohort showing HIV incidence declines concentrated in young men and women, shifting peak incidence 5 y older in men and 2 y in women
author: Akullian et al.
published: 2021-07-09
resource: 10.1073/pnas.2013164118
local: raw/10.1073/pnas.2013164118
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:23
---

A population-based cohort analysis of HIV-1 seroconversions in the Africa Health Research
Institute (AHRI) surveillance area, rural Umkhanyakude district, northern KwaZulu-Natal,
covering 2004 to 2019 and spanning the scale-up of antiretroviral therapy (ART), voluntary
medical male circumcision (VMMC), and universal test and treat (UTT, instituted September
2016). Extracted content sits in `raw/10.1073/pnas.2013164118`.

The cohort is 22,406 adults (men 15-54, women 15-49) with an HIV-negative test followed by
at least one further test, contributing 103,775 person-years (43,629 men, 60,146 women) and
3,574 seroconversions (887 men, 2,687 women). Overall incidence is 3.4 per 100 py, split
2.0 per 100 py in men and 4.5 per 100 py in women. Seroconversion dates were imputed at
random between last negative and first positive over 300 datasets, and age-year incidence
surfaces were fit with Poisson generalized additive models using thin-plate splines.

## Relevance to project

A comparator and a shape target, not a Rakai calibration target. The model's calibration
site is Rakai, Uganda; this is a different cohort in a different country, so the levels do
not transfer. What does transfer is the qualitative pattern any HIV model of a maturing
southern/eastern African epidemic should reproduce: incidence falling fastest in the
youngest ages and stalling in the 25-39 band, so the age distribution of new infections
drifts older as coverage rises. If the canary-stis HIV component is run out to a period of
ART scale-up and produces a static incidence age profile, that is a structural failure
this paper flags.

It also bears directly on who a point-of-care STI panel would reach. Prevention targeted at
adolescent girls and young women is aimed where incidence is falling fastest; the residual
incidence sits in women 25-39 (IRR 0.96 at 30-34, 0.89 at 35-39, neither significant) and
men 30-34 (IRR 0.85). A diagnostic delivered at a symptomatic care-seeking door, as the POC
arm assumes, has an age reach set by who presents, and the paper argues the prevention
target ages need widening past 25.

Sexual network relevance: the authors' explanation leans on age-assortative mixing plus a
lagged indirect effect, male incidence declining first and female incidence following as
those men's partners age. A risk-structured network with age mixing is the mechanism they
invoke, which supports carrying age mixing in the shared network rather than treating risk
groups as age-flat.

## Key points

Pre-UTT (2004-2015) versus post-UTT (2016-2019) incidence rate ratios, per 100 py, by
5-year age band:

- Men 15-19: 0.92 to 0.32, IRR 0.36 (0.15-0.82), a 64% decline.
- Men 20-24: 2.74 to 0.87, IRR 0.32 (0.18-0.59), 68%.
- Men 25-29: 3.91 to 2.13, IRR 0.54 (0.31-0.94), 46%.
- Men 30-34: 3.26 to 2.78, IRR 0.85 (0.49-1.46), not significant.
- Women 15-19: 5.32 to 3.00, IRR 0.56 (0.43-0.73), 44%.
- Women 20-24: 6.73 to 5.12, IRR 0.76 (0.62-0.96), 24%.
- Women 25-29: 5.96 to 4.53, IRR 0.76 (0.56-1.02), not significant.
- Women 30-34: 4.17 to 4.01, IRR 0.96 (0.64-1.42).

Median age at seroconversion rose 5.5 y in men (25.5 in 2004 to 31.0 in 2019) and 3.0 y in
women (21.0 in 2004 to 24.0 in 2019). The underlying HIV-negative cohort aged less than
that, by 3.0 y in men and 4.0 y in women, so the shift is not purely demographic. Age of
peak incidence moved from 26 to 31 in men (all of it after 2012) and 22 to 24 in women.
Peak age-specific incidence fell from 5.0 to 2.0 per 100 py in men; in women it rose from
6.3 (2004) to 7.3 (2012) before falling to 4.4 (2019). The share of the incidence age
distribution under 25 fell from 20.0% to 10.2% in men and 42.2% to 36.2% in women, both
measured from their 2009 maxima.

Adjusting for individual circumcision status leaves the young-male declines nearly intact
(15-19 IRR 0.43, 20-24 IRR 0.38), so differential VMMC uptake by age is not the main driver.
Cohort context: HIV prevalence in the area rose from 22% (2005) to 37% (2016); ART coverage
among people living with HIV in 2017 was 38.4% in men and 50.6% in women; ever-initiated
ART in the incidence cohort was 33.2%; ever-circumcised among men 37.1% at last visit.

The three mechanisms offered, none tested here: age-targeted primary prevention, uneven
age-specific population viremia (prevalence more than doubling above 25 while ART coverage
rises), and a lower force of infection lengthening time to infection so more susceptible
individuals survive uninfected into older ages.

## Limitations

Unmeasured behavioural change over the 16 years is not accounted for, and differential
change by age could explain part of the shift; the authors lean on stable self-reported
condom use since 2012 as partial reassurance. Non-participation in annual HIV testing ran
34-60%, addressed with inverse probability weights that did not move the age-sex results.
Median time between last negative and first positive was 3.0 y (IQR 1.4-5.8), a long
censoring interval that the random-point imputation is meant to handle. Post-UTT cells are
thin at older male ages, with the 40-54 band returning uninformative intervals (0.00-Inf).
No STI data at all, so nothing here speaks to STI prevalence, cofactor effects, or care
seeking.

## Methodology

Incidence is directly observed serostatus change in a household demographic surveillance
system with annual dried blood spot testing, which is the strongest design for
population-level incidence and is why the age trend is worth taking seriously. The
continuous age-year GAM surface, rather than fixed age bands, is what makes the shift in
peak age readable; the categorical IRRs in Table 2 are the transportable numbers.
