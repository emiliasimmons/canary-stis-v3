---
type: entry
title: Factors Associated with Short and Long Term Mobility and HIV Risk of Women Living in Fishing Communities Around Lake Victoria
description: Cross-sectional survey of 901 women in six Lake Victoria fishing villages; 72% took an overnight trip in 4 months, and longer trips carried more condomless sex.
author: Bahemuka et al.
published: 2022-09-10
resource: https://doi.org/10.1007/s10461-022-03824-0
local: ../raw/10.1007/s10461-022-03824-0
tags: [hiv, sexual-networks, care-seeking]
updated: 2026-09-10 00:36
---

Source: [bahemuka-2022](https://doi.org/10.1007/s10461-022-03824-0)

A cross-sectional survey run by the Lake Victoria Consortium for Health Research in six fishing
villages across Kenya (Kete, Ogal), Tanzania (Kayenze, Itabagumb) and Uganda (Kiimi, Lambu),
each village of roughly 1000 residents with prior-survey HIV prevalence between 15 and 34%.
Roughly 150 women aged 15 and over were randomly sampled per village from a dwelling census, 901
in total, and interviewed once between March 2018 and June 2019 about overnight trips in the
preceding four months. The outcome is trip duration, not HIV status: nobody was tested, and no
incidence or prevalence was measured in this sample.

## Relevance to project

Context, not a target or a prior. The model runs a closed population on a static risk-structured
network in Rakai, and this survey says how badly that assumption fails in a comparable East
African high-prevalence setting: 645 of 901 women (71.6%) reported at least one overnight trip
away from the village in four months, and 164 of 901 (18.2%) had a most-recent trip of seven
nights or more. Only 100 of 645 recent trips (15.5%) went to another fishing community; 462
(71.6%) went to a regional town or another town or district. Turnover on that scale means a
fraction of both HIV and STI transmission for women in this kind of community happens outside the
simulated network, so an incidence gap between the model and data from a fishing or trading
population is expected rather than a calibration failure. Rakai's own communities differ, and the
number that transfers is the ordering of magnitudes, not the percentages.

For the diagnostic arms, the useful figure is care-seeking outside the community. Among
single-night trips, 63 of 275 (22.9%) were taken to seek health care, against 13 of 205 (6.3%)
for trips of two to six nights and 17 of 164 (10.4%) for a week or more. Both arms of the model
put the symptomatic care-seeking door inside the simulated community. Where a fifth of short
trips exist to reach care elsewhere, an in-community point-of-care panel reaches fewer symptomatic
women than the arm's coverage parameter implies, which is a bound on the POC benefit in a mobile
subpopulation rather than a value to fit.

Sexual activity on a trip is too rare here to parameterize anything: 50 of 645 women (7.8%)
reported sex on the most recent trip, 36 of them without a condom. Treat that as a floor under
heavy social desirability bias, not as a mixing rate.

## Key points

Adjusted prevalence ratios come from a two-level multinomial logistic regression on the 645
travellers, clustered at country level, with a single night away as the base outcome.

Trip duration falls with age. Women aged 46-75 were less likely than women aged 15-24 to take a
trip of a week or more rather than a single night, aPR 0.41 (95% CI 0.18-0.91).

Purpose dominates. Against trading, a trip to visit family, friends or a partner ran aPR 5.23
(2.14-12.81) for two to six nights and 4.89 (1.98-12.10) for a week or more; a trip home ran
15.16 (3.35-68.61) and 9.03 (1.81-45.10). Seeking health care was indistinguishable from trading,
aPR 1.13 (0.41-3.11) and 1.06 (0.39-2.90).

Frequency trades off against duration. Women who took one trip in four months, against more than
two, had aPR 4.33 (2.54-7.37) for a trip of a week or more. The mobile population splits into
frequent short movers and occasional long movers.

Condomless sex on the trip tracked duration: aPR 5.24 (1.76-15.63) for two to six nights and
5.86 (1.90-18.06) for a week or more, against reporting no sex. Protected sex reached
significance only at a week or more, aPR 4.44 (1.05-18.88) on 14 events.

Destination matters. Against another fishing community, a regional town gave aPR 2.27
(1.14-4.51) for two to six nights, and another town or district 3.52 (1.87-6.64).

## Limitations

Cross-sectional, so the direction between long trips and condomless sex is unresolved: the
authors themselves raise that some long trips are to a marital home, where sex is condomless for
reasons unrelated to risk. Prevalence ratios are labelled as such rather than as relative risk
ratios for this reason.

The six villages were selected, not sampled, from the Lake Victoria shoreline, and the authors
say the results do not generalize to all fishing communities there. Fishing communities are
themselves a high-prevalence outlier, so nothing here transfers to a general adult population.

No woman self-reported sex work as an occupation, in communities where sex work is documented,
and only 7.8% reported any sex on a trip. Both figures are implausibly low and mark the size of
the social desirability problem in the behavioural variables.

Four-month recall on trip counts and destinations. Twelve women could not remember how often they
travelled.

Confidence intervals on the travel-purpose ratios are enormous (3.35 to 68.61 for a trip home),
resting on 3 to 14 events per cell. Rank the purposes; do not use the point estimates.
