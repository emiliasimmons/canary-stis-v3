---
type: entry
title: "Phylogenetic and Demographic Characterization of Directed HIV-1 Transmission Using Deep Sequences from High-Risk and General Population Cohorts/Groups in Uganda"
description: Deep-sequence phylogenetics quantifying HIV-1 transmission flow between general population, fisherfolk and high-risk women in central and southwestern Uganda, 2014-2017.
author: Bbosa et al.
published: 2020-03-18
resource: 10.3390/v12030331
local: raw/10.3390/v12030331
tags: [hiv, rakai, sexual-networks, phylogenetics]
updated: 2026-09-10 11:17
---

Source: [bbosa-2020](https://doi.org/10.3390/v12030331)

A viral deep-sequence phylogenetic study run by the MRC/UVRI and LSHTM Uganda Research Unit
in central and southwestern Uganda, distinct from the Rakai Community Cohort Study though
written by an overlapping group and set up to test the same question. Between August 2014
and August 2017 it enrolled 6185 HIV-1 positive adults through community health facilities
and voluntary counselling and testing campaigns across three general population (GP) sites,
ten Lake Victoria fisherfolk (FF) communities and three sites recruiting women at high risk
of infection and their male clients (WHR). Deep sequencing of the virus in each person
yields many sequence fragments rather than one consensus sequence, and the ordering of
those fragments in a phylogeny carries information about who infected whom, so the analysis
recovers the direction of transmission and not only the fact of linkage.

## Relevance to project

A structural input on how much HIV transmission crosses between risk strata in a Ugandan
setting, usable as a check on the mixing the model's risk-structured sexual network
produces between a high-prevalence fishing-community stratum and the surrounding general
population. The headline usable quantity is the flow ratio, 1.56 (95% CrI 0.68-3.72) for
transmissions from GP sources to FF recipients divided by the reverse, on
phylogenetically supported source-recipient pairs excluding same-sex pairs. Flow ratios
are the only figures here that survive the convenience sampling, because the differential
recruitment probability of each group cancels in the ratio. The one-directional
percentages do not: they describe the sample, and fisherfolk were deliberately
over-recruited relative to their share of the population.

Not a calibration target. This is not RCCS, the sample is a convenience sample recruited
at clinics and testing campaigns rather than a population-based census, and the flow
percentages are conditional on being in that sample. It supplies nothing on STIs, on
care-seeking, or on diagnostic performance, and nothing that constrains the POC arm's
intervention design.

## Key points

Of 6185 HIV-positive enrollees, 2531 (40.9%) were deep-sequenced at depth above 30 over at
least 5000 nucleotides. Sequencing required being antiretroviral-naive with viral load
above 1000 copies/mL. Sampling fractions by group: 1309 of 3200 GP participants (40.9%),
895 of 2185 FF participants (41.0%), 301 of 720 high-risk women (41.8%), and 26 of 80 male
clients (32.5%).

123 transmission networks were reconstructed, 101 of them a single pair, and 105
source-recipient pairs met the threshold of 0.6 on the phyloscanner score for both linkage
and direction.

Counts of those 105 pairs by source and recipient group: 36 (34.3%) GP to GP, 33 (31.4%)
FF to FF, 14 (13.3%) GP to FF, 10 (9.5%) within WHR, 9 (8.6%) FF to GP, 2 (1.9%) FF to
WHR, 1 (1.0%) WHR to GP.

Adjusted transmission flows among study participants, excluding same-sex pairs and
adjusting for the group-specific sequencing fractions above: 45.5% (95% CrI 34.1-57.0)
FF to FF, 22.3% (13.4-32.7) GP to GP, 19.5% (11.4-29.3) GP to FF, 12.7% (6.1-21.3) FF to
GP. Including same-sex pairs the same four quantities read 35.8%, 39.0%, 15.3% and 9.9%,
the difference driven by 20 of the 21 same-sex pairs falling within the GP.

Sources of infection, same population, same adjustment: for an FF infection in the sample,
70.4% (56.2-81.9) from FF and 29.6% (18.1-43.8) from GP; for a GP infection, 80.2%
(66.8-90.0) from GP and 19.8% (10.0-33.2) from FF. The authors read 70.4% as an upper
bound and 80.2% as a lower bound on the corresponding population quantities, given that FF
were over-recruited.

Assortativity within FF and GP was 0.32 (95% CrI 0.10-0.53). An estimated 68.0%
(56.6-78.1) of transmissions in the sample originated from men and 32.0% (21.9-43.4) from
women, after excluding same-sex pairs and adjusting for the sex-specific sequencing
fractions.

Among the 72 male-female pairs used for the age analysis, with age at diagnosis banded
18-24 and 25-59, the largest adjusted flow was men 25-59 to women 25-59 at 29.8%
(19.2-41.7). For women aged 18-24 in the sample, 65.3% (44.1-82.9) of infections came from
men aged 25-59, and for men aged 18-24, 75.8% (46.0-93.7) came from women aged 25-59. No
age combination showed net female-to-male flow, which cuts against the picture of young
women infected by older men then transmitting to men their own age.

## Limitations

Recruitment through clinics and testing campaigns excludes people not yet linked to care.
Sequencing excluded anyone on therapy and anyone with viral load below 1000 copies/mL, so
people who suppressed soon after infection are under-represented. Only 26 male clients of
high-risk women were sequenced, and of 13 supported pairs involving high-risk women just
one was male-female, so the WHR group was dropped from the flow analysis entirely and the
study cannot say what those women contribute as a source. Same-sex pairs are read by the
authors as artefacts of unsampled intermediates rather than as transmission routes.
Unsampled intermediates cannot be excluded in any reconstructed chain, so a
"source-recipient" pair may be separated by one or more unobserved people.

## Methodology

Reads were assembled with shiver, phylogenies reconstructed with phyloscanner 1.8.0 in 250
bp windows stepping 25 bp across the genome, and pairs scored on the proportion of windows
supporting linkage and each direction. The 0.6 threshold on both scores defines the 105
pairs. Flows were then estimated with the phyloflows R package 1.1.0, a Bayesian model
that treats each group as randomly sampled at its own rate and reweights the observed pair
counts by those rates, run for 50,000 MCMC iterations with 5% burn-in.

The reweighting is what decides how far the numbers travel. It corrects for the different
fractions sequenced within each group, and it cannot correct for the fact that the groups
themselves were recruited in proportions unrelated to their population sizes. That is why
the study reports a ratio for its main claim, and why the directional percentages are
labelled as flows among study participants rather than in the population.
