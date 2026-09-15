---
type: entry
title: "Comparison of Empirically Derived and Model-Based Estimates of Key Population HIV Incidence and the Distribution of New Infections by Population Group in Sub-Saharan Africa"
description: Triangulation of empirical incidence-rate ratios, 94 transmission-model applications, and UNAIDS estimates; FSW incidence 8.6x and MSM 41.8x sex-matched total-population incidence, with 12% of 2021 SSA infections among FSW and MSM
author: Stevens et al.
published: 2024-01-01
resource: https://doi.org/10.1097/qai.0000000000003321
local: raw/10.1097/qai.0000000000003321
tags: [hiv, modeling, sexual-networks]
updated: 2026-09-10 00:12
---

Source: [stevens-2024](https://doi.org/10.1097/qai.0000000000003321)

Cross-source comparison of how much of HIV incidence in sub-Saharan Africa falls on key populations: female sex workers (FSW), men who have sex with men (MSM), and people who inject drugs (PWID). Three sources are placed side by side for 2021: incidence-rate ratios pooled from empirical cohort studies, outputs from 94 country applications of 9 dynamic transmission models, and the UNAIDS 2022 Global AIDS Update.

## Relevance to project

Supplies a defensible **bound on the incidence multiplier for the model's highest-risk network position** and a **comparator** for what the STIsim risk structure should produce once calibrated. The empirically derived incidence-rate ratio (E-IRR) for FSW relative to sex-matched total-population female incidence aged 15-39 is 8.6 (95% CI 5.7-12.9) across SSA, and 5.3 (3.7-7.6) in Eastern and Southern Africa, the region containing Rakai. That ESA figure is the directly usable number here: a sex-worker compartment in a Ugandan calibration should carry roughly 5-fold the female population incidence, not the 20-fold that UNAIDS-reported infection shares imply (Table 1 gives UNAIDS-IRR 19.8 for FSW in ESA against an E-IRR of 5.3).

Two further constraints for the risk-group design. First, the share of new infections attributable to the group is close to linear in the assumed group size: across models for South Africa, Lesotho, and Eswatini the correlation between key-population size proportion and the percentage of new infections was R^2 = 0.69 for FSW and 0.94 for PWID. Whatever fraction of women the model assigns to the high-activity position largely determines the infection share it reports, so that fraction is a calibration parameter to be justified, not a nuisance. Second, the incidence-to-prevalence ratio is a cheap internal consistency check on a calibrated run: empirical FSW estimates give 0.05 in ESA (0.06 SSA), model-based estimates a median 0.10, against 0.19 implied by UNAIDS. A run producing an FSW incidence-to-prevalence ratio near 0.2 is inconsistent with the empirical data.

Not a source for anything STI-specific, and not a calibration target for Rakai: everything is regional (ESA/WCA) because empirical incidence data were too sparse for country-level analysis, and MSM and PWID positions are outside the model's scope. The paper also argues explicitly that a cross-sectional share-of-new-infections metric misrepresents the value of prevention in high-transmission network positions, since it omits averted onward transmission. That bears directly on how POC-diagnostic impact should be reported here: a counterfactual scenario comparison over a long horizon, rather than the fraction of infections occurring in the targeted group.

## Key points

- MSM incidence was 41.8-fold (95% CI 21.9-79.6) sex-matched male total-population incidence aged 15-29 across SSA: 22.0 (14.1-34.3) in ESA and 141.7 (52.2-384.7) in WCA. Applied to UNAIDS national incidence, this gives MSM incidence rates of 3.3/100 person-years in ESA and 4.25/100 py in WCA.
- FSW incidence rates derived the same way were 1.59/100 py in ESA and 1.36/100 py in WCA, against total-population female incidence of 0.30 and 0.06/100 py.
- Combining E-IRRs with published key-population size estimates gives 12% of 2021 SSA adult infections among FSW (5%) and MSM (7%), from populations comprising about 1% of adults at risk. Regionally: 7% of ESA infections, 34% of WCA infections.
- Across the 94 model applications the median share of new infections was 3% FSW (IQR 2-6%), 2% MSM (0-4%), 1% PWID (0-2%), summing to about 6.4% (IQR 3.2-11.7%). UNAIDS reported 25% for the three groups combined.
- Varying key-population size proportions across their 95% credible range moved the FSW-plus-MSM share only to 9-19%, still below the UNAIDS figure.
- Models for the same country disagreed more than two-fold on key-population HIV prevalence and size. For South Africa across 7 models, FSW size proportion ranged 0.2-0.9% of adults and MSM 0.4-1.0%.
- Empirical MSM incidence exceeded what models fitted to prevalence produce, and in places exceeded matched cross-sectional MSM prevalence, which should represent cumulative incidence over the whole at-risk duration. The authors attribute this to young-skewed survey recruitment and to models collapsing MSM into one age or risk compartment.

## Methodology

Two workflows run in opposite directions. UNAIDS-published shares of new infections were converted into implied incidence rates by multiplying by total adult (15-49) infections from Spectrum and dividing by HIV-negative key-population size from a pooled survey collation. Separately, study-level incidence ratios from systematic reviews (Stannah et al for MSM, Jones and Anderson et al for FSW) were pooled by mixed-effects meta-analysis with a region fixed effect and country-district nested random effects, each study matched to district-age-year total-population incidence from the Naomi small-area model, then multiplied back up by national incidence and key-population size.

## Limitations

76 of 94 model results came from a single model (Goals), in two size-assumption variants, so the model distribution is not 9 independent views. District-level incidence denominators for years before 2022 were extrapolated by scaling the 2022 district estimate along the national trajectory, which assumes uniform proportional decline across districts. Key-population studies were mostly urban and younger than the 15-49 denominator used, which inflates the derived ratios somewhat. Every derived quantity depends on one set of national size and prevalence estimates that were themselves regression extrapolations in countries without local surveillance. No empirical PWID incidence-rate ratio could be estimated at all.
