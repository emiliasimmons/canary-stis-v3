---
type: entry
title: "HIV seroprevalence, incidence, and viral suppression among Ugandan males with bar or sex worker partners"
description: RCCS 2013-2020 population-based estimates of HIV prevalence, incidence, and viremia in men reporting female bar or sex worker partners, versus men who do not.
author: Feng et al.
published: 2025-03-23
resource: https://doi.org/10.1101/2025.03.22.25324410
local: raw/10.1101/2025.03.22.25324410
tags: [rakai, hiv, sexual-networks, prep]
updated: 2026-09-10 00:30
---

A medRxiv preprint (not peer reviewed) reporting a secondary analysis of the Rakai Community Cohort Study: 17,438 men aged 15-49 across 4 Lake Victoria fishing and 37 inland communities, contributing 35,273 visits over survey rounds 16-19 (July 2013 to November 2020). The exposure is self-reported sex in the past year with a partner whose primary or secondary occupation was sex work or bar work (FBSW, female bar or sex worker; the two were pooled). Extracted content sits in `raw/10.1101/2025.03.22.25324410`.

## Relevance to project

A calibration target and a risk-structure prior for the client side of the sex-work compartment in a Rakai-parameterised model. The concrete numbers a model would have to reproduce:

- Population share: 13.9% of men reported an FBSW partner at one or more visits (2,420/17,438), 37.1% at baseline in fishing communities versus 6.2% inland. This sets how large a "client" group the network needs.
- HIV incidence: 1.93/100 person-years (43 events, 2,233 PY) in men with FBSW partners versus 0.44/100 (111 events, 25,163 PY) in men without, age-adjusted IRR 4.46 (95% CI 3.09-6.32), over 27,396 total person-years. This is a direct incidence target by risk stratum, and the ratio is a bound on how much incidence heterogeneity the network must generate among men.
- HIV prevalence: 32.6% versus 10.3% at baseline (age-adjusted PR 2.46, 95% CI 2.28-2.65); 21.0% versus 7.5% inland, 38.6% versus 23.0% in fishing communities.
- Partnership structure: 5,505 of 51,437 reported partnerships (10.7%) involved FBSWs, median duration 0 days (IQR 0-90) against 365 days (IQR 90-2,186) for non-FBSW partnerships, and 77.7% were not ongoing at survey. Condom use "always" in 48.5% of FBSW partnerships versus 20.2% otherwise. These are calibration handles for partnership duration and act-level protection in the high-risk layer.
- Bridging: 2,692 of 3,479 person visits with an FBSW partner (77.0%) also involved a non-FBSW partner, so clients are not a closed compartment. This supports the network's bridge from the sex-work layer into the general population.
- PrEP coverage, round 19 only: among 6,910 HIV-seronegative men, 10.6% of those with FBSW partners had ever used PrEP and 5.7% were currently using, versus 2.0% and 1.0% among men without. A low-coverage baseline for the prevention arm, and a comparator for any PrEP-targeting scenario.

Two figures bear on the STI side without settling it. Genital ulcer disease in the past year was reported by 12.4% of men with FBSW partners versus 7.1% of sexually active men without, and among men with FBSW partners, HIV prevalence was 46.7% with GUD versus 30.6% without. That is a syndromic self-report, confounded by shared exposure, so it is context for the ulcerative-STI cofactor, not an estimate of it. The paper measures no laboratory STI outcome and says nothing about diagnostics or syndromic management, so it cannot inform the POC/SOC contrast directly.

## Key points

- HIV incidence declined in both groups from 2013-2020 (0.49 to 0.34/100 PY without FBSW partners, 2.04 to 1.75/100 with) while the disparity widened: age-adjusted IRR rose from 4.06 in rounds 16-17 to 6.19 in rounds 18-19.
- The incidence disparity was stronger inland (IRR 4.73) than in fishing communities (IRR 1.95, P interaction = 0.030), consistent with saturation in a ~40% prevalence setting.
- Viral suppression among men with HIV was near-identical by exposure (70.2% versus 73.4% of seropositive visits, PR 0.95, 95% CI 0.91-1.00). The excess population prevalence of viremia (PR 1.61, 95% CI 1.41-1.84) comes from the higher background seroprevalence, not from worse treatment.
- Dose-response: among visits reporting exactly four past-year partners (n = 2,601), HIV prevalence rose with the number who were FBSWs, reaching 37.3% when all four were.
- Bar-worker and sex-worker partnerships differ. 86.3% of FSW partnerships were client/sex-worker relationships; FBW partnerships were most often described as girlfriends (42.4%), longer, and more often ongoing. A model that treats sex work as a single short-duration partnership type loses this.
- Awareness is not the binding constraint: 95.3% of men with HIV and FBSW partners knew their status and 73.9% of seronegative ones had heard of PrEP, against ~6% current PrEP use.

## Limitations

- Exposure is self-reported, capped at the four most recent partners, and subject to social-desirability bias under sex-work stigma. Underreporting biases the client group small and its incidence rate ratio in an unclear direction.
- 34.8% of eligible men were away for work or school at survey time and were excluded. Mobile men are plausibly higher-risk, so both arms of the comparison may be attenuated.
- Only 63.6% of seronegative men at first visit had a follow-up visit. Loss to follow-up was similar by exposure (32.9% versus 33.4%) and censoring weights did not move the IRR (4.40 versus 4.46).
- FBW and FSW partners are pooled in the headline estimates despite differing partnership profiles; the split appears only in supplementary tables.
- Data end in 2020, before recent PrEP scale-up, so the PrEP coverage figures are a floor for the present day.

## Methodology

Exposure was time-varying for the incidence analysis: a man contributed exposed person-time for an interval if he reported an FBSW partner at the start or end of that interval, with seroconversion placed at the interval midpoint and one missed visit allowed. Modified Poisson regression with robust standard errors gave prevalence ratios; GEE with an exchangeable correlation structure handled repeated measures for viremia. Adjustment sets were nested (age; then demographics; then sexual behaviour), and the behaviour-adjusted estimates are the most conservative, since partner number and alcohol use before sex are plausibly on the causal path from FBSW contact to infection rather than confounders of it. Serostatus came from a three-test rapid algorithm confirmed by enzyme immunoassay; suppression was defined at <200 copies/mL.
