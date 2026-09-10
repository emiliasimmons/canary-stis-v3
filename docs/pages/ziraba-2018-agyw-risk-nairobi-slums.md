---
type: entry
title: "Understanding HIV risks among adolescent girls and young women in informal settlements of Nairobi, Kenya: Lessons for DREAMS"
description: Cross-sectional sexual-behaviour and HIV-testing profile of 1,390 girls and women aged 12-23 in two Nairobi slums in 2009, before DREAMS.
author: Ziraba et al.
published: 2018-05-31
resource: 10.1371/journal.pone.0197479
local: raw/10.1371/journal.pone.0197479
tags: [sexual-networks, hiv, care-seeking]
updated: 2026-09-10 00:26
---

A pre-intervention baseline for the DREAMS Partnership, built from Wave 2 (2009) of the
Transition to Adulthood study nested in the Nairobi Urban Health and Demographic
Surveillance System. The analysis covers 1,390 female respondents aged 12-23 in the
Korogocho and Viwandani informal settlements. Extracted text sits in
`raw/10.1371/journal.pone.0197479`.

Four behavioural outcomes are reported (ever tested for HIV and received the result,
condom use at last sex, more than one partner in 12 months, age-disparate sex), plus age
at debut, and a five-item composite risk score. Regression models are stepwise: age and
slum are forced confounders, socio-demographic terms enter at p < 0.10, then mediators
(social-group membership, peer risk behaviour, closeness to parents, volunteering).

## Relevance to project

Context and a weak off-site comparator for the sexual-network layer. Nairobi slums in
2009 are neither the calibration site nor the calibration period, so nothing here is a
target. Three numbers are usable as loose sanity bounds on network structure among young
women, if the model is ever exercised outside Rakai:

- Age mixing among 578 ever-sexually-active females aged 12-23: 55.7% of last partners
  within 4 years of the respondent's age, 35.5% at 5-9 years, 5.0% at 10-15 years
  (3.8% missing). The 5+ year share, roughly 41%, is a candidate upper end for an
  age-disparate mixing parameter in a high-prevalence urban setting.
- Concurrency/partner turnover: 4.8% of the 481 with a partner-count answer reported 2-7
  partners in the past 12 months, 95.2% reported one. This is low against the project's
  usual assumptions about young urban women and the authors flag it as probably
  under-reported.
- Median age at first sex 16 years (IQR 15-18) among those who had ever had sex; 41.6%
  of the full 1,390 had ever had sex, rising from 3.4% at 12-14 to 80.1% at 20-23.

For `care-seeking`, the testing gradient is the usable part: 51.7% of all 1,390 had ever
tested and received a result, running 14.6% at 12-14, 44.9% at 15-19, 81.8% at 20-23.
Marriage and cohabitation drive that gradient hard (90.1% of the 253 currently married
had ever tested; adjusted OR 3.18, 95% CI 1.78-5.70 for living with a spouse versus one
parent), which supports treating antenatal and couple contact as a separate testing door
from symptomatic care-seeking. Condom use at last sex was 25.6% of the 578 sexually
active, and 6.8% among the 251 married (adjusted OR 0.09, 95% CI 0.05-0.16 versus
unmarried), a large marital-status effect on per-act protection that a risk-structured
network could reproduce.

The paper supplies nothing on STIs. No prevalence, no symptoms, no treatment. It cites
the STI-HIV cofactor only in passing from the literature, so it cannot inform the
`coinfection` or `diagnostics` side of the model.

## Key points

- HIV testing coverage rose from 14.6% to 81.8% across the 12-14 to 20-23 age bands
  (adjusted OR 7.08, 95% CI 4.28-11.69 for 20-23 versus 12-14).
- Testing exceeded sexual experience below age 20: 29.2% of 15-19-year-olds had ever had
  sex against 44.9% ever tested, which the authors attribute to under-reported sexual
  activity or to mass testing that reaches the sexually inexperienced.
- All 9 girls under 15 who reported sex reported no condom at last sex.
- Composite risk score was higher for those aged 20-23, married, out of school, of Luo
  ethnicity, living alone or with a friend or spouse, and with peers in two or more of
  six risk behaviours (+0.79, 95% CI 0.52-1.05). Muslim faith, living with both parents
  (-0.36, 95% CI -0.60 to -0.11) and social-group membership (-0.59, 95% CI -0.79 to
  -0.39) went the other way.
- The two slums differ: Viwandani had lower odds of age-disparate partnership (adjusted
  OR 0.62, 95% CI 0.43-0.90) than Korogocho, consistent with its lower reported HIV
  burden.

## Limitations

Cross-sectional and self-reported, with no biomarkers, so no HIV or STI prevalence
attaches to any of the behaviour strata. Data are from 2009 and published in 2018; the
authors present them as a pre-DREAMS reference point, not as current. Denominators are
small in places: 9 sexually active girls aged 12-14, 29 partnerships with a 10-15 year
age gap. The composite risk score mixes an outcome (ever tested) with exposures and is
weighted by no external calibration, so its regression coefficients do not transfer as
model parameters. Under-reporting of partner counts is acknowledged by the authors and
is the most likely explanation for the 4.8% multiple-partner figure.
