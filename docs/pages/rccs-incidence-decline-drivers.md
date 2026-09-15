---
type: synthesis
title: RCCS HIV incidence decline and its drivers
description: The RCCS incidence trajectory by age and sex from the 1990s to 2018, and how much of the decline ART, VMMC, and later sexual debut account for.
tags: [rakai, hiv, modeling]
updated: 2026-09-14 21:36
---

# RCCS HIV incidence decline and its drivers

HIV incidence in the Rakai Community Cohort Study (RCCS, an open population-based cohort
of adults 15-49 across 30-40 communities in south-central Uganda) fell by roughly 40% to
75% between the early 2000s and 2018, fastest in men and in women under 25. Three drivers
already carried in the model as background account for most of it: antiretroviral therapy
(ART) scale-up, voluntary medical male circumcision (VMMC), and rising age at first sex,
and they combine close to additively. For this project the consequence is that
a curable-STI diagnostic competes for the residual these three leave, not for the headline
decline, so reading the 42% ([Grabowski
2017](grabowski-2017-prevention-scaleup-incidence-rakai.md)) or 71% ([Akullian
2026](akullian-2026-hiv-incidence-agyw.md)) drop as STI headroom double-counts scale-up
the model already represents.

## HIV incidence by age and sex, 1990s to 2018

Incidence was flat and high through the 1990s and declined from about 2011-2012. In
1990-1992 it stood near 2.0 per 100 person-years and stayed stable even as prevalence
fell, because HIV mortality removed infected adults faster than seroconversion replaced
them ([Wawer 1997](wawer-1997-prevalence-incidence-mature-epidemics.md)), and the
mid-1990s baseline was 1.5 per 100 person-years ([Wawer
1999](wawer-1999-rakai-std-mass-treatment-trial.md)). Matched against modelled estimates,
adult 15-49 incidence was flat from 2000 to about 2010 and then fell 75-90% over
2010-2023, and Rakai is one of the cohorts whose observed and modelled trends agree
([Stevens 2026](stevens-2026-modelled-vs-empirical-hiv-incidence.md)).

The best-denominated age-and-sex targets, per 100 person-years:

| Group | ~2000-2004 | ~2016-2018 | Decline | Source |
|---|---|---|---|---|
| Total cohort, agrarian + trading | 1.17 | 0.66 | adj IRR 0.58 | [Grabowski 2017](grabowski-2017-prevention-scaleup-incidence-rakai.md) |
| Men, agrarian + trading | 1.17 | 0.46 | adj IRR 0.46 | [Grabowski 2017](grabowski-2017-prevention-scaleup-incidence-rakai.md) |
| Men, inland | 1.05 | 0.34 | 68% | [Monod 2023](monod-2023-genomic-surveillance-rakai-natmicro.md) |
| Women 15-24, inland | 1.42 | 0.36 | 75% | [Monod 2023](monod-2023-genomic-surveillance-rakai-natmicro.md) |
| Women 25-34, inland | 1.51 | 0.84 | 44% | [Monod 2023](monod-2023-genomic-surveillance-rakai-natmicro.md) |
| Women 35-49, inland | 0.90 | 0.56 | 37% | [Monod 2023](monod-2023-genomic-surveillance-rakai-natmicro.md) |
| Fishing communities, all adults | 3.43 (2011) | 1.59 (2017) | adj IRR 0.52 | [Kagaayi 2019](kagaayi-2019-combination-hiv-fishing-communities.md) |

The inland series runs 2003 to 2018 and excludes the Lake Victoria fishing communities;
the agrarian-and-trading total runs 1999 to 2016; the fishing figure is a separate
hyperendemic stratum four to five times inland incidence. A round-indexed long series with
confidence intervals sits in [Santelli 2021](santelli-2021-wealth-hiv-incidence-rakai.md)
(overall 1.45 at 1995-96 to 0.40 at 2016-18), and the round-by-round 15-24 series in
[Grilo 2025](grilo-2025-aya-hiv-declines-rakai.md).

The age distribution of infection drifts older as incidence falls in the young. Median age
at female infection moved from 23.4 to 28.2 years over 2003-2018 while the male median did
not shift, and the female-to-male incidence rate ratio in 2018 was 1.59 ([Monod
2023](monod-2023-genomic-surveillance-rakai-natmicro.md)). Male incidence peaks at 25-34
(IRR 2.21 against 15-24), while women show no such peak ([Santelli
2021](santelli-2021-wealth-hiv-incidence-rakai.md)). Rakai is the one ALPHA-network cohort
where the female mean age at infection did not drift older and the peaked age pattern
persisted through the study period ([Risher
2021](risher-2021-age-patterns-hiv-incidence-alpha.md)).

## Contributions of ART, circumcision, and later debut

The one explicit additive decomposition is an EMOD-HIV model calibrated to the same RCCS
cohort, which attributes the 71% decline in women 15-24 (1.57 to 0.45 per 100
person-years, 2000-2019) across three drivers by holding each at baseline in turn
([Akullian 2026](akullian-2026-hiv-incidence-agyw.md)):

