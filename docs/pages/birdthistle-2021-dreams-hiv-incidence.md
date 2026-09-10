---
type: entry
title: "Evaluating the impact of DREAMS on HIV incidence among adolescent girls and young women: A population-based cohort study in Kenya and South Africa"
description: Directly observed HIV incidence in two open cohorts (uMkhanyakude, South Africa; Gem, Kenya) showing declines in AGYW that began before DREAMS and did not accelerate under it
author: Birdthistle et al.
published: 2021-10-25
resource: https://doi.org/10.1371/journal.pmed.1003837
local: raw/10.1371/journal.pmed.1003837/
tags: [hiv, sexual-networks, prep]
updated: 2026-09-10 00:21
---

Population-based cohort evaluation of the DREAMS Partnership, a 12-intervention combination HIV prevention package for adolescent girls and young women (AGYW) rolled out from 2016. HIV incidence was measured directly by repeat serology in two demographic surveillance sites: uMkhanyakude (KwaZulu-Natal, South Africa, annual rounds 2006-2018, 26,393 person-years among women 15-24) and Gem (Siaya, western Kenya, six rounds 2010-2019, 10,382 person-years). Extracted content in [raw/10.1371/journal.pmed.1003837/](../raw/10.1371/journal.pmed.1003837/).

## Relevance to project

An HIV incidence comparator from settings outside Rakai, useful mainly as a bound on what a general-population, non-biomedical prevention package delivers over three years, and as a set of age- and sex-specific incidence levels the model's HIV component should be able to reach.

Concrete numbers usable as targets or plausibility bounds. uMkhanyakude, women, per 100 person-years: 15-19 fell 4.54 (2011-2015) to 2.78 (2016-2018), age-adjusted rate ratio 0.62 (95% CI 0.48-0.82); 20-24 fell 7.08 to 5.80, aRR 0.82 (0.65-1.04). Men in the same site: 20-24 fell 2.56 to 1.13 (aRR 0.44, 0.26-0.77); 25-29 fell 4.07 to 2.36 (aRR 0.58, 0.34-0.99). Gem is an order of magnitude lower: women 15-24 at 0.76/100 py (2010-2015) and 0.56/100 py (2016-2019), aRR 0.74 (0.35-1.53). The female-to-male incidence ratio at ages 20-24 in uMkhanyakude is roughly 5 (about 5.8 versus about 1.1 per 100 py in the DREAMS period), a sex asymmetry a risk-structured network model has to reproduce.

The paper carries no STI diagnostics, no etiological versus syndromic comparison, and no STI prevalence, so it does not supply a parameter for either arm. It bears on the project as background on the counterfactual problem: in a setting with an ongoing secular decline driven by treatment scale-up and circumcision, an added prevention package produced no detectable extra effect over three years. Any modelled POC-diagnostic effect on HIV incidence competes against the same background.

## Key points

In uMkhanyakude, annual incidence estimates locate the start of the decline before DREAMS: 15-19 year-old women peaked in 2012 (5.45/100 py) and declined every year through 2017 (2.48/100 py); 20-24 year-olds peaked in 2014 (7.74/100 py) and fell to 5.22/100 py by 2018. Fitting a trend, incidence in the younger group fell about 13% per year over 2013-2015 (aRR 0.87, 0.76-0.99, p = 0.03), with no additional change during 2016-2018 (aRR 1.06, 0.81-1.39). The equivalent test in the older group also found nothing (aRR 1.02, 0.63-1.64).

The authors attribute the pre-existing decline to HIV testing, ART, and voluntary medical male circumcision reaching the men in the partner age range for AGYW, citing modelling and phylogenetic work that preventing transmission from one young man averts infections in up to four young women. They note that community-randomised universal test-and-treat trials themselves only produced 20-30% incidence reductions over 3-4 years.

Where DREAMS did move things, it was upstream of incidence: in Gem, beneficiaries reported fewer lifetime partners and less condomless sex than non-beneficiaries, but the link from HIV testing onward to PrEP and condoms was weak and uptake of both remained low through 2019. In uMkhanyakude, investment stopped in 2018 before PrEP was integrated.

## Limitations

No counterfactual. DREAMS districts were chosen for high HIV burden, not randomised, so nothing separates a DREAMS effect from the secular trend, and universal ART was introduced over the same window.

Power is the binding constraint in Kenya: 13 seroconversions among women 15-24 in the whole 2016-2019 period. The Gem estimates are compatible with rate ratios from 0.35 to 2.14.

Participation was low and variable. In uMkhanyakude, consent among those contacted ranged 37-67% by year and the share of the eligible cohort with a repeat test fell to 57% by 2018. In Gem, an average of 34% of eligible AGYW were contacted, because the survey ran as a home-based testing service rather than a research visit. Requiring two tests to observe a seroconversion likely biases absolute incidence downward, since more mobile people are disproportionately missed; the authors argue the direction of the participation trend is stable enough that time comparisons survive.

## Methodology

Seroconversion dates were multiply imputed (100 imputations in Gem, 250 in uMkhanyakude) as a uniform draw within the interval between last negative and first positive test, rather than assigned to the mid-point, which would cluster events by calendar year when rounds are not annual. Person-time and seroconversions occurring while a participant was resident outside the surveillance area were excluded from the main analysis; a sensitivity analysis retaining them raised Gem's follow-up to 8,456 person-years for women 15-24, lowered absolute incidence, and left the time trends unchanged. Rate ratios come from Poisson regression on calendar period with age adjustment. Comparison periods in the interrupted-time-series style analysis were chosen a posteriori from the observed annual rates, which is a fitted-then-tested structure worth remembering when reading the trend p-values.
