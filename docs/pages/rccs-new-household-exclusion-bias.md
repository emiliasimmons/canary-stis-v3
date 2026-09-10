---
type: entry
title: Implications of rapid population growth on survey design and HIV estimates in the RCCS
description: Quantifies how excluding residents of newly built households biases RCCS HIV seroprevalence and viremia estimates, the cohort this project calibrates to.
author: Khalifa et al.
published: 2023-08-01
resource: https://doi.org/10.1136/bmjopen-2022-071108
local: raw/10.1136/bmjopen-2022-071108
tags: [rakai, hiv]
updated: 2026-09-10 00:37
---

Since 2008 the Rakai Community Cohort Study censuses everyone inside its surveillance
boundaries but only surveys residents of households already on the books before that year.
People who move into newly built structures as entirely new households are counted and then
left out of the interview and blood draw. This paper asks what that exclusion costs the
cohort's headline HIV numbers, using round 19 (June 2018 to November 2020, 33 inland rural
and peri-urban communities) and an ensemble machine-learning model to impute serostatus and
viremia for the excluded group. Extracted text and tables sit in
`raw/10.1136/bmjopen-2022-071108`.

## Relevance to project

RCCS is the first planned calibration site, so this is a bound on the calibration targets
themselves rather than a source of parameters. Three numbers matter for how targets are
used.

The exclusion is large and growing: of 24,729 census-eligible adults aged 15-49 in round
19, 2,920 (12%) were excluded as new-household residents, up from 90 in 2009, with the
steepest rise between 2017 and 2020. At the household level 2,108 of 12,644 (17%) were
excluded.

Overall adult seroprevalence is close to unbiased. Observed 11.7% (95% CI 11.2-12.3) among
surveyed residents of old households; 10.8% (9.6-11.8) predicted for the excluded; 11.6%
(10.9-12.2) for the combined population. A prevalence target taken from published RCCS
round-19 figures for adults 15-49 needs no adjustment at the resolution the model works at.

Age-specific prevalence and population viremia are not. For ages 15-24 the excluded group
was predicted at 4.9% (3.6-6.1) against 2.6% (2.2-3.1) observed, so a young-adult prevalence
target drawn from RCCS is biased low. Population-level viremia (viral load above 1000
copies/mL, denominator the whole adult population, not just people with HIV) goes from 1.7%
(1.5-1.9) observed to 2.1% (1.8-2.4) with the excluded included, a 24% increase; for ages
15-24 it goes from 0.8% (0.6-1.1) to 1.2% (0.9-1.7). Viremia is the quantity closest to the
force of HIV infection the model has to reproduce, so an RCCS-derived viremia or
suppression target is the one most worth widening or shifting upward.

The paper says nothing about STIs, sexual behaviour, or care-seeking, and supplies no
network or partnership structure. It is a caveat attached to RCCS targets, not an input to
the model.

## Key points

Excluded residents differ from the surveyed sample on every measured characteristic except
gender: more likely aged 20-29, married (57.9% vs 48.5%), household head (57.4% vs 40.6%),
renting (65.2% vs 40.2%), transient with under six months per year at the household (15.5%
vs 4.0%), and in one- or two-person households (56.8% vs 29.2%). Nearly half (46.5%) were
new in-migrants arriving since the previous round, against 19.5% of the surveyed sample.

The age split in predicted seroprevalence points two ways at once. The authors read the
excess among 15-24s as a migrant health penalty, young people moving into occupations
(boda-boda and truck driving, bar and restaurant work) tied to higher HIV risk, and the
deficit among 25-49s as a healthy-migrant effect, married men relocating for work or family.

Predicted viremia was higher in the excluded group across every age and sex subgroup, which
matches other sub-Saharan African cohorts and the argument that mobile people face
interruptions in treatment.

## Methodology

Super Learner stacking over seven R algorithms (gam, biglasso, xgboost, glm,
glm.interaction, bayesglm, ranger) at default settings, weighted by AUC under 10-fold
cross-validation, with a second 10-fold pass to score the ensemble and household ID used as
the clustering unit. Predictors come from census data only: sex, five-year age group,
marital status, relation to household head, permanent versus transient residence, recent
in-migration, region, an asset-based socioeconomic index, land ownership, household size,
sex of household head, youth dependency ratio. Uncertainty comes from Bernoulli draws on
each predicted probability across 100 bootstrap resamples.

## Limitations

Model discrimination is moderate for seroprevalence (AUC 0.78, 0.73-0.81) and weak for
viremia (0.71, 0.65-0.75), which is the estimate the project would most want to lean on.
The census carries no behavioural data, so the strongest predictors of both outcomes
(age-disparate partnerships, alcohol use) are absent.

The whole imputation assumes predictors of serostatus and viremia act the same way in
excluded and surveyed households, which is exactly the assumption a healthy-migrant or
migrant-penalty story puts in doubt.

The observed sample has its own separate coverage problem the paper does not address: of
21,208 old-household residents, 17,339 (82%) were survey-eligible and only 11,942 (69% of
those eligible) were present at survey time. Absentees are plausibly the more mobile, so
the true bias in an RCCS target is larger than the new-household exclusion alone.
