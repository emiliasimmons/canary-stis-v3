---
type: entry
title: "HIV incidence among women engaging in sex work in sub-Saharan Africa: a systematic review and meta-analysis"
description: 83 empirical incidence estimates from 32 studies, 1985-2020; HIV incidence in women who engage in sex work is 7.8x matched total-population female incidence (4.9x in eastern and southern Africa) with no change in the ratio over time
author: Jones et al.
published: 2024-08-01
resource: https://doi.org/10.1016/S2214-109X(24)00227-4
local: raw/10.1016/s2214-109x(24)00227-4
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:15
---

Source: [jones-2024](https://doi.org/10.1016/S2214-109X(24)00227-4)

Systematic review and meta-analysis of directly measured HIV incidence among women who engage in sex work (WESW) in sub-Saharan Africa, and of that incidence relative to women in the general population living in the same district, of the same age, in the same year. Searches ran to Feb 28, 2024 and yielded 83 incidence estimates from 32 studies covering 1985-2020: 2194 seroconversions over 51,490 person-years. Each WESW estimate was divided by an age-district-year matched total-population female incidence, taken from the UNAIDS Naomi district model for 2022 and extrapolated backwards parallel to national female incidence trajectories, to give an incidence rate ratio (IRR).

## Relevance to project

The usable number here is a **bound on the incidence multiplier for the model's highest-activity female network position**, together with a **comparator** for whether a calibrated run puts too much or too little HIV on that position. Pooled IRR across sub-Saharan Africa is 7.8 (95% CI 5.1-11.8); the regionally appropriate figure for a Ugandan calibration is the eastern and southern Africa estimate, 4.9 (3.4-7.1). Western and central Africa is 19.9 (9.6-41.0) and should not be carried over, because that gap comes mostly from a small general-population denominator rather than higher sex-worker incidence: median WESW incidence in western and central Africa (3.8 per 100 person-years) is slightly lower than in eastern and southern Africa (4.3).

Absolute levels give a second check. Median WESW incidence is 4.3 per 100 person-years (IQR 2.8-7.0) across the whole 1985-2020 span; a calibration should not reproduce that median as a modern target, because the same review shows incidence falling steeply within cohorts (Mombasa, Kenya: 15.8 per 100 person-years in 1994 down to 1.3 in 2017).

The closest data to the calibration site are the three Kampala, Uganda estimates from Kasamba et al (2019), matched to age 15-39: incidence 2.9 per 100 person-years in 2010 (IRR 2.53), 3.3 in 2014 (IRR 3.53), and 3.0 in 2016 (IRR 3.59), against matched total-population female incidence of 1.15, 0.93, and 0.84 per 100 person-years. Those IRRs sit below the ESA pooled value, which matters if the model's high-activity position is calibrated against Uganda specifically.

The time-trend result constrains model behaviour rather than a single parameter. There is no evidence the IRR changed (IRR per 5 years 0.9, 95% CI 0.7-1.2), so a run in which the sex-work position's relative risk drifts as the general epidemic declines is inconsistent with the pooled data, though the Zimbabwe case study (IRR rising 1.6 per 5 years, 1.3-2.1, 2009-2019) shows a single country can depart from that.

The paper carries no STI data, no partner-notification content, and no diagnostic performance figures. It cannot supply a cofactor effect, a testing-coverage prior, or anything about the curable STIs.

## Key points

- Pooled IRR 7.8 (5.1-11.8) SSA; 4.9 (3.4-7.1) eastern and southern Africa; 19.9 (9.6-41.0) western and central Africa. Heterogeneity very high (I-squared 96.9% overall).
- Median IRR 6.1 (IQR 3.9-9.4) is close to the pooled estimate, so the pooling is not being driven by a few extreme studies.
- Sensitivity analyses hold: restricting to the 20 studies scoring above 60% on the quality tool gives 7.0 (4.1-12.0); matching to national rather than district incidence gives 9.5 (6.6-13.7).
- WESW incidence correlates with matched general-population female incidence (Pearson r 0.6, 0.5-0.8), so the two are not decoupled.
- The log-linear mixed-effects model puts the IRR at 4.9 (3.3-7.3) in 2003, lower than the meta-analytic pool, reflecting different weighting of the sparse older estimates.
- 65 of 83 estimates are from eastern and southern Africa, 49 of 83 from Kenya and Zimbabwe alone. Median study year 2008 (IQR 2000-2015).
- No study covered transgender women who engage in sex work, or stratified by gender identity.

## Limitations

Fewer than half of sub-Saharan African countries contribute data, and Uganda contributes one study (a Kampala cohort). Country-specific IRRs could not be estimated, so the ESA pooled value is the finest regional resolution available.

The denominator is modelled, not observed: for all but one study, matched total-population incidence comes from extrapolating 2022 Naomi district estimates backwards in time parallel to national trajectories. Uncertainty in that extrapolation is not propagated into the reported IRRs, and is worst for the oldest studies, which are also the ones with the largest IRRs (Dakar 1987 estimates carry IRRs of 83 to 640 against a matched population incidence of 0.01-0.02 per 100 person-years). Treat individual study IRRs as unusable and the pooled regional values as the product.

Study populations are heterogeneous in what counts as sex work (self-identification, exchange of sex for money or goods, working in a known sex-work venue) and in recruitment (respondent-driven, time-location, clinic, convenience). Clinic- and programme-linked samples plausibly under-sample women in the highest-risk period just after starting sex work. Any model position calibrated to these numbers inherits that definitional fuzziness: the group being measured is not a fixed fraction of the population with a stable risk.

Studies where the cohort was exposed to an HIV-prevention intervention, PrEP in particular, were excluded, so these estimates describe incidence without that protection.

## Methodology

Incidence was mostly derived from seroconversion between repeat HIV tests (27 of 32 studies), typically at the midpoint between last negative and first positive result. Four studies used recency assays, and one back-calculated from age-specific prevalence; for those, person-years were imputed (recency: tested individuals times 0.5), which is why some rows in the extracted table carry constructed rather than observed denominators. Meta-analysis used study-district nested random effects with regional fixed effects; the time trend came from a Bayesian log-linear mixed-effects model with log total-population incidence and person-years as offsets, so its coefficients are on log IRR directly.
