---
type: entry
title: "Temporal dynamics and drivers of durable HIV viral load suppression and persistent high- and low-level viraemia during Universal Test and Treat scale-up in Uganda"
description: RCCS 2015-2020 population-based estimates of durable viral suppression and persistent viraemia, with the demographic and behavioural profile of who stays viraemic
author: Rosen et al.
published: 2024-02-08
resource: 10.1002/jia2.26200
local: raw/10.1002/jia2.26200
tags: [hiv, rakai]
updated: 2026-09-10 00:18
---

Source: [rosen-2024](https://doi.org/10.1002/jia2.26200)

A population-based analysis of longitudinal viral load outcomes among people living with HIV
in 40 Rakai Community Cohort Study (RCCS) communities in southern Uganda across survey
rounds 17-19 (February 2015 to October 2020), spanning the national rollout of Universal
Test and Treat (UTT). Suppression is measured on stored plasma with the Abbott RealTime
HIV-1 assay at a threshold of <200 RNA copies/ml, and the unit of analysis is a visit-pair:
two consecutive visits about 18 months apart, classified as durable suppression, new or
renewed suppression, viral rebound, or persistent viraemia. Viraemia is split into low-level
(200-999 copies/ml) and high-level (>=1000 copies/ml). 3080 participants aged 15-49
contributed 4604 visit-pairs.

## Relevance to project

Supplies the HIV treatment-and-suppression layer the model runs on top of at the Rakai
calibration site, in two uses.

As a calibration target and prior for the viral suppression cascade: 72.4% of visit-pairs
durably suppressed and 11.8% persistently viraemic (weighted, all ages 15-49, both sexes,
2015-2020), rising from 68.4% durable suppression in the February 2015-September 2016 index
window to 76.6% in October 2016-May 2018. The transition matrix from Figure 3 is directly
usable as per-18-month probabilities for an HIV treatment state model: of those suppressed
at index (n=3521), 96.8% stayed suppressed, 2.1% rebounded to high-level and 1.1% to
low-level viraemia; of those with high-level viraemia at index (n=960), 53.0% reached
suppression and 44.7% stayed high-level; of those with low-level viraemia at index (n=123),
53.6% suppressed, 17.9% stayed low-level, 28.5% rose to high-level.

As a prior on the correlation between infectiousness and sexual risk, which is the mechanism
the project's targeting arm depends on. Persistent high-level viraemia concentrates in
exactly the strata that carry STI risk: adjusted risk ratio 2.96 (95% CI 2.21-3.96) for ages
15-29 versus 40-49, 2.40 (1.87-3.07) for males versus females, and 1.38 (1.10-1.74) for
inconsistent condom use with non-marital or casual partners versus people with no partners
or permanent partners only. Persistent viraemia reached 32.0% of visit-pairs among males
aged 15-29 against 15.2% among females of the same age. That gives a defensible non-zero
covariance between HIV infectiousness and network position when the model assigns viral
load to agents, instead of assigning suppression independently of risk group.

It does not supply STI data, HIV incidence, or any diagnostic performance figure, and the
visit-pair design cannot give a monthly or annual transition rate without an assumption
about what happens between visits.

## Key points

- Among visit-pairs with any viraemia at the index visit (23.5%, n=1083), 46.9% remained
  viraemic at follow-up, and 91.3% of that persistent viraemia was high-level.
- Low-level viraemia is not a benign stopping point: 28.5% of people at 200-999 copies/ml
  rose to >=1000 copies/ml within about 18 months, 14 times the rebound rate from suppression.
- 20.8% of persistent high-level viraemia visit-pairs (n=429) were in people self-reporting
  current ART use at both visits, at least 12 months apart, which points at adherence or
  virologic failure rather than never-treated infection. The remaining majority had never
  started ART: at the index visit 79.8% of those with any viraemia reported never using ART.
- Declines in persistent high-level viraemia over calendar period held across sex (males
  adjRR 0.70, females 0.81) and community type (inland 0.83, fishing 0.69), but
  community-level declines were mostly not individually significant and their spread was not
  explained by community type.
- Durable suppression was similar in inland (73.5%) and fishing (71.1%) communities, despite
  HIV prevalence of 9-26% inland versus 38-43% in fishing communities.

## Limitations

Only 62.8% of eligible people living with HIV had the two visits needed for inclusion, and
those excluded were younger, more mobile, and less suppressed (59.3% versus 71.1% suppressed
at index), so the estimates understate viraemia in the source population even after inverse
probability of selection weighting. ART use and all behavioural covariates are self-reported.
No adherence duration, regimen, treatment interruption, or drug resistance data. Viral load
is observed only at the two ends of a >=12-month interval, so intermittent viraemia inside
the interval is invisible and the transition probabilities are interval-scale quantities.
Ages 15-49 only. Fishing-community results transfer poorly outside similar settings.
