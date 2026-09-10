---
type: entry
title: "Quantifying rates of HIV-1 flow between risk groups and geographic locations in Kenya: A country-wide phylogenetic study"
description: Country-wide Kenyan pol phylogenetics finding 88.5% within-risk-group clustering and net virus flow from heterosexuals into key populations.
author: Nduva et al.
published: 2022-03-03
resource: 10.1093/ve/veac016
local: raw/10.1093/ve/veac016
tags: [hiv, sexual-networks, phylogenetics]
updated: 2026-09-10 11:18
---

A phylogenetic and phylogeographic analysis of 4058 Kenyan HIV-1 pol sequences sampled
1986-2019, combining 755 newly generated sequences with 3303 previously published ones,
annotated by risk group (heterosexual, men who have sex with men, female sex workers,
people who inject drugs) and by former administrative province. Unlike the two Ugandan
deep-sequence studies, direction here is inferred not from within-host viral diversity but
from a discrete-trait phylogeographic model: risk group and province are treated as states
on a dated tree, and the expected number of state changes along branches (Markov jumps) is
counted. The extracted text and tables sit at `raw/10.1093/ve/veac016`.

## Relevance to project

A weak structural input, and honest to say the fit is loose. It offers a second setting in
which risk groups are strongly assortative, 88.5% of clusters falling within a single risk
group, which is the qualitative shape a risk-structured sexual network should reproduce.
It also offers a second instance of the finding that high-prevalence or high-risk strata
are net recipients rather than net sources, here flow running from heterosexuals into key
populations.

It is not a calibration target, not a prior, and not usable as a bound. The setting is
Kenya rather than Rakai, the risk strata are defined by MSM, sex work and injection drug
use rather than by the agrarian, trading and fishing community structure the model uses,
and the sampling density is 0.3% of the national epidemic. At that density the mixing
percentages describe the clusters that happened to be sampled, and the authors say
directly that the rates of transmission from key populations to heterosexuals are likely
underestimated because clients of sex workers and partners of people who inject drugs are
under-represented. Read it as context and as a directional comparator for the Ugandan
results, and take no number from it into the model.

## Key points

Sampling density is the binding constraint. The 4058 sequences represent an estimated 0.3%
of people with HIV-1 in Kenya, broken down as 10.8% of MSM, 1.7% of people who inject
drugs, 0.6% of female sex workers and 0.3% of heterosexuals. Sequence counts by group:
3401 heterosexual (83.8%), 372 MSM (9.2%), 227 female sex workers (5.6%), 58 people who
inject drugs (1.4%), all 58 of the last from Coast province.

1832 (45%) of sequences fell into 409 supported clusters. 362 (88.5%) of those clusters
were confined to one risk group: 316 heterosexual, 37 MSM, 7 female sex worker, 2 people
who inject drugs. The remaining 47 (11.5%) mixed risk groups, most commonly MSM with
heterosexual (15 clusters) and female sex worker with heterosexual (15). Compared with
heterosexuals, MSM and people who inject drugs were more likely to cluster, adjusted odds
ratios 4.4 (95% CI 3.2-6.0) and 3.4 (1.8-6.5).

Markov jumps between risk groups, from the cluster-wise sub-sampled analysis, totalled 47
supported events with Bayes factor at least 3: heterosexual to female sex worker 16
(34.0%), heterosexual to MSM 15 (31.9%), heterosexual to people who inject drugs 8
(17.0%), people who inject drugs to heterosexual 3 (6.4%), MSM to heterosexual 3 (6.4%),
MSM to female sex worker 2 (4.3%). That is 82.9% of between-group jumps originating from
heterosexuals against 12.8% originating from key populations. These counts are of inferred
events on trees, not of people, and the total of 47 is small.

Geographically, 109 (62.6%) of 174 supported jumps were within Kenya, 42 (24.1%) exports
and 23 (13.2%) imports. West-to-east movement, from higher-prevalence Nyanza and Rift
Valley toward lower-prevalence Nairobi and Coast, made up 76.1% of within-country jumps.
No within-country jump originated from Coast, which received 18.3% of all jumps.

Restricting to sequences sampled 2010-2019 and re-sub-sampling reproduces both directions.
Proportional sub-sampling gave 319 (88%) west-to-east against 43 (12%) east-to-west, and
126 (94%) heterosexual-to-key-population against 3 (2%) the reverse. Uniform sub-sampling,
which equalises sequences per state and so removes the effect of group size, weakens both:
213 (78%) against 61 (22%) for geography, and 126 (72%) against 20 (11%) for risk group.
The gap between the two sub-sampling schemes is the size of the sampling artefact in these
proportions.

The Kenyan direction contradicts Uganda. Ratmann and Bbosa found flow into rather than out
of the high-prevalence Lake Victoria fishing stratum; Nduva finds flow out of the
high-prevalence western provinces toward the lower-prevalence east. The authors note they
had no fisherfolk data and that undisclosed fisherfolk would have been classed as
heterosexual within Nyanza.

## Limitations

Sampling density of 0.3% means most links in any true transmission chain are missing, so
cluster membership understates connectedness and rare subtypes go undetected. Western,
Central, Eastern and North Eastern provinces were dropped from the phylogeographic analysis
as under-represented, so the geographic conclusion covers only Nyanza, Rift Valley, Nairobi
and Coast. All sequences from people who inject drugs come from one province and one time
window ending 2010, so nothing about that group's recent dynamics is observable. Clients of
sex workers and partners of people who inject drugs are under-sampled, which biases
key-population-to-heterosexual flow downward. Sequences are single-consensus pol, so
direction rests on the phylogeographic model rather than on within-host diversity, and many
inferred jumps date to the 1980s and 1990s and describe historical rather than current
flow.

## Methodology

Maximum-likelihood trees in PhyML under GTR+G4+I defined clusters, with approximate
likelihood ratio support at least 0.9 and at least 80% Kenyan sequences required.
Bayesian inference ran in BEAST 1.10.4 under a Skygrid coalescent with an uncorrelated
lognormal relaxed clock. Directional flow came from an asymmetric continuous-time Markov
chain on discrete states with robust counting of Markov jumps, summarised over an
empirical tree distribution.

Sub-sampling is what decides how far the numbers travel. Because a discrete-trait model
over-scores transitions out of over-sampled states, the authors ran the analysis three
ways: cluster-wise on 30 replicate datasets sub-sampled proportional to each state's share
of the epidemic, proportionally on 2010-2019 sequences, and uniformly with equal sequences
per state. The proportional scheme builds the assumed epidemic composition (64%
heterosexual, 15% MSM, 14% female sex worker, 4% people who inject drugs; 35% Nyanza, 17%
Rift Valley, 13% Nairobi, 7% Coast) into the input, so it cannot independently confirm that
composition. The uniform scheme removes it and the asymmetries shrink. Both schemes keep
the same sign, which is the claim that survives.
