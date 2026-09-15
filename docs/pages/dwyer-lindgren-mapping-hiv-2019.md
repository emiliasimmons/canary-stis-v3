---
type: entry
title: Mapping HIV prevalence in sub-Saharan Africa between 2000 and 2017
description: Gridded 5x5-km Bayesian estimates of adult HIV prevalence across 47 countries, quantifying how much HIV prevalence varies within a country.
author: Dwyer-Lindgren et al.
published: 2019-05-15
resource: 10.1038/s41586-019-1200-9
local: raw/dwyer-lindgren_mapping_2019
tags: [hiv]
updated: 2026-09-10 00:06
---

Source: [dwyer-lindgren-2019](https://doi.org/10.1038/s41586-019-1200-9)

An IHME geospatial mapping paper estimating HIV prevalence among adults aged 15-49 on a 5x5-km grid, annually 2000-2017, for 47 sub-Saharan African countries, along with the number of people living with HIV per cell. Estimates are aggregated up to first- and second-level administrative subdivisions and calibrated to national GBD 2017 figures.

## Relevance to project

Context for the geographic targeting argument, and an external check on how far a single-site calibration travels. The project calibrates to one setting (Rakai, southern Uganda), and this paper puts a number on the spread that assumption papers over: 36 of 47 countries show more than a twofold difference in adult prevalence between their lowest and highest second-level subdivisions, and 14 show more than fivefold. A Rakai-calibrated HIV prevalence level is a point in that distribution, not a national average, so results transported elsewhere carry the subnational spread as their uncertainty.

It also supports the prevention-targeting half of the project's pathway split. The paper's own framing is that local prevalence is the substitute for local incidence data, which is what geographically targeted prevention allocation has to run on. That is the same logic the POC arm uses at the individual level: a positive STI test marks a person likely to be in a high-transmission position, where a high-prevalence grid cell marks a place.

What it is not: no incidence, no STI prevalence, no partnership or network structure, and nothing on treatment coverage. Prevalence here is the joint outcome of incidence, mortality, and migration, and the authors say explicitly that a subnational rise in prevalence is not by itself a rise in transmission, since ART-driven survival pushes prevalence up while incidence falls. So it cannot serve as a calibration target for the model's incidence, and its prevalence estimates are too coarse and too uncertain at grid-cell level to target a single community.

## Key points

Sub-Saharan African adult prevalence fell from 5.5% (5.2-5.7%) in 2000 to 4.0% (3.8-4.2%) in 2017, while the number of people living with HIV aged 15-49 rose from 17.0 million (16.3-17.8) to 20.1 million (19.0-21.2) on population growth.

Within-country range at the district level is large in both high- and low-prevalence settings. Botswana, national 22.8% (19.8-26.1%), ranges 15.1% to 27.7% across districts. Tanzania, national 3.9% (3.6-4.3%), ranges 0.4% in Kusini Pemba to 9.1% in Njombe. In the DRC, national 0.7%, districts range 0.3% to 1.4%: a small absolute gap, a large relative one.

Direction of change is not uniform inside a country. Between 2000 and 2017, 20 of 47 countries (42.6%) contained second-level subdivisions moving in opposite directions; at grid-cell level that rises to 28 of 47. Mozambique holds both a 5.8-point decline (Manica) and a 17.2-point increase (Guija).

People living with HIV are spatially concentrated but with a long tail: 34.3% live in the 0.2% of grid cells holding more than 1,000 each, while a comparable 32.0% live in cells holding fewer than 100 each. The concentrated cells grew 37.5% between 2000 and 2017; the sparse ones were flat. Prevention strategies that assume concentration miss roughly a third of the epidemic.

Areas outside southern Africa (districts in Kenya, Malawi, Uganda, Tanzania) exceed 10% adult prevalence even where the national figure is well below that.

## Methodology

Inputs are 29,103 data points from 134 seroprevalence surveys in 41 countries and 9,794 antenatal-clinic sentinel surveillance points from 1,858 sites in 46 countries. Prevalence is modelled as binomial with a logit link, combining a regional intercept, covariate effects, country random effects, a space-time Gaussian process (Matern in space, AR1 in time), and a nugget. Antenatal-clinic bias relative to general adult prevalence is absorbed by a fixed offset plus a spatially varying term, and predictions are made with that indicator set to zero. Fitted in R-INLA with the SPDE approximation, separately for four GBD regions, then raked so national population-weighted means match GBD 2017.

Covariates are stacked (generalized additive models, boosted regression trees, lasso, five-fold cross-validated). Eight were built for this analysis from survey data: male circumcision, self-reported STI symptoms, marriage or cohabitation, partner living elsewhere, condom use at last sex, ever had sex among young adults, and multiple partners in the past year for men and for women separately. Self-reported STI symptoms therefore enter as a spatial predictor of HIV prevalence, though the paper reports no coefficient for it in the extracted text and stacking makes any single covariate's contribution hard to read off.

Code is at https://github.com/ihmeuw/lbd/tree/hiv-africa-2019, estimates at the Global Health Data Exchange.

## Limitations

Data coverage has real spatial and temporal gaps, and grid-cell estimates carry wide uncertainty intervals as a result. Survey GPS coordinates are deliberately displaced by 2-5 km for confidentiality, and 22% of data by sample size had only polygon-level location, resampled into pseudo-points. Non-response bias in seroprevalence surveys is the authors' named concern, and the behavioural covariates rest on self-report about sex, which varies with cultural context. Antenatal-clinic prevalence is a biased proxy for general adult prevalence and the correction is modelled rather than measured. Cross-validation showed minimal bias and good 95% interval coverage.
