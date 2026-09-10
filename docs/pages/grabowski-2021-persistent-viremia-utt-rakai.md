---
type: entry
title: Prevalence and Predictors of Persistent HIV Viremia and Viral Rebound After Universal Test and Treat
description: Population-based longitudinal viral load in four Rakai fishing communities, 2011-2017, giving durable suppression, rebound, and persistent viremia by sex, age, and migration.
author: Grabowski et al.
published: 2021-01-20
resource: 10.1093/infdis/jiab021
local: raw/10.1093/infdis/jiab021
tags: [hiv, rakai, sexual-networks]
updated: 2026-09-10 00:18
---

Repeat viral load measurements on HIV-positive participants in the Rakai Community Cohort Study, restricted to the four Lake Victoria fishing communities (adult HIV prevalence 38-43%), across three surveys with viral load testing: midpoints January 2012 (pre-UTT), May 2015, and January 2017. Universal test and treat was implemented in 2013. The unit of analysis is a visit-pair, two consecutive person-visits classified by suppression status at each end: durable suppression, new/renewed suppression, loss of suppression (rebound), or persistent viremia. Suppression is viral load below 400 copies/mL on the Abbott RealTime assay. 1346 participants contributed 1883 visit-pairs. Extracted text in `raw/10.1093/infdis/jiab021`.

## Relevance to project

A calibration target for the HIV treatment cascade in the RCCS fishing communities, and a bound on how much viral suppression the SOC arm should reach. Population-level durable suppression rises from 29.7% (216/727 visit-pairs) over the 2012-2015 interval to 67.9% (698/1028) over 2015-2017; cross-sectional suppression across all HIV-positive participants including those without follow-up goes 65.5% (1036/1583) to 78.3% (1357/1734). Persistent viremia falls 20.8% to 13.3%. The sex split is the part the model needs most: at the second interval, 19.0% of HIV-positive men (89/469) versus 8.6% of women (48/559) are persistently viremic, and cross-sectional suppression is 72.5% in men against 83.1% in women. A simulation that suppresses men and women equally will put too little virus in the male half of the network.

The persistently viremic subgroup is where onward HIV transmission concentrates, and it overlaps the same risk positions the POC arm is meant to find: persistent viremia is 27.6% among those reporting more than 3 partners in the past year against 14.2% at 0-1 partners, 19.7% among those reporting transactional sex against 15.1% without, and 22.6% among fishing-related workers. This gives an empirical size for the correlation between unsuppressed HIV and high partner turnover in Rakai, usable as a prior for how the model couples viral suppression to network position rather than assigning it independently.

Not a source for STI parameters. Its only STI-adjacent measurement is self-reported genital ulcer disease in the past year, present in 207/1733 sexually active visit-pairs, unassociated with persistent viremia after adjustment (adjRR 1.21, 95% CI 0.90-1.64). The fishing communities are a hyperendemic slice of RCCS, so these levels are not the RCCS-wide cascade.

## Key points

Adjusted relative risks of persistent viremia against durable or new/renewed suppression, from modified Poisson regression with GEE, adjusted for age, sex, marital status, education, occupation, migration, and survey period: male sex 2.09 (1.47-2.95), age 15-29 versus 40-49 1.80 (1.19-2.71), never married versus married 1.88 (1.34-2.62), in-migrant of 0-2 years versus long-term resident 1.91 (1.34-2.73). Among men the migration effect is stronger, 2.09 (1.35-3.23) for recent in-migrants.

Viremia is mostly untreated rather than failing treatment. Among the 274 visit-pairs where the participant did not report ART use, 71.2% were persistently viremic; among the 1609 reporting ART, 7.1% were. Loss of suppression is rare overall, 54 of 1883 visit-pairs (2.9%), and the rate halved between intervals (IRR 0.45, 95% CI 0.26-0.78) while new/renewed suppression rose 48% (IRR 1.48, 1.25-1.75).

Still, one third of persistent viremia sits inside the treated population: 114 of 309 persistently viremic visit-pairs (36.9%) reported ART use, spanning 101 individuals. Geometric mean viral load among persistently viremic visit-pairs was 13 087 copies/mL in ART reporters and 17 007 in non-reporters, not significantly different (P = .127). Among those persistently viremic at the final survey, 81.0% (128/158) acknowledged being HIV-positive, against 99.5% among the durably suppressed.

Among the 537 participants seen at all three surveys, 76.9% (413) reached durable suppression by the third visit, 7.8% (42) were viremic at all three, and 5.0% (27) showed intermittent viremia.

## Limitations

Loss to follow-up was 45.1% (1106/2452), and those lost were disproportionately young, male, recent in-migrants, and unsuppressed at baseline. The authors state their persistent viremia and rebound figures should be read as lower bounds. Inverse probability of selection weighting did not change the associations, but cannot correct for unmeasured differences. Suppression levels differed between those with and without follow-up by a widening margin: 33.1% versus 27.7% at survey 1, 84.4% versus 64.9% at survey 3.

ART use is self-reported with no clinical records or drug regimen, though the authors cite prior work in this population finding 99% of self-reported ART users have at least one detectable antiretroviral drug. No drug resistance testing. The four fishing communities are not representative of the agrarian and trading communities that make up most of RCCS.
