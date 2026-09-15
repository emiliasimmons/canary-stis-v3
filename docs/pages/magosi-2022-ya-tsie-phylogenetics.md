---
type: entry
title: Deep-sequence phylogenetics to quantify patterns of HIV transmission in the BCPP/Ya Tsie trial
description: Phylogenetically inferred HIV transmission pairs in 30 Botswana communities, giving age mixing, geographic mixing, and male/female source shares
author: Magosi et al.
published: 2022-03-01
resource: https://doi.org/10.7554/eLife.72657
local: raw/10.7554/elife.72657
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:17
---

Source: [magosi-2022](https://doi.org/10.7554/eLife.72657)

Deep-sequence phylogenetic reconstruction of who infected whom among participants in the
Botswana Combination Prevention Project (Ya Tsie), a 30-community pair-matched trial of
universal test-and-treat run 2013-2018 across roughly 175,664 residents. HIV-1 whole
genomes were deep-sequenced for 5114 consenting adults aged 16-64; 3832 passed genome
completeness criteria, about 14% (3832 / 27,446) of the people estimated to be living with
HIV in trial communities.

## Relevance to project

Supplies empirical mixing structure for the shared risk-structured network, from a
generalized southern African epidemic with a sampling frame comparable to the Rakai
Community Cohort Study.

Age mixing is the usable target. After weighting for differential sampling by gender and
5-year age band, men in inferred male-female transmission pairs were a mean 1.3 years
(SD 10.4) older than women overall: 3.8 (SD 6.9) years in male-to-female events and -1.3
(SD 12.7) in female-to-male events. Unweighted the same gaps are 3.5 (SD 9.6), 4.9 (SD
7.5), and 1.8 (SD 11.6). These are candidate calibration targets for the age-mixing kernel
in the sexual network, and their width (SD roughly 7-13 years around a small mean offset)
bounds how tightly age-assortative the kernel should be. The weighted analysis found
transmission concentrated between similarly aged partners and, notably, little genetic
evidence that older men were a substantial source of infection to younger women, contrary
to the KwaZulu-Natal result the paper contrasts itself with.

Source share by sex is a second target: 55% [95% CI 39.8-69.1] of the 82 male-female
transmission events had a male source, 45% [30.9-60.2] female, and adjusting for sampling
by gender did not change the pattern. A model whose HIV transmissions run
disproportionately male-to-female would sit outside this interval.

Sex work as a driver gets an upper bound here. Among the 286 clustered participants who
were also in the behavioral baseline survey, 10% (30 / 286) reported more than one partner
in the past 12 months, 73% (208 / 286) reported one, 15% (44 / 286) reported none, and of
the 30 with multiple partners, 27 reported exactly one additional partner. Most reported
no transactional sex in the past 12 months, and the authors read the contribution of sex
work to observed transmission as limited. That argues against tuning a large, highly
connected sex-work compartment when calibrating this kind of generalized epidemic, and
gives a comparator against which a Rakai-calibrated network's concurrency can be checked.

Spatial mixing is context rather than a target, since the model has no geography: 69% (57
/ 82) of sampled transmission events were within a single trial community, 21% between
communities in the same region, 10% across regions, and after sampling adjustment an
estimated 24% of transmissions to a trial-community resident originated in a different
trial community. Median driving distance between linked communities was 161 km [IQR
108-420] and drive time 1.86 h [1.41-4.68], shorter than expected under random mixing
(permutation test, p < 0.01).

The trial-arm contamination result does not transfer to this project's SOC/POC contrast.
Post-baseline, transmission flow into intervention communities from control communities
was 30% [12.2-56.7] versus 3% [0.1-27.3] the reverse, against 7% [1.5-25.3] and 5%
[0.9-22.9] at baseline. That asymmetry is evidence that a geographically randomized
prevention trial dilutes its own effect through cross-arm partnerships. This project's arms
are counterfactual whole-population simulations with no mixing between them, so the finding
is a caution about reading trial effect sizes as the model's target, not a structural
requirement.

Nothing here bears on STIs, diagnostics, or care-seeking. The paper offers no STI data.

## Key points

- 236 genetic similarity clusters were found among 3832 sequences, holding 14% (525 / 3832)
  of participants. 97% (230 / 236) of clusters had two or three members; the largest had 12.
  52% (124 / 236) sat entirely inside one community.
- Phyloscanner yielded 153 highly supported directed pairs; 82 were male-female and were
  the basis of every transmission-flow estimate. The 71 same-sex pairs (65 female-female,
  6 male-male) were treated as chains with unsampled intermediates.
- 86% (n = 4410) of the 5114 sequenced participants were on antiretroviral therapy and
  virally suppressed (400 copies/mL or below) at sampling, so 81% (n = 4142) of genomes came
  from proviral DNA.
- Genotyping density was 15% (2730 / 17,815) for women and 11% (1102 / 9631) for men, and
  ranged 2.7% to 36.2% across the 30 communities. Sampling weights carry a lot of the
  adjusted estimates.

## Limitations

Sampling fraction of 14% means most transmission pairs are unobserved, and the
flow estimates rest on a missing-at-random assumption conditional on group membership
(the Carnegie et al. 2014 estimator). The false discovery rate for direct transmission in a
linked male-female pair was calibrated at up to 36% (about 30 of 82 pairs), using
male-male linkage as the error yardstick; the authors argue this is inflated. Dates of
transmission were not inferred, so "post-baseline" means the recipient was first sampled a
year or more after baseline, not that transmission occurred after the intervention started.
Sequences from outside the 30 trial communities were unavailable, so any transmission
originating in the roughly 90% of Botswana's population outside the trial is invisible.
Because most participants were virally suppressed, the sampled clusters may not represent
transmission among people with unsuppressed virus. Men and 16-24 year olds are
underrepresented relative to the 2011 census, which is exactly the group whose age-mixing
behavior the age-gap estimate depends on.

## Methodology

Clustering ran first as a filter: HIV-TRACE and Cluster Picker on whole-genome consensus
sequences, cluster threshold 4.5% nucleotide substitutions per site (chosen from the
distance distribution of epidemiologically linked HPTN 052 subtype-C couples) plus 80%
bootstrap support for Cluster Picker, with the union of the two used downstream. Within
clusters, Phyloscanner did parsimony ancestral host state reconstruction over 42
non-overlapping 200-bp windows spanning 8400 bp, calling a pair linked at a subgraph
patristic distance below 0.035 substitutions per site and requiring a linkage-and-direction
score above 57% of informative windows. Population flows were recovered from sampled pair
counts by inverse sampling probabilities per group, with group denominators built from an
empirical Bayes age-gender HIV prevalence model fitted to 12,570 baseline survey
participants and standardized to the 2011 census. Confidence intervals use Goodman's
simultaneous multinomial method with a continuity correction, treating the 82 pairs as
independent. The estimator is packaged as the R package `bumblebee`.
