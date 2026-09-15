---
type: entry
title: "Association of life-course events with predictors of HIV risk behaviour and HIV acquisition in Manicaland, Zimbabwe"
description: Eight rounds of a Zimbabwean population cohort showing HIV risk behaviour turns over in under 3 years, and that marital, employment, and migration events predict HIV acquisition better than self-reported risk behaviour.
author: Pickles et al.
published: 2025-02-14
resource: https://doi.org/10.1016/S2352-3018(24)00317-5
local: raw/10.1016/s2352-3018(24)00317-5
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:18
---

Source: [pickles-2025](https://doi.org/10.1016/S2352-3018(24)00317-5)

A longitudinal analysis of the Manicaland general population cohort in eastern Zimbabwe,
eight survey rounds between 1998 and 2021, asking how quickly an individual's HIV risk
behaviour changes and whether life-course events (marriage, divorce, widowing, employment
change, in-migration, birth of a child) predict who acquires HIV better than the risk
behaviours or demographics prevention programmes normally screen on. 21,213 individuals
interviewed at least twice contributed 34,212 participant observations (63.2% women);
median gap between an observation and the previous interview 2.8 years (IQR 2.3-3.1). HIV
serostatus came from dried blood spots in rounds 1-7, so acquisition is defined only
between rounds 2 and 7.

## Relevance to project

The usable output here is a **turnover rate for risk-behaviour states**, a prior on how
persistent an agent's high-risk position in the network should be. Across a median 2.8-year
interval, the fraction of people reporting a behaviour who also reported it at the previous
round was 12.3% (102/831) for transactional sex, 40.8% (1047/2564) for multiple partners,
36.2% (405/1118) for concurrency, 41.0% (1359/3312) for a non-regular partner, 30.2%
(514/1700) for drug use, and 66.9% (3397/5079) for bar attendance. Condom non-use was the
only consistently reported state. In a risk-structured network where the POC arm's benefit
depends partly on finding high-transmission positions, this bounds how long a person stays
in one: a static risk group assignment persisting over a whole simulation is not what this
cohort shows, and neither is week-scale churn. Persistence is higher in men than women for
most indicators, so turnover is sex-specific.

Second use is a **comparator for risk-targeting efficiency**. Taking the top 20% predicted
at risk, sociodemographic variables captured 29.4% of the 783 HIV acquisitions in rounds
1-6 (230.3 events), current risk behaviours 31.3% (244.8), and life-course events 38.4%
(300.4). Any targeting mechanism this project models, including using an STI diagnosis as
a marker of elevated HIV risk, should be read against roughly 30% capture at 20% coverage
from behavioural screening. That is a low ceiling, and it is the argument for a marker
(a positive etiological test) that does not rely on self-report.

It is not a calibration target for canary-stis. Manicaland is not Rakai, the cohort carries
no STI data at all, and the analysis reports odds ratios adjusted only for survey round
rather than incidence rates the model could be fit to. Use it for structure and priors,
not for numbers to match.

## Key points

Odds ratios for HIV acquisition in the current round (each state modelled separately,
adjusted for survey round only, reference = not in that state): recent divorce 2.67
(2.04-3.50), recent widowing 2.23 (1.67-2.99), recent marriage 2.18 (1.79-2.65), recent
in-migrant 1.68 (1.15-2.45). These exceed every behavioural predictor: concurrent partners
1.95 (1.45-2.60), multiple partners in the past year 1.88 (1.53-2.32), non-regular partner
1.84 (1.55-2.17), transactional sex 1.45 (1.04-2.01), bar visit 1.28 (1.08-1.53). Condom
non-use at last sex was 0.89 (0.74-1.07), not associated.

Marital and employment events improved model fit for almost every risk behaviour (change
in AIC of -10 or less against a base model of sex, age, site type, education, round, and an
age-sex interaction). The largest was condom non-use with marital status, ΔAIC -1843.
Migration and birth of a child improved fit for condom non-use only. Marital-status effects
were not confined to recent events: divorce and separation, recent or not, were both
associated with starting partnership-related risk behaviours relative to a non-recent first
marriage.

Turnover in employment was high in itself: 15.9% of observations were recently employed,
19.8% recently unemployed. Recent in-migrants were 3.1% of observations.

## Limitations

Risk behaviour and partnership data are self-reported, and reporting bias is the authors'
stated motivation for preferring life-course events as a risk proxy. With a median 2.8-year
inter-round interval, the ordering of the life-course event and the seroconversion cannot
be established, so "recent divorce predicts acquisition" is compatible with acquisition
preceding the divorce. Individual variation in the gap between rounds was not adjusted for,
which matters directly if the turnover fractions are read as rates. Follow-up was 48-61%
in rounds 1-6, then 3% in round 7 (site composition changed and the gap to round 6 was six
years) and 48% in round 8, so attrition is severe and mostly by migration, the same process
being studied. Transactional sex from round 3 was dropped because reporting spiked during
an 18% GDP contraction. The analysis used simple logistic regression on paired observations
and did not exploit the full longitudinal structure. No STI outcomes were measured.
