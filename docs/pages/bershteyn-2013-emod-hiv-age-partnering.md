---
type: entry
title: "Age-dependent partnering and the HIV transmission chain: a microsimulation analysis"
description: EMOD-HIV v0.7 model description and its transmission-chain analysis, identifying high-concurrency STI-co-infected males 26-29 and females 23-24 as the agents who keep the epidemic young.
author: Bershteyn et al.
published: 2013-08-21
resource: 10.1098/rsif.2013.0613
local: raw/10.1098/rsif.2013.0613
tags: [modeling, hiv, sexual-networks, coinfection]
updated: 2026-09-10 00:27
---

First peer-reviewed description of EMOD-HIV v0.7, an agent-based model of heterosexual
partnership formation and HIV transmission calibrated to South African demography and
prevalence by age, sex and year. The paper does two things: documents the model's structure
(pair formation algorithm, partnership types, concurrency flags, disease progression), and
then dissects the simulated transmission chains to ask which agents keep the epidemic from
ageing out of the population. Extracted text sits in `../raw/10.1098/rsif.2013.0613/`; the
parameter table and model description are in electronic supplements not included here.

## Relevance to project

A structural comparator and a design reference for the network layer, not a source of
calibration targets. Every number below is model output from a South African calibration,
so none of it can serve as data for the Rakai fit.

Three specific uses. First, the STI cofactor result gives a sense of how much of the
transmission burden a co-infection attribute can carry when it is assigned as a static,
non-assorting flag: transmission-enhancing STIs were present in 5.3% of non-transmitters
versus 57% of individuals causing five or more onward transmissions, a tenfold enrichment.
That is the mechanism canary-stis is trying to quantify, arrived at here as an emergent
model property rather than measured.

Second, the paper is the clearest available statement of why STI status must be correlated
with partner choice if it is to shape transmission chains. In EMOD-HIV, STI and concurrency
flags were assigned independently of partnering, so recipient risk factors showed no
variation across transmitter classes. The authors are explicit that risk assortativity does
not emerge from heterogeneous risk in a network model, it has to be written into the pair
formation rule. This bears directly on whether the shared risk-structured network in
canary-stis puts STI and HIV risk on the same axis, since the third pathway the project
wants to separate (identifying high-transmission network positions via STI diagnosis) only
exists if STI positivity marks a network position rather than an independent draw.

Third, age targeting. The model's most efficient groups for a transmission-blocking
intervention were males aged 26-29 and females aged 23-24 at initiation of a non-ageing
round trip, with the per-infectious-person-year peak at ages 23-28 (men) and 18-22 (women),
stable across the 1985-1995, 1995-2005 and 2005-2015 decades. Useful as a hypothesis about
where POC diagnostic targeting would pay off, and as a reference point if the project ever
compares its own targeting result to a prior model.

## Key points

Lifetime onward transmissions per infected agent are roughly exponentially distributed,
zero to more than a dozen, with about twice as many non-transmitters as single-transmitters
and so on down the tail.

Concurrency dominates. Agents with no concurrency flag never transmitted onward in 62% of
cases and transmitted twice or more in under 10%; agents with all three flags (marital,
informal, transitory) had zero onward transmissions in 23% of cases and two or more in 49%.
Among five-plus transmitters, 11% carried all three flags against 1.6% of non-transmitters.

High transmitters skew male: 58% of five-plus transmitters versus 41% of non-transmitters.

Circumcision, modelled at 60% protection against acquisition only, showed almost no
variation across transmitter classes, since it does not touch the infectivity of an
already-infected man.

A transmission is "non-ageing" when the recipient is younger at infection than the
transmitter was at his or her own infection, which requires a negative age gap larger than
the time since the transmitter was infected. One-third of all transmissions in a simulation
are non-ageing; 15% of female-to-male transmissions versus 5% of male-to-female. Fewer than
30% of same-sex round trips (male-female-male or female-male-female) are non-ageing, yet
that is enough to sustain the epidemic, because each non-ageing event seeds a cascade of
ageing transmissions before another rescues the chain.

The age dependence is a tug-of-war: younger agents are recruited into transitory
partnerships, so they turn partners over fast and transmit soon after infection, while older
agents form the larger age gaps (about 5 years in marital partnerships). The proportion of
non-ageing forward transmissions peaks at intermediate ages, 26 in men and 21 in women.

Age-mixing is imposed through data-driven matrices of partnership age distributions
(MOPADs), one per partnership type. Age is the only assigned property with assortative
pairing.

## Limitations

Baseline scenario with no ART and no prevention scale-up; the decade-stability claim assumes
no large programme rollout. Results are 20 stochastic replicates of a South African
calibration, not Rakai.

Per-contact transmission rate is a function of disease stage only, with no correlation to
survival time. The authors note that adding the viral-load correlation would likely reduce
the importance of the young transmitters their analysis highlights, which weakens the age
targeting conclusion in the direction of older ages.

STI status is a static binary flag with no natural history, no treatment, no clearance, and
no correlation with partner choice, so the 57% figure describes an attribute the model gave
its high transmitters rather than a measured cofactor. There is no pathogen-specific
structure and no diagnostic pathway at all.

The NART-per-person-year curves spike at ages below about 16 because infected person-years
in the denominator approach zero there; those spikes are noise.
