---
type: entry
title: "PopART-IBM, a highly efficient stochastic individual-based simulation model of generalised HIV epidemics"
description: Model description and ABC calibration of an individual-based HIV model to 248 age- and sex-stratified prevalence and cascade targets in a Zambian HPTN 071 community.
author: Pickles et al.
published: 2021-09-02
resource: 10.1371/journal.pcbi.1009301
local: raw/10.1371/journal.pcbi.1009301
tags: [modeling, hiv, sexual-networks]
updated: 2026-09-10 10:30
---

Source: [pickles-2021](https://doi.org/10.1371/journal.pcbi.1009301)

Description of PopART-IBM, an open-source discrete-time stochastic individual-based model
of heterosexual HIV transmission written in C, built for the HPTN 071 (PopART) trial in
Zambia and South Africa. The paper covers the model structure (demography, partnership
formation and dissolution, HIV transmission and progression, testing and treatment
cascade), a worked ABC calibration to one Zambian trial community, and counterfactual
projections with the trial intervention switched off. The parameter tables, age-mixing
matrices and marginal posteriors are in S1 Appendix, which is not included. Code is at
`github.com/BDIpathogens/POPART-IBM`.

## Relevance to project

A design reference for the network and cascade layers, and a concrete template for what an
ABC calibration of an agent-based HIV model to stratified survey data costs. It supplies no
STI structure at all: the authors state outright that coinfections, including HSV-2 and
anything else modifying HIV transmission, are not modelled, so nothing here bears on the
STI cofactor pathway.

Three uses. First, the risk-structure design. Individuals get one of three sexual activity
levels at entry, fixed for life, which sets both the maximum concurrent partners (1 low, 3
medium, 10 high) and the partnership formation rate. Mixing across activity levels runs
through a single assortativity parameter chi from 0 (proportionate) to 1 (fully
assortative), left free in calibration with a uniform prior on 0.05-0.95. That is the same
one-parameter treatment canary-stis would need if it puts STI and HIV risk on a shared
risk-structured network, and the prior range is a defensible starting bound.

Second, partnership parameters usable as priors or bounds rather than targets, since they
come from Zambia and South Africa. Relative partnership counts by risk group against low
risk were 8.89 (medium) and 22.4 (high) in Zambia, 2.06 and 6.38 in South Africa. Unscaled
within-patch partnership durations were 15.4, 6.1 and 3.8 years for low, medium and high
risk in Zambia (9.80, 6.99, 4.16 in South Africa), with a free multiplier on 1.0-2.0
scaling all durations. Annual within-community partnership formation rates for low-activity
individuals peak at ages 23-29 in men (0.0409 Zambia) and 18-22 in women (0.0177 Zambia).
Reporting bias is handled by a free multiplier on partner counts with a uniform prior on
0.625-5, which the authors justify by noting under-reporting is expected but the range must
cover 1 and allow over-reporting.

Third, the calibration budget. APMC-ABC over 17 free parameters (out of more than 350 in
the model) hit 248 summary statistics, converged after 130 steps and 131,000 simulations,
and took about 37 hours on 12 cluster cores at a 5% stopping threshold (5, 8, 14 and 70
hours at 40%, 20%, 10% and 1%). Each step ran 2,000 simulations, kept the best 50% by
Euclidean distance, and drew 1,000 new parameter sets. A single 120-year run of two patches
of about 50,000 adults each took under 30 seconds and under 2 GB, scaling linearly in
population size.

The 248 targets decompose as 116 prevalence statistics, 60 on awareness of status among
people living with HIV, 60 on ART among those aware, and 12 on viral suppression, all
stratified by age group and sex. Useful as a template for how many stratified targets an
ABC fit of this class can absorb.

## Key points

Timestep is 1/48 year. Simulations start in 1900 so the partnership network stabilises
before HIV is seeded, and seeding is repeated annually over several years so epidemics with
R0 just above 1 are not lost to stochastic extinction.

Transmission occurs only within serodiscordant partnerships, with per-timestep probability
depending on the positive partner's CD4 stage, set-point viral load and ART status, the
negative partner's sex, and medical circumcision in men. Only the net transmission rate is
free (uniform 0.05-0.3 per timestep hazard); relative rates come from the literature. The
male-to-female hazard multiplier was calibrated on a uniform 1-3 prior.

Two spatial patches represent the study community and its surroundings. Individuals form
partnerships across patches but never migrate. Cross-patch partnerships form at 0.562 the
within-patch rate in Zambia and last 0.456 as long, with reduced transmission to reflect
lower coital frequency.

The model fits self-reported ART coverage low while fitting viral suppression well. The
authors read this as the model implicitly correcting for upward bias in self-reported
adherence, and take the viral-load fit as reassurance. No weighting was applied across the
data sources.

Under the counterfactual with trial testing and linkage switched off, incidence declines to
a plateau near 1.02 per 100 person-years by 2030 (model output quantiles 0.665-1.40),
prevalence 15.1% (11.6-18.4%), ART coverage plateauing at 59.2% of people living with HIV,
and incident cases 18.9% higher in 2030 than 2020 (0.0-36.8%) because the population is
growing.

The simulated transmission tree shows two tempi: slow low-branching chains interspersed with
rapid outbreaks among high-risk individuals holding several concurrent partnerships.

## Limitations

Zambia and South Africa, generalised heterosexual epidemics above 10% prevalence. The
authors say it fits poorly where overall prevalence is low and burden concentrates in key
populations.

Omissions the authors list: no transmission outside heterosexual partnerships, no key
populations, no migration, no viral strain structure or drug resistance, no ART regimen
distinction, no condom use, no coinfections.

Sexual activity level is assigned at entry and never changes, so risk is a lifetime
attribute rather than a state that can move with life stage.

The authors warn against generalising their compute times, since these depend on cluster
size, parameter count, data variability and how much each run writes to disk. Runs that
drive HIV extinct finish much faster, so the average simulation during calibration is
cheaper than a calibrated one.

Fit to the three Zambian DHS rounds (2002, 2007, 2013) is visibly worse than to the trial
cohort and CHiPs data, attributed to DHS variability within and between rounds and to being
outnumbered by trial data points.
