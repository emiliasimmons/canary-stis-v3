---
type: entry
title: "Declines in HIV Incidence and Prevalence and Predictors Among Adolescents and Young Adults: An Observational Cohort Study, Rakai, Uganda, 2005-2020"
description: RCCS rounds 11-19 age- and sex-stratified HIV incidence and prevalence for 15-24s, with round-by-round ART coverage, community viremia and VMMC prevalence.
author: Grilo et al.
published: 2025-01-07
resource: 10.1101/2025.01.07.25320118
local: raw/10.1101/2025.01.07.25320118
tags: [hiv, rakai, sexual-networks]
updated: 2026-09-10 00:22
---

medRxiv preprint reporting HIV trends among adolescents and young adults (15-24) in the
Rakai Community Cohort Study, nine survey rounds from 2005 to 2020 across the 30
continuously followed communities, 35,938 person-rounds (19,473 for women, 16,510 for
men). Extracted content in [raw/10.1101/2025.01.07.25320118/](../raw/10.1101/2025.01.07.25320118/),
with the round-by-round trend tables under `tables/`.

## Relevance to project

The RCCS is the project's first planned calibration site, and this source supplies HIV
targets on the age band the model's risk structure is most sensitive to, stratified by sex
and by 15-19 versus 20-24, round by round. It is a calibration target and a set of time-
varying intervention inputs, not a source on STIs: the paper reports no gonorrhoea,
chlamydia, syphilis or trichomoniasis outcome, and no care-seeking or diagnostic data.

Incidence per 1000 person-years, 15-24, rounds 11 through 19 (table `t02.csv`):

- Men: 4.2, 6.8, 6.4, 8.9, 4.5, 2.1, 2.5, 2.8, 3.0 (p=0.008 for trend)
- Women: 14.2, 14.1, 10.9, 13.8, 10.2, 12.7, 12.1, 2.1, 4.9 (p<0.001)

Prevalence, same band and rounds: men 2.4% to 1.4%, women 7.9% to 3.5%. The 20-24 band
carries most of the burden, women 10.3% down to 6.1%, men 4.6% down to 2.0%.

The community-level series (`t09.csv`) gives the intervention background the model has to
reproduce over the same calendar window. Among women's communities, ART coverage among
people living with HIV rose 6.5% to 72.8% and community viremia fell 11.2% to 2.9%; among
men's, 4.0% to 65.8% and 8.0% to 1.8%. Community male circumcision prevalence rose 21.8%
to 73.8%. If the model's HIV arm is calibrated to a Rakai trajectory, these are the
coverage curves that drive it, and running them flat would misattribute the decline to the
STI pathway.

Behavioural inputs usable as bounds on the network module: ever having had sex among
15-19s fell from 65% to 35% in women and 58% to 38% in men, while two-or-more partners in
the past year among the sexually experienced rose (women 10% to 14% at 15-19, 8% to 12% at
20-24) and consistent condom use fell (women 15-19, 25% to 17%; men 20-24, 34% to 25%).
A model that ties declining incidence to declining partner numbers or rising condom use
contradicts this cohort.

Effect sizes usable as comparators for the model's own counterfactuals, adjusted for
round, age, marital status, SES, school enrolment and partner number: circumcision gives
IRR 0.42 (0.23-0.76) on incidence and OR 0.64 (0.48-0.86) on prevalence in young men; each
10 percentage-point rise in community viremia gives OR 1.73 (1.21-2.47) on prevalence and
IRR 1.85 (0.90-3.81) on incidence in men, OR 1.39 (1.17-1.65) and IRR 1.71 (1.03-2.84) in
women.

## Key points

Incidence turned down first in men, after round 14 (2010-2011), a 66% fall to round 19
(8.9 to 3.0 per 1000, p=0.07). In women the turn came after round 17 (2015-2016), a 60%
fall (12.1 to 4.9 per 1000, p=0.09). The five-year lag is read as circumcision protecting
men directly and women only later, through reduced prevalence in their partners.

Community viremia is defined as community HIV prevalence minus 90% of the ART-covered
share of it: viremia = prevalence x (1 - 0.9 x ART coverage). It is computed on the
partner age band rather than on the index group, men 15-34 for young women's risk and
women 15-30 for young men's, following the age-mixing pattern in this cohort.

Marital status is the strongest individual predictor. Previously married carries OR 5.44
(3.65-8.13) for prevalent infection in young men and 3.36 (2.61-4.34) in young women
against never married, and IRR 5.89 (2.66-13.04) and 2.76 (1.58-4.80) for incidence.
Currently married young women have lower incidence than never-married ones, IRR 0.58
(0.37-0.90), while currently married young men have higher, IRR 2.63 (1.40-4.95).

## Limitations

Everything but HIV serostatus is self-reported. Self-reported ART use validates at 99%
specificity and 77% sensitivity in this population, self-reported circumcision at 90%
specificity, both against Rakai clinical records. The incidence analysis is
underpowered: the headline 60% and 66% declines carry p=0.09 and p=0.07, and several
15-19 male and female round estimates are 0.0 per 1000 on small denominators, so a
likelihood built on these cells needs a count model rather than a normal approximation on
the rate. The cohort is open with high mobility and roughly 25% of censused residents
absent at any round. Round 19 spans the COVID-19 school closures, which confounds the
school-enrolment series against the last data point. The design is associational
throughout, so the circumcision and viremia estimates are adjusted observational
associations rather than the causal quantities a counterfactual simulation produces.
