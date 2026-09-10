---
type: entry
title: Association of Medical Male Circumcision and Antiretroviral Therapy Scale-up With Community HIV Incidence in Rakai, Uganda
description: Population-level effect of MMC and ART scale-up on community HIV incidence in 45 Rakai communities, 1999-2013.
author: Kong et al.
published: 2016
resource: https://doi.org/10.1001/jama.2016.7292
basis: abstract
tags: [rakai, hiv]
updated: 2026-09-10 10:02
---

Ecological analysis of person-level data from population-based surveys in 45 rural Rakai
communities, 1999-2013, examining whether increasing community-level coverage of medical
male circumcision (MMC) and antiretroviral therapy (ART) was associated with reduced
community HIV incidence. Published in JAMA.

## Relevance to project

The model runs on the Rakai population with ART and VMMC as background prevention that is
already in place when the POC diagnostic intervention is switched on. This study provides:

- **Background-prevention coverage trends**: community-level MMC and ART coverage
  trajectories in Rakai over 1999-2013, needed to parameterize the model's exogenous
  prevention scale-up.
- **Community-level HIV incidence calibration target**: incidence trends across 45
  communities over 14 years, stratified by prevention coverage, usable for validating
  whether the model reproduces the observed decline.
- **Effect-size bound**: the population-level incidence reduction attributable to MMC and
  ART quantifies how much of the HIV decline is already accounted for by these
  interventions, bounding the residual that STI treatment could address.

The study is ecological (community-level exposure, person-level outcome), so it does not
establish individual-level causal effects. It does not measure STI prevalence or
treatment, so the STI-mediated pathway is not isolated.

## Key points

- Covers the full RCCS sampling frame (45 communities) over a long observation window
  (1999-2013), spanning the pre- and post-scale-up periods for both MMC and ART.
- Uses person-level HIV seroconversion data linked to community-level coverage, combining
  the strengths of individual outcome ascertainment with ecological exposure variation.
- Provides one of the few direct estimates of population-level prevention impact for MMC
  and ART in a well-characterized African cohort.

## Limitations

- Ecological exposure assignment: individual MMC and ART status are not used as exposures,
  so unmeasured community-level confounders could bias the association.
- Ends in 2013, before universal test-and-treat and PrEP rollout.
- Restricted to rural Rakai communities; the effect sizes may not transfer to urban or
  peri-urban settings.

## Methodology

Person-level HIV seroconversion (paired sera at consecutive RCCS visits) modeled against
community-level MMC and ART coverage using modified Poisson regression with
generalized estimating equations accounting for community clustering. Exposure is lagged
community coverage; outcome is individual seroconversion.
