---
type: entry
title: Inferring HIV-1 transmission networks and sources of epidemic spread in Africa with deep-sequence phylogenetic analysis
description: Deep-sequence phylogenetics on 2652 Rakai RCCS participants, reconstructing 446 partial transmission networks and inferring transmission direction at a 16.3% error rate
author: Ratmann et al.
published: 2019-03-22
resource: https://doi.org/10.1038/s41467-019-09139-4
local: raw/10.1038/s41467-019-09139-4
tags: [hiv, rakai, sexual-networks]
updated: 2026-09-10 00:31
---

The methods paper establishing that HIV-1 deep-sequence phylogenetics (phyloscanner) can
be scaled from suspected transmission pairs to a whole population-based sample, and that
the direction of transmission can be recovered without assuming anything about the
epidemic. The data are the Rakai Community Cohort Study, 40 communities surveyed August
2011 to January 2015, so the population is the same one canary-stis will calibrate to.
Extracted content in `raw/10.1038/s41467-019-09139-4`.

## Relevance to project

Two uses, both about the sexual network rather than about STIs.

First, a sampling-fraction bound on any claim built from Rakai phylogenetics. Of 37,645
eligible people aged 15-49, 25,882 participated, 5142 were HIV-positive, 3878 (75.4%)
reported no ART, and 2652 passed sequence-quality thresholds. That is 68.4% of untreated
infected participants, 65.6% of participants estimated to have unsuppressed virus, and
45.1% of all eligible infected people with unsuppressed virus once non-participants are
imputed. Combined with the prior estimate that ~30% of infections came from outside the
cohort, the transmitter of a sequenced person is expected to be in the data in roughly 3
of 10 cases (0.451 x 0.7). Any transmission-source distribution read off this cohort is a
sample of about a third of the relevant links, and the model should not be tuned to match
its absolute counts.

Second, a structural check on partnership reporting. Among 331 concordant-positive couples
who self-identified as sexual partners, only about 70% were expected to be transmission
pairs on prior couple analyses, and the phylogenetic distance distribution was indeed
bimodal, splitting couples into a phylogenetically close group and a distant group. In the
population sample, 176/376 (46.8%) of highly supported male-female linkages were between
enrolled couples, meaning over half of inferred transmission linkages sit outside reported
cohabiting partnerships. That supports a network with substantial partnership formation
outside the reported main-partner structure, which is the same heterogeneity the model
needs for its risk strata.

The paper supplies no STI data, no incidence rate, and no intervention effect, so it is
not a calibration target and not a prior on any transmission parameter. It is a bound on
how far Rakai phylogenetic source attributions can be pushed, and a design reference if
the project ever wants to compare simulated who-infected-whom flows against phylogenetic
ones.

## Key points

- 3,515,226 possible pairs were screened. Subgraph distance alone ruled out direct
  transmission for 99.96% of them, leaving 1426; adding subgraph topology left 1191
  potential pairs forming 446 transmission networks over 1334 individuals.
- Networks are small: 261/446 (58.5%) are just two people, 36 have more than five.
- Of 537 highly supported linkages, 376 were male-female and the source could be inferred
  in 293/376 (77.9%).
- Direction error was validated against two independent clinical signals: seroconversion
  histories (false discovery rate 12.9% [5.1-28.9%], 4 inconsistent of 31 resolvable) and
  CD4 discrepancy (20.8% [9.2-40.5%]). Combined, 16.3% [8.8-28.3%]. Error was much lower
  in reported couples (7.4%) than in other linked pairs (25%).
- Deep sequencing cannot prove transmission between two named people. 161/537 (30%) of
  highly supported linkages were same-sex, including 80 female-female, and two
  female-female pairs had heavily intermingled near-identical subgraphs, the pattern
  previously claimed to exclude unsampled intermediates. The authors draw the explicit
  conclusion that the method must not be used in criminal prosecutions.
- The same-sex linkage proportion was near-identical for men (81, 15.1%) and women (80,
  14.9%), which the authors read as no evidence of an extensive MSM sub-epidemic in rural
  Rakai, with the caveat of likely undersampling of a stigmatised group.

## Methodology

Serum from seropositive participants not reporting ART, deep-sequenced on Illumina, reads
assembled with shiver, phylogenies reconstructed in 250 bp sliding genomic windows
(coverage was mostly the gag gene). For each pair, phyloscanner classifies the topological
relation of their read subgraphs per window (ancestral either way, intermingled, sibling,
disconnected) and the shortest patristic distance between subgraphs. Distance thresholds
came from the couples analysis: below 0.025 substitutions per site transmission is likely,
above 0.05 it is ruled out, in between is a grey zone. Support is the proportion of
windows favouring linkage or a direction, with an adjustment for window overlap, and
classification uses a threshold of 0.6 chosen so the posterior probability that the true
proportion exceeds 50% is at least 80%. Most likely chains come from Edmonds's algorithm
over the network's directed edge weights.

## Limitations

- Sequence sampling is incomplete (45.1% of eligible unsuppressed infections), so
  unsampled intermediates are common and inferred pairs are not necessarily direct.
- Restricted to people not reporting ART, since suppressed virus is hard to sequence. As
  treatment coverage rose after 2015, this design is progressively harder to repeat, and
  the sequenced set is systematically the untreated fraction.
- Reads covered only ~250 bp, primarily gag, rather than the whole genome, which the
  authors expect understates achievable accuracy.
- Women and people aged 35+ are under-represented among the sequenced relative to infected
  participants; fishing-site residents are over-represented.
- Direction inference degrades when virus is more closely related within hosts, so the
  method is expected to work less well in rapidly spreading high-risk networks.
