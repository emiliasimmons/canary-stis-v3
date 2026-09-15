---
type: entry
title: "Demographics of sources of HIV-1 transmission in Zambia: a molecular epidemiology analysis in the HPTN 071 PopART study"
description: Deep-sequence phylogenetics on 300 directed transmission pairs, giving the age and sex profile of HIV sources in a generalised Zambian epidemic.
author: Hall et al.
published: 2023-12-13
resource: 10.1016/S2666-5247(23)00220-3
local: raw/10.1016/s2666-5247(23)00220-3
tags: [hiv, sexual-networks, modeling]
updated: 2026-09-10 00:15
---

Source: [hall-2023](https://doi.org/10.1016/S2666-5247(23)00220-3)

Phylogenetic source attribution nested in the HPTN 071 (PopART) universal-test-and-treat
trial in Zambia. Viral genomes from 7124 participants across nine Zambian trial communities
were deep-sequenced; 5612 sequences passing a 50% consensus-coverage threshold went into
phyloscanner, which reconstructed 300 opposite-sex transmission pairs with a determined
direction and a transmission date inside the trial window (Nov 2013 to Dec 2018). Ages are
at the estimated time of transmission, not at sampling, using within-host phylogenetic
diversity to date infection. Counts are reweighted (iterative proportional fitting) so the
recipient sample matches the trial's HIV-positive population on sex, birth cohort,
community, and marital status, with the first three targets taken from the PopART-IBM
simulation and marital status from the 2018 Zambia DHS.

## Relevance to project

A comparator and a structural check on who sustains a generalised southern-African HIV
epidemic, for a model whose HIV component runs on a risk-structured heterosexual network.
Three things it supplies concretely.

An age-sex source profile to compare simulated transmissions against: 59.4% of 300
transmissions male-to-female; male sources median age 32 years (range 20-64), female
sources median 25 years (17-49); men aged 25-39 supplied 43.3% of all transmissions while
being 19.4% of prevalent infections in 2017, and women aged 20-34 supplied 29.0% against
27.3% of prevalence. If the model reproduces incidence but not this source distribution,
the mixing structure is wrong even where the totals are right.

A per-capita transmission ratio the network can be checked against: HIV-positive men
transmitted 2.09-fold (95% CI 2.06-2.29) more per person than HIV-positive women, still
1.79-fold (1.78-1.95) with the not-on-ART population as the denominator, rising to 4.38
(2.8-8.25) at ages 30-34 and 5.87 (2.78-15.8) at 35-39. The 20-24 group is the one where
women's relative rate peaks (2.0, 1.41-2.67) and where the male-to-female ratio's CI covers
1.

A negative result that bears on how the project frames prevention targeting. Source
characteristics did not cluster: high-risk age band, out-of-community residence, and
drug-resistant virus co-occurred at roughly the rates expected under independence, so no
small combined-risk group carries the epidemic. 86.8% (243-274 of 300) of transmissions
were within-community, and only 13.2% (26-57) crossed communities. This weakens the case
that identifying a compact high-transmission position in the network delivers most of the
prevention gain in a generalised epidemic, which is one of the three pathways canary-stis
is set up to separate. It argues for a modest prior on the targeting pathway relative to
direct treatment effects.

What it cannot do here: no STI measurements, no diagnostic performance, nothing on
symptomatic care-seeking. It is Zambia rather than Rakai, so it is not a calibration target
for the Ugandan site, and it says nothing about partner notification.

## Key points

Drug resistance in sources was common but not concentrated: of 288 sources with resistance
data, 18.1% (38-69) carried virus with some resistance to first-line ART, split 7.0% (12-32)
low-level and 11.1% (21-46) high-level. Recipients looked the same (79.7% sensitive), so
resistant lineages were not transmitting disproportionately.

The "renewal cycle" hypothesis (young women infected by much older men who were themselves
infected by women their own age, the basis for DREAMS-style targeting) was not confirmed.
The age gap between male sources and their recipients is real but small, and earlier
estimates ran older partly because they used age at sampling.

Between-community transmission differed by trial arm (chi-square p=0.035): 11.2% in arm A,
20.1% in arm B, 8.5% in control arm C, consistent with the intervention suppressing local
transmission so imports make up a larger share of what remains.

No evidence of a substantial hidden MSM contribution: male-to-male linkage rates
(4.09e-5 of all male pairs) did not exceed female-to-female rates (5.2e-5), and the latter
must be spurious.

## Limitations

Sampling covered 13.0% to 35.2% of people living with HIV in the study communities.
Sequencing required more than 5000 viral copies per mL, so anyone virally suppressed on
effective ART is essentially absent from the source set, and the population cohort sampled
one person per household, which suppresses detection of within-household pairs. Health-care
facility participants dominate (90.8% of sources), carrying whatever bias self-presentation
introduces.

Sources living outside the trial communities entirely could never be sampled, so 13.2% is a
floor on imported transmission, possibly a low one.

Phyloscanner cannot rule out a chain with two or more missing intermediaries, and the trial
context itself (including its control arm) may not generalise to communities with no trial
present.
