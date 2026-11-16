---
type: decision
title: Settings are hypothetical epidemics crossed by prevalence and phase
description: Four settings cross high (about 25%) or medium (about 15%) HIV prevalence with a mature or expanding epidemic, each an ensemble of simulations selected on prevalence at ages 15-49 in 2026, with STI and HIV biology shared and STI burden left to the model.
tags: [hiv, sti, modeling, study-concept]
updated: 2026-11-15 23:09
---

The study runs four settings: high (about 25%) or medium (about 15%) HIV prevalence, each
as a mature epidemic and as an expanding epidemic. A setting is the ensemble of
simulations, selected from a parameter exploration, whose HIV prevalence lands within
about 3 percentage points of its target, at ages 15-49 with both sexes pooled, in 2026
(the year before the 2027 intervention year), averaged over replicates. Prevalence is the
only quantity selected on. Every simulation also reports its incidence at ages 15-49, the
year that incidence peaked, and the ratio of prevalence to incidence, and the modeller
judges its phase from that trajectory.

The study tests the pathway-decomposition method across kinds of epidemic, so the settings
have to be set apart from one another and recognisable as real kinds of epidemic.
Matching any one site is outside its scope, so settings approximate levels with no formal
calibration.

Phase replaced an incidence cut point as the second axis. Epidemic phase is the
explanation [Hayes 2010](hayes-2010-sti-treatment-hiv-prevention.md) gives for why only
the Mwanza trial, in an expanding epidemic with a prevalence-to-incidence ratio of 4.6
years, cut HIV incidence by treating STIs, while the mature epidemics in Rakai, Masaka and
Manicaland (ratios 10-15) did not. In a mature epidemic most transmission runs through
stable partnerships where curable STIs are less common, which is the contrast the
decomposition is after. Rakai is the standard mature example
([Wawer 1999](wawer-1999-rakai-std-mass-treatment-trial.md)). An incidence axis also
asks for a cell with no explicitly observed population: no cohort combines 10-19%
prevalence with incidence above 1.5 per 100 person-years. The closest comparator is
national, South Africa in 2005 at 16.2% and 2.4 per 100 person-years by recency assay
(prevalence from Rehle 2010, doi:10.1371/journal.pone.0011094; incidence from Rehle
2007, *National HIV incidence measures: new insights into the South African epidemic*).

An expanding epidemic may have already peaked, provided the peak was recent. Measured in
2026, a temporary dip in incidence looks the same as a real decline, so only the full
simulated curve can tell them apart. How recent counts as recent depends on the parameter
ranges the settings experiments explore, so no fixed peak year is set in advance.

Both phases at a prevalence level share one target, so the mature-versus-expanding
contrast is not also a prevalence contrast. Ages 15-49 match most of the comparators,
and including older adults would raise prevalence and lower incidence. A single
measurement year is used because averaging over replicates already removes run-to-run
noise, and in an expanding epidemic a multi-year window would lag the trend.

Curable-STI prevalence differs across settings as an outcome of the model. Each setting's
2026 prevalence of gonorrhoea, chlamydia, trichomoniasis and syphilis is compared against
a sourced band and never selected on. Starting STI prevalences may differ by setting,
preferably by little. STI biology (per-act transmission probabilities, infection
durations, symptom probabilities, treatment efficacy), HIV biology (per-act transmission
probabilities and the STI-to-HIV cofactors) and STI care (care-seeking, the syndromic drug
mix, syphilis testing) are meant to be shared by all four settings, with network structure
expected to drive most of the divergence between them. The direct-treatment and network
pathways both scale with STI burden, and STI parameters set separately for each setting
would make part of their difference across settings a product of those choices.

What produces each phase, which network and HIV-programme parameters move between
settings, which setting the shared STI parameters are first set on, and whether shared
parameters are fixed or explored over common ranges depend on simulation results and are
left to the [settings experiments](../../experiments/settings/STATUS.md).
