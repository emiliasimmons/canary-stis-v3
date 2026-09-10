---
type: entry
title: Dynamics of spread of HIV-1 infection in a rural district of Uganda
description: 1989-90 population serosurvey of 21 clusters in Rakai district, showing a roadside-to-agricultural HIV prevalence gradient of 38.5% to 8.6%
author: Wawer et al.
published: 1991-11-23
resource: https://doi.org/10.1136/bmj.303.6813.1303
local: raw/10.1136/bmj.303.6813.1303
tags: [hiv, rakai, sexual-networks]
updated: 2026-09-10 00:34
---

The baseline seroprevalence survey of the population that later became the Rakai Community
Cohort Study. A two-stage cluster sample of Rakai district, south-west Uganda: 21 of the
district's 780 level-one resistance committees were selected at random, with trading-centre
committees deliberately oversampled, then one index household plus 39 contiguous households
enrolled in each, for 840 households. Everyone aged 13 and over resident at least three
months of the year was enumerated (1927 adults); 1292 (594 men, 698 women) gave blood and
answered a sociodemographic, sexual-behaviour and STI-symptom questionnaire. HIV-1 status
was screened by ELISA (Recombigen, stated sensitivity 98.8%, specificity 93.3%) and
confirmed by western blot on all positives plus 200 random negatives. Extracted text in
`raw/10.1136/bmj.303.6813.1303`.

## Relevance to project

A pre-intervention, pre-ART anchor for HIV prevalence in the calibration site, and the
clearest early statement that the risk structure in Rakai is geographic as much as it is
individual.

Two concrete uses. First, a burden target for the epidemic's early phase: weighted adult
(13+) district seroprevalence 12.6% (95% CI 8.7% to 16.5%, design effect 3.5) around
1989-90, against 19.7% crude in the oversampled sample. If the simulation is initialised
before the RCCS rounds proper, this is the number the initial prevalence should reproduce,
with the sampling weight applied rather than the raw sample figure.

Second, a bound on how much heterogeneity the risk-structured network has to carry. Cluster
prevalence ranged from 1.2% to 52.8%, a factor of forty across communities in a single
district. By stratum, adult prevalence was 38.5% in main-road trading centres, 25.4% in
rural trading villages, and 8.6% in rural agricultural villages; the crude relative risk
against agricultural villages was 3.3 (2.0 to 5.1) for men and 5.0 (3.5 to 7.4) for women
in trading centres. A model whose highest-risk group sits only two- or three-fold above the
lowest cannot reproduce this spread. The behavioural correlates give the mechanism the
network layer should encode: two or more partners in the past five years reported by 61.6%
of trading-centre men versus 33.0% of agricultural-village men, and by 30.0% versus 9.0% of
the corresponding women; transactional sex ("sex for pay or gift") 10.2% versus 4.2%.

The sex ratio of infection is the most useful single feature for the network. Among 20-34
year olds in trading centres, 57% of women were positive against 39% of men, and among
13-19 year olds 50% of women against 0% of men (0/29). Female excess concentrated in the
youngest bands, in exactly the communities with bars, lodges and through traffic, is the
signature of age-disparate mixing plus a small commercial-sex core, and is what an age-mixing
and sex-work parameterisation should be checked against.

What it cannot supply: no incidence, no STI test results, no partnership-level data, and no
follow-up. Reported STI history is symptom recall only (20.3% of trading-centre adults
versus 10.9% in agricultural villages), so it does not serve as a gonorrhoea, chlamydia,
syphilis or trichomoniasis prevalence target. It also predates ART, male circumcision
scale-up and the RCCS interventions, so it is a starting condition and not a comparator for
either arm.

## Key points

- Weighted district adult seroprevalence 12.6%, consistent with the 12.1% preliminary
  Ugandan national serosurvey figure for the rural central region.
- Sample prevalence 14.8% in men, 23.9% in women.
- Stratification into main-road trading centre, rural trading village, and rural
  agricultural village was set a priori from community characteristics (hotels, bars,
  distance to main road), not from prevalence, and it explained prevalence better than any
  behavioural variable: standardised beta 0.600 for men and 0.838 for women.
- In cluster-level multiple regression, the proportion of the cluster working in agriculture
  was the only significant predictor for men (beta -0.677) and the strongest for women
  (beta -0.807). For women, multiple partners (0.814), travel to Kampala or abroad (0.579)
  and injections in the past year (0.483) also entered. After adjusting for stratum, only
  multiple partners survived for women (0.446).
- The gradient runs against information access: 98% in the two trading strata knew of AIDS
  versus 89% in agricultural clusters, and education and health-care access were also
  higher where prevalence was higher.
- The authors read the gradient as diffusion from main-road centres through secondary-road
  trading villages into agricultural villages, introduced largely by male travel and
  onward partnering after return.

## Limitations

- Cross-sectional. The diffusion claim is inferred from a prevalence gradient at one time
  point, with no contact tracing and no repeat rounds; a stable endemic gradient would look
  the same.
- Ecological regression at the cluster level (21 units, up to four predictors), so the
  coefficients describe communities, not individuals, and the model is thin on degrees of
  freedom.
- Trading centres were deliberately oversampled, so every crude sample figure overstates the
  district; only the weighted 12.6% is district-representative, and its design effect of 3.5
  widens the interval substantially.
- 1292 of 1927 enumerated adults (67%) were surveyed. Absence was mostly work or visits away
  from the village, which is itself the mobility correlated with infection, so the
  direction of the resulting bias is toward underestimation.
- ELISA specificity 93.3% is low, though western blot confirmation of all positives limits
  the effect on prevalence.
- Age-stratified cells are small (for example 1/30 and 0/29 in the youngest bands), so
  stratum-by-age-by-sex prevalences carry wide uncertainty.
