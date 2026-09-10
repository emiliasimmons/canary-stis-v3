---
type: entry
title: Sexual partnership age pairings and risk of HIV acquisition in rural South Africa
description: Population-based cohort quantifying HIV acquisition risk by sexual partner age group in men and women in hyperendemic KwaZulu-Natal
author: Akullian et al.
published: 2017-10-01
resource: 10.1097/qad.0000000000001553
basis: abstract
tags: [sexual-networks, hiv]
updated: 2026-09-10 10:02
---

A population-based cohort study of HIV acquisition in Umkhanyakude district, rural
KwaZulu-Natal, following women 15-49 and men 15-55 from 2004 to 2015 in the Africa Health
Research Institute (AHRI) surveillance area. Generalized additive models estimated smoothed
HIV incidence rates across partnership age pairings, linking self-reported partner ages to
seroconversion events.

## Relevance to project

A shape target for the age-mixing matrix in the shared sexual network. The model needs to
assign HIV acquisition risk by partner age, and this paper provides the empirical surface
of incidence across ego-partner age pairings in a high-prevalence rural African population.
The setting is KwaZulu-Natal rather than Rakai, so the absolute rates do not transfer as
calibration targets. What transfers is the qualitative structure: which partner age pairings
carry the highest transmission risk, whether age-discordant partnerships drive excess risk
in young women, and the relative contribution of older male partners. This directly informs
how age mixing is parameterized in the network layer.

See also [Akullian et al. 2021](akullian-2021-age-shifts-hiv-incidence-kzn.md) for the
same cohort's later analysis of how incidence age patterns shifted through 2019.

## Key points

Women's HIV risk was most strongly associated with partnerships with men 25-29 years old,
regardless of the woman's own age, consistent with that male age group carrying the highest
community viral load in this setting. Young women (15-24) in partnerships with men 5 or
more years older had elevated risk compared to age-concordant partnerships.

Men's risk was associated with partnerships with women in the 20-29 age band, where female
HIV prevalence peaks.

The GAM approach avoids the arbitrary binning of age-mixing matrices used in most
transmission models, providing a continuous surface that could inform smoothed mixing
kernels. The results support carrying age-assortative mixing as a structural feature of the
network rather than treating risk groups as age-homogeneous.

## Limitations

Partner ages are self-reported in the demographic surveillance questionnaire, subject to
reporting bias and rounding. The study links partner age to seroconversion but cannot
directly observe transmission events or directionality. The cohort is in a hyperendemic
setting (community HIV prevalence exceeding 30%) where the age-prevalence profile is mature,
which shapes the risk surface in ways that may differ from a lower-prevalence setting like
Rakai. No STI data are available, so the extent to which STI cofactor effects modify the
age-pairing risk surface is unmeasured.

## Methodology

Seroconversion dates were imputed between last-negative and first-positive HIV tests (annual
testing rounds). Partnership age data come from a structured sexual-behaviour questionnaire
administered alongside HIV testing. The GAM framework with tensor product smooths allows
incidence to vary flexibly over both ego age and partner age without imposing a parametric
form on the mixing surface.
