---
type: entry
title: "Age at first marriage, age at first sex, family size preferences, contraception and change in fertility among women in Uganda: analysis of the 2006-2016 period"
description: Uganda DHS decomposition of the 2006-2016 fertility decline, carrying national distributions of age at sexual debut and age at first marriage for women 15-49.
author: Ariho and Kabagenyi
published: 2020-01-15
resource: 10.1186/s12905-020-0881-4
local: raw/10.1186/s12905-020-0881-4
tags: [sexual-networks]
updated: 2026-09-10 00:29
---

Source: [ariho-2020](https://doi.org/10.1186/s12905-020-0881-4)

A demographic decomposition of Uganda's fertility decline between the 2006 and 2016 Uganda
Demographic and Health Surveys, using a nonlinear multivariate decomposition (Poisson,
`mvdcmp`) of children ever born. The analytic sample is women aged 15-49 who reported ever
having had sex: weighted n = 7,281 in 2006 and n = 15,799 in 2016.

## Relevance to project

The decomposition itself is not for this project. The descriptive tables are: they give
nationally representative Ugandan distributions of sexual debut age and first-union age
for women 15-49, on the same DHS frame and over the same decade the model's Rakai
calibration sits in, and those are the two quantities the network module needs to place
women into partnerships.

Debut age (Table 1, women ever having had sex, percent):

| Age at first sex | 2006 | 2016 |
|---|---|---|
| < 15 | 20.1 | 19.0 |
| 15-19 | 55.0 | 69.6 |
| 20+ | 24.9 | 11.5 |

Age at first marriage over the same rows: never married 10.7 -> 13.2, below 15
15.2 -> 11.2, 15-19 56.4 -> 49.1, 20+ 17.8 -> 26.5 percent. Debut and first union move in
opposite directions across the decade, so the gap between sexual debut and marriage widens.
That is the structurally useful line here: a sexual-debut prior anchored to marriage age
would misplace a growing share of Ugandan women, and the model should sample debut
independently.

Usable as a prior on the debut-age distribution for female agents in a Uganda-calibrated
run, and as a bound on how much drift to allow across the 2006-2016 span. Not usable as a
calibration target: fertility is not a model output here, the paper reports nothing on HIV
or STI, and the sample is national rather than Rakai, whose debut ages need not match.

## Key points

- TFR among women who had ever had sex fell from 7.2 (2006) to 5.8 (2016) children per
  woman. The paper's national headline figures for all women are 6.7 to 5.4.
- The overall decomposition splits the fertility change 37.1 percent to changing
  composition of women and 62.9 percent to changing fertility behavior.
- Only age at sexual debut contributed significantly to the behavioral component: 43.5
  percent with education and residence in the model, 85.5 percent with education dropped,
  driven by the 20+ debut category.
- Contraceptive use rose from 22.9 to 35.4 percent of women and accounted for 8.2 percent
  of the fertility change. Preference for 5+ children fell from 48.0 to 43.0 percent.
- TFR by debut age in 2016: 5.7 (debut < 15), 6.0 (15-19), 4.4 (20+). Never-married women
  had a TFR of 2.5 in 2016 against 6.0 to 6.5 for those married before 20.

## Limitations

Both surveys are cross-sectional, so nothing here is causal. Debut age and marital status
at first sex are self-reported on a question the authors expect to be under-reported and
misreported where premarital sex is disapproved of, biasing debut upward and premarital
first births downward. Excluding women who reported never having had sex removes any who
concealed sexual activity, and that exclusion is why the sample TFR (7.2) sits above the
national figure (6.7). The decomposition compares exactly two survey years, so it cannot
separate the 2007 universal secondary education rollout or the 2008 population policy
revision from the trend they sit inside. Retrospective birth histories carry recall error
and birth backdating.
