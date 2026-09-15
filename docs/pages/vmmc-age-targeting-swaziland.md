---
type: entry
title: "Voluntary Medical Male Circumcision for HIV Prevention in Swaziland: Modeling the Impact of Age Targeting"
description: Compartmental model of VMMC scale-up by client age group in Swaziland, reporting infections averted, incidence reduction, and cost per infection averted.
author: Kripke et al.
published: 2016-07-13
resource: 10.1371/journal.pone.0156776
local: raw/10.1371/journal.pone.0156776
tags: [hiv, modeling]
updated: 2026-09-10 00:22
---

Source: [kripke-2016](https://doi.org/10.1371/journal.pone.0156776)

A policy-facing modeling exercise run for the Swaziland Ministry of Health in 2013-2014, asking which male age groups a voluntary medical male circumcision (VMMC) program should target. The tool is DMPPT 2.0, a compartmental Excel model that tracks circumcised males by five-year age group through ageing and mortality, and compares a scale-up scenario against a baseline holding circumcision prevalence fixed.

Inputs: age-specific male HIV incidence from the Swaziland HIV Incidence Measurement Survey (SHIMS); population, mortality, births, and HIV prevalence from a national Spectrum/Goals projection; baseline circumcision prevalence by age from the 2006-07 Swaziland DHS (8.2% overall, 4% at ages 10-19 rising to 20% at 35-39). VMMC unit cost $109 USD, held constant across ages; ART $536 per person-year. Costs, circumcisions, and infections averted all discounted 3% per year. National context: adult HIV prevalence 31% and incidence 2.4% per year at ages 18-49.

## Relevance to project

Context and a design reference, not a parameter source. Nothing here feeds the canary-stis model directly: it is HIV-only, has no STI compartments, no sexual network, and is not Rakai. Its use here is as a worked example of the question canary-stis is asking in a different intervention idiom, which is how much HIV prevention benefit you buy by targeting a delivery channel at particular people rather than expanding it uniformly.

Two things transfer. First, the metric set: VMMCs per infection averted, incidence reduction at 5 years (immediacy), incidence reduction at 15 years (magnitude), and cost per infection averted. That is a usable template for reporting POC-versus-SOC arm differences, and it makes explicit that a targeting conclusion is only defined relative to a stated horizon. The paper's own results invert between horizons: ages 20-29 give the fastest incidence drop by 2018, ages 15-29 the largest by 2028, ages 10-14 the largest over 2014-2048.

Second, the null result on discrimination. Because the SHIMS age-specific incidence estimates carry wide confidence intervals, the uncertainty bounds on infections averted overlap across every age group, so the age strategies are formally indistinguishable in this analysis. Cost per infection averted ranges $1,200-$1,500 across the six named scenarios with intervals like ($900, $1,600) that cover the whole spread. This is a direct warning for the pathway-decomposition aim here: if the calibration target's uncertainty is wide, a decomposition into direct treatment, prevention targeting, and network position may not separate the pathways even when the point estimates differ.

Also a mild comparator on magnitude. VMMC's efficacy against female-to-male transmission is 60% and lifelong, and scaling to 70% coverage among males 10-49 averted 47-72% of infections in the model over 15 years. Any HIV-incidence reduction claimed for POC STI diagnostics should be read against that scale.

## Key points

- The lowest VMMCs per infection averted over 2014-2028 come from circumcising ages 15-19 (12, +/- 4), 20-24 (8, +/- 2.3), 25-29 (8, +/- 2.8), and 30-34 (9, +/- 4.3); bounds overlap.
- Lowest cost per infection averted over 15 years: ages 15-34 at $870, ages 15-29 at $890. Scenarios with 10 as the lower age bound cost more per infection averted than the matching scenarios starting at 15.
- Scaling up ages 10-34 delivers 93% of the infections averted by scaling up ages 10-49.
- Infections averted are counted population-wide, including secondary infections in women avoided because fewer men are infected.
- Early infant circumcision adds cost and contributes nothing to infections averted inside the 15-year window, since the boys reach sexual maturity 15-18 years later.
- The Ministry of Health adopted Scenario E (50% neonatal, 80% at ages 10-29, 55% at 30-34) into the 2014-2018 Male Circumcision Strategic and Operational Plan, choosing on feasibility and demand as much as on the model, and against overlapping uncertainty bounds. Demand was the binding constraint: clients aged 10-24 were 75% of the program's 2009-2014 caseload and under 5% were over 35.

## Limitations

- SHIMS incidence was held fixed at its measured value for every model year, so no incidence decline is projected. Absolute impact is biased in whichever direction incidence actually moved; relative ranking across age groups survives only if the age distribution of incidence is stable.
- Unit cost came from PSI expenditure data, not a facility-based costing study, and was assumed identical across client ages despite differing reach.
- SHIMS did not enroll anyone under 18. Incidence at 10-14 was set to zero by assumption and at 15-19 to 70% of the 18-19 value; incidence above 49 came from the Goals model.
- The model carries no sexual network and no risk structure beyond age and sex, so it cannot say anything about who within an age group is reached.
- Nothing on how to achieve scale-up: demand creation, its cost, and human resource requirements are all outside the model.
