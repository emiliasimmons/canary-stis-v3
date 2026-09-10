---
type: entry
title: "Quantifying HIV transmission flow between high-prevalence hotspots and surrounding communities: a population-based study in Rakai, Uganda"
description: RCCS deep-sequence phylogenetics showing Lake Victoria fishing hotspots are net recipients, not sources, of HIV flow to inland Rakai communities.
author: Ratmann et al.
published: 2020-01-14
resource: 10.1016/s2352-3018(19)30378-9
local: raw/10.1016/s2352-3018(19)30378-9
tags: [hiv, rakai, sexual-networks, phylogenetics]
updated: 2026-09-10 11:17
---

The population-based deep-sequence phylogenetic analysis of HIV transmission flow in the
Rakai Community Cohort Study, covering 36 inland communities and the four fishing
communities within 3 km of the Lake Victoria shoreline, over survey rounds between 10
August 2011 and 30 January 2015. Deep sequencing gives many virus fragments per person
rather than one consensus sequence, and the ordering of each person's fragments in a
phylogeny supports an inference about which of a linked pair infected the other.
Reconstructed pairs were then combined with individual migration histories so that a
source could be placed in the community they lived in before a recent move. The extracted
text and tables sit at `raw/10.1016/s2352-3018(19)30378-9`.

## Relevance to project

The strongest structural input the project has on how much HIV transmission crosses between
communities in the RCCS, which is the first calibration site. It sets the scale of
cross-community mixing the model's sexual network should reproduce: after scaling to the
inland and lakeside populations, an estimated 4.3% (95% CrI 2.3-7.0) of transmissions ran
inland to lakeside and 1.7% (0.6-3.5) lakeside to inland, against 88.7% (84.5-91.9) within
inland and 5.2% (3.8-7.0) within lakeside. Fishing communities in the model should
therefore be a stratum with high internal prevalence and weak outward connectivity, not a
core group seeding the surrounding epidemic.

It also supplies the sex asymmetry in who transmits, 59.7% (53.9-65.3) of transmissions in
RCCS communities originating from men against 61.2% of prevalent infections being in
women, and the finding that recent in-migrants transmit in proportion to their share of
prevalent infections rather than in excess of it.

Not a calibration target for prevalence or incidence, because the numbers here are flow
proportions among reconstructed pairs rather than cohort-wide rates. It says nothing about
STIs, about care-seeking at the symptomatic door, or about diagnostic performance. Its
bearing on the POC arm is indirect: it is evidence about whether geographically targeting
a high-prevalence stratum propagates benefit outward, which is the same shape of question
as whether targeting high-transmission network positions does, without answering the
latter.

## Key points

Denominators for the cohort. 25 882 people aged 15-49 participated across 40 communities.
Inland: 29 116 census-eligible residents, an estimated 16.2% of the 179 982 people aged
15-49 living in the inland area, of whom 19 799 (68.0%) participated. Lakeside: 8529
census-eligible, an estimated 75.7% of the 11 272 people aged 15-49 in the lakeside area,
of whom 6083 (71.3%) participated. HIV prevalence among participants was 13.7% inland
(2703 of 19 799) and 40.1% in fishing communities (2439 of 6083).

Sequencing sampling fractions, which bound everything downstream. 3878 (75.4%) of the 5142
HIV-positive participants reported no ART use and were prepared for sequencing. 2652 met
the read-length and depth criteria, a 68.4% sampling fraction among infected ART-naive
participants and an estimated 45.1% among all census-eligible infected people with
unsuppressed virus. Sequencing rates varied by sex, age, migration status and community,
and the flow model adjusts for that variation.

446 transmission networks were reconstructed and 293 pairs had support for both linkage
and direction in at least 60% of phylogeny evaluations. Raw counts of those 293: 141
(48.1%) fishing to fishing, 94 (32.1%) inland to inland, 23 (7.8%) inland to fishing, 17
(5.8%) external to fishing, 7 (2.4%) fishing to inland, 6 (2.0%) external to inland, 5
unresolved origin.

Adjusted for participation and sequencing differences, flows among RCCS communities were
44.5% (95% CrI 38.6-50.5) fishing to fishing, 35.5% (29.8-41.6) inland to inland, 7.8%
(5.1-11.3) inland to fishing, 3.5% (1.7-6.3) fishing to inland, 5.8% (3.5-8.9) external to
fishing and 2.5% (1.0-5.0) external to inland, giving an adjusted flow ratio of 2.25 (95%
CrI 1.04-5.23) inland-to-fishing over the reverse. These within-community figures are not
interpretable separately, since the cohort sampled 75.7% of the lakeside population and
16.2% of the inland population.

Scaling to the whole inland and lakeside areas gives the predicted flows quoted above and
a predicted flow ratio of 2.50 (95% CrI 1.02-7.30) from inland to lakeside. The abstract
of the corrected version quotes 5.7% (4.4-7.3) within lakeside, 89.2% (86.0-91.8) within
inland, 1.3% (0.6-2.6) lakeside to inland and 3.7% (2.3-5.8) inland to lakeside, slightly
different from the table values used above.

Migration. 6511 (25.2%) of participants were recent in-migrants. Movement was strongly
asymmetric, 536 in-migrants from inland to fishing communities against 27 the other way.
An estimated 22.1% (17.3-27.5) of all transmissions originated from in-migrants, no larger
than their share of prevalent infections. Cross-community transmission split roughly evenly
between two mechanisms: 42.2% (26.1-59.7) from residents with a partner in the other
community type, and 57.8% (40.3-73.9) from in-migrants.

Sex. Inland, the ratio of transmissions from resident men to resident women was 2.26
(1.45-3.62); in fishing communities 1.30 (0.94-1.82). Among in-migrants the ratio was near
unity in both settings, 1.07 (0.44-2.66) inland and 1.11 (0.57-2.16) in fishing
communities.

## Limitations

People on ART were excluded from sequencing. ART coverage was higher inland, so the
excluded group plausibly removes more inland-to-fishing transmissions than the reverse,
which if anything makes the inland-to-lakeside flow ratio conservative. About 30% of
censused people did not participate, mostly because they were away for work or school,
and short-term mobility is not captured at all. The 293 pairs are a small slice of the
transmissions that actually occurred in the period. Scaling the adjusted estimates from
RCCS communities up to the whole inland and lakeside areas rests on the assumption that
whether a community entered the cohort was unrelated to how much transmission crossed its
boundary. The window is 2011-2015, before further treatment scale-up, and the authors do
not claim the pattern transfers to other hotspots.

## Methodology

Sequencing was restricted to self-reported ART-naive participants because deep sequencing
fails below roughly 1000 copies/mL. Phyloscanner reconstructs phylogenies across sliding
windows of the genome and scores each pair; the 60% threshold on linkage and direction was
calibrated against pairs with independent epidemiological evidence of direction, and the
estimated false discovery rate for calling the wrong direction is 15-20%. Flows were
estimated with Bayesian multilevel models in the phyloflows R package 1.1.0, adjusting for
participation and sequence sampling by individual characteristics, then scaled by the
number of men and women in the inland and lakeside areas using WorldPop density estimates
checked against Ugandan Bureau of Statistics figures.

The two-stage structure is what decides how far the numbers travel. The adjusted estimates
describe transmission among RCCS communities and are defensible on the cohort's own
sampling. The predicted estimates extrapolate to the surrounding populations, and it is
only at that stage that the 88.7% inland share appears, because the inland area is roughly
sixteen times the lakeside population but only 16.2% of it was in the cohort.
