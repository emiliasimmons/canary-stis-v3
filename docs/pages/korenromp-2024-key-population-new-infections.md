---
type: entry
title: "New HIV Infections Among Key Populations and Their Partners in 2010 and 2022, by World Region"
description: UNAIDS multi-model estimates of the share of adult new HIV infections falling on sex workers, their clients, MSM, PWID, transgender women, and non-key-population partners, by region and year.
author: Korenromp et al.
published: 2024-01
resource: 10.1097/QAI.0000000000003340
local: ../raw/10.1097/qai.0000000000003340
tags: [hiv, modeling, sexual-networks]
updated: 2026-09-10 00:14
---

UNAIDS's 2023-round reconstruction of how adult (15-49) new HIV infections are distributed
across key populations and their sex partners, for 2010 and 2022, covering 172 countries
with populations above 250,000. It replaces the earlier annual point estimates, which the
authors say could not be compared across rounds because the methods kept changing.
Extracted text and the four main tables are in `../raw/10.1097/qai.0000000000003340`.

Country estimates were pulled from whichever transmission model that country's national
HIV estimate rested on, under a fixed hierarchy: Goals (71 countries, and all of
sub-Saharan Africa apart from South Africa), Thembisa (South Africa), the AIDS Epidemic
Model (13 Asian countries), Optima (9 in eastern Europe and central Asia), and
Estimates and Projections Package fits (15 countries). Forty countries had one or more
groups approximated from first-time diagnoses by mode of transmission, and any remaining
country-group gap was filled with the regional median proportion applied to that country's
Spectrum total. No uncertainty intervals are given.

## Relevance to project

Context and a sanity bound on how much of Rakai-like HIV incidence the model's high-risk
compartments should carry. The East and southern Africa (ESA) row is the relevant one:
in 2022, of adult new infections, 5.2% were among sex workers, 11% among clients of female
sex workers, 3.0% among MSM, 0.74% among PWID, 0.16% among transgender women, 3% among
non-client partners of any of these, and 77% in the remaining population. In 2010 the same
row read 4.8% sex workers, 14.8% clients, and 74% remaining population. A model that puts
sex work and its clients much above roughly a sixth of ESA incidence, or the general
population much below three quarters, is out of line with the UNAIDS synthesis.

The incidence rate ratios give priors on risk heterogeneity for the network. In ESA 2022,
relative to all adults 15-49, the median country IRR was 11 for sex workers, 3.1 for MSM,
6.5 for PWID, and 1.1 for clients of female sex workers, down from 16, 2.5, 5.8, and 2.4
in 2010. On absolute rates per 100 person-years, ESA 2022 was 1.6 for sex workers, 1.0 for
PWID, 0.64 for MSM, 0.40 for clients, against 0.17 for adults overall (2010: 6.2, 2.5,
1.6, 1.7, against 0.53). Clients sit close to the population average, which matters for
how much extra risk the model should assign to a client role beyond partner count.

Not a calibration target. These are model outputs synthesized across models, not
measurements, and there are no confidence intervals; using them as data would be fitting to
another model's fit. They also carry nothing on STIs, so they bear on the HIV side of the
network only.

## Key points

Globally in 2022, 55% of adult new infections were among key populations and their
partners. Global proportions moved from 2010 to 2022 as: sex workers 7.7% to 7.7%, MSM 11%
to 20%, transgender women 0.72% to 1.1%, PWID 6.8% to 8.0%, clients 12% to 10%, non-client
partners 5.3% to 8.2%, remaining population 56% to 45%. Overall adult new infections fell
35% globally over the period (41% in women, 29% in men), so a rising proportion does not
always mean a rising count.

Sub-Saharan Africa moved opposite to the rest of the world for three groups: proportions
fell among sex workers, clients, and non-key-population partners but rose among PWID, while
outside SSA the signs reversed. Annual infection numbers in SSA fell for every key
population, with the decline shallower than the overall 54% drop for PWID, MSM, and
transgender women and steeper for sex workers, clients, and other partners.

The estimates come out lower, with lower IRRs, than UNAIDS published between 2016 and 2022.
The authors attribute this to dropping pre-2010 modes-of-transmission study data in favour
of current transmission-dynamic models.

Cross-checks the authors report against independent evidence: meta-analyses of female sex
worker cohorts in SSA found declining incidence and stable IRRs over 2010-2020, and
prevalence ratios of 1.5-1.85 for clients relative to all men, both consistent with these
results. For MSM in SSA, a meta-regression gave IRRs of 27-150 relative to all men against
the 2.5-7.9 here, which the authors put down partly to their denominator being men and
women combined and partly to incidence studies oversampling higher-risk MSM.

## Limitations

Uncertainty was never quantified; the authors say they presume it is substantial and defer
it to future work. Population size and turnover estimates, which drive infection counts for
a given prevalence, are scarce, and slower assumed turnover for sex workers and PWID would
understate new infections in those groups.

Key populations are treated as disjoint compartments when they overlap in reality (MSM who
inject drugs), and turnover is generally modeled only out to the general population, not
between key populations. Ignoring overlap double-counts; ignoring key-population-to-key-
population turnover deflates prevalent infections in those groups.

Where a model had no transgender-women compartment, MSM infections were split 95% MSM / 5%
transgender women, and population size 94% / 6%, from the median ratio across countries
that did disaggregate. The near-identical 2010-to-2022 trends for MSM and transgender women
are an artifact of that fixed split, and the paper says so.

The authors flag that compartmental models may generate too many infections in long-term
heterosexual partnerships because low-risk individuals are assumed to repartner annually.
They name agent-based models as the way to represent the dynamic network effects their
sources miss, which is the structure this project uses.

Annual infection shares also understate cumulative attributable fractions, since onward
transmission past the immediate partner is not counted.
