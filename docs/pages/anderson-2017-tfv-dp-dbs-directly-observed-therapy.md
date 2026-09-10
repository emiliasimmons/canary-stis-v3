---
type: entry
title: Intracellular Tenofovir-Diphosphate and Emtricitabine-Triphosphate in Dried Blood Spots following Directly Observed Therapy
description: Directly observed dosing confirms the 350/700/1250 fmol/punch adherence thresholds for 2, 4 and 7 doses per week, the scale on which PrEP efficacy gradients are reported.
author: Anderson et al.
published: 2017
resource: https://doi.org/10.1128/aac.01710-17
local: raw/10.1128/aac.01710-17/content.md
tags: [prep, hiv]
updated: 2026-09-10 10:30
---

Randomised crossover pharmacokinetic study in 48 HIV-negative adults (25 women) in Denver
and San Francisco, each taking two 12-week directly observed regimens of 33%, 67%, or 100%
of daily FTC-TDF separated by a 12-week washout. Raw content in
[raw/10.1128/aac.01710-17/content.md](../raw/10.1128/aac.01710-17/content.md).

## Relevance to project

Fixes the dose-to-concentration mapping that lets a PrEP efficacy estimate reported by
dried blood spot concentration be read as an efficacy estimate per doses per week. The
paper also carries the iPrEx OLE efficacy gradient itself: 84% HIV risk reduction (95% CI
21-99%) at 350-699 fmol/punch and 100% (95% CI 86-100%) at 700 fmol/punch or above, in men
who have sex with men. Those two figures are candidate values for a PrEP efficacy
parameter conditioned on an adherence state, and the corresponding dose levels (roughly 2-3
and 4 or more doses per week) give the adherence bands a behavioural model can carry.

The sex difference matters for a model that assigns PrEP effectiveness by sex: at the same
number of doses per week women reach 17-19% higher blood TFV-DP than men, so a fixed
concentration threshold implies fewer required doses for women (75% of women reached 700
fmol/punch on 2.0 doses per week or more, against 3.2 for men).

Concentration-efficacy evidence is from men who have sex with men only, so the female
mapping supports an adherence interpretation, not an efficacy value.

## Key points

TFV-DP was dose proportional (slope 1.01, 90% CI 0.92-1.10 by randomisation arm), with
mean steady-state concentrations of 530, 997, and 1,605 fmol/punch for 33%, 67%, and 100%
dosing. Median washout half-life 17 days (range 14-23), steady state by week 8.

Fitted 25th percentiles for 2, 4, and 7 doses per week were 347, 714, and 1,280
fmol/punch, within 3% of the previously used 350/700/1,250 thresholds; every subgroup by
site, race, and sex fell within 14%.

Intermittent missed doses and weekend-holiday missed doses gave concentrations within 4% of
each other at the same weekly total, so the measure reads weekly dose count and not the
pattern.

Once at steady state, within-person concentrations were stable: 95% of consistently
adherent participants would fall within roughly plus or minus 6% of their previous value.

Fingerstick spots ran 11.7% lower (95% CI 9.5-13.9%) than paired venipuncture spots, with
intraclass correlation 0.89.

Across iPrEx OLE, ATN 110/113, and PrEP-Demo (over 2,000 person-years), of 37 seroconverters
23 were below the limit of quantitation, 13 fell below 350 fmol/punch, one fell in 350-699,
and none reached 700 or above.

## Limitations

Forty-eight participants in two US cities, median age 29, dosing directly observed with 97%
of doses taken near a meal, so between-person variability is narrower than a field
population's.

A single concentration maps to a wide range of possible dosing rates: 700 fmol/punch in men
corresponds to a median 4.1 doses per week with a quarter of individuals below 3.2, so an
adherence category assigned from one spot carries substantial misclassification.

Blood concentrations only. The paper draws no tissue inference, and the mechanism behind
the sex difference is unresolved.

Three breakthrough HIV infections have been reported at 1,478-2,297 fmol/punch, two
involving resistant virus, so the 100% risk reduction estimate at high concentrations is an
upper bound from a small number of events.
