---
type: entry
title: "Estimating the contribution of key populations towards HIV transmission in South Africa"
description: Deterministic HIV model ("Key-Pop") splitting South African adults into low-risk, female sex workers, their clients and MSM, giving transmission population attributable fractions by partnership type and the impact of ART scale-up by group.
author: Stone et al.
published: 2021-02
resource: 10.1002/jia2.25650
local: ../raw/10.1002/jia2.25650
tags: [hiv, modeling, sexual-networks]
updated: 2026-09-10 00:17
---

A compartmental HIV transmission model of South African adults 15-49, dividing the
population into low-risk males and females, female sex workers (FSW), clients of FSW, and
men who have sex with men (MSM) split at age 30. It asks how much of ongoing HIV
transmission runs through each partnership type, and what scaling ART within each group
would achieve. Extracted text and tables are in `../raw/10.1002/jia2.25650`.

The model runs three partnership types (main, casual, commercial), tracks vaginal and anal
acts separately, and layers condom use, male circumcision, and ART with loss to care on top.
Sexual mixing is balanced by letting male reported behaviour determine female behaviour.
PrEP and people who inject drugs are both excluded, on the grounds of low coverage (<5% of
HIV-negative FSW/MSM) and small population share (0.2% of adults).

## Relevance to project

A comparator for the pathway-decomposition question, and a source of risk-group structure
and behavioural priors.

The comparator use is the tPAF machinery. Stone et al. define the transmission population
attributable fraction as the share of new infections over a window that disappears when the
transmission risk of one partnership type is set to zero for that whole window, which is the
same counterfactual shape as asking how much of a POC diagnostic's HIV impact comes from
removing transmission on particular network positions. It is a partnership-type
counterfactual, not an intervention, so it gives an upper envelope rather than an achievable
impact, and the fractions overlap and sum above 100%.

Their headline numbers for 2010-2019, South Africa, adults 15-49: sex between low-risk males
and females 59.7% (95% CrI 47.6-68.5), non-commercial sex of clients 41.9% (35.1-53.2),
commercial sex between FSW and clients 6.9% (4.5-9.3), sex between men 5.3% (2.3-14.1), and
sex between MSM and their female partners 3.7% (1.6-9.8). Over the longer 1990-2019 window
commercial sex contributed 21.6% (14.5-30.5), so the commercial-sex share fell threefold as
condom use rose and prevalence spread into the general population. That decline over time is
the transferable point for this project: a network position's contribution is a function of
epidemic phase, so a decomposition run on a mature Rakai epidemic should not be expected to
reproduce a 1990s split.

The efficiency-versus-impact contrast is the second comparator. Scaling ART to 81% coverage
over 2020-2030 among low-risk individuals averts 20.6% (14.7-27.5) of new infections at 13.4
(10.8-16.6) infections averted per 100 person-years of ART; among clients it averts 18.2%
(14.0-24.4) at 30.4 (24.0-34.3) per 100 py, 2.3 (1.5-2.9) times more efficient. Near-equal
impact at more than double the efficiency is the shape this project expects from targeting a
POC panel at high-transmission positions rather than broadening it, and these ratios give
a rough scale for what a targeting gain looks like.

Behavioural parameter ranges in Table 1 are usable as priors on a risk-structured network,
though they are South African and would need Rakai-specific replacement for the calibration
site. Commercial partners per year: 100-1000 for FSW, 2.3-72.8 for clients. Main
heterosexual partners per year among those with partners: 1.1-2.8 low-risk males, 1.0-1.3
low-risk females. Casual heterosexual partners per year: 1.7-2.9 for both low-risk groups,
1.0-18.0 for FSW, 1.1-15.1 for clients. Vaginal acts with main partners: 42.0-70.8 per year
for low-risk adults. The indirectly derived client population size, 22% (18-29%) of adult
men, is the parameter with the most leverage and the least data behind it.

What it cannot do here: it carries no STI compartments at all, so it supplies nothing on the
STI cofactor effect, on syndromic versus etiological management, or on any diagnostic. It is
also deterministic and compartmental, so the network positions it can represent are the six
risk groups it defines, not the individual-level contact structure this project's
agent-based model resolves.

## Key points

Clients of FSW carry the epidemic more through their non-commercial partnerships than
through the commercial sex that defines them: 41.9% versus 6.9% over 2010-2019. The model
attributes this to a large client population with high HIV prevalence (13-22%), frequent
casual sex, and ART coverage assumed at 0.7-1 times that of adult men.

Historical intervention counterfactuals: without ART from 2003, 3.3 million (2.9-3.9)
more infections through 2019, and 2019 prevalence 39.6% higher. Without the rise in condom
use from the early 1980s, 4.7 million (3.9-5.9) more infections and prevalence 47.8% higher.
Without circumcision scale-up from 2002, 0.2 million (0.2-0.4) more and prevalence 3.9%
higher.

Calibration used approximate Bayesian computation with sequential Monte Carlo, starting from
10,000 Latin-hypercube prior draws and retaining 10,000 fits, with targets on population
size, ART coverage, adult HIV incidence, and HIV prevalence among all males, all females,
FSW, and MSM. Two client prevalence estimates, one FSW incidence estimate, and three MSM
incidence estimates were held out for cross-validation.

## Limitations

The client population size has no direct estimate. It was inferred by balancing commercial
acts reported by FSW against those reported by clients, which leans entirely on the national
FSW size estimate (0.69-0.96% of adult women in 2013, from a Wisdom-of-the-Crowds study).
The resulting 22% of adult men is an order of magnitude above what South African household
surveys report (<2%), which the authors attribute to social-desirability bias, citing
polling-booth surveys from Benin and Nigeria (~20%) and an ACASI household survey in
Diepsloot (one-fifth in the last year) in support.

Because household surveys could not separate clients from non-clients, all-male survey data
parameterized low-risk male behaviour, which likely inflates low-risk sexual activity and so
the 59.7% low-risk tPAF.

Client data came from two small unpublished surveys (Port Elizabeth 2017/18, Klerksdorp
2018). Most key-population ART coverage is self-reported and probably upward-biased: three
of four studies with viral suppression data showed a gap, with clients at 32.3-37.3%
self-reported ART against 26.7-29.0% suppressed.

No stratification by violence or stigma, no PrEP, no PWID, and no costing of the ART
scale-up scenarios, so the efficiency figures are infections per person-year, not per dollar.
