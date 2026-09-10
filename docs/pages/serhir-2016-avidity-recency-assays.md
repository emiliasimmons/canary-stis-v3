---
type: entry
title: "Performance of Bio-Rad and Limiting Antigen Avidity Assays in Detecting Recent HIV Infections Using the Quebec Primary HIV-1 Infection Cohort"
description: MDRI and false-recency estimates for the CDC-modified Bio-Rad and Sedia LAg avidity assays alone and as a two-step algorithm, in a subtype B cohort with known infection dates.
author: Serhir et al.
published: 2016-05-25
resource: 10.1371/journal.pone.0156023
local: raw/10.1371/journal.pone.0156023
tags: [diagnostics, hiv]
updated: 2026-09-10 10:33
---

Laboratory evaluation of two HIV recency assays in PLOS ONE. Mean duration of recent
infection (MDRI) came from 473 longitudinal specimens from 123 treatment-naive
seroconverters in the Quebec Primary HIV-1 Infection cohort, whose infection dates are
pinned by detectable HIV RNA with a negative EIA followed by documented western blot
seroconversion. False recency rate (FRR) came from 420 specimens from separate individuals
with established infection (90 cohort members over 14 months post-infection, 330 public
health laboratory serobank specimens confirmed positive over 24 months earlier). MDRI was
estimated by nonparametric interval-censored survival, as the area under the survival
curve. Extracted text sits in `../raw/10.1371/journal.pone.0156023/`.

## Relevance to project

Observation-model parameters for any HIV incidence estimate the project uses as a
calibration target that came from a cross-sectional recency assay rather than from observed
seroconversions in a cohort. A recency-based incidence estimate is only as good as its MDRI
and FRR, and this paper supplies both with confidence intervals for two widely used assays
and for a sequential algorithm combining them.

The numbers: CDC-modified Bio-Rad at an avidity index cutoff of 30% gave MDRI 234 days
(95% CI 220-249) and FRR 10.2% (7.5-13.5%). Sedia LAg at a normalised optical density
cutoff of 1.5 gave MDRI 120 days (109-132) and FRR 6.0% (3.9-8.7%). Running Bio-Rad first
at 30% and then LAg at 1.7 gave MDRI 136 days (123-148) and FRR 3.3% (1.8-5.6%).

Direct transport to Rakai is not available: the cohort is 99% subtype B, 96% male, 92%
white, 76% men who have sex with men. Uganda's epidemic is subtype A1 and D and
heterosexual, and both MDRI and FRR are known to be subtype- and setting-dependent. Use
these as an order-of-magnitude bound on the width of the recency window and the size of the
misclassification correction, not as parameters.

The paper supplies nothing on STIs, care-seeking, or transmission.

## Key points

Avidity assays measure how tightly HIV-specific antibodies bind viral protein. Low avidity
early after infection is the recency signal; the two assays differ in dissociation agent
(0.1 M diethylamine for Bio-Rad, 0.1 M citrate for LAg) and in the antigen, LAg using a
recombinant gp41 immunodominant region.

Bio-Rad classified more specimens as recent in the first 6 months (134 against 77) but its
avidity ramps up slowly and erratically, so many individuals remain below the 30% cutoff
past a year: 84 of 150 seroconverters had not crossed it by 12 months, against 16 of 150
for LAg at 1.5. That long tail is what produces the 10.2% FRR, and it is why running the
sensitive assay first and the specific assay second recovers a 3.3% FRR at the cost of
halving the recency window.

Nine of 150 seroconverters (6%), all treatment-naive with viral load under 2.6 log10
copies/mL and CD4 above 450 cells/mm3, showed no avidity maturation at all on either assay.
Elite or near-elite controllers are permanently misclassified as recent.

Antiretroviral exposure during follow-up did not change the avidity maturation profile in
this cohort, so treatment status was not a confounder here. The comparison is between 123
naive and 27 treated individuals, a small treated group.

Manufacturer and reference values for comparison: 130 days claimed for LAg at ODn 1.5, and
220 days for Bio-Rad in subtype B. The cohort estimate for Bio-Rad (234 days) sits above the
reference figure.

## Limitations

The population is a Canadian primary-infection cohort, overwhelmingly subtype B, male,
white and men who have sex with men, with 46 injecting drug users and only 11
heterosexuals across the whole cohort of 240.

FRR is defined against specimens over 14 months (cohort) or over 24 months (serobank) post
confirmation, and the serobank specimens have no CD4, viral load or treatment data at all,
so the established-infection group cannot be characterised by disease stage.

MDRI was estimated from 3 to 4 serial specimens per individual over at most 400 days, and
the survival estimate assumes for the longest-observed subject that recency ended at the
last observation.

The multiassay algorithm cutoffs (30% then 1.7) were selected by scanning a grid of cutoffs
on the same data used to estimate the resulting MDRI and FRR, with no separate validation
set.
