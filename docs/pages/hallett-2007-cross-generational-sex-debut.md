---
type: entry
title: "Behaviour change in generalised HIV epidemics: impact of reducing cross-generational sex and delaying age at sexual debut"
description: Age-structured deterministic HIV model showing that age-disparate mixing and later sexual debut move population-level risk far less than individual-level risk factor analyses imply.
author: Hallett et al.
published: 2007
resource: 10.1136/sti.2006.023606
local: raw/10.1136/sti.2006.023606
tags: [hiv, modeling, sexual-networks]
updated: 2026-09-10 00:29
---

Source: [hallett-2007](https://doi.org/10.1136/sti.2006.023606)

A deterministic partial-differential-equation model of heterosexual HIV transmission with
yearly age resolution, parameterised to the Manicaland (eastern Zimbabwe) population-based
survey of roughly 10,000 adults in 12 communities, 1998-2000. It asks what two widely
promoted behaviour interventions, discouraging cross-generational sex and delaying sexual
debut, would do at the population level rather than to one woman's own risk.

## Relevance to project

A structural justification for how age mixing enters the shared risk network, and a
cautionary comparator on what network-targeted prevention buys. Three concrete uses.

The Manicaland partner age-difference distribution is log-logistic, with mean male-minus-female
age difference of 7 years and roughly 25% of partnerships at 10 or more years apart. That is a
usable functional form and a pair of anchors for an age-mixing kernel in the STIsim network,
from a Zimbabwean rather than Ugandan sample, so treat it as a prior shape and not a Rakai
calibration target.

The model reproduces observed female-to-male HIV prevalence ratios among 15-24-year-olds with
no assumed sex or age difference in per-act susceptibility. Age mixing plus duration of
exposure is sufficient. That bounds how much the project needs to load onto biological
susceptibility terms when the young-women prevalence excess appears in RCCS calibration.

The headline result is the comparator for the project's targeting question. Moving
cross-generational partnerships from 20% to 5% while preserving total partnership count cuts
lifetime infection risk 10% in women and 5% in men, and raises prevalence among young men.
Removing those partnerships without replacement cuts lifetime risk 25% and 22%. Rearranging
who partners with whom does much less than removing risky contacts, which is directly
analogous to the project's split between direct STI treatment, prevention targeting, and
identifying high-transmission network positions.

## Key points

Endemic HIV does not require age-disparate mixing. With every partnership between exact
peers the epidemic fails to establish, but 1% of partnerships one year apart is enough for
HIV to become endemic at a high level. Prevalence rises only slightly across a wide range of
cross-generational mixing.

Delaying sexual debut two years reduces lifetime risk by at most 8%, and only under the
optimistic assumption that susceptibility falls with age and lost partnerships are not
replaced. If men replace would-be young partners with the youngest available sexually active
women, incidence among women rises in their first years of activity. Raising age at first sex
from 18 to 21 gives a 9% lifetime risk reduction if women are unmarried 12 months less, 6%
with no change in marriage timing, and essentially nothing if they spend three extra years
unmarried. Incidence in this population was 2% per person-year while sexually active and
unmarried against 1% per person-year while married, over the first three years of follow-up.

Raising condom use among men aged 25 and over to the level young men report cuts lifetime
risk by about 20% in both sexes, exceeding both a doubling of population-wide condom use and
a two-year debut delay. Condom use in all acts in the last partnership was reported by 17% of
men and 8% of women with a partnership in the past month.

The benefit of peer-to-peer mixing to a young woman is negatively frequency dependent: as
more women switch to same-age partners, prevalence among young men rises and the former
low-risk contact becomes high risk.

## Methodology

Three asymptomatic HIV stages before AIDS, with a 3-month high-transmission acute phase, a
long low-transmission phase up to a mean of 10 years depending on age, and a 6-month
high-transmission late phase. Population stratified by sex, single year of age, and sexual
activity group; most individuals enter the lowest activity group at debut. Mixing is assortative
by activity and skewed toward older-men-younger-women via the log-logistic age difference
function. Runge-Kutta, 0.02-year time step, 100-year burn-in to a stable pre-AIDS demographic
structure, seeded with HIV in 0.01% of men aged 25-29 in the highest activity group.

Two distinct cross-generational interventions are simulated and the distinction drives the
result: reshaping the age-difference distribution while holding total partnerships fixed, versus
deleting a fraction of age-disparate partnerships outright. Because the mixing matrix must be
consistent for both sexes, the model must specify whose demand is accommodated, and results
are reported for male-dominated, female-dominated, and compromise mixing.

## Limitations

No STIs. The model carries HIV alone, so it says nothing about cofactor effects or about how
STI screening would interact with age structure. Zimbabwe rather than Uganda, cross-sectional
self-reported behaviour with the usual reporting bias (partly mitigated by a confidential
voting method for sensitive questions in three-quarters of literate respondents' interviews).
The authors present the results as qualitative insight from one well-parameterised example,
not as an exhaustive description of African epidemics. Deterministic and compartmental, so
individual partnership duration, concurrency, and network position are not represented, which
is exactly the dimension this project's agent-based network is built to carry. The male
behavioural response to female abstinence is unmeasured and is the main driver of the
sexual-debut results.
