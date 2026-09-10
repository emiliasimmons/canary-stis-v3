---
type: entry
title: Effectiveness of Voluntary Medical Male Circumcision for HIV Prevention in Rakai, Uganda
description: RCCS cohort 2009-2016, adjusted IRR 0.47 for HIV acquisition in newly circumcised non-Muslim men, with VMMC uptake 9.8/100 PY
author: Loevinsohn et al.
published: 2021-04-01
resource: 10.1093/cid/ciaa1533
local: raw/10.1093/cid/ciaa1533
tags: [hiv, rakai]
updated: 2026-09-10 00:21
---

An observational cohort analysis inside the Rakai Community Cohort Study measuring how much
protection men actually got from the PEPFAR-supported circumcision programme, as opposed to
the 50-60% efficacy the three randomized trials established. Extracted text and tables sit in
`raw/10.1093/cid/ciaa1533`.

The cohort is 3916 non-Muslim men, HIV-uninfected and uncircumcised at entry, followed across
RCCS survey rounds 13-17 (2008-2016, surveys roughly every 18 months) in 30 agrarian and
semiurban communities, for 17 088 person-years (PY).

## Relevance to project

Two uses, both for the HIV side of the model at the Rakai calibration site.

A prior or fixed parameter for male circumcision as a per-exposure susceptibility reduction:
adjusted incidence rate ratio 0.47 (95% CI 0.28-0.78) with adjustment for demographics and
sexual behaviour, 0.49 (0.30-0.81) with demographics alone, crude 0.41 (0.25-0.66). The effect
does not decay: incidence is 0.75/100 PY in the first year after surgery and 0.31/100 PY at
1-2 years, staying low beyond 5 years, so a time-invariant multiplier on male acquisition is
defensible.

Background HIV incidence levels and their decline over the calibration window, in men aged
15-49: 0.98/100 PY uncircumcised (118/12 095.1 PY) and 0.40/100 PY circumcised
(20/4992.8 PY) over the whole period. Split by round, uncircumcised men went from 1.33/100 PY
(visits 13-14, 2008-2011) to 0.74/100 PY (visits 15-17, 2011-2016), a 44% decline, while
circumcised men went from 0.86 to 0.30/100 PY. By age among uncircumcised men, incidence is
0.64/100 PY at 15-24, 1.57/100 PY at 25-34, and 0.76/100 PY at 35 and over, which gives a
shape for the male age-incidence profile to calibrate against.

Circumcision coverage is a time-varying model input rather than a static one. Incident VMMC
ran at 9.80/100 PY (95% CI 9.26-10.37) overall, rising monotonically from 7.0/100 PY to
11.6/100 PY by 2016; 34% of the eligible non-Muslim cohort was circumcised during follow-up.
Roughly 15% of men in the region are Muslim and circumcised in infancy, and about 60% of male
RCCS participants were circumcised as of 2017.

What it cannot supply: nothing on STI incidence, on care-seeking for STI symptoms, or on the
diagnostic pathway. Genital ulcer disease appears only as a self-reported binary covariate
(9% vs 7% at baseline in men who stayed uncircumcised vs those who took up VMMC), which is too
coarse to serve as an STI calibration target.

## Key points

Men adopting VMMC were selected: median age 23 (IQR 18-31) versus 27 (19-35) for men who
stayed uncircumcised, more never-married (53% vs 43%), less likely to have started sex
(80% vs 85%), and more likely to report consistent condom use with casual partners
(52% vs 43%, among those reporting casual partners). The median age at VMMC fell from 28
(IQR 21-35) to 22 (IQR 18-29) across the study period. Adjusting for these behaviours barely
moved the effect estimate, 0.49 to 0.47, so the selection is not what produces the protection.

Effectiveness held across age strata and calendar periods, with wide intervals in each cell.
Protection persisted in a falling-incidence setting, so the multiplier does not need to be
conditioned on epidemic phase.

## Limitations

Circumcision status and sexual behaviour are self-reported, and the date of surgery is
unknown, only bracketed by 18-month survey intervals. VMMC was assumed to have occurred at
the start of the person-interval in which it was first reported; sensitivity analyses placing
it at the end, or restricting to the interval of surgery, did not move the estimate. Of the
20 infections in circumcised men, 12 were detected at the same visit at which VMMC was first
reported, so the ordering of the two events is unresolved for most of the events driving the
first-year incidence. 68 men (1.7%) reported being uncircumcised after a prior VMMC report and
were retained as circumcised in the primary analysis.

Exposure to HIV-positive female partners was not measured, and residual confounding by
partner serostatus cannot be excluded. Oral PrEP use was not collected, though availability
was scarce in the region during the study window.