| Driver | Women 15-19, by 2020 / 2050 | Women 20-24, by 2020 / 2050 |
|---|---|---|
| Later age at first sex | 17% / 37% | smaller |
| ART scale-up | smaller | 13% / 43% |
| VMMC | 4-5% / 13-22% | 4-5% / 13-22% |
| Combined (additive) | 32% / 74% | 19% / 65% |

Age at first sex rose about three years in women and two in men over the period and is the
largest contributor for adolescents; ART carries the 20-24 band; VMMC is modest
historically and grows over longer horizons.

The observed cohort corroborates each driver but cannot separate them. ART and
circumcision scaled concurrently in every community, so their contributions are not
identifiable from the incidence data alone, and the significant decline began in 2012 when
ART coverage was 36% and circumcision 43% ([Grabowski
2017](grabowski-2017-prevention-scaleup-incidence-rakai.md)). Circumcision protects men
directly at an individual effectiveness of adjusted IRR 0.47 that does not decay over time
([Loevinsohn 2021](loevinsohn-2021-vmmc-effectiveness-rakai.md)), and the sex-lagged
pattern follows: incidence turned down in men after 2010-2011 and in women about five
years later, as circumcision protected men first and women followed through reduced
partner prevalence ([Grilo 2025](grilo-2025-aya-hiv-declines-rakai.md)). The behavioural
change of any size was delayed debut, with never-had-sex among 15-19s rising from 30% to
55% while consistent condom use stayed flat ([Grabowski
2017](grabowski-2017-prevention-scaleup-incidence-rakai.md)).

Male treatment specifically drives the diverging female trend. Men supply 62.8% of onward
transmission while holding 49.2% of unsuppressed virus in 2018, so the counterfactual
gains sit in the male cascade: closing half the male suppression gap cuts female incidence
25%, closing it entirely 51%, and reaching 95-95-95 in men 58% ([Monod
2023](monod-2023-genomic-surveillance-rakai-natmicro.md)). Any POC-versus-SOC incidence
difference sits against a 25-58% counterfactual from male ART alone in the same
communities.

## Background coverage: ART, suppression, and circumcision

These enter as conditioned inputs, since the observed incidence decline is measured
against them. ART coverage among people with HIV rose 12% (2006) to 69% (2016), population
viral suppression 42% (2009) to 75% (2016), and male circumcision among all men 15% (1999)
to 59% (2016) ([Grabowski 2017](grabowski-2017-prevention-scaleup-incidence-rakai.md)). By
2022 suppression among people with HIV reached about 90% and the population prevalence of
viremic HIV, the quantity governing force of infection, had fallen 4.6-fold to 1.7%
([Martin 2025](martin-2025-dolutegravir-transition-rakai.md)). Running these coverage
curves flat would misattribute the decline to whatever else the model varies, including
the STI pathway.

## Denominator, exclusion bias, and age composition

Incidence targets must be built from seroconversions between consecutive visits.
First-positive counts overstate local incidence, because at round 16 in-migrants were 57%
of newly detected HIV but only 14% were true incident cases with a prior negative test
([Grabowski 2020](grabowski-2020-migration-hotspots-rakai.md)).

The published RCCS prevalence and viremia targets understate the youngest band. Residents
of newly built households, 12% of censused adults by 2018 and rising, are counted but not
surveyed. Overall seroprevalence stays near-unbiased, but predicted 15-24 prevalence is
4.9% against 2.6% observed, and population viremia rises from 1.7% to 2.1% once they are
included ([RCCS exclusion bias](rccs-new-household-exclusion-bias.md)). Viremia is the
quantity closest to force of infection, so a viremia or suppression target drawn from RCCS
should be shifted up.

RCCS and the global models disagree on the age composition of new infections. RCCS and its
sibling cohorts put 15-24s at a median 25% of new infections in 2017-2022 and falling,
with incidence dropping 7% per year at 15-24 against 3% per year at 25-49, while UNAIDS
Spectrum assigns 40-50% under a constant age pattern, fixed over time in 58 of 74
sub-Saharan Spectrum files ([Stevens
2026](stevens-2026-modelled-vs-empirical-hiv-incidence.md)). A network built to a static
age profile places too much incidence in the youngest band.

## Open questions

No entry separates ART from VMMC in the observed Rakai data. The two scaled together, and
the only clean separation is the EMOD counterfactual ([Akullian
2026](akullian-2026-hiv-incidence-agyw.md)), which is a model rather than a measurement.
The absolute per-round incidence series for the exact fitting window lives in source
tables ([Grabowski 2017](grabowski-2017-prevention-scaleup-incidence-rakai.md), [Monod
2023](monod-2023-genomic-surveillance-rakai-natmicro.md)) and a Zenodo dataset behind
[Stevens 2026](stevens-2026-modelled-vs-empirical-hiv-incidence.md), which is where the
calibration targets should be pulled from rather than from the summary figures above.
