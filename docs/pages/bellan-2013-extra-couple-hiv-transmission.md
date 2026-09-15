---
type: entry
title: "Extra-couple HIV transmission in sub-Saharan Africa: a mathematical modelling study of survey data"
description: Mechanistic model decomposing HIV transmission into pre-couple, within-couple, and extra-couple routes using DHS couple serostatus data from 18 sub-Saharan African countries.
author: Bellan et al.
published: 2013-02-05
resource: 10.1016/s0140-6736(12)61960-6
local: raw/10.1016/s0140-6736(12)61960-6/content.md
tags: [hiv, sexual-networks, modeling]
updated: 2026-09-10 09:47
---

Source: [bellan-2013](https://doi.org/10.1016/s0140-6736(12)61960-6)

Bellan et al. built a mechanistic couple-transmission model fitted to DHS data from
27,201 cohabiting couples (men 15--59, women 15--49) in 18 sub-Saharan African countries
(surveys 2003--2011). The model separates the probability that a seropositive individual in
a couple was infected before the partnership formed, by their partner, or through
extra-couple intercourse, using each couple's relationship duration, ages at sexual debut,
country-specific HIV prevalence trends, and age-at-seroconversion survival estimates.
Parameters were estimated by Bayesian MCMC with uninformative priors on transmission
coefficients and an informative log-normal prior on the female-to-male vs. male-to-female
within-couple transmission ratio (centered at 1, SD 0.5).

## Relevance to project

The decomposition of HIV incidence by transmission route bears on how much of the model's
HIV dynamics depend on partnership structure outside the index couple. If 30--65% of male
and 10--47% of female HIV incidence in cohabiting couples comes from extra-couple
intercourse (the 2011 projections), then the STI-driven HIV reduction the POC arm can
achieve depends on whether the sexual network captures these outside contacts. The paper
provides country-specific transmission coefficients (prevalence-standardized hazard rates)
for each route and sex (Table 2), usable as priors or plausibility bounds on the rate of
partnership formation and extra-pair contact in the Starsim network. It also supplies the
empirical observation that fitted extra-couple transmission coefficients are small per unit
prevalence exposure, but dominate population incidence because most person-time is spent in
concordant-negative couples at risk only from outside contacts.

The paper does not address STI coinfection, curable STIs, or any diagnostic intervention.
Its value is in structuring the HIV-transmission side of the network, not the STI side.

## Key points

- Extra-couple transmission accounted for 27--61% of all recorded infections in men and
  21--51% in women across countries. Projected to 2011 prevalence and ART coverage, it
  accounted for 32--65% of incident male infections and 10--47% of incident female
  infections in cohabiting couples.
- Within serodiscordant couples specifically, 50--80% of male and 31--74% of female
  infections were attributed to extra-couple intercourse, with the remainder from
  pre-couple transmission (not from the seropositive partner).
- Within-couple transmission propagates predominantly from men to women, driven by men's
  longer average duration of pre-couple sexual activity and, in some countries, higher
  extra-couple hazard rates.
- Women face a high-risk period before entering a cohabiting partnership: fitted female
  pre-couple transmission coefficients (0.12--0.83 per unit prevalence-year) substantially
  exceed extra-couple coefficients (0.028--0.11), consistent with higher per-act
  susceptibility and age-mixing with older, higher-prevalence men.
- Most cohabiting couples are concordant negative. The large amount of person-time at risk
  only from extra-couple contact is why small extra-couple coefficients still dominate
  population-level incidence.

## Limitations

- Assumes homogeneous mixing by age for pre-couple and extra-couple contacts. Actual
  age-assortative mixing (young women with older men) is absorbed into the fitted
  transmission coefficients rather than modeled explicitly, so the coefficients are not
  directly interpretable as per-act transmission probabilities.
- No STI coinfection, circumcision, condom use, or viral load heterogeneity in the model.
  These factors are folded into the aggregate transmission coefficients.
- ART coverage was negligible for most of the survey period. The 2011 projections assume
  ART eliminates infectiousness entirely; sensitivity analyses relaxing this were conducted
  but are secondary.
- Excludes polygamous couples, those with missing serostatus, and couples with inconsistent
  data (41--80% of couples retained per country). Selection bias was assessed as unlikely
  to be large.
- DHS is cross-sectional, so the model infers infection timing from relationship histories
  and survival curves rather than observing seroconversion directly.

## Methodology

The hazard of infection for each month of an individual's sexual activity is the product of
a gender-route-specific transmission coefficient and the probability that the sexual
contact is with an infectious individual (partner serostatus for within-couple; national
sex-specific infectious HIV prevalence for pre-couple and extra-couple). Infectious
prevalence is HIV prevalence times (1 minus ART coverage). Couple serostatus probabilities
are computed iteratively from sexual debut forward. Country-specific parameters were
estimated by MCMC, with posterior medians and 95% credible intervals reported. Survival
bias (couples where one partner died before sampling) was corrected by inverse-probability
weighting. Validation used simulated data from an independently coded event-driven
simulation. Sensitivity analyses covered individual-level hazard heterogeneity (50-fold
variation at the 2.5th and 97.5th percentiles), inclusion of couples with missing
serostatus, relaxed ART assumptions, and reporting bias in women's sexual debut.
