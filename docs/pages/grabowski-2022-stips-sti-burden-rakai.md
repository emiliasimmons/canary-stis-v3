---
type: entry
title: The HIV and STI syndemic after mass scale-up of combination HIV interventions in southern Uganda (STIPS)
description: Population-based prevalence of four curable STIs, HSV-2 and HIV in two RCCS communities in 2019, with STI-HIV and STI-STI prevalence risk ratios and the sensitivity of symptom-based diagnosis.
author: Grabowski et al.
published: 2022-11
resource: 10.1016/S2214-109X(22)00424-7
local: raw/10.1016/s2214-109x(22)00424-7
tags: [rakai, sti, hiv, coinfection, diagnostics, sexual-networks]
updated: 2026-09-10 00:12
---

Source: [grabowski-2022](https://doi.org/10.1016/S2214-109X(22)00424-7)

The Sexually Transmitted Infection Prevalence Study (STIPS), a cross-sectional study nested
in round 19 of the Rakai Community Cohort Study, tested 1825 consenting residents aged
18-49 in two RCCS communities between May 27 and Oct 25, 2019: one semi-urban inland
trading centre with surrounding villages (n=919) and one Lake Victoria fishing community
(n=906). Chlamydia and gonorrhoea by Abbott m2000 RealTime CT/NG on penile meatal
(clinician-collected) and vaginal (self-collected) swabs; trichomonas by OSOM rapid antigen
test on the same swabs; syphilis by SD Bioline treponemal antibody with RPR titre on
seropositives, high-titre defined as RPR >=1:8; HSV-2 by Kalon ELISA; HIV by rapid-test
algorithm with viral load on seropositives.

## Relevance to project

This is the primary calibration-target set for STI prevalence at the project's first
calibration site, measured in the same cohort and the same year the model represents, on
etiological tests rather than syndromic diagnosis. Targets, by community, unweighted
prevalence among adults 18-49 (inland first, fishing second):

- Chlamydia 9.6% (95% CI 7.9-11.7) and 9.9% (8.1-12.0)
- Gonorrhoea 5.0% (3.8-6.7) and 8.4% (6.8-10.5)
- Trichomonas 9.4% (7.7-11.5) and 12.2% (10.2-14.5)
- High-titre syphilis 1.4% (0.8-2.4) and 9.4% (7.7-11.5); any positive treponemal serology 7.1% and 24.2%
- HSV-2 43.0% (39.9-46.3) and 64.4% (61.3-67.6)
- Any curable STI (chlamydia, gonorrhoea, trichomonas, or high-titre syphilis) 21.2% (18.7-24.0) and 31.2% (28.4-34.4)
- HIV prevalence 14.0% and 39.8%, with about 90% viral suppression among people living with HIV in both

Inverse-probability-weighted estimates correcting for selective participation differ by
under 1.5 percentage points on every STI, so the unweighted figures are usable directly.

The paper also fixes the contrast the model's two arms are built around. Sensitivity of
clinically indicative self-reported symptoms for etiological diagnosis of chlamydia,
gonorrhoea or trichomonas was at most 50% in women and under 40% in men, and the authors
state most such infections would not have been diagnosed under syndromic management. That
bounds how much infection the SOC arm's symptomatic door can reach, and it is the
justification for the POC arm replacing the panel at that same door rather than adding a
new screening channel. Symptom-level sensitivity and specificity by sex sit in the
appendix, which is not in the extracted text.

For the HIV-STI cofactor, the adjusted prevalence risk ratios (modified Poisson, adjusted
for sex, age and community type) give cross-sectional association strengths for
co-occurrence, not acquisition hazards. With HIV serostatus as the risk factor: gonorrhoea
1.46 (1.18-1.80), trichomonas 1.38 (1.16-1.63), high-titre syphilis 1.47 (1.21-1.78),
HSV-2 3.61 (2.79-5.67), chlamydia 0.82 (0.62-1.09). Any curable STI was 51% more common
among people living with HIV (adjusted PRR 1.51, 1.27-1.78), with no difference by
suppression status. These are comparators for the model's emergent HIV-STI clustering
rather than parameters to fit: the model's clustering arises from shared network position,
and a simulated adjusted PRR near 1.5 for any curable STI would indicate the network
structure reproduces the observed overlap.

STI-STI adjusted PRRs support the shared-network structure directly: chlamydia and
gonorrhoea 2.45-2.67 in either direction, trichomonas with chlamydia 1.71, trichomonas with
high-titre syphilis 2.09-2.21.

The 12 HIV incident cases (0.69 per 100 person-years overall, 1.26 in the fishing community
versus 0.36 inland, over 1746 person-years) are too few to calibrate an incidence target
against, and the incidence rate ratios built on them (HSV-2 IRR 6.14, 1.62-39.92) carry
intervals too wide to constrain anything.

## Key points

478 participants (26%) had at least one of the four curable STIs; 100 of those (21%) had
more than one. Prevalence exceeded UNAIDS 95-95-95 targets being met in the same
population, which is the paper's central claim: HIV epidemic control did not bring STI
control with it.

High-titre syphilis in the fishing community, 9.4%, is roughly four times the national
Ugandan estimate of about 2% (UPHIA 2016-17). Among men living with HIV in the fishing
community, 16.9% (11.9-24.0, n=154) had high-titre infection.

Chlamydia ran opposite to the other STIs: lower among people living with HIV (6.6% versus
10.9% unadjusted) and highest under age 30, declining with age in both sexes. The authors
attribute the inverse association to partial protective immunity from past infection rather
than to lower HIV acquisition risk.

Of 107 pregnant women, 33 (31%) had a curable STI. Pregnancy itself carried no excess after
adjustment (adjusted PRR 0.99, 0.74-1.32), but pregnant women living with HIV did:
13/24 (54.2%) versus 20/83 (24.1%), adjusted PRR 1.87 (1.10-3.17).

Neither viral suppression status nor PrEP history was associated with any curable STI. PrEP
use was rare: 0.5% inland and 7.2% in the fishing community among HIV-negative
participants.

Circumcision cut trichomonas in men (3.3% versus 6.8%, adjusted PRR 0.52, 0.29-0.94) but
was associated with higher chlamydia (12.4% versus 6.4%, adjusted PRR 1.78, 1.13-2.79),
which the paper does not explain.

## Limitations

Two communities, both high-HIV-burden, chosen for representativeness within the RCCS and
enrolment timing. The inland community is a trading centre plus villages, so it is not a
clean agrarian stratum, and the fishing community is the RCCS's highest-risk stratum. A
model calibrated to these two points is not calibrated to the RCCS's 30-community average.

Participation was 1825 of 2583 census-eligible (71%), lower among men, younger people,
recent in-migrants and those of unknown serostatus. Weighting barely moves the estimates.

Age range is 18-49, narrower than the RCCS survey's 15-49, so the youngest RCCS band has no
STI measurement here.

The OSOM trichomonas test is not validated on male penile meatal swabs, which is what was
used, so male trichomonas prevalence carries unquantified test-performance error. No
syphilis treatment history was collected, so positive serology cannot be split into active,
latent, and resolved; high-titre RPR >=1:8 is the paper's stand-in for likely active
infection and is the figure to calibrate against. Self-collected vaginal swabs raise a
contamination possibility the authors cannot rule out.

STIs among incident HIV cases were measured at the first positive test, so they may have
been acquired at or after HIV acquisition. Nothing here identifies direction of
transmission.
