---
type: entry
title: Detection of HIV-1 Transmission Clusters from Dried Blood Spots within a Universal Test-and-Treat Trial in East Africa
description: Phylodynamic analysis of 745 SEARCH trial participants in rural Uganda and Kenya, finding nine transmission clusters arising during the trial, 78% within-community and 67% opposite-sex.
author: Pujol-Hodge et al.
published: 2022-07-29
resource: https://doi.org/10.3390/v14081673
local: raw/10.3390/v14081673
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:16
---

Source: [pujol-hodge-2022](https://doi.org/10.3390/v14081673)

A molecular epidemiology paper working from dried blood spots banked during the SEARCH
universal test-and-treat trial (32 communities in Western Uganda, Eastern Uganda, and
Western Kenya, June 2013 to June 2017). Partial *gag* (n = 549) and *pol* (n = 488)
consensus sequences from 745 HIV-positive participants were used first to pick genetic
clusters, then to date them, so that transmissions occurring inside the trial period could
be separated from ones that predated it.

## Relevance to project

Context and a structural check on how HIV transmission is spatially and demographically
arranged in rural East Africa, near the model's calibration setting. Nothing here is a
calibration target: sequencing density is far too low (3.45% of prevalent infections,
32.5% of incident ones) for the cluster counts to be population rates.

What it does supply is a comparator for network structure. Among nine clusters dated to
the trial period, 7/9 (78%) were within-community and 2/9 (22%) between communities, both
of the between-community pairs in Western Kenya. The paper contrasts this with roughly 40%
inter-community phylogenetic clustering reported for rural Rakai, so the two Ugandan
settings differ by about a factor of two on the same measure. That is a caution for any
future spatial or community-mixing structure in the model, and a reason to take the Rakai
figure as site-specific rather than regional.

Transmission was mostly heterosexual: 6/9 (67%) of trial-period clusters were
opposite-sex. The three same-sex clusters (two female-female, one male-male) are read by
the authors as unsampled intermediate partners, which supports keeping the model's network
heterosexual without treating the phylogenetics as evidence against unsampled bridging.

Occupation predicts clustering in a direction the model's risk structure should reproduce:
participants in "low-risk informal sector" work (farmers, shopkeepers, homemakers;
68.7% of the sequenced sample) had an adjusted odds ratio of 0.16 (95% CI 0.05-0.46) for
membership in a trial-period cluster, meaning transmission concentrated in the formal and
high-risk informal occupations (fishmongers, fishers, bar workers, transport workers;
6.7% of the sample). The magnitude is not usable as a prior because the sequenced sample
is a convenience subset, but the sign and rough scale support risk heterogeneity keyed to
occupation.

The paper carries no STI data and no diagnostic performance figures, so it bears on neither
arm of the SOC/POC comparison.

## Key points

Sequenced participants (n = 745): 55% female, median age 33 (range 17 to 86), 63% prevalent
infections. Only samples with viral load at or above 5000 copies/mL went to sequencing.

Thirteen clusters were picked at the under-1.5% pairwise genetic distance threshold with
over 90% bootstrap support. Nine survived the Bayesian time-calibrated filter as having a
median time to most recent common ancestor after June 2013: eight pairs and one triplet.
Allowing the 95% highest posterior density interval to merely overlap the trial start would
have added four more clusters and expanded one from two members to four.

Subtype A1 dominated (58.8% of *gag*, 56.8% of *pol*), followed by D (19.3%, 19.7%). Subtype
D was about twice as frequent in the two Ugandan regions (~20-25%) as in Western Kenya
(~12%).

Drug resistance in *pol* (n = 488): 14.1% resistant to at least one drug class by WHO
criteria, 25.2% carrying at least one resistance mutation. NNRTI resistance was 13.5%,
NRTI 5.3%, protease inhibitors 0%. K103N was the commonest mutation (n = 37, 7.6%,
95% CI 5.4-10%). Ugandan SEARCH participants ran below the 2016 national estimates for
Uganda (13.1% vs 17.4% any resistance), not significantly.

Two trial-period clusters carried high-level NNRTI resistance with K103N, one of them
consistent with onward transmission of the resistance. Both were in intervention
communities, on efavirenz-based first-line ART.

## Limitations

The sequencing fraction is the binding constraint. 3.45% of prevalent and 32.5% of incident
infections were sequenced, and prevalent-case density varied from 9.15% in Western Uganda
to 0.31% in Eastern Uganda, so cluster membership reflects who was sampled at least as much
as who transmitted.

The intervention arm was sampled yearly and the control arm only at baseline and year three.
Under the plain genetic-distance threshold this produced an apparent 3.34-fold higher odds
(95% CI 1.42-8.79) of clustering for intervention participants, which the authors show to
be a sampling artefact: the effect disappears under the phylodynamic approach. Any
comparison of arms drawn from the distance-threshold results alone would be wrong.

Incident cases had 7.78-fold higher adjusted odds (95% CI 2.48-34.2) of trial-period
cluster membership, expected given they are at most three years into infection and their
partners were densely sampled among prevalent cases.

Consensus sequences from DBS, not deep sequencing, so the direction of transmission within
a pair is not resolved and clusters are putative rather than confirmed pairs.
