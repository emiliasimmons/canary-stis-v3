---
type: entry
title: "Risk of HIV acquisition among high-risk heterosexuals with nonviral sexually transmitted infections: A systematic review and meta-analysis"
description: Pooled risk ratios for HIV acquisition given gonorrhoea, chlamydia, trichomoniasis, syphilis, and M. genitalium among high-risk heterosexuals
author: Barker et al.
published: 2022-06-01
resource: 10.1097/olq.0000000000001601
local: raw/10.1097/olq.0000000000001601/content.md
tags: [hiv, sti, coinfection]
updated: 2026-09-10 09:47
---

Source: [barker-2022](https://doi.org/10.1097/olq.0000000000001601)

Systematic review and meta-analysis of 32 studies (97 effect sizes) on HIV acquisition
risk among high-risk heterosexuals diagnosed with a nonviral STI. Searched PubMed, Web of
Science, and Embase through December 2017. Included only studies where STI diagnosis was
confirmed to precede HIV diagnosis, addressing the temporality bias that weakened earlier
reviews.

## Relevance to project

The pooled RR estimates give empirical bounds on the STI-to-HIV cofactor multiplier for
each pathogen in the model. For females (the better-powered stratum):

| Pathogen       | RR (95% CI)        | k  | I^2   |
|----------------|--------------------|----|-------|
| Gonorrhoea     | 2.81 (2.25, 3.50)  | 16 | 10.9% |
| M. genitalium  | 3.10 (1.63, 5.92)  |  2 |  0.0% |
| Syphilis       | 1.67 (1.23, 2.27)  | 17 | 43.7% |
| Trichomoniasis | 1.54 (1.31, 1.82)  | 17 |  0.0% |
| Chlamydia      | 1.49 (1.08, 2.04)  | 14 | 23.4% |

For males, only syphilis had enough data to pool (RR 1.77, 95% CI 1.22-2.58, k=5).
Gonorrhoea had one male estimate (RR 2.80, 95% CI 1.50-5.20) and chlamydia one
(RR 0.80, 95% CI 0.30-1.90).

These RRs bound the per-act or per-partnership HIV acquisition multiplier that STI
cofactor parameters should reproduce. They are not per-act transmission probabilities:
each reflects the ratio of HIV incidence rates between STI-positive and STI-negative
groups over follow-up periods averaging 5.5 months. The model's cofactor multiplier should
produce population-level incidence rate ratios in this range when STI prevalence and
duration are set to observed values.

Restricting to higher-quality data (multivariate-adjusted, low temporality bias, excluding
case-control studies) generally preserved or slightly increased the estimates, suggesting
the overall pooled values are not inflated by low-quality studies.

## Key points

Most data come from female sex workers in sub-Saharan Africa (84% of studies in non-OECD
countries, 66% female-only). Gonorrhoea carries the largest and most precisely estimated
cofactor among the four project pathogens, with low heterogeneity. Chlamydia's cofactor is
the smallest and its CI barely excludes 1. M. genitalium shows the highest point estimate
but rests on only two studies.

Multivariate-adjusted estimates are similar to or higher than unadjusted ones for every
pathogen except gonorrhoea (which drops slightly), indicating that residual confounding
from shared risk behaviour does not fully explain the association.

## Limitations

The review population (predominantly female sex workers in low-income settings) does not
match the RCCS general-population cohort. The cofactor in a general population with lower
STI prevalence and fewer concurrent partnerships could differ.

No study controlled for all major confounders simultaneously (partner HIV status, number of
partners, condom use, injection drug use, other concurrent STIs). The RRs therefore mix
biological cofactor effects with residual behavioural confounding.

Follow-up intervals averaged 5.5 months, long enough for STIs to clear or new ones to
appear between assessments. This dilutes the measured association and means the true
biological cofactor could be larger than the pooled RR.

M. genitalium is not in the current model, so its estimate is informational only. Male
estimates for gonorrhoea, chlamydia, and trichomoniasis each rest on a single study.

## Methodology

Random-effects meta-analysis pooling risk ratios (odds ratios converted via Zhang and Yu).
Risk of bias assessed per GRADE/MAGIC, with domains for STI and HIV diagnostic accuracy,
confounder adjustment, temporality, and recruitment. Subgroup analyses by adjustment
status, temporality risk, geography, and risk group. Sensitivity analyses removing one
study at a time.
