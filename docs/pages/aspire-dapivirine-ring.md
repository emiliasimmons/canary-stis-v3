---
type: entry
title: Use of a Vaginal Ring Containing Dapivirine for HIV-1 Prevention in Women (MTN-020-ASPIRE)
description: Phase 3 trial of the monthly dapivirine ring in African women, giving a 27-37% HIV-1 efficacy estimate, placebo-arm HIV incidence by age, and baseline STI prevalence in a trial cohort.
author: Baeten et al.
published: 2016-12-01
resource: https://doi.org/10.1056/NEJMoa1506110
local: raw/10.1056/nejmoa1506110
tags: [prep, hiv, sti]
updated: 2026-09-10 00:25
---

Source: [baeten-2016](https://doi.org/10.1056/NEJMoa1506110)

Phase 3, randomized, double-blind, placebo-controlled trial of a monthly silicone vaginal ring containing 25 mg dapivirine, a non-nucleoside reverse-transcriptase inhibitor, in 2629 HIV-1-seronegative women aged 18-45 at 15 sites in Malawi, South Africa, Uganda and Zimbabwe, enrolled August 2012 to June 2015.

## Relevance to project

Three uses here, in descending order of directness.

A prior on topical/long-acting PrEP efficacy for a prevention arm: 27% reduction in HIV-1 incidence (95% CI 1 to 46) across all 15 sites, 37% (95% CI 12 to 56) after excluding the two low-adherence sites. Both are intention-to-treat effectiveness under trial-level adherence, not per-protocol biological efficacy, so they bound what a ring-delivered product does in practice rather than what the drug does in an adherent user. The age split is the operative number for any targeting question: 56% (95% CI 31 to 71) above age 21, -27% (95% CI -133 to 31) at ages 18-21, tracking measured adherence (plasma dapivirine detected in 82% of samples overall; adherence higher by a factor of 4.1 in women 27-45 than in women 18-21).

A comparator for background HIV incidence in a high-risk female population receiving a full prevention package. The placebo arm ran at 4.5 per 100 person-years overall despite monthly HIV testing, risk-reduction counselling, partner testing, STI screening and treatment, and free condoms. By age band, placebo-arm incidence was 5.4 per 100 person-years (18-21), 6.1 (22-26) and 3.0 (27-45). The 22-26 figure is the one to hold against a model's peak-incidence age. These are trial-cohort rates, not population rates: participants were screened for eligibility and 2884 of 5516 screened were excluded, most commonly for HIV seropositivity.

Weak context for STI prevalence. Baseline prevalence among enrolled women was 13%/11% chlamydia (dapivirine/placebo), 4%/4% gonorrhoea, 7%/7% trichomoniasis. These are trial-entry screening prevalences in a selected multi-country cohort, not Rakai and not population-based, so they are a plausibility check on the model's female STI prevalence rather than a calibration target. Only 253 of 2629 participants (10%) were Ugandan, and the paper does not break STI prevalence down by country.

The paper carries nothing on point-of-care diagnostics or on the STI cofactor effect. Incident STIs are reported only as "similar rate in the two groups", with the numbers in a supplementary table not in the extracted text.

## Key points

- 168 incident HIV-1 infections over 4280 person-years: 71 dapivirine (3.3 per 100 person-years), 97 placebo (4.5 per 100 person-years).
- Trial was powered for a 60% reduction. The observed effect was significant against a 0% null but did not exclude an efficacy below 25% in either analysis (P = 0.88 for 15 sites, P = 0.30 for 13 sites).
- Adherence rose over the first year and then held; protection was sustained through 24+ months of follow-up. This runs opposite to the decline-over-time pattern in oral PrEP trials.
- Safety was flat: primary safety endpoint in 14% of each group. Non-nucleoside resistance mutations among seroconverters were 12% dapivirine versus 10% placebo (P = 0.80), so the ring did not measurably select resistance in breakthrough infections.
- Pregnancy incidence 3.9 versus 4.0 per 100 person-years; ring withheld during pregnancy, accounting for about 2% of follow-up time.

## Limitations

The two-site exclusion and the sample-size recalculation to ~2600 women were made in October 2013, after the trial started, though while groups were still masked and with data-safety-monitoring-board approval. The 37% figure is therefore from a modified analysis plan and the 27% all-sites figure is the more conservative one to carry.

The age-efficacy relationship below 25 was prespecified, but the 18-21 versus over-21 cut is post hoc, chosen to balance infection counts across thirds. Treat 56% above 21 as a subgroup signal rather than an estimate to plug in directly.

The adherence definitions (plasma dapivirine > 95 pg/ml, residual ring dapivirine < 23.5 mg) count a woman as adherent even if she wore the ring for only part of the month or reinserted it hours before the visit, so adherence is likely overstated and the adherence-efficacy gradient understated. Blinded placebo-controlled conditions also depress adherence relative to open-label use, which is the setting a model of a deployed programme would represent.

## Methodology

Intention-to-treat Cox regression stratified by site, end-point-driven design continuing until 120+ infections accrued and all participants had 12 months minimum follow-up. Participants with detectable HIV-1 RNA at enrollment were excluded from the primary analysis by retrospective PCR on archived plasma, so the incidence denominators exclude prevalent infection missed by serology.
