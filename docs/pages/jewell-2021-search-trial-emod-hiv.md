---
type: entry
title: Predicting HIV incidence in the SEARCH Trial using EMOD-HIV
description: EMOD-HIV model of UTT in Uganda/Kenya; predicted 4-43% incidence reduction depending on counterfactual
author: Jewell et al.
published: 2021
resource: 10.1097/qai.0000000000002684
basis: abstract
tags: [modeling, hiv]
updated: 2026-09-10 10:21
---

Mathematical modeling study using EMOD-HIV (an agent-based model) to simulate communities
in the SEARCH trial across Uganda and Kenya. Parameterized with demographic data, HIV
prevalence, male circumcision coverage, and viral suppression. Cataloged from abstract;
the full text has not been extracted.

## Relevance to project

A modeling comparator. EMOD-HIV is a major agent-based HIV transmission model, and this
application covers East African communities overlapping in demographics with the Rakai
site. The predicted effect sizes (4-40% reduction between trial arms, up to 43% against
a true control without baseline testing) provide a benchmark for the magnitude of
prevention impact the canary-stis model should be able to reproduce under analogous
universal-test-and-treat scenarios. The parameterization choices (demographic, prevalence,
circumcision, viral suppression) parallel the inputs this project needs.

## Key points

- EMOD-HIV configured for SEARCH communities in Uganda and Kenya, parameterized with
  site-level demographic and HIV cascade data.
- Before unblinding, predicted 4-40% HIV incidence reduction between trial arms.
- Universal baseline testing and rapid ART expansion narrowed the between-arm contrast,
  producing effect sizes smaller than the trial was powered to detect.
- Against a "true control" without baseline testing, the intervention reduced HIV
  incidence by up to 43%.

## Limitations

Abstract-only; the parameterization details, network structure, and calibration approach
are not available from the abstract. SEARCH communities (rural Uganda and Kenya) differ
from Rakai in STI burden and population structure.

## Methodology

Agent-based simulation (EMOD-HIV) calibrated to site-level data from the SEARCH trial.
