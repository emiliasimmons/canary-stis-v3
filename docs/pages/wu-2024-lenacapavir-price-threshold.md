---
type: entry
title: "Health impact, budget impact, and price threshold for cost-effectiveness of lenacapavir for HIV pre-exposure prophylaxis in eastern and southern Africa"
description: EMOD-HIV modelling of six-monthly injectable lenacapavir in South Africa, Zimbabwe and western Kenya. Risk-targeted coverage of 1.6-4.0% averts 12-18% of HIV infections over ten years, and targeting narrowly raises the affordable price while cutting infections averted
author: Wu et al.
published: 2024-09-20
resource: https://doi.org/10.1016/S2352-3018(24)00239-X
local: raw/10.1016/s2352-3018(24)00239-x/
tags: [hiv, prep, modeling, economics, sexual-networks]
updated: 2026-09-10 00:32
---

An agent-based modelling analysis of scaling up lenacapavir, a twice-yearly injectable pre-exposure prophylaxis, in three eastern and southern African settings from 2026 to 2035. The model is EMOD-HIV, an individual-based heterosexual-network microsimulation with monthly time steps, calibrated to HIV prevalence by age and sex and to numbers on ART, with 100 resampled parameter sets carrying the uncertainty. The paper's contribution is the maximum per-dose price at which lenacapavir clears a cost-effectiveness threshold, and how that price moves as coverage widens. Extracted content in [raw/10.1016/s2352-3018(24)00239-x/](../raw/10.1016/s2352-3018(24)00239-x/).

## Relevance to project

This is a comparator and a design reference for the POC arm's benefit accounting, not a source of STI parameters.

The targeting result is the part canary-stis can use directly. Table 3 gives the exchange rate between how narrowly a prevention product is aimed and what it buys. In South Africa, lenacapavir to female sex workers alone sustains $589 per dose (95% UI 454-726) but averts only 6.0% (1.0-14.0) of infections; opening it to females with a VOICE risk score above 1 plus males with more than one partner takes infections averted to 42.5% (38.3-46.9) at $32 per dose (31-33). In western Kenya the same two ends of the range are $23 and 7.0% averted versus $4.20 and 71.0% averted. Diminishing marginal returns on infections averted alongside a collapsing affordable price is the pattern any argument that POC STI diagnostics work by *identifying* high-transmission network positions has to beat: the value of a targeting signal is bounded by how few people it selects and how much higher their incidence is.

It also sets a scale for a prevention product's plausible population-level effect. Population coverage of 1.6-4.0% averting 12.3-18.0% of infections over ten years, at 24-34 infections averted per 1000 doses, is the order of magnitude a well-targeted, 95%-effective prevention product delivers in these epidemics. An STI-diagnostic pathway that returns HIV incidence reductions well above that band, at the coverage the SOC and POC arms actually reach through the symptomatic care-seeking door, is a result to check rather than report.

The cost side is a method reference. Costs run on the payer perspective in 2021 US$, with a $500 per DALY averted supply-side threshold (plus $200 and, for South Africa, $1175 sensitivity thresholds), demand generation at 10% of per-dose price, 5% wastage, and provision at $8.55 per dose. Country ART provision costs are $196.85 (western Kenya), $189.56 (South Africa) and $176.01 (Zimbabwe) per year; facility-based HIV tests cost $2.24-5.62 depending on setting and result. Nothing here is Ugandan, so the numbers do not transfer to a Rakai-calibrated model as inputs, and none of them price an STI assay.

## Key points

- Main-analysis coverage assumptions, drawn from a literature review of stated PrEP preferences: 40% of female sex workers, 40% of male clients, 32% of women aged 15-24 with more than one partner, 36% of women 25 and older with more than one partner, 32% of men with more than one partner. The higher-coverage scenario doubles these to 64-76%.
- Doubling coverage roughly doubles doses and DALYs averted but lowers the affordable price 10-18%, to $88.34 (South Africa), $17.71 (Zimbabwe) and $14.78 (western Kenya).
- Price thresholds at the $500 threshold: $106.28 (95% UI 95.72-115.87) South Africa, $21.15 (17.70-24.89) Zimbabwe, $16.58 (15.44-17.70) western Kenya. The five-fold South African premium tracks its higher HIV prevalence and health-care costs, not a better epidemic fit.
- Five-year budget impact at those prices: $507.3 million South Africa, $16.8 million Zimbabwe, $4.09 million western Kenya. Over 90% is lenacapavir provision; averted ART and illness costs return under 2% in the main scenario, 5-8% at higher coverage.
- Adding males with more than one sexual partner beat expanding to the next-riskiest female stratum in South Africa and Zimbabwe, but not in western Kenya, which the authors attribute to high voluntary medical male circumcision coverage there. A targeting rule's value is setting-specific.
- Assumed efficacy is 95% for six months for lenacapavir and 75% for oral PrEP with three-month persistence. Results were robust to tripling background oral PrEP and to oral adherence of 58% or 95%, because current oral coverage is low enough that tripling it stays small.

## Limitations

- Uptake rests on stated-preference literature, since lenacapavir was not yet available in the region. Behaviour may not follow.
- Heterosexual mixing only: no men who have sex with men, no people who inject drugs, no pregnant women.
- Fixed point probabilities rather than distributions for model inputs; the uncertainty intervals come from the 100 calibration parameter sets, so they carry calibration uncertainty and not input uncertainty.
- Payer perspective excludes participant costs.
- No STI co-infection, no syndemic pathway, and no competing long-acting products (cabotegravir, dapivirine ring) in the counterfactual.
- Assumed 2026 availability. Delay lowers price thresholds because background incidence is falling.
