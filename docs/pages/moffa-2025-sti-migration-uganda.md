---
type: entry
title: "Sexually transmitted infections and migration in Uganda: A population-based study"
description: STIPS cross-sectional prevalence of four curable STIs by recent migration status in two Rakai communities, adults 18-49, 2019.
author: Moffa et al.
published: 2025
resource: 10.1136/sextrans-2024-056190
local: raw/10.1136/sextrans-2024-056190
tags: [sti, rakai, hiv, coinfection, sexual-networks]
updated: 2026-09-10 00:35
---

Secondary analysis of the Sexually Transmitted Infection Prevalence Study (STIPS), a cross-sectional survey of chlamydia, gonorrhoea, trichomonas, syphilis and HSV-2 nested in the Rakai Community Cohort Study, run May-October 2019 in two communities: an inland semi-urban trading centre with surrounding villages, and a Lake Victoria fishing community. 1,825 consenting adults aged 18-49, of whom 358 (19.6%) were classified as recent migrants, meaning they had moved into the community since the prior RCCS census round roughly 18 months earlier. Extracted source in `raw/10.1136/sextrans-2024-056190`.

## Relevance to project

Two uses here, both about the risk structure of the network rather than about diagnostics.

A **prevalence target with a mobility stratum**, for the Rakai calibration site. All figures below are point prevalence in adults 18-49 across the two STIPS communities, 2019, by NAAT for chlamydia and gonorrhoea (Abbott m2000 RealTime CT/NG), OSOM rapid test for trichomonas, and treponemal antibody plus RPR for syphilis. Combined curable-STI prevalence (gonorrhoea, chlamydia, high-titer syphilis with RPR titer at least 1:8, trichomonas) was 34.4% in migrants against 24.2% in long-term residents. Per pathogen, migrants against residents: chlamydia 13.8% vs 8.8%, gonorrhoea 9.8% vs 6.0%, trichomonas 12.6% vs 10.3%, syphilis antibody 16.5% vs 15.3%, high-titer syphilis 8.7% vs 4.6%, HSV-2 47.6% vs 55.1%, HIV 23.7% vs 27.6%.

A **bound on how much heterogeneity a mobility or in-migration mechanism should buy**, if the model ever adds one. Adjusting for sex, age, community type, education, occupation and marital status collapses most of the crude excess: adjusted prevalence risk ratio for combined curable STIs is 1.23 (95% CI 1.03-1.47), down from an unadjusted 1.42 (1.20-1.68). Chlamydia and gonorrhoea lose significance entirely once adjusted (1.09, 0.79-1.51; and 1.44, 0.95-2.16). Only high-titer syphilis survives with a clear effect, adjusted PRR 1.68 (1.10-2.55). Read literally, most of the migrant excess in this sample is the age, sex and community composition of migrants, who are younger and more concentrated in the fishing community, and only the syphilis signal is separately about migration. That argues for reproducing the migrant excess through the existing age and community risk structure rather than adding a migration state.

The interaction with HIV serostatus is the piece that bears on the coinfection structure. Curable STI prevalence among people living with HIV was 49.4% in migrants and 32.6% in residents (adjusted PRR 1.42, 1.10-1.85), against 29.7% and 21.0% in HIV-negative participants (adjusted PRR 1.10, 0.88-1.39). High-titer syphilis among migrants living with HIV was 20.0% against 5.2% in migrants without HIV. STI-HIV clustering is therefore steeper in the mobile subgroup, which matters for any targeting arm that reaches people through HIV services.

What it cannot supply: no incidence, no duration, no treatment or care-seeking outcome, and no diagnostic performance figure. It is cross-sectional, so it cannot say whether infections were acquired before or after the move, which is exactly the quantity a mobility mechanism in the model would need.

## Key points

High-titer syphilis in male migrants was 11.2%, against 4.9% in long-term resident men (adjusted PRR 1.82, 1.06-3.13), and against a 2.0% national estimate of active syphilis in Ugandan men from UPHIA 2016-17. Among migrants aged 40 and above it was 16.3% against 3.6% in same-age residents (adjusted PRR 3.48, 1.52-7.95). Syphilis is the one pathogen where the migrant signal is large, male-skewed, and older-skewed, inverting the usual female-higher pattern of the other three.

Curable STI prevalence in female migrants was 38.8% against 28.3% in male migrants (age-adjusted PRR 1.38, 1.01-1.89).

Migrants reported more partners in the past year: 39.9% reported more than one against 30.5% of residents. They were also less likely to be on ART if self-reporting HIV, 68.2% against 90.6%.

HIV prevalence was lower in migrants (23.7% vs 27.6%) and not significantly different after adjustment, which the authors flag as inconsistent with larger analyses in this same population that do find elevated HIV incidence among recent migrants.

## Limitations

Cross-sectional, so acquisition before versus after migration is indistinguishable. Two communities selected partly for a highly migratory fishing population, both high HIV burden, so the levels do not transfer to lower-burden settings. Participation was 73% of census-eligible individuals and skewed: 64.1% in men against 77.7% in women, 64.4% at ages 15-29 against 76.3% at 30-49, biasing prevalence in the direction of the groups that showed up. Short-term mobility and migration distance were not captured, so "long-term resident" includes circular movers. No multiplicity adjustment across the many subgroup analyses. The OSOM trichomonas rapid test is not validated for male penile meatal swabs, and female swabs were self-collected, so trichomonas figures in particular carry measurement error. Serology cannot separate active, latent and resolved syphilis, which is why high-titer syphilis at RPR at least 1:8 is the more usable of the two syphilis numbers.

## Methodology

Modified Poisson regression with robust standard errors, giving prevalence risk ratios directly rather than odds ratios. Sexual behaviour was deliberately left out of the adjustment set, on the grounds that it is both mediator and confounder and that the question was which demographic subgroup to prioritise for services. So the adjusted PRRs above are not "migration net of behaviour", they are migration net of demography with the behavioural pathway left open.
