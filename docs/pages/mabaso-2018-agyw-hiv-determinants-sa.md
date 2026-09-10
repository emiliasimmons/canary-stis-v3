---
type: entry
title: "Determinants of HIV infection among adolescent girls and young women aged 15-24 in South Africa"
description: Cross-sectional determinants of HIV prevalence in South African women 15-24, giving an age gradient and an age-disparate-partnership odds ratio.
author: Mabaso et al.
published: 2018-01-26
resource: 10.1186/s12889-018-5051-3
local: raw/10.1186/s12889-018-5051-3
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:18
---

Secondary analysis of the 2012 South African National HIV Prevalence, Incidence and
Behaviour Survey, a multi-stage stratified cluster household sample with dried blood spot
HIV testing. The analysis sample is 3092 women aged 15-24 interviewed and tested, weighted
to national population estimates. Survey-weighted logistic regression with stepwise
selection, fitted three times: all 15-24, girls 15-19, and women 20-24. Extracted text in
`raw/10.1186/s12889-018-5051-3`.

## Relevance to project

Context and a soft comparator for the age structure of female HIV risk, not a calibration
target. The site is South Africa in 2012, not Rakai, and the outcome is prevalence in a
cross-section rather than incidence, so nothing here calibrates the model's HIV
transmission parameters directly.

Two numbers are usable as sanity checks on the model's age-mixing and risk-heterogeneity
structure. The prevalence gradient is 5.6% (95% CI 4.2-7.5) at 15-19 against 17.4%
(14.6-20.6) at 20-24, a threefold step across five years of age in the same survey. In the
adjusted 15-24 model, a partner within five years of the woman's own age carries
OR 0.53 (0.32-0.87) against a partner five or more years older, and 0.29 (0.10-0.84) in the
20-24 stratum alone. If the model's age-mixing kernel is doing work, a simulated
cross-section should reproduce a gradient and an age-gap contrast of roughly this size,
adjusted for the different setting. Partner number gives OR 0.43 (0.20-0.91) for one
partner against two or more, a weak constraint on the risk-group structure.

The paper measures no STIs and no diagnostics, so it bears on neither arm of the
SOC/POC comparison.

## Key points

Overall weighted HIV prevalence 11.4% (9.8-13.2) in women 15-24. Black African women 13.5%
against 0.9% in other race groups; urban informal settlements 19.1% against 9.2% urban
formal. Prevalence falls monotonically across household asset quintiles above the second,
16.7% in quintile 2 down to 3.0% in quintile 5.

Reported condom use at last sex is associated with *higher* HIV odds, OR 1.91 (1.17-3.14)
overall and 2.09 (1.17-3.73) in 20-24. The authors read this as reverse causation and
inconsistent use rather than condoms failing.

Low-risk drinking (AUDIT 1-7) appears protective, OR 0.19 (0.04-0.78), against abstainers
as reference. Prevalence in abstainers is 12.6% and in high-risk drinkers 3.0%, the
opposite of the expected direction and almost certainly confounding by age and by who
abstains, so the alcohol result should not be carried anywhere.

Stratified models select different variables: for 15-19 only race, marital status, and
asset quintile survive; for 20-24 race, alcohol, age-disparate partnership, education, and
condom use.

## Limitations

Cross-sectional prevalence cannot separate acquisition from survival, and the authors say
so. Behavioural variables are self-reported, with the recall and social-desirability
problems that implies, which is the most likely explanation for the inverted condom
result.

Stepwise selection at entry/removal thresholds of 0.10/0.20 means the reported odds ratios
and confidence intervals are conditional on a data-driven model and are optimistically
narrow.

Table 2 is internally inconsistent: the partner-number rows give n=1395 at 8.6% for one
partner and n=127 at 91.4% for two or more, so the percentage column appears transposed.
The stated text ("91.4% had two or more sexual partners") contradicts the counts. Do not
use the partner-number distribution from this paper; the adjusted OR is less affected but
also suspect.

The "other race" odds ratios (0.06 overall, 0.01 in adolescent girls) rest on very few
events and are not informative about anything the model represents.
