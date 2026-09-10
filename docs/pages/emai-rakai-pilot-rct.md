---
type: entry
title: Mobile ecological momentary assessment and intervention in Rakai, Uganda
description: Pilot RCT in an RCCS subsample measuring daily self-reported condomless sex with a non-regular partner, among other behaviors
author: Beres et al.
resource: https://doi.org/10.2196/22693
local: raw/10.2196/22693
tags: [rakai, sexual-networks]
updated: 2026-09-10 00:36
---

A 90-day pilot randomized trial in Rakai, Uganda, testing whether automated, behavior-responsive phone messaging (ecological momentary assessment and intervention, EMAI) changes five self-reported behaviors: fruit and vegetable consumption, alcohol, cigarette smoking, and sex with a non-marital or non-long-term partner without a condom. Registered as NCT04375423, funded by the Johns Hopkins Center for Global Health.

The extracted file at `raw/10.2196/22693` is the CONSORT-EHEALTH submission form (57 pages, July 2020), not the article. It carries quoted excerpts from the manuscript, so numbers below come from those quotes; the trial's tables (1-4) are not reproduced in it.

## Relevance to project

Context, and a weak order-of-magnitude check on non-regular-partner sex frequency in the Rakai population. Not a calibration target and not a prior.

The one figure with any bearing on the model is the mean proportion of follow-up days on which a participant reported sex with a non-marital or non-long-term partner without a condom: 1.9% of days in the control arm and 6.6% in the intervention arm during the first ~30-day period, falling to 1.0% and 1.3% by the third period. Denominator is person-days of app follow-up among 48 analysed adults aged 18-49 (24 per arm), self-reported, in an RCCS subsample restricted to people with a listed phone number and at least secondary education, purposively recruited for variation in age, sex, and occupation with a target of at least 20% traders and 20% farmers.

That sampling frame is the reason this cannot be a target. It is a small, educated, phone-owning slice of the cohort, the arms differ threefold at baseline on the very behavior of interest, and the measure is days-with-an-act rather than acts or partners, which is not the quantity the network model parameterizes. It does say that condomless non-regular-partner sex is reported on a low single-digit percentage of days in this group, which is a sanity bound on act rates through casual partnerships if nothing better is available.

The trial has no STI or HIV endpoints, no diagnostics, and no biomarkers, so it bears on none of the diagnostic-performance or treatment-pathway parameters.

## Key points

- 71 screened between 10 June 2016 and 1 March 2017, 58 enrolled, 48 in the analysis set. Eight excluded for an early application failure, two dropped out at 15 and 79 days.
- All participants submitted EMA data alone for the first 30 days, then were randomized; the intervention arm additionally received automated messages responsive to their reports for days 31-90.
- Behavioral data were captured on 85.5% of combined follow-up days.
- Condomless non-regular-partner sex fell significantly within both arms between periods 1 and 3 (control 1.9% to 1.0% of days, P=.02; intervention 6.6% to 1.3%, P=.03), and within the intervention arm between periods 1 and 2 (6.6% to 2.1%, P=.04). No significant between-arm difference in change for this behavior.
- Alcohol fell in both arms (control 9.6% to 4.3% of days, P=.03; intervention 7.2% to 2.4%, P=.01). The only significant between-arm difference on any behavior was vegetable consumption.
- The authors read the within-arm declines in both groups as evidence that measurement alone, not just the messaging, may move reported behavior.

## Limitations

Pilot sized, explicitly not designed to generalize beyond its target population or 90 days, and analysed descriptively. Everything is self-reported, and the authors concede they cannot separate real behavior change from social-desirability reporting reinforced by the intervention messages. Participants were current RCCS members accustomed to research participation. Block randomization with at most ten simultaneously active participants confounds calendar time with arm, which the authors invoke to explain the control-arm vegetable decline; the same confounding applies to the sexual-behavior series.
