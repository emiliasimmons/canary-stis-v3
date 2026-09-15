---
type: entry
title: "Evaluating the biomedical and behavioral drivers of HIV incidence decline in adolescent girls and young women in Uganda"
description: EMOD-HIV model calibrated to RCCS quantifying additive contributions of ART, VMMC, and delayed sexual debut to 71% HIV incidence decline in AGYW 15-24
author: Akullian et al.
published: 2026-03-25
resource: https://doi.org/10.1371/journal.pmed.1004993
local: raw/basis/pmed.1004993.pdf
tags: [hiv, rakai, modeling]
updated: 2026-09-04 16:20
---

Source: [akullian-2026](https://doi.org/10.1371/journal.pmed.1004993)

Agent-based EMOD-HIV model calibrated to 20 years of Rakai Community Cohort Study data (1999-2019, ~40,000 adults, 30 communities in southern Uganda).

HIV incidence among women 15-24 declined 71% between 2000 and 2019, from 1.57 to 0.45 per 100 person-years. The study decomposes this decline across three drivers using counterfactual scenarios.

## Key points

- Age at first sex increased by ~3 years in women and ~2 years in men over the study period. This was the largest contributor to incidence decline in adolescents 15-19, averting 17% of cumulative infections by 2020 and 37% by 2050.
- ART scale-up had the greatest impact among women 20-24, averting 13% of infections by 2020 and 43% by 2050.
- VMMC contributed modestly to historical declines (4-5% of infections averted by 2020) but has larger projected effects over longer horizons (13-22% by 2050).
- The three drivers acted largely additively. Combined, they averted 32% of infections in women 15-19 and 19% in women 20-24 by 2020. By 2050, the combined effect reaches 74% and 65%.
- Delayed AFS restructured the sexual network: younger women formed fewer relationships, but older women (23-31) formed more as male partners redistributed.

## Relevance to project

The model is from IDM and uses EMOD-HIV calibrated to the same Rakai cohort that anchors canary-stis. The incidence targets (age- and sex-specific, 2000-2019) and the ART/VMMC coverage trajectories are directly usable as calibration comparators. The counterfactual decomposition framework (one driver removed at a time, effects measured as cumulative infections averted) is a template for the POC/SOC pathway analysis.

The paper models STIs as a generic transmission cofactor but does not disaggregate by pathogen, which is the gap canary-stis fills.

## Methodology

Stochastic agent-based network model (EMOD-HIV) with a pair formation algorithm that structures heterosexual partnerships by age. Calibrated to age-, sex-, and year-specific HIV prevalence and population counts. 100 best-fitting parameter sets sampled from 6,600 simulations via roulette resampling. Counterfactual scenarios hold one driver at baseline levels while others follow observed trajectories.

## Limitations

- Relies on self-reported sexual behavior (AFS, partnership data).
- Cannot capture all real-world sexual network dynamics.
- PrEP not included because of limited availability in the study population.
- STIs treated as a generic cofactor, not disaggregated by pathogen.
