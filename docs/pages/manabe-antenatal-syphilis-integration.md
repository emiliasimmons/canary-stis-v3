---
type: entry
title: "Integration of antenatal syphilis screening in an urban HIV clinic: a feasibility study"
description: Kampala HIV antenatal cohort, 570 women, 5.1% RPR-positive but 1.8% treponemal-confirmed, and 34% of partners returned for treatment.
author: Manabe et al.
published: 2015-01-21
resource: https://doi.org/10.1186/s12879-014-0739-1
local: raw/10.1186/s12879-014-0739-1
tags: [sti, hiv, diagnostics, partner-notification]
updated: 2026-09-10 00:11
---

A single-site descriptive cohort at the Infectious Diseases Institute in Kampala, Uganda,
testing whether syphilis screening can be bolted onto an antenatal clinic already embedded
in an adult HIV clinic. Consecutive HIV-positive pregnant women were enrolled October 2010
to December 2011, screened with lab-based rapid plasma reagin (RPR), treated on site with
2.4 MU benzathine penicillin if positive, and given an anonymized slip to pass to their
partner. Treponemal antibody testing (Determine Syphilis TP) was run retrospectively on
batched samples. Extracted content sits in `raw/10.1186/s12879-014-0739-1`.

## Relevance to project

Two numbers here are usable, and both are about the diagnostic and the partner pathway
rather than about transmission.

The screen-confirm discrepancy bounds what a non-treponemal screening test means in an
HIV-positive antenatal population: 29/570 (5.1%) RPR-positive, of which only 10 (34%)
confirmed treponemal, giving a confirmed active-syphilis prevalence of 1.8% (10/570) among
HIV-positive pregnant women aged mostly 25-32 in urban Kampala. That is a comparator for
the specificity penalty the SOC arm's syphilis pathway carries, and a caution on reading
any RPR-based prevalence figure as a calibration target without the confirmatory
denominator. The authors attribute the excess to biological false positives from pregnancy
and HIV plus uncontrolled lab conditions, so the 34% confirmation rate is a floor specific
to this setting, not a transportable test characteristic.

The partner cascade gives an empirical ceiling on partner notification under intensive
counseling: of 29 index cases, 17 (58%) agreed to notify a partner, and 10 (34.5% of the
29, 58.8% of those who agreed) partners returned for testing and treatment. The paper cites
comparators from the same region: under 1% of partners returning in a Ugandan PMTCT
implementation study, and 9.9% of invited men testing in a Uganda/Zambia evaluation. Since
canary-stis implements no partner-notification pathway, this is support for that choice
rather than a parameter: even a well-resourced clinic with dedicated counselors converted
about a third of index cases into a treated partner.

Not a source for HIV incidence, STI transmission parameters, or POC test performance. Its
point-of-care discussion is a literature summary the authors did not test.

## Key points

- 584 of 606 women approached consented (95.7%); 570 unique participants, median age 29
  (IQR 25-32), median CD4 402 cells/uL (IQR 272-575), 54.2% on ART.
- All 29 RPR-positive women were asymptomatic, all were contacted and treated, no adverse
  reactions.
- RPR-positive women were younger (median 25, IQR 22-27, versus 29; RR 1.15, 95% CI
  1.065-1.248, p < 0.001). Age was the only variable differing between groups.
- Adverse birth outcomes: 61/570 (12.1%) overall. Among RPR-positives contacted postpartum
  (28/29), 3 spontaneous abortions (10.7%) and no stillbirths or neonatal deaths. Among
  RPR-negatives contacted (505/541), 17 premature (3.4%), 23 spontaneous abortions (4.6%),
  11 stillbirths (2.2%), 10 deaths within 7 days (2.0%).
- 73.3% (418/570) presented in the first or second trimester; no later-trimester retest
  strategy was in place, which the authors flag as a gap given reinfection risk.
- Screening required no additional staff, which is the feasibility claim the paper rests on.

## Limitations

Descriptive, single-site, no control clinic, and no comparison against a vertical screening
program, so the feasibility conclusion is a demonstration rather than an effect estimate.
Twenty-nine positives is too few to detect an effect of treatment on birth outcomes, and the
authors say so. Quantitative RPR titers were not affordable, so active versus treated
infection could not be separated, and treponemal confirmation was retrospective and did not
affect who was treated. Previous adverse birth outcomes were participant recall. The
population is HIV-positive pregnant women in an urban referral clinic, roughly the
best-case setting for retention in sub-Saharan Africa, so both the 95.7% consent and the
34.5% partner return are upper bounds on what a peripheral facility would achieve.
