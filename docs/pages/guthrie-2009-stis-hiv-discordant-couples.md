---
type: entry
title: "Sexually Transmitted Infections among HIV-1-Discordant Couples"
description: Enrollment cross-section of 416 Kenyan HIV-discordant couples: 16% of couples had a curable STI, and a partner's STI raised the odds 5.9-fold
author: Guthrie et al.
published: 2009-12-14
resource: https://doi.org/10.1371/journal.pone.0008276
local: raw/10.1371/journal.pone.0008276/
tags: [sti, hiv, coinfection, partner-notification]
updated: 2026-09-10 00:12
---

Source: [guthrie-2009](https://doi.org/10.1371/journal.pone.0008276)

Cross-sectional analysis of enrollment data from 416 stable HIV-1-discordant couples in Nairobi, Kenya, recruited 2004-2007 from voluntary counseling and testing centers and antenatal clinics. The couples were nested in the Partners in Prevention HSV/HIV Transmission Study, an acyclovir trial, so every HIV-positive partner was HSV-2-seropositive with CD4 >= 250 cells/uL and not on ART. All participants were tested at enrollment for syphilis (RPR with TPHA confirmation), chlamydia, gonorrhoea and trichomoniasis (nucleic-acid amplification on male urine and female cervical swabs), plus HSV-2 serology, bacterial vaginosis and cervical cytology.

## Key points

- 65 of 403 couples (16.1%) with known status had a curable STI (syphilis, gonorrhoea, chlamydia or trichomoniasis) in one or both partners. Among individuals, 46 of 416 women (11.4%) and 30 of 416 men (7.2%) were positive.
- Trichomoniasis and syphilis carried the burden. Trichomoniasis ran 8.5% in HIV-positive women (27/322), 3.5% in HIV-negative women, 5.0% in HIV-negative men and 2.1% in HIV-positive men. Syphilis ran 1.9-3.2% across the four strata. Chlamydia was found in 7 people total (<= 1.2% in any stratum) and gonorrhoea in nobody.
- Curable-STI prevalence did not differ by HIV status within sex (P > 0.30 both sexes).
- A participant was 5.9-fold more likely to carry a curable STI if the partner did (OR 5.90, 95% CI 2.31-14.37, FDR-corrected P < 0.01). Despite that, only 11 of 64 affected couples (17.2%) were concordant-positive; in 35 (54.7%) only the woman was infected and in 18 (28.1%) only the man. Among the 51 STI-discordant couples the woman was the infected partner in 68.6% (binomial P = 0.01).
- Couple-level correlates: any unprotected sex in the past month OR 2.43 (1.34-4.37), less than primary education in either partner OR 3.00 (1.68-5.37), relationship duration >= 4 years OR 0.30 (0.14-0.64) against <= 1 year. An outside partner in the past month gave OR 4.36 (1.23-15.49), not significant after FDR correction.
- Bacterial vaginosis was present in 32.0% of HIV-positive and 29.6% of HIV-negative women, and was the strongest individual correlate of a curable STI in women (OR 3.68, 1.76-7.79).
- Recent genital sores predicted *lower* odds of a current curable STI in HIV-positive participants (OR 0.17, 0.02-0.69), which the authors read as syndromic treatment already having cleared the infection.
- HSV-2 serodiscordance was common: among HIV-negative partners of HSV-2-positive index cases, 77.7% of women but only 50.0% of men were seropositive (RR 1.55, 1.33-1.81).

## Relevance to project

A prior on within-partnership STI clustering, and a comparator for the couple-level structure of curable STI burden outside Rakai. The 5.9-fold partner odds ratio and the 17% concordant / 83% discordant split among affected couples bound how tightly the model should correlate infection status across a stable partnership: a shared-network model that produces near-perfect within-couple concordance in curable STIs would be too clustered for this data, while independence across partners would miss the observed 5.9-fold association.

The stratum-specific prevalences are usable as an urban Kenyan comparator, not as calibration targets. Gonorrhoea at 0/832 and chlamydia at 7/832 are far below what the model needs to reproduce for Rakai, and the trial's eligibility criteria explain most of the gap (see limitations). Trichomoniasis at 8.5% in HIV-positive women is the one figure in the same range as population-based southern Uganda estimates.

Two further uses. First, the genital-sores finding is direct evidence that syndromic management does clear curable infections in the population that presents with symptoms, which supports the SOC arm treating symptomatic care-seeking as an effective (if narrow) door. Second, the 83% of affected couples that are STI-discordant quantifies what a partner-notification pathway would be reaching. The model implements no such pathway, so this figure sizes the omission rather than parameterizing anything.

## Limitations

- Eligibility selected on stability and health: couples reported sex >= 3 times in the prior 3 months, planned to stay together, and the index partner had CD4 >= 250 and no clinical AIDS. The authors expect this lowered risk behavior and curable-STI prevalence below the general population. 79% of women and 77% of men reported zero unprotected sex acts with the study partner in the past month.
- All HIV-positive partners were HSV-2-seropositive by design, so the HSV-2 figures are conditional on that and are not population seroprevalences.
- The zero gonorrhoea count and near-zero chlamydia counts leave those two pathogens with no usable estimate here; several odds ratios (cervical cytology 4.97, CI 0.75-210.06) rest on single-digit cell counts.
- Cross-sectional at enrollment, so nothing about incidence, and STI discordance cannot be separated into not-yet-transmitted, already-cleared, and assay false-negative.
- Syphilis by RPR plus TPHA cannot cleanly separate current from treated past infection, though most positives had RPR >= 1:8.
- The HSV-2 Focus ELISA cutoff of 3.5 (raised for specificity) will have missed true infections and inflated measured serodiscordance.
- Nairobi, urban, 2004-2007, pre-ART-for-prevention. Care-seeking and treatment context differ from the model's calibration site.
