---
type: entry
title: Early Coital Debut and Associated HIV Risk Factors Among Young Women and Men in South Africa
description: Nationally representative 2003 South African survey of 7,692 sexually active 15-24-year-olds giving age at first sex, partner age gaps, coercion, and condom use at debut.
author: Pettifor et al.
published: 2009
resource: 10.1363/ifpp.35.082.09
local: raw/10.1363/ifpp.35.082.09
tags: [sexual-networks, hiv]
updated: 2026-09-10 00:20
---

Source: [pettifor-2009](https://doi.org/10.1363/ifpp.35.082.09)

A descriptive and regression analysis of first sexual experiences drawn from a 2003
household survey run by the University of the Witwatersrand's Reproductive Health and HIV
Research Unit. Stratified, disproportionate systematic sampling across all nine South
African provinces, one randomly selected 15-24-year-old per household, 77% response,
11,904 interviewed, of whom the 7,692 who reported ever having had sex are analysed.
Percentages are weighted to the 2001 census; N's quoted below are unweighted.

## Relevance to project

An age-mixing and debut-age prior for the risk-structured network, from a general
population outside the Rakai calibration site. Four quantities are directly usable as
network parameters or as bounds on them.

Age at first sex: mean 16.4 years for males, 16.8 for females; 18% of men and 8% of women
debuted at 14 or younger. Sexual activity by age band: among 15-19-year-olds 50% of males
and 47% of females had ever had sex, rising to 88% and 91% at 20-24. That gives an entry
schedule into the sexually active population for a 15-49 model, at least for its youngest
band.

Partner age difference at first partnership, weighted, is the most transferable number
here. Among women 15-19, 10% had a first partner the same age or younger, 72% 1-4 years
older, 17% 5-9 years older, 1.7% 10 or more years older; at 20-24 the split is 14 / 62 /
21 / 2.9. Men mirror it: 82% (15-19) and 88% (20-24) had a first partner the same age or
younger. This is a bound on the right tail of the age-mixing kernel for first
partnerships, and the paper's own reading is that large gaps are rare enough that the
"sugar daddy" pattern does not describe this population. It bounds first partnerships
only, not the mixing kernel over all concurrent or later partnerships, which is what the
model actually needs.

Condom use at first sex, by weighted percentage of those with a first partner: 53% of
women and 44% of men aged 15-19, 41% and 38% at 20-24. Consistent ("always") use with the
first partner is far lower, 21-35% depending on sex and age band. Since condom use scales
per-act transmission for both HIV and the curable STIs, the always-use fraction is the
more conservative input.

The paper carries no STI prevalence, no diagnostic performance, and no treatment or
care-seeking data, so it is not a calibration target for anything the POC arm changes. Its
role is a South African comparator for network structure the Rakai fit will set, and a
check that a fitted age-mixing kernel is not putting implausible mass on gaps of 10+
years.

## Key points

Poisson regression without an offset, giving prevalence ratios, stratified by sex.
Each additional year by which the first partner was older raised the prevalence of early
debut (before age 15): adjusted PR 1.07 (95% CI 1.03-1.11) for women, 1.12 (1.07-1.16) for
men, adjusted for age band, education and urban/rural residence.

Forced sex by the first partner was reported by 6.7% of women aged 15-19 and 5.3% at
20-24, against 0.5% and 0.3% of men. Among women it was associated with early debut,
adjusted PR 2.45 (1.68-3.58); among men it was not, 0.81 (0.26-2.58) on very few events.

Wantedness diverges sharply by sex. 96-97% of men said they were willing participants at
first sex against 57-61% of women; 83-84% of men said they "really wanted" it against
27-32% of women. About 4% of women in each age band reported being raped or forced.

Condom nonuse at first sex, adjusted: for men, elevated by early debut (PR 1.47,
1.36-1.59) and by forced sex (1.56, 1.16-2.09), with no interaction. For women the two
interact: relative to later debut without force, later debut with force gives 1.37
(1.23-1.52) and early debut without force gives 1.29 (1.16-1.44), but early debut with
force gives 1.15 (0.79-1.70), non-significant on the 1% of sexually experienced women in
that cell.

Transactional sex with the first partner was reported by 2% of women and 4% of men. First
partners were overwhelmingly main partners (96% for women, 79% for men); the sex-worker
category was statistically 0.0% in every sex-by-age cell.

## Limitations

Self-reported sensitive behaviour with recall stretching back years for the older band;
the authors expect underreporting of forced sex in particular, and note their figures
match other national South African estimates of lifetime nonconsensual sex.

Cross-sectional, so debut, coercion and condom use are all measured at one interview and
the regressions describe association only. "Ever forced by first partner" is not
time-anchored to the debut act, which weakens its reading as a determinant of condom use
at that act.

The transferability gap matters most for this project: 2003 South Africa at roughly 29%
antenatal HIV prevalence is a different epidemiological and social setting from Rakai,
Uganda, and the survey covers 15-24 only, so it says nothing about mixing for the 25-49
part of the model's population.

In the extracted table 2, the female Model 2 rows repeat 2.45 (1.68-3.58) for both the
forced-sex PR and the 15-19 age-band PR, which looks like a typesetting or extraction
artifact. Do not use the age-band coefficient without checking the published table.
