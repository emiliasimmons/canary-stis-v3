---
type: entry
title: Point-of-care STI testing improves HIV pre-exposure prophylaxis initiation in pregnant women in antenatal care in Cape Town, South Africa
description: POC STI testing doubled the odds of PrEP initiation among pregnant women compared to lab-based testing, but PrEP continuation at 3 months was lower in the POC group.
author: de Voux et al.
published: 2023-02-01
resource: 10.1097/olq.0000000000001729
local: raw/10.1097/olq.0000000000001729/content.md
tags: [sti, diagnostics, prep]
updated: 2026-09-10 09:47
---

Prospective cohort study (PrEP-PP) of 1194 HIV-uninfected pregnant women at their first
antenatal visit at the Gugulethu MOU in Cape Town, South Africa (2019-2021). Women were
tested for CT and NG by POC (Cepheid GeneXpert, Aug 2019 to Nov 2020) or lab-based assay
(ThermoFisher TaqMan, Dec 2020 to Oct 2021) depending on when they enrolled. The switch
from POC to lab testing was forced by COVID-era supply chain disruption, not randomised.
All women received HIV risk counselling and were offered oral PrEP (TDF/FTC). Source at
`raw/10.1097/olq.0000000000001729/content.md`.

## Relevance to project

The paper quantifies a behavioural pathway from POC STI testing to HIV prevention that
operates through PrEP uptake rather than through direct STI cure. The project's POC arm
models the direct effects of etiological test-and-treat on STI prevalence and downstream
HIV transmission, but does not currently model PrEP channelling. This study provides a
comparator estimate for that omitted pathway: a 12 percentage-point increase in PrEP
initiation (90% vs 78%) attributable to same-day STI results and counselling. It is not a
calibration target (the population is pregnant women in Cape Town, not the RCCS cohort),
but it bounds the magnitude of a mechanism the model leaves out and could inform a
sensitivity analysis on unmeasured prevention benefits of POC testing.

## Key points

- STI prevalence was the same across testing groups: 28% any STI (CT or NG) in both POC
  and lab arms.
- POC-tested women had higher PrEP initiation at baseline: 90% vs 78% (aOR 2.07, 95% CI
  1.47-2.91), adjusted for age, gravidity, STI diagnosis, IPV, gestational age,
  employment, HIV risk perception, and cohabitation.
- Same-day STI results and treatment were the proposed mechanism: 79% of POC-tested women
  treated on the day of diagnosis vs 0% of lab-tested women.
- Mean time from test to treatment: 3 days (POC) vs 38 days (lab). 28% of lab-diagnosed
  women never returned for treatment.
- PrEP continuation at 3 months was lower in the POC group: 54% vs 64% (aOR 0.65, 95% CI
  0.49-0.85). The authors suggest the same-day "nudge" that drove initiation may not
  sustain adherence.
- In a sensitivity analysis redefining initiation to include baseline or 3-month start,
  overall PrEP uptake rose to 89%, still higher in POC-tested women (93% vs 84%).

## Limitations

- Not randomised. The switch from POC to lab testing was driven by supply disruption during
  COVID, so the two groups were enrolled in different calendar periods (POC: Aug 2019 to
  Nov 2020; lab: Dec 2020 to Oct 2021). Residual confounding by pandemic-era behaviour
  changes is plausible and acknowledged.
- Population is pregnant women in urban Cape Town, with 27% background HIV prevalence among
  ANC attendees. Generalisability to the Rakai cohort (rural Uganda, both sexes, general
  population) is limited.
- TV was excluded from the STI comparison because the lab assay did not test for it.
- PrEP adherence was measured by self-report and pill count, not by drug levels.
- The PrEP continuation result runs counter to the initiation finding and complicates any
  net HIV-prevention estimate.

## Methodology

Open prospective cohort, not a trial. Logistic regression for PrEP initiation and
continuation, adjusting for eight covariates. n = 1194 for initiation analysis, n = 940
for continuation (after excluding losses and pregnancy losses). Self-collected vaginal
swabs for both testing modalities.
