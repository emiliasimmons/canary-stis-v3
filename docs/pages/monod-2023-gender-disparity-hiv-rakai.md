---
type: entry
title: "Growing gender disparity in HIV infection in Africa: sources and policy implications"
description: RCCS incidence, viral suppression and deep-sequence transmission flows by age and sex over 2003-2018, plus counterfactual scenarios closing the male suppression gap.
author: Monod et al.
published: 2023-03-20
resource: 10.1101/2023.03.16.23287351
local: raw/10.1101/2023.03.16.23287351
tags: [hiv, rakai, sexual-networks, modeling]
updated: 2026-09-10 00:31
---

medRxiv preprint combining the Rakai Community Cohort Study incidence cohort with
longitudinal HIV deep-sequence phylogenetics across nine survey rounds (rounds 10-18,
September 2003 to May 2018) in 36 inland communities of south-central Uganda. Fishing
communities are excluded; 28 of the 36 communities were surveyed continuously. 36,988
participants aged 15-49 enrolled, 22,729 seronegative at first survey contributing an
estimated 127,217 person-years and 1,100 incident infections. 2,174 participants with HIV
were deep-sequenced, yielding 227 heterosexual source-recipient pairs with a consistent
inferred direction of transmission placed in calendar time. Transmission flows were fitted
with a semi-parametric Poisson regression constrained to reproduce the age- and
sex-specific incidence trend, so the phylogenetic and cohort data are not independent
pieces of evidence.

## Relevance to project

Rakai is the first planned calibration site, so this is the closest thing the project has
to a full set of HIV calibration targets on the RCCS frame, over the same 15 years the
model would be run through.

Incidence targets per 100 person-years, inland communities, ages 15-49 unless stated,
2003 (round 10) to 2018 (round 18): men 1.05 [1.03-1.08] falling 67.8% to 0.34
[0.33-0.35]; women 15-24 1.42 [1.35-1.5] falling 74.5% to 0.36 [0.33-0.40]; women 25-34
1.51 [1.45-1.57] falling 43.9% to 0.84 [0.80-0.89]; women 35-49 0.90 [0.85-0.94] falling
37.4% to 0.56 [0.52-0.60]. Median age of female incident infection moves from 23.4
[22.6-24.1] to 28.2 [27.1-29.2]; the male median does not shift. The female-to-male
incidence rate ratio in 2018 is 1.59 [1.38-1.82].

Treatment-cascade targets, among people with HIV in 2018: viral suppression (below 1,000
copies/mL) at age 20 is 59.5% [51.4-67.2] in women against 29.2% [17.9-42.4] in men, at
age 30 75.8% [71.7-79.7] against 54.7% [47.6-63.0], at age 40 92.1% [89.3-94.8] against
76.1% [69.2-82.1]. These pin the ART arm of the model by sex and age, and the widening
gap is what drives the diverging incidence trends.

Network-structure checks. The share of onward transmission from men rises from 57.9%
[56.1-59.6] in 2003 to 62.8% [60.2-65.2] in 2018, while men account for only 49.2%
[44.3-54.1] of unsuppressed viraemia in 2018. A model that assigns transmission in
proportion to infectious person-time will therefore under-attribute transmission to men by
roughly 14 percentage points, and the residual has to come from per-act infectivity,
contact structure, female susceptibility, or male circumcision. Age mixing: the median age
of transmitting male partners rises from 28.7 [27.1-30.1] to 33.3 [31.0-35.7] years, and
in 2018 the median age gap between an incident infection in a woman aged 15-24 and her
transmitting partner is 9.0 [6.0-11.0] years against a reported median partner age gap of
3.6 [3.5-3.9] years for the same women. Transmitting partners are drawn from an older tail
than the reported mixing matrix, which is a direct bound on how a risk-structured network
must be parameterised: matching reported age mixing alone will not reproduce the observed
flows.

Flow shares to bound the network by 2018: to women 15-24 from men 0-6 years older 8.7%
[6.2-11.7] and from men 6+ years older 11.5% [8.6-14.7], both down about a third from 2003
(16.0% [12.8-19.3] and 15.5% [12.2-18.8]); to women 25-34 from men 0-6 years older 8.5%
[7.0-10.2] in 2003 doubling to 13.2% [10.5-16.0]; to men 25-34 from women 0-6 years older
11.0% [9.3-12.6].

As a comparator for the POC arm, the counterfactual scenarios give the incidence reduction
achievable through the male treatment cascade alone in this population: closing half the
male-female suppression gap reaches 75.1 [53.9-96.0] additional men and cuts female
incidence 25.2% [24.2-26.2]; closing it entirely reaches 150.2 [107.8-193.0] men and cuts
female incidence 50.6% [48.7-52.7]; 95-95-95 in men reaches 172.6 [136.8-210.0] men and
cuts female incidence 58.4% [55.1-61.6]. Any HIV-prevention benefit attributed to
point-of-care STI diagnostics sits against a 25-58% counterfactual from male ART alone in
the same communities.

The source carries no STI data and says nothing about care-seeking, syndromic management,
or the STI cofactor effect, so it cannot inform the STI side of the model. It also does
not report absolute numbers of infections averted, only proportional reductions in 2018.

## Limitations

Participation averaged 69% overall (63% men, 75% women), and non-participants, mostly
absent for work or school, are modelled using first-time participants as a proxy; the
authors' sensitivity analyses indicate more men would need to be reached than the headline
counterfactuals imply. Suppressed individuals could not be deep-sequenced, and sequence
coverage of participants with HIV was 46-56% from round 14, falling over time as
suppression rose. Direction of transmission cannot be established for an individual pair,
only in aggregate. Viral suppression before round 15 is imputed from self-reported ART use
adjusted by sensitivity and specificity measured in rounds 15-16, so the early suppression
series is a derived quantity. Reported female contact rates were adjusted upward for
under-reporting using a Bayesian rate-consistency model, meaning the age-mixing comparison
depends on that correction. Findings are for rural and semi-urban inland communities and
do not extend to fishing communities, urban areas, or key populations.
