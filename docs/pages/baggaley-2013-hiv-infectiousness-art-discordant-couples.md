---
type: entry
title: "Heterosexual HIV-1 infectiousness and antiretroviral use: systematic review of prospective studies of discordant couples"
description: Meta-analysis of 50 prospective serodiscordant-couple studies, giving 3.6 per 100 person-years without ART against 0.2 with, a 91% reduction, and 5-10 per 100 PY as the baseline partnership transmission rate in low-income settings
author: Baggaley et al.
published: 2013-01
resource: https://doi.org/10.1097/EDE.0b013e318276cad7
local: raw/10.1097/ede.0b013e318276cad7/
tags: [hiv, coinfection]
updated: 2026-09-10 10:36
---

Source: [baggaley-2013](https://doi.org/10.1097/EDE.0b013e318276cad7)

Systematic review and random-effects Poisson meta-analysis of per-partnership HIV-1 infectiousness in prospective heterosexual serodiscordant-couple studies, searched to July 2011. Fifty publications included, of which nine compared ART-using with non-ART-using index cases within the same study and 41 did not stratify. Outcome is HIV incidence rate per 100 person-years of partnership exposure, not per act. The stated motivation is that trials with intensive adherence counselling overstate what treatment-as-prevention achieves in routine settings.

## Key points

- Within the ART-stratified studies, summary incidence was 3.6 per 100 person-years (95% CI 2.0-6.5) for couples where the index was not on ART, against 0.2 (0.07-0.7) where the index was, incidence rate ratio 0.09 (0.04-0.21), a 91% (79-96%) reduction. HPTN 052 alone had given 96%.
- Across the non-ART-stratified studies, the any-versus-no ART incidence rate ratio was 0.31 (0.14-0.69), combining directions and settings. The gap between 0.09 and 0.31 is the difference between within-study comparison and comparison across studies with unmeasured ART coverage.
- Transmission with ART is not zero. The 0.2 per 100 PY figure sits above zero with a confidence interval excluding it.
- Setting dominates. Incidence rates ranged 0.0-17.4 per 100 PY in high-income settings and 0.0-33.7 in low-income settings. Only 3 of 15 high-income estimates reached 5.0 per 100 PY, against 13 of 24 low-income estimates. By region, no-ART combined transmission summarised at 3.6 per 100 PY (0.4-32.6) for Europe and the Americas, 7.7 (5.5-10.7) for Africa, 10.9 (1.7-69.5) for Asia.
- The authors nominate 5-10 per 100 person-years, from the majority of low-ART low-income studies published 1992 to 2001, as the reasonable baseline partnership transmission rate for projecting the impact of ART, PrEP or other interventions in discordant couples.
- No clear difference by direction of transmission (man-to-woman against woman-to-man) in either setting.
- Subgroup analysis found no substantial difference in summary incidence by reported condom use or by STI prevalence, though the authors stress that both were reported inconsistently and only at study level. Studies whose index cases were classified as more infectious (high proportion late-stage or acute) generally gave higher rates. Studies in higher-circumcision-prevalence settings gave lower rates, but an ecological analysis using country-level circumcision prevalence found no difference for woman-to-man transmission in low-income settings (5.8 per 100 PY in both high- and low-prevalence strata).
- Heterogeneity remained substantial in 13 of 15 low-income no-ART subgroup pools, so the setting-level summaries describe a range rather than a common rate.

## Relevance to project

The per-partnership counterpart to per-act transmission estimates, and the source for two things the model needs. First, an ART effect on infectiousness of roughly 91% (79-96%) measured under observational rather than trial conditions, which is what an ART-era SOC arm should assume rather than the 96% from HPTN 052. Second, a baseline of 5-10 per 100 person-years for HIV transmission within a discordant partnership in a low-income, pre-ART setting, usable as a sanity check on whether the network model's within-partnership transmission is in the right range once per-act probabilities and coital frequencies are composed.

For the coinfection pathway it is a negative result worth recording: stratifying these studies by reported STI prevalence produced no substantial difference in partnership-level transmission. That is weak evidence, because STI status was captured only as a crude study-level aggregate, but it means partnership-level data do not independently corroborate the per-act STI cofactor.

The systematic underestimation the authors describe is the caution that matters for calibration. Discordant-couple studies recruit couples who have already survived the high-transmission window without seroconverting (left censoring), so these rates are floors, not averages. A model calibrated to reproduce them will under-transmit.

## Limitations

- Left-censoring and frailty selection. Couples who transmit fast become concordant before they can be enrolled, so the design over-samples less infectious index cases and less susceptible partners.
- Serodiscordant couples in stable partnerships are not the general population, and studies apply risk-reduction and condom counselling that community members do not receive.
- Risk factors were reported too inconsistently for multivariate analysis; every subgroup analysis is univariate on study-level aggregates.
- Viral load could not be stratified on at all, for lack of data.
- Only two of the nine ART-stratified studies reported results by direction of transmission, so no ART effect by sex is available.
- Observational ART-stratified studies tended to put index cases with more advanced disease on treatment, which works against the ART effect, while non-random treatment assignment leaves residual confounding in an unknown direction.
- Studies could not follow couples who separated, which frequently happens after diagnosis.
