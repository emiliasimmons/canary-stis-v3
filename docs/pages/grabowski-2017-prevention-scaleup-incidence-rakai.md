---
type: entry
title: "HIV Prevention Efforts and Incidence of HIV in Uganda"
description: Seventeen years of RCCS seroconversion data giving population HIV incidence per 100 person-years by survey round and sex, alongside ART, viral suppression and circumcision coverage
author: Grabowski et al.
published: 2017-11-30
resource: https://doi.org/10.1056/NEJMoa1702150
local: raw/10.1056/nejmoa1702150
tags: [hiv, rakai, care-seeking]
updated: 2026-09-10 11:17
---

Observational analysis of 12 Rakai Community Cohort Study survey rounds between April 1999 and September 2016, covering 30 continuously surveyed communities of adults 15 to 49 in Rakai District, south-central Uganda. 33,937 participants contributed 103,011 person-visits; the incidence cohort of 17,870 initially HIV-negative people contributed 58,344 person-intervals and 94,427 person-years, in which 931 seroconversions were observed. Fishing communities are not in this analysis: data collection there began only in 2011. Extracted content in [raw/10.1056/nejmoa1702150/](../raw/10.1056/nejmoa1702150/).

## Relevance to project

This is the primary HIV incidence calibration target for the Rakai site. It supplies a full time series of incidence per 100 person-years with confidence intervals, indexed to survey round and median interview date, for the whole cohort and separately for women, men, and circumcised and uncircumcised men. A model run over 1999 to 2016 on an agrarian-and-trading Rakai population should reproduce both the pre-scale-up level near 1.17 per 100 person-years and the 2016 level near 0.66, with the sex gap intact: incidence fell to 0.46 in men and only 0.84 in women.

It also supplies the coverage trajectories that any HIV counterfactual has to carry: ART coverage among people living with HIV, population viral suppression, and male circumcision coverage, each by year. These are structural inputs to the HIV side of the model rather than free parameters, because the observed incidence decline is conditioned on them.

The source says nothing about STIs. Genital ulcer disease enters only as a self-reported covariate in the regression, with no coefficient reported, and no curable bacterial STI is measured. It cannot be used to attribute any share of the incidence decline to STI treatment, and it cannot bound the HIV-prevention effect of STI diagnostics. The 42% decline it reports belongs to ART and circumcision scale-up in a combination package, and reading it as headroom for an STI intervention would double-count.

Care-seeking here is HIV testing and treatment uptake, not symptomatic presentation for STI care, so it does not inform the rate at which agents arrive at the syndromic-management door.

## Key points

Incidence for the total cohort, per 100 person-years with 95% CI, by survey: pre-scale-up (surveys 2 through 5, roughly 2000 to 2004, 254 infections in 21,765 person-years) 1.17 (1.03-1.32); Jan 2006, 1.11 (0.89-1.36); Oct 2007, 1.20 (0.98-1.44); July 2009, 1.23 (1.02-1.45); Jan 2011, 1.07 (0.88-1.29); June 2012, 0.83 (0.67-1.02); July 2014, 0.66 (0.53-0.81); Jan 2016, 0.66 (0.53-0.81). The adjusted incidence rate ratio for 2016 against pre-scale-up is 0.58 (0.45-0.76).

Women, same measure: 1.17 (0.99-1.37) pre-scale-up falling to 0.84 (0.64-1.08) in 2016, adjusted IRR 0.68 (0.50-0.94). Men: 1.17 (0.96-1.40) falling to 0.46 (0.31-0.65), adjusted IRR 0.46 (0.29-0.73). Uncircumcised men only: 1.21 (0.98-1.47) falling to 0.65 (0.37-1.04), adjusted IRR 0.51 (0.29-0.88). Circumcised men had lower incidence than uncircumcised men throughout, adjusted IRR 0.62 (0.48-0.79), and declined further by 2016, adjusted IRR 0.43 (0.19-0.99).

ART coverage, as the percentage of all HIV-positive participants self-reporting ART use regardless of eligibility, rose from 12% (118/1003) in 2006 to 69% (1051/1526) in 2016, split 61% in men (285/466) and 72% in women (766/1060). Viral suppression, defined as below 1000 RNA copies per millilitre among all HIV-positive participants whether or not on ART, rose from 42% (464/1115) in 2009 to 75% (1151/1526) in 2016. Among those reporting ART use, 94% (1228/1301) were suppressed.

Male circumcision coverage among all men rose from 15% (374/2518) in 1999 to 59% (3177/5361) in 2016, and among non-Muslim men from 3% (77/2217) to 53% (2492/4666). By 2016 the median community-level values across the 30 communities were 70% ART coverage (IQR 61-75) and 61% circumcision (IQR 55-65).

The one behavioural change of any size was delayed sexual debut in 15-to-19-year-olds, from 30% reporting never having initiated sex in 1999 to 55% in 2016 (boys 35% to 56%, girls 28% to 55%). Multiple partnerships among adolescent boys fell from 40% to 19%. Consistent condom use with casual partners did not change measurably in any age group across the period.

Incidence began to decline significantly only in 2012, at which point ART coverage was 36% and circumcision 43%. The authors decline to read these as thresholds, since the two interventions scaled together and the effect may lag.

## Limitations

ART use, circumcision status and sexual behaviour are self-reported. Self-reported ART has been validated in this population at 99% specificity (96-100) and 77% sensitivity (70-83), so coverage is more likely understated than overstated. Circumcision self-report has 100% specificity against clinical records.

Viral loads were run on stored serum, and RNA degradation over storage time would overstate suppression in the earlier surveys and understate the increase.

The cohort is open with heavy migration. Mean participation among all census-eligible people was 64% (range 59 to 67 across surveys), and 42 to 63% of losses to follow-up were out-migration. Participation was lower among the young, among men, among trading-centre residents, and among people reporting higher-risk sexual behaviour, though these gradients were stable over time. Inverse probability weighting for selective participation did not change the inferences.

ART and circumcision scaled concurrently in every community, so their contributions cannot be separated in these data. The design is observational, and unmeasured secular trends are not excluded.

## Methodology

The incidence denominator is person-intervals between consecutive surveys among people HIV-negative at the earlier of the two visits, with one missed visit permitted, and infections placed at the interval midpoint. Median inter-survey gap grew from 1.0 year early on to about 1.6 to 2.0 years later, so the effective observation window per round is not constant, which matters when lining a simulated annual incidence up against a round-indexed observation. Rate ratios come from Poisson regression with generalized estimating equations and an exchangeable correlation structure, adjusted for sex, age, education, community type (agrarian or trading), number of partners in the past year, sex with partners outside the community, non-marital partners, condom use, self-reported genital ulcer disease, and a categorical term for community HIV prevalence. The comparison period is the whole pre-2006 span pooled, not a single round, so the reference is a four-round average rather than a baseline year.
