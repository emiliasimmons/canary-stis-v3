---
type: entry
title: Viral Load and Heterosexual Transmission of HIV-1
description: Rakai discordant-couple cohort giving per-partnership HIV incidence by viral load, with null STI effects after adjustment.
author: Quinn et al.
published: 2000-03-30
resource: https://doi.org/10.1056/nejm200003303421303
local: raw/10.1056/nejm200003303421303
tags: [hiv, rakai, coinfection, partner-notification]
updated: 2026-09-10 00:32
---

Prospective follow-up of 415 HIV-1-serodiscordant couples identified retrospectively inside
the Rakai STD Control for AIDS Prevention community trial (15,127 adults, Rakai district,
Uganda, November 1994 to October 1998; five surveys at 10-month intervals; median follow-up
22.5 months, up to 30). Serum HIV-1 RNA was measured on archived samples from the index
partner at the visit before each 10-month at-risk interval, about 4 to 5 months before
probable seroconversion, and was never available to clinicians during the trial. No
antiretroviral therapy was available in rural Uganda at the time, so viral loads are
untreated natural-history values. Extracted text sits in `raw/10.1056/nejm200003303421303`.

## Relevance to project

Two uses here, one direct and one cautionary.

The direct use is a prior on HIV infectiousness as a function of viral load, which is the
functional form an HIV module needs to place transmission along the untreated course of
infection. Per log10 increment in the index partner's serum HIV-1 RNA, the adjusted rate
ratio for transmission is 2.45 (95% CI 1.85 to 3.26), estimated by Poisson regression
adjusting for age, sex, circumcision, partner number, and STI diagnoses and symptoms. The
categorical version gives transmission rates per 100 person-years in the susceptible
partner of 2.2 below 3500 copies/ml, rising to 23.0 at 50,000 or more copies/ml, with
adjusted rate ratios of 5.80, 6.91 and 11.87 for the 3500-9999, 10,000-49,999 and 50,000+
strata against a <3500 copies/ml reference. Zero transmissions occurred across the 51
couples whose index partner was below 1500 copies/ml. Because the study runs in Rakai and
the population is a community sample rather than a clinic series, these are usable as
calibration-adjacent values for the model's first planned site.

The overall per-partnership incidence, 90 seroconversions in 760 person-years, 11.8 per 100
person-years among initially seronegative partners of a positive spouse, is a level check on
what the model produces for stable serodiscordant partnerships in a high-prevalence setting
(community HIV prevalence 16.1%, subtypes A and D). Male-to-female (12.0) and
female-to-male (11.6) rates were statistically indistinguishable, and remained so after
adjusting for viral load (P=0.76), so a symmetric per-act transmission probability by
direction is defensible for this population once viral load is conditioned on.

The cautionary use bears on the project's central mechanism. This cohort found no
significant STI cofactor effect on HIV transmission or acquisition once viral load was in
the model: adjusted rate ratios spanning 1 for syphilis, gonorrhoea, chlamydia,
trichomoniasis, bacterial vaginosis, genital ulcer disease, discharge and dysuria in both
directions. The unadjusted signals that did reach significance were symptom-based and in
the transmitting partner: genital discharge 20.7 versus 11.1 per 100 person-years, dysuria
14.5 versus 11.5. The chlamydia estimate for transmission, adjusted rate ratio 0.22 (95% CI
0.01 to 0.97), rests on 199 seropositive subjects with ligase-chain-reaction results and
should not be read as protection. The model's STI-cofactor multipliers should therefore not
be sourced from this paper, and if they are set high, this cohort is the comparator that
argues against them.

The circumcision result, zero seroconversions among 50 circumcised HIV-negative male
partners against 40 in 137 uncircumcised (16.7 per 100 person-years, P<0.001), is context
for a Ugandan population rather than a parameter this project needs.

## Key points

- Viral load was the dominant predictor of transmission; nothing else in the multivariate
  model came close.
- Mean HIV-1 RNA among index partners who transmitted was 90,254 copies/ml against 38,029
  among those who did not (P=0.01); on log10 scale 4.48 versus 3.89.
- Men carried higher loads than women (4.11 versus 3.90 log10 copies/ml, P=0.008), and the
  gap was widest among transmitters (4.62 versus 4.30, P=0.015). Equal transmission rates by
  direction therefore coexist with unequal viral loads, meaning per-act female-to-male
  efficiency at matched viral load is not lower here.
- Incidence was highest in the youngest partners (15-19 years, 15.3 per 100 person-years)
  and fell with age; adjusted for viral load the transmission rate ratio was 0.32 for index
  partners aged 30-39 and 0.27 for 40-59 against 15-19.
- Condom use was rare: 89% of seronegative partners reported never using them. Current use
  rose over four years from 4.4% to 7.4% (women) and 9.9% to 16.9% (men).
- 88% of the 415 seropositive partners had detectable RNA; the assay floor was 400 copies/ml
  and undetectable samples were coded 399.

## Limitations

The 10-month survey interval sits between the viral load measurement and the documented
seroconversion, so the load at the moment of transmission is measured with error, and the
same interval structure means STI status was ascertained at the visits bracketing the
at-risk window rather than during it. The authors name this as a plausible reason their STI
associations are diluted, which matters for how much weight the null cofactor result can
carry. Couples were identified retrospectively from a community trial, so the sample avoids
the selection of clinic-recruited discordant-couple studies, but partner identification was
available for only 75% of eligible couples. Transmission within a couple is not attributed:
a seroconversion is assumed to have come from the index partner, and extra-couple
transmission is not excluded. The rates conflate per-act infectivity, coital frequency, and
genital shedding, none of which are separately identified. Sample size limits the strata,
with 51 couples below 1500 copies/ml supporting the zero-transmission claim and 14 index
partners meeting WHO AIDS criteria supporting the 27.3 per 100 person-years AIDS-symptom
rate.

## Methodology

Nested inside a randomised community trial of STI mass treatment, five clusters intervention
and five control, so the cohort experienced an active STI-treatment intervention in half the
communities, and this study does not stratify the transmission analysis by trial arm.
Non-transmitting couples were frequency-matched to transmitting couples on sex and age
(within five years) of both partners and on sample timing, so the viral load comparison is
matched while the incidence rates are not. HIV by two enzyme immunoassays with Western blot
resolution of discordants; syphilis by toluidine red with treponemal confirmation;
gonorrhoea and chlamydia by urine ligase chain reaction in a subgroup only; trichomoniasis
by InPouch culture of self-collected vaginal swabs; bacterial vaginosis by Gram stain.
Seroconversion was assigned to the midpoint of the 10-month interval for person-time.
