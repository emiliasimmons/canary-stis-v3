---
type: entry
title: "Transactional Sex, Alcohol Use and Intimate Partner Violence Against Women in the Rakai Region of Uganda"
description: Cross-sectional RCCS analysis of 8,248 women 15-49, giving past-year transactional sex prevalence, partner-count distribution and HIV prevalence by community type.
author: Miller et al.
published: 2021-04-01
resource: 10.1007/s10461-020-03069-9
local: raw/10.1007/s10461-020-03069-9
tags: [sexual-networks, rakai, hiv]
updated: 2026-09-10 11:17
---

Source: [miller-2021](https://doi.org/10.1007/s10461-020-03069-9)

A cross-sectional secondary analysis of Rakai Community Cohort Study (RCCS) survey rounds
collected between August 2016 and May 2018, asking whether women who engage in
transactional sex, or who drink, are at higher risk of intimate partner violence.

Transactional sex here means a non-commercial sexual relationship carrying an implicit
expectation that sex is exchanged for material support. It is measured by a single question
asked about each of up to four past-year partners: "Were money, gifts or favors exchanged
for sex with this partner?" A woman counts as exposed if she reports exchange, given or
received, with any of those partners. This is deliberately distinct from sex work as an
occupation, which only 15 women (0.18% of 8,248) named as their primary occupation.

## Relevance to project

A structural input for sizing risk groups and partner-count distributions in the sexual
network, and nothing more. The analytic sample is 8,248 women aged 15-49 who reported
sexual activity in the past year, drawn from 40 RCCS communities: 53.8% resident in agrarian
communities, 24.3% in fishing communities, 21.9% in trading communities, mean age 30.7 years
(SD 8.2). Within that denominator, 15% reported past-year transactional sex, 39.5% reported
any past-year alcohol use, and 88.6% reported exactly one sexual partner in the past year.
HIV prevalence, by rapid test at interview, was 22% across the whole sample, 34.2% among
women reporting both transactional sex and alcohol use, and 19.2% among women reporting
neither. Those four numbers are the usable content: a partner-count distribution that a
network model has to reproduce, a transactional-sex group size, and an HIV prevalence
gradient across a behaviourally defined stratum.

The paper measures no STI other than HIV, no symptom reporting, and no care seeking, so it
supplies no calibration target, prior, or bound for anything the point-of-care diagnostics
question turns on. The HIV prevalence figures are cross-tabulations from a behavioural
survey with rapid testing rather than a designed prevalence estimate, and the sample is
restricted to sexually active women, so it should not be used as an RCCS HIV prevalence
target where a properly denominated one exists.

## Key points

Associations are reported as prevalence risk ratios (PRR) from modified Poisson regression
with robust variance, so they are ratios of past-year IPV prevalence between exposure
groups, not incidence rate ratios and not causal effects.

In the adjusted models covering all 8,248 women, transactional sex carried a 20% higher
prevalence of verbal IPV (PRR 1.20, 95% CI 1.05 to 1.36), 14% higher physical IPV (PRR 1.14,
95% CI 1.00 to 1.30) and 25% higher sexual IPV (PRR 1.25, 95% CI 1.06 to 1.48) relative to
women reporting no transactional sex. Any past-year alcohol use carried PRR 1.33 (1.22 to
1.45) for verbal, 1.37 (1.24 to 1.41 as printed) for physical, and 1.22 (1.07 to 1.40) for
sexual IPV. The unadjusted ratios are considerably larger for transactional sex, 1.44 (1.28
to 1.62) for physical and 1.55 (1.32 to 1.81) for sexual IPV, so most of the crude
association is carried by covariates, principally partner count.

Partner count itself is the strongest behavioural predictor in the adjusted models. Women
reporting more than one past-year partner had PRR 2.21 (1.86 to 2.63) for sexual IPV and
1.83 (1.61 to 2.09) for physical IPV against women with one partner.

Stratifying by community type, transactional sex was associated with all three forms of IPV
only in agrarian communities (verbal PRR 1.21, 1.03 to 1.42; physical 1.26, 1.05 to 1.50;
sexual 1.34, 1.12 to 1.59). No significant transactional-sex association appeared in fishing
or trading communities, the two settings where transactional sex is most common. The authors
read this as a sign that constrained relationship agency, not exchange itself, drives the
association, women in fishing and trading communities having more independent income.

Past-year IPV prevalence in the full sample was 25.5% verbal, 20.2% physical and 11.0%
sexual, on the adapted Conflict Tactics Scale items listed in the methods.

Alcohol use was somewhat more common among women reporting transactional sex, 45.4% against
38.5%, and the interaction term between alcohol and transactional sex was not significant in
any model.

## Limitations

Cross-sectional, so no temporal ordering between exchange, drinking and violence. Everything
except HIV serostatus is self-reported to an interviewer, on questions where under-reporting
is expected and likely differential by community type.

The transactional-sex measure does not record motivation, partner type, or whether the
partner was a spouse. Current guidance on measuring transactional sex in large surveys
advises excluding marital relationships, and 71.5% of this sample was currently married, so
the 15% exposed group mixes marital gift exchange with the non-marital arrangements that
carry the network risk. That matters directly if the figure is used to size a high-activity
group.

Alcohol is a binary any-versus-none over twelve months, with no quantity or frequency, and
no link to whether drinking preceded sex.

Two printed intervals do not behave. The adjusted physical-IPV PRR for alcohol is given as
1.37 with 95% CI 1.24 to 1.41, an interval that does not sit symmetrically around the point
estimate on the log scale and is probably a transcription error for the upper bound. The
adjusted verbal-IPV PRR for having more than one partner is 0.11 (0.08 to 0.16), a
ninefold protective effect that runs opposite to the physical and sexual results and is not
discussed. Neither figure should be carried forward.

## Methodology

Covariate selection was stepwise on significance: only variables significant at p <= 0.05 in
bivariate analysis entered the multivariate model, and the interaction term and covariates
were retained only if significant there. Stratified models were rebuilt from scratch per
community type by the same rule, so the three community models do not share a covariate set
and their coefficients are not directly comparable to each other. This is why the
transactional-sex association appearing only in agrarian communities cannot be read as a
tested difference between community types, and the authors do not test one.

Partner count was added as a covariate after a sensitivity analysis found that both
transactional-sex reporting and HIV prevalence rose steeply with the number of past-year
partners reported. Adjusting for partner count is what shrinks the transactional-sex ratios
from around 1.5 to around 1.2, which means the adjusted estimates answer the question of
whether exchange adds risk beyond having more partners. For a network model the unadjusted
gradient is the more relevant quantity, since partner count is an outcome the model
generates rather than a nuisance to remove.
