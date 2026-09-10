---
type: entry
title: "Progress towards the UNAIDS 90-90-90 goals by age and gender in a rural area of KwaZulu-Natal, South Africa"
description: Household survey of the HIV care cascade in Mbongolwane and Eshowe, 2013, with laboratory-confirmed ART status and viral load by sex and age
author: Huerga et al.
published: 2018-03-01
resource: https://doi.org/10.1186/s12889-018-5208-0
local: raw/10.1186/s12889-018-5208-0
tags: [hiv, care-seeking]
updated: 2026-09-10 00:20
---

A cross-sectional household survey of 5649 people aged 15-59 (84.5% of 6688 eligible, 2377 households, two-stage stratified cluster sample from the 2011 census) in the Mbongolwane and Eshowe Health Service Areas of KwaZulu-Natal, South Africa, conducted July-October 2013, eight years into the public ART programme and two years into MSF support. Extracted text sits in `raw/10.1186/s12889-018-5208-0`.

What distinguishes it from self-reported cascade surveys: ART status was measured as antiretroviral drug presence in blood (nevirapine, efavirenz, lopinavir, by LC-MS/MS on dried blood spots), not by asking. Only diagnosis awareness and linkage were self-reported. The ART initiation threshold at the time was CD4 below 350 cells/uL, so the numbers describe a pre-universal-treatment programme.

## Relevance to project

A comparator cascade for the model's HIV treatment pathway, and a source of conditional-probability priors on the steps between infection and suppression. The three UNAIDS proportions here, among the 1384 HIV-positive participants with complete diagnosis, drug-presence and viral-load data: 76.4% (95% CI 74.1-78.6) knew their status, 69.9% (67.0-72.7) of those diagnosed were on ART, and 93.1% (91.0-94.8) of those on ART were suppressed below 1000 copies/mL. Referred to the full HIV-positive denominator, 71.0% were linked to care, 62.7% in care, 53.5% on ART, and 57.4% virally suppressed.

The sex and age gradients are the part worth carrying into a risk-structured model. Diagnosis was 79.0% in women versus 68.3% in men (p < 0.001), and 83.3% at ages 30-59 versus 64.0% at 15-29 (p < 0.001). Suppression among the full positive denominator was 60.3% in women versus 47.9% in men, and 66.2% at 30-59 versus 41.3% at 15-29. Suppression conditional on ART did not differ by sex (93.4% versus 92.1%, p = 0.584), so the entire sex gap in population viral suppression comes from the diagnosis and treatment-initiation steps, not from adherence. That maps directly onto the project's care-seeking door: the same asymmetry that keeps men out of HIV diagnosis is the one that governs who reaches a symptomatic-STI clinic visit where a point-of-care panel could be offered.

Of 590 unsuppressed HIV-positive participants, 279 (47.3%) were undiagnosed and 260 (44.1%) were diagnosed but not on ART, a bound on how much residual transmission a testing-side intervention could in principle reach in this setting.

HIV prevalence among 15-59s was 25.2% (95% CI 23.6-26.9): 30.9% in women, 15.9% in men, peaking at 56.5% in women aged 30-34 and 45.5% in men aged 35-39, with the male peak lagging the female one by about five years. Usable as a rough prevalence and age-shape check, though for a Rakai-calibrated model this is an out-of-site comparator, not a target.

## Key points

- ART coverage measured by drug assay rather than self-report, so the second 90 is not inflated by reporting bias.
- The third 90 was met in every sex and age stratum; the first two were not.
- Among 1400 HIV-positive participants with a CD4 count, median was 483 cells/uL (IQR 332-665) and 9.3% were below 200. Among the 655 not on ART, 11.9% were below 200, so late presentation persisted despite a functioning programme.
- Peak female prevalence at 30-34 and male at 35-39.

## Limitations

- 2013 data under a CD4 350 initiation threshold. Second-90 figures are not transferable to a treat-all era.
- KwaZulu-Natal, not Rakai. Prevalence, cascade, and demography all differ from the project's calibration site, so this is a comparator and a shape prior rather than a target.
- Diagnosis awareness and linkage self-reported, subject to misclassification (the authors' own caveat).
- Cross-sectional and 15-59 only; says nothing about incidence, nothing about STIs, and nothing about partnership structure.
- Women were 62.3% of participants and men aged 15-19 were 31.9% of male participants, plausibly reflecting out-migration of working-age men, which may bias the male cascade estimates.
