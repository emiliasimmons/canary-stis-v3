---
type: entry
title: "Time to HIV testing of sexual contacts identified by HIV-positive index clients in Siaya County, Kenya"
description: Routine partner-services program data on 6,845 elicited sexual contacts; median 14.5 days from notification to HIV test, with only 48.8% projected to ever test over 1.25 years.
author: Wekesa et al.
published: 2020-09-08
resource: 10.1371/journal.pone.0238794
local: raw/10.1371/journal.pone.0238794
tags: [partner-notification, hiv, care-seeking]
updated: 2026-09-10 00:19
---

Retrospective analysis of routine partner-services registers from 117 health facilities in
Siaya County, western Kenya (June 2017 to August 2018), a setting with 15-21% adult HIV
prevalence. HIV-positive index clients named adult (18+) sexual contacts; the analysis
follows those contacts from the date they were named to the date they tested for HIV, with
contacts untested at the August 2018 data cut right-censored. Cox proportional hazards
with facility-level clustering and, where the proportionality assumption failed,
time-varying covariates interacted with log time.

## Relevance to project

This is the delay-and-leakage bound on a partner-notification pathway, which the model
does not implement. It supplies the numbers that say why that omission is defensible and
what would have to be assumed if a PN arm were ever added: of 6,845 elicited contacts only
2,800 (40.9%) had tested by the data cut, and the Kaplan-Meier projection over 1.25 years
of follow-up reaches 48.8% (95% CI 46.8-50.8). So roughly half of named contacts never
arrive at the testing door at all, and the ones who do arrive at a median of 14.5 days
(IQR 2.5-62) after notification, not same-day. A PN arm parameterised optimistically at
near-complete partner reach would be inconsistent with routine program data from a
high-prevalence East African setting.

It is also a care-seeking comparator for the model's symptomatic-presentation door. The
delay here is measured from an exposure notification rather than from symptom onset, so it
does not transfer directly to the symptomatic care-seeking rate, but it bounds the tail: a
quarter of tested contacts took more than 62 days, and among the untested the median
follow-up already stood at 173.5 days (IQR 124.5-261.5).

The differential by partnership type bears on the risk-structured network. Non-spouse
contacts tested faster than spouses (aHR 1.23, 95% CI 1.15-1.32, time-varying model) but
spouses who did test were the fastest group in absolute terms (median 6.5 days, IQR
0.5-35.5, versus 21.5 days, IQR 5.5-74.5 for non-spouses); the hazard ratio is driven by
the large body of spouses who never tested (2,096 of 3,064, 68%). Reaching casual and
non-marital partners is slow, not absent.

Nothing here is a calibration target: the site is Siaya County, not Rakai, the outcome is
HIV testing rather than STI treatment, and the denominators are program registers rather
than a population cohort.

## Key points

Of 6,845 contacts, 3,858 (56.4%) men, 3,209 (46.9%) aged 25-34, 3,873 (56.6%) married
monogamous, 3,781 (55.2%) non-spousal.

Testing uptake by the data cut differed by partnership: 65.4% of tested contacts were
non-spouse versus 48.2% of untested (p < 0.001). Married monogamous contacts were
over-represented among the untested (60.3% versus 51.1%, p < 0.001).

Younger contacts tested sooner: aHR 1.32 (95% CI 1.01-1.73) for ages 18-24 and 1.18
(1.01-1.39) for 25-34, both relative to 35-44. The effect vanished in the time-varying
model (aHR 0.94 and 0.96, both non-significant), meaning the age advantage is an early-days
effect that does not persist.

Married polygamous (aHR 1.12, 1.01-1.25) and single contacts (aHR 1.17, 1.08-1.27) tested
sooner than married monogamous, in the time-varying model.

Median days to test varied nearly fourfold by sub-county, from 9.5 (Alego Usonga) to 39.5
(Ugunja), on a shared program protocol.

## Limitations

Routine implementation data collected for program management, not research: the authors
flag likely incompleteness and inaccuracy. The date of notification is taken as the date
the contact was named by the index client, so any lag between elicitation and the contact
actually being reached is folded into the measured time-to-test, inflating it by an unknown
amount.

Contacts still under follow-up at the August 2018 cut are censored, and the censoring is
heavy (59.1% of the sample), so the 48.8% figure is a model projection rather than an
observed proportion.

The notification method (passive, provider, contract, dual referral) is not recorded, and
the Malawi trial the authors cite shows time to presentation depends strongly on it. So
the 14.5-day median is a mixture over unknown notification modes.

Marital status is unknown for 1,855 contacts (27.1%), and that category behaves distinctly
in the model (aHR 1.25, 1.14-1.38), which suggests it is not missing at random.

Single-county data; the authors do not claim generalizability beyond Siaya.
