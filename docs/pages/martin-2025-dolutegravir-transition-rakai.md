---
type: entry
title: "Patterns of HIV-1 viral load suppression and drug resistance during the dolutegravir transition"
description: RCCS 2011-2023 population-scale trends in HIV prevalence, ART coverage, viral suppression and the prevalence of viraemia, alongside drug resistance during dolutegravir scale-up.
author: Martin et al.
published: 2025-09-02
resource: 10.1101/2025.09.01.25334862
local: raw/10.1101/2025.09.01.25334862
tags: [hiv, rakai, care-seeking]
updated: 2026-09-10 10:35
---

medRxiv preprint, not peer reviewed. Six Rakai Community Cohort Study survey rounds from
August 2011 to March 2023, covering 48,914 people and 109,328 participant-visits, with HIV
testing, Abbott m2000 viral load quantification and viral deep sequencing. Prevalences were
estimated by robust Poisson regression with generalised estimating equations for repeat
participation, resistance outcomes were inverse-probability weighted for missing sequence
data, and the individual-level suppression analysis used Bayesian logistic regression with
post-stratification by survey, age, community type and sex. Extracted text sits in
`../raw/10.1101/2025.09.01.25334862/`.

## Relevance to project

The treatment-cascade time series for the project's calibration site, on the exact quantity
that determines the force of infection. Population prevalence of viraemic HIV among all
RCCS participants fell 4.6-fold (95% CI 4.06-5.21) over the study period to 1.7% (1.6-2.0%)
by 2022, and the authors are explicit that this is what governs acquisition risk for
seronegative participants.

Fittable series, all RCCS aged 15-49 (the questionnaire frame; the abstract quotes 15-59):

- HIV prevalence among participants fell from 20.5% (19.9-21.2%) to 18.1% (17.6-18.7%).
- Ever having been on ART, self-reported, among people living with HIV rose from 35.4%
  (33.9-37.1%) to 94.4% (93.6-95.2%).
- Suppression below 1,000 copies/mL among people living with HIV rose from 57.1%
  (55.4-58.8%) in 2014 to 90.3% (89.2-91.4%) in 2022, and among the treatment-experienced
  from 93.6% (92.8-94.4%) in 2019 to 95.4% (94.6-96.1%) in 2022.
- Among people with viraemia, the treatment-experienced share rose 3.14-fold (prevalence
  ratio CI 2.6-3.80), from 13.4% (11.7-15.3%) in 2014 to 42.1% (36.7-48.3%) in 2022.

That last series is the structural point for a model of the SOC and POC arms. As treatment
coverage saturates, the residual viraemic population stops being people who never started
and becomes people who started and disengaged, which is a different group to reach and a
different care-seeking pathway. A model that represents ART as coverage alone misses this
composition shift.

Baseline context the paper gives for RCCS communities: inland prevalence about 14-17%,
Lake Victoria fishing communities about 42%, survey rounds every 18-24 months.

Drug resistance is out of scope for a model with no viral strain structure. Nothing here
bears on STIs.

## Key points

Dolutegravir uptake at the 14 clinics serving 74.1% of 2022 RCCS participants reporting ART
went from 53.6% (13,248/24,735) at the end of 2019 to 97.2% (26,831/27,597) at the end of
follow-up. Uptake was slower among women during early 2020 (adjusted p = 0.0002); by 2020
84.4% of men and 64.6% of women were on dolutegravir-based regimens.

Resistance to any drug class among treatment-experienced viraemic people fell from 51.1%
(40.7-64.1%) in 2014 to 27.9% (21.3-36.5%) in 2022, which the authors read as the viraemic
population shifting from treatment failure towards disengagement from care.

Only two participants carried intermediate or high-level dolutegravir resistance
(inQ148R, inE138K, inG140A), and none was seen pre-treatment. A low-level integrase
inhibitor mutation, inS153Y, appeared in 7.5% of sequenced viraemic individuals, with
genetic clustering suggesting transmission among 5 of them.

Pre-treatment NNRTI resistance kept rising after NNRTI-based first-line regimens were
discontinued, reaching 14.8% by 2022.

By 2022, prior NNRTI or NRTI resistance no longer predicted failure to suppress (risk
ratios 1.14, 95% HPD 0.96-1.32, and 1.12, 0.88-1.35).

Median age of participants with HIV rose from 32 (IQR 10) to 37 (IQR 11) years over the
study, so the prevalence series is measured against an ageing infected population.

## Limitations

Preprint, not peer reviewed.

Denominators need care. The results report 48,914 people, 8,781 of them seropositive at
some point, contributing 109,328 participant-visits, while the abstract quotes 20,383
people living with HIV. The larger figure is almost certainly participant-visits among
people living with HIV rather than distinct people, and a target drawn from this page
should be checked against the appendix tables.

Treatment-experienced viraemic analyses start in 2014 because 2012 viral loads are missing,
so the resistance series is one round shorter than the suppression series.

ART exposure and care history are self-reported, and the pre-treatment definition depends
on a participant never reporting a test result, care access, long-term medication or ART
across all rounds back to 1994.

The dolutegravir prescription data come from clinic records at 14 facilities, not from
participants, and cover 74.1% of those reporting ART use in 2022, so uptake outside those
clinics is unobserved.

Suppression is defined at under 1,000 copies/mL, and part of the recent gain is attributed
to a shift towards viral loads at or below 200 copies/mL, so the threshold choice affects
the size of the trend.
