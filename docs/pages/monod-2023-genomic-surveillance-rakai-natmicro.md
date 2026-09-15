---
type: entry
title: "Longitudinal population-level HIV epidemiologic and genomic surveillance highlights growing gender disparity of HIV transmission in Uganda"
description: Fifteen years of RCCS incidence plus deep-sequence phylogenetics, giving age- and sex-specific incidence rates 2003-2018 and transmission flows showing men's contribution rising from 58% to 63%
author: Monod et al.
published: 2023-12-05
resource: https://doi.org/10.1038/s41564-023-01530-8
local: raw/10.1038/s41564-023-01530-8/
tags: [hiv, rakai, sexual-networks, modeling]
updated: 2026-09-10 10:33
---

Source: [monod-2023](https://doi.org/10.1038/s41564-023-01530-8)

Combines the Rakai Community Cohort Study incidence cohort with longitudinal HIV deep-sequence phylogenetics across 36 inland communities in south-central Uganda, nine survey rounds (rounds 10-18) from September 2003 to May 2018. 38,749 participants enrolled, 22,724 seronegative at first survey contributing 127,217 person-years, 1,117 incident infections observed, 1,978 people with viraemic HIV deep-sequenced, and 227 heterosexual source-recipient pairs placed in calendar time. Transmission flows were fitted with semi-parametric Poisson flow regression under the constraint of matching the observed age- and sex-specific incidence.

## Key points

- Male incidence fell from 1.05 (95% CI 1.03-1.08) to 0.34 (0.33-0.35) per 100 person-years between 2003 and 2018, a 67.8% decline, with no shift in the median age of male infection.
- Women aged 15-24 fell comparably fast, 1.42 (1.35-1.50) to 0.36 (0.33-0.40) per 100 PY, a 74.5% decline. Women aged 25-34 fell only 43.9%, from 1.51 (1.45-1.57) to 0.84 (0.80-0.89), and women 35-49 only 37.4%, from 0.90 to 0.56. Median age of female infection moved from 23.4 (22.6-24.1) to 28.2 (27.1-29.2) years.
- Female-to-male incidence rate ratio was 1.59 (1.38-1.82) in 2018.
- Men's share of onward transmission rose from 57.9% (56.2-59.6) in 2003 to 62.8% (60.2-65.2) in 2018, while men were only 49.2% (44.3-54.1) of viraemic individuals, so men transmit more than population viral load alone predicts.
- Median age of transmitting male partners rose from 28.5 (27.1-30.1) to 33.5 (31.0-36.0) years; median age of transmitting female partners stayed near 25-26 years.
- Flows into girls and women aged 15-24 fell by about a third. From male partners 0-6 years older, 15.5% (12.3-18.9) of all transmissions in 2003 to 8.1% (5.6-11.0) in 2018; from male partners more than 6 years older, 16.0% to 12.1% (9.3-15.2). The single largest flow by 2018 was to women aged 25-34 from men 0-6 years older, up by half from 7.7% (6.2-9.3) to 12.0% (9.1-15.0). The largest flow into men in 2018 was to men 25-34 from women 0-6 years older, 10.6% (8.9-12.3).
- Transmitting partners are not drawn evenly from reported partners. For infections in girls and women 15-24 in 2018, the median age gap to the transmitting man was 9.0 (7.0-12.0) years, against a median age gap of 3.6 (3.5-3.9) years for their reported sexual partners in the same communities. For women 30 and older, transmitting partners had an interquartile age range of 30.3-38.0 years while reported partners were 40.0-42.7 years. Male age 25-40 rather than age gap tracks transmission risk.
- Round 18 (2016-2018) male cross-section by age: HIV prevalence 0.8% at 15-19 rising to 16.8% at 40-44; the proportion of men with HIV who were unsuppressed fell from 73.2% at 15-19 to 19.4% at 45-49, overall 33.9% (29.7-38.3) against a male-female gap of 14.8 percentage points (10.0-19.6).
- Counterfactuals at round 18: closing half the male suppression gap (75 additional men suppressed) would cut female incidence 25.1% (24.2-26.2); closing it entirely (150 men) 50.6% (48.6-52.8); reaching 95-95-95 in men (173 men) 58.4% (54.9-61.7). Closing the gap entirely would move the female-to-male incidence rate ratio from 1.59 to 0.78 (0.69-0.87).

## Relevance to project

The calibration target set for HIV in the RCCS inland communities: age- and sex-specific incidence per 100 person-years across nine rounds spanning 2003 to 2018, plus HIV prevalence and the unsuppressed fraction by five-year male age band at round 18. Those are the trajectories the Starsim HIV component has to reproduce before any STI intervention is layered on, and they come from the same cohort and communities the project has chosen as its first site.

For the network side it supplies a directly relevant constraint: who infects whom, by age and sex, and how that differs from who reports partnering with whom. The 9-year median age gap in transmissions to young women against a 3.6-year gap in reported partnerships is a mismatch a risk-structured network model will not produce by mixing on reported partner ages alone. That is a test of whether the model's high-transmission positions are in the right place, which is the third pathway in the project's triad.

The counterfactual suppression scenarios give a comparator scale for what an intervention has to beat. Suppressing an additional 150 men in round 18 halved female incidence. Any POC-versus-SOC incidence reduction should be read against that.

No STIs appear anywhere in this analysis, so it supplies nothing on cofactor effects, syndromic care-seeking, or STI burden.

## Methodology

Direction of transmission was called with phyloscanner on within-host deep-sequence phylogenies, then filtered on last-negative and first-positive test dates; infection dates were estimated from the sequence data. The flow model adjusts for detection probability and is fitted jointly against the incidence estimates, so the transmission flows and incidence rates are not independent pieces of evidence. Viral suppression is defined at 1,000 copies/ml plasma per WHO criteria, measured from 2011 (round 15) onward, with first-time participants used as a proxy for non-participants.

## Limitations

- 227 source-recipient pairs across 15 years, and only 61 in rounds 16-18. The round-18 counterfactuals rest on those 61 pairs plus hierarchical borrowing from earlier rounds, so age-band-level flow estimates are thin.
- Deep-sequence phylogenetics cannot establish direction for an individual pair; the claim is population-level.
- Transmission pairs require both partners enrolled and sequenced, so infections sourced from outside the study communities are missed, and the flows describe within-community transmission.
- Inland communities only. Lake Victoria fishing communities, which have much higher incidence, are excluded from these outcomes.
- The counterfactuals assume undetectable equals untransmittable and that the fitted flow structure holds when the infectious pool changes, which forecloses behavioural response to treatment scale-up.
- Non-participants are proxied by first-time participants for the viral-load estimates.
