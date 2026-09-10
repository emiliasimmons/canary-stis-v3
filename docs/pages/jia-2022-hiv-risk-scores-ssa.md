---
type: entry
title: "Risk scores for predicting HIV incidence among adult heterosexual populations in sub-Saharan Africa: a systematic review and meta-analysis"
description: Pooled hazard ratios for individual-level HIV risk factors including STIs, and the discriminatory limits of risk scoring in general populations.
author: Jia et al.
published: 2022-01-13
resource: 10.1002/jia2.25861
local: raw/10.1002/jia2.25861/content.md
tags: [hiv, sti]
updated: 2026-09-10 09:45
---

Systematic review and random-effects meta-analysis of 14 HIV incidence risk scores
from 13 studies (134,423 individuals, 301,820 person-years) across sub-Saharan Africa.
The review pools effect estimates for individual-level predictors of HIV seroconversion
among heterosexual adults and evaluates how well composite scores discriminate future
infections. Raw extraction in `raw/10.1002/jia2.25861/content.md`.

## Relevance to project

The pooled adjusted hazard ratios for STI-associated HIV acquisition ground the
cofactor effect that the model's POC arm exploits. Among all-age sexually active women,
curable STIs at baseline carried a pooled aHR of 1.45 [1.17, 1.79] and HSV-2 an aHR
of 1.67 [1.34, 2.09]. Among AGYW, curable STIs were stronger (aHR 2.14 [1.40, 3.25])
and HSV-2 comparable (aHR 1.77 [1.24, 2.54]). These provide an external reference for
the magnitude of the STI-HIV cofactor in the model's likelihood, alongside any
site-specific estimates from [RCCS calibration targets](../tags/rakai.md).

The review also includes Kagaayi 2014, which developed risk scores directly from RCCS
data in Rakai, Uganda. Kagaayi found community HIV prevalence significantly predictive
(aHR 1.03 per percentage-point increment for both sexes), alongside age, education,
partner characteristics, circumcision status, and STIs.

The scores' moderate discriminatory power (AUC-ROC 0.56-0.79, pooled external
validation of the VOICE score 0.626) is itself informative: individual-level risk
factors alone do not cleanly separate who seroconverts, consistent with the project's
premise that transmission depends on network position and community-level exposure, not
just individual behavior.

The paper cannot supply cofactor estimates specific to the POC diagnostic pathway
(etiological testing changes who gets treated, not who is at risk), and does not model
the causal effect of STI treatment on HIV incidence.

## Key points

- Across all-age women (4 scores, all from South African RCTs of sexually active
  contraceptive-seeking women): younger age (aHR 1.62 [1.17, 2.23] for under 25),
  not married/cohabiting (aHR 2.33 [1.73, 3.13]), and curable STIs (aHR 1.45
  [1.17, 1.79]) were retained in 3 or 4 of 4 final models. HSV-2 (aHR 1.67
  [1.34, 2.09]) and multiple partners (aHR 1.62 [1.27, 2.07]) were retained in 2
  of 4.

- Among AGYW (3 scores): HSV-2 was the only factor selected in all three. Curable
  STIs (aHR 2.14), multiple partners (aHR 1.76), and partner concurrency (aHR 2.35)
  were selected in 2 of 3. Being single/non-cohabiting was not selected in any AGYW
  model, unlike the all-age models.

- Community HIV prevalence was considered in only 3 of 11 multi-site studies but was
  highly predictive in all three. Roberts et al. found that age plus community
  viraemia alone achieved AUC-ROC 0.65 (women) and 0.71 (men), compared to 0.68 and
  0.72 with all individual-level factors added.

- The VOICE score, the only model externally validated by multiple studies (9), had a
  pooled external AUC-ROC of 0.626 [0.588, 0.663] (I-squared 64%), down from 0.69
  internally.

- Removing laboratory-diagnosed STIs from scores (substituting self-report or
  syndromic assessment) reduced AUC-ROC by 1-8 percentage points, quantifying the
  information value of etiological diagnosis for risk stratification.

## Limitations

- Ten of 13 studies enrolled only women, and 7 of those recruited sexually active
  contraceptive-seekers from RCTs. The pooled estimates do not represent general-population
  men or women not seeking contraception.

- Data were disproportionately from South Africa (10 of 13 studies contributed South African
  data), where marriage rates are lower and HIV epidemiology differs from East Africa. The
  all-age risk factors (especially non-cohabitation) may not generalize to settings like Rakai
  with higher marriage prevalence.

- About half the study data predate 2012, before large-scale ART rollout altered community
  viral load and the age distribution of new infections.

- Adjusted and unadjusted hazard ratios were pooled together in the meta-analysis, because
  adjusted estimates were available only from studies that retained a given predictor in the
  final model. This may bias pooled estimates away from the null.

- The review covers prognostic association, not causal effect. The STI hazard ratios reflect
  correlation between prevalent STI and subsequent HIV seroconversion, confounded by shared
  risk behavior.

## Methodology

Searched 9 databases through February 2021. Inclusion required prospective HIV
seroconversion measurement (baseline HIV-negative with follow-up testing) among adult
heterosexual populations in sub-Saharan Africa. Key populations (MSM, FSW, PWID,
serodiscordant couples) excluded. Random-effects meta-analysis with Sidik-Jonkman
estimator for between-study variance. Risk of bias assessed with PROBAST: only 1 of 12
development models and 2 of 9 validations were low risk. Inadequate adjustment for
overfitting was common (6 of 9 development studies).
