---
type: entry
title: "Transmission networks and risk of HIV infection in KwaZulu-Natal, South Africa: a community-wide phylogenetic study"
description: Phylogenetic linkage in a 9812-person household survey showing young women acquire HIV from men on average 8.7 years older, who link back to women aged 25-40.
author: de Oliveira et al.
published: 2017-01
resource: 10.1016/S2352-3018(16)30186-2
local: raw/10.1016/s2352-3018(16)30186-2
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:15
---

A cross-sectional household survey of 9812 randomly selected adults aged 15-49 in two
uMgungundlovu subdistricts (one urban, one rural) of KwaZulu-Natal, South Africa, enrolled
June 2014 to June 2015, with HIV-1 *pol* sequencing on everyone above 1000 copies per mL
and a maximum-likelihood phylogeny used to identify transmission clusters. Extracted text
and tables sit in `raw/10.1016/s2352-3018(16)30186-2`.

## Relevance to project

An age-mixing target and a structural justification for the risk-structured network. The
paper supplies a directly usable calibration target for the age gap between female and
male partners as a function of the woman's age: mean partner age difference 11.5 years for
women 16-20, 7.0 years for women 21-25, 1.5 years for women 26-30, 1.7 years for 31-35,
and -0.5 years for 36-40 (phylogenetically linked pairs, HIV-positive women). The
self-reported comparison in the same survey gives a flatter and smaller gap, roughly 3-4
years across all age bands for HIV-negative women, which bounds how much a model calibrated
to reported partner ages will understate the mixing that actually carries transmission.

Also a target for age- and sex-specific HIV prevalence: weighted 22.3% in women under 25,
59.8% in women 25-40, 50.1% in women 41-49, 7.6% in men under 25, 40.3% in men 25-40, 47.2%
in men 41-49. These are South African, not Rakai, so they serve as a shape check on the
prevalence-by-age-and-sex profile the model produces, not as a fitting target for the
planned Uganda calibration.

It supports the project's third pathway, identifying high-transmission positions in the
network. The men bridging young and older women were largely undiagnosed and untreated: of
79 men linked to women under 40, 62 (78.5%) did not know they were positive, 76 (96.2%)
were not on ART, and 29 (36.7%) carried more than 50000 copies per mL. That is the profile
of a person a symptomatic-care-seeking POC panel could plausibly reach, and it gives a
concrete population for asking what a diagnostic contact is worth beyond the STI it cures.

The paper contributes nothing on STI coinfection, diagnostics, or partner notification, and
it measures no incidence itself.

## Key points

- 3969 of 9812 enrolled tested HIV positive (weighted 36.3%, 95% CI 34.8-37.8). 1847 had
  viral load above 1000 copies per mL; 1589 sequences passed quality control, covering 86.0%
  of those eligible for sequencing.
- 469 sequences (29.5%) fell into 202 clusters; 90 clusters contained at least one man and
  one woman, linking 123 women to 103 men, giving 188 possible male-female pairings.
- Of 60 possible pairings involving the 43 women under 25, 37 (61.7%) of probable male
  partners were 25-40 years old and 18 (30.0%) were under 25; mean age difference 8.7 years
  (95% CI 6.8-10.6, p<0.0001). For the 92 pairings involving women 25-40, the difference
  fell to 1.1 years (95% CI -0.6 to 2.8, p=0.111).
- 16 of 41 (39.0%) probable male partners of a woman under 25 were also linked to a woman
  aged 25-40. Mean age of these bridging men 29.6 years (SD 7.1), linked to a younger woman
  averaging 22.1 years and an older woman averaging 32.6 years.
- Median viral load was higher in clustered men than clustered women (31000 vs 16629 copies
  per mL, p=0.002). 49 of 123 women (39.8%) knew their status versus 27 of 103 men (26.2%,
  p=0.035).
- Reported ART use was 42.3% (weighted) among HIV-positive participants, comparable to
  national coverage among eligible individuals at the time.
- Education, age at sexual debut, lifetime and current partner numbers, and condom use did
  not differ appreciably across the subpopulations, HIV-positive or not, clustered or not.

## Methodology

Multistage random sampling: 221 of 591 enumeration areas, then households by GPS, then one
individual per household, weighted for the design and for non-response. Clusters were
defined as clades with SH-aLRT support above 90% and intra-clade genetic distance at or
below 4.5% (mean genetic diversity 2.8%, mean branch support 99.6%), confirmed with a
bootstrapped PhyML tree and a Bayesian tree that agreed.

Direction of transmission was not inferred from the trees. It was assigned by the
prevalence gradient across age-sex strata, running 59.8% (women 25-40) to 40.3% (men 25-40)
to 22.3% (women under 25), justified by sequencing coverage above 25% in every age-sex
stratum and by the absence of evidence for super-spreaders pushing against the gradient.

## Limitations

- The sequenced set is only those above 1000 copies per mL, so anyone virally suppressed on
  ART is excluded. The picture is skewed toward recent and untreated infection, and the
  authors note this kind of study gets harder as treatment coverage rises.
- The sample is 4% of the census population, so most links in any transmission chain are
  unobserved; a cluster pair need not be a direct transmission pair, only phylogenetically
  close.
- Directionality rests on the prevalence gradient, which the authors call crude. The
  fraction of transmissions running against the gradient is not quantified.
- One district in one province. Two earlier studies (a population cohort in rural
  KwaZulu-Natal and the VOICE trial) found no age-disparity effect on acquisition using
  self-reported partner ages, which the authors attribute to those partners not necessarily
  being the transmitting ones.
- Age bands are wide (under 25, 25-40, 41-49) and men over 50 were not enrolled, so partner
  ages for women over 40 are truncated.
