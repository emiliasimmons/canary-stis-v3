---
type: entry
title: School attendance, HIV infection and sexual behaviour among young people in rural South Africa
description: Cross-sectional survey of 1919 unmarried 14-25 year-olds in rural Limpopo, 2001, reporting partner counts, partner age gaps, condom use and HIV prevalence by school attendance
author: Hargreaves et al.
published: 2008-02
resource: 10.1136/jech.2006.053827
local: raw/10.1136/jech.2006.053827
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:28
---

A random population sample of 916 unmarried men and 1003 unmarried women aged 14-25 in eight villages of rural Limpopo province, South Africa, interviewed in 2001 as the baseline of a microfinance cluster-randomised trial. HIV serostatus came from oral-fluid ELISA (OraSure, Vironostika Uni-Form II) and was available for 1518 of the 1919 respondents (61.1% of those eligible). The primary exposure is current attendance at school or college, with everyone else, mostly unemployed, as the comparison group. Extracted text and tables sit in `raw/10.1136/jech.2006.053827`.

## Relevance to project

The project's calibration site is Rakai, not Limpopo, so nothing here is a calibration target. Its use is as a prior and a sanity bound on the age-mixing and partner-count structure of the risk-structured network the model runs on, for the young adult band where HIV incidence concentrates.

Age mixing, among unmarried 14-25 year-olds in 2001: women's male partners were a median 4 years older (IQR 2-7 years) across 700 partnerships with age data, men's female partners a median 2 years younger (IQR 1-4 years) across 750. That asymmetry is the shape an age-mixing kernel for this age band should reproduce, and it is roughly the gap Rakai-based work reports too, so the two can be read against each other.

Partner counts give a bound on network degree in the same band: median lifetime partners 2 for both sexes (IQR 0-4 men, 0-3 women), with 63.1% of men and 70.4% of women ever having had sex, and only 28.1% of non-student men versus 13.2% of student men reporting more than one partner in the past year. Concurrency-relevant heterogeneity is therefore driven by a minority, not by a high population mean.

Condom use at last sex, per partnership, was 37.0% for men and 29.4% for women, a bound on the protected fraction of acts in an unmarried young adult population before large-scale prevention scale-up.

The paper is also a structural argument the project does not implement: schooling as a determinant of network position, with an intervention lever (fees, cash transfers, school feeding) that sits entirely outside the STI diagnostic pathway. Read it as context for why network position is worth resolving, not as a comparator arm.

## Key points

HIV prevalence in the sampled 14-25 band was 3.4% among men and 9.8% among women, rising across the age range. Antenatal clinic prevalence in the surrounding region was 13.2% in 2000.

Male students were less likely to be HIV positive than male non-students: 1.6% (8/514) versus 8.2% (16/195), adjusted odds ratio 0.21 (95% CI 0.06 to 0.71) after adjustment for age, village, household wealth and temporary migration. Among women the difference in raw prevalence was large, 5.7% (29/507) versus 16.6% (50/302), but the adjusted odds ratio was 0.73 (95% CI 0.36 to 1.50), consistent with confounding by age and childbirth.

Students of both sexes reported fewer lifetime partners: men more than three partners aOR 0.67 (0.44 to 1.00), women more than two partners aOR 0.54 (0.37 to 0.79) before adjusting for childbirth and 0.69 (0.46 to 1.04) after.

Female students were less likely to have a partner more than three years older, aOR 0.52 (0.34 to 0.80), to have had sex more than five times in a partnership in the past year, aOR 0.57 (0.37 to 0.87), and to report no condom use in the past year, aOR 0.60 (0.40 to 0.91), all adjusted for childbirth.

No mechanism ran through knowledge or services. HIV knowledge, household communication about sex, and ever having been tested were not more favourable among students, and testing was near-absent overall (4.1% of men and 6.1% of women had ever tested). School-based sexual health programmes were poorly developed in the study area at the time. The authors attribute the protective association to sexual network structure instead.

## Limitations

Cross-sectional, so temporality is unresolved. For young women this is severe: childbearing is a common reason for leaving school, so the childbirth adjustment (model 3) may be over-adjusting on a variable that sits on the causal pathway rather than confounding it.

HIV results were available for only 61.1% of eligible respondents, and 36.4% of oral fluid samples were stored longer than the manufacturer recommends. One interviewer's data (125 records, 7.6%) were dropped for quality. The 24 HIV-positive men behind the headline aOR of 0.21 make that estimate fragile, and the paper ran many tests without correction.

Interviewed respondents differed systematically from those missed: younger, less likely to be sleeping away from home, more likely to be students. Migrants and the mobile are under-represented, which biases against exactly the high-network-position individuals the project cares about identifying.

No data on whether sexual partners were themselves attending school, so the network mechanism the discussion proposes is inferred rather than measured.

## Methodology

Two hundred households were randomly selected per village, all never-married 14-25 year-olds enumerated as members were eligible, and dwellings were revisited at least three times. Response was 77.2% of the 2486 eligible. Interviews were face-to-face in Sepedi at a location the respondent chose.

Outcomes were binarised with cut-offs chosen to reflect the sex-specific distribution: more than three lifetime partners for men, more than two for women. Logistic regression with robust standard errors for intra-household clustering. Model 1 adjusts for age, model 2 adds village, number of co-resident young people, residence in village of birth, parental status, household wealth from a participatory wealth-ranking exercise, and temporary migrancy. Model 3, women only, adds previous childbirth. Factors judged to be on the causal pathway were otherwise left unadjusted.
