---
type: entry
title: "Improving HIV Case Finding Through Index Testing: Findings from Health Facilities in 12 Districts of South Africa, October 2019-September 2021"
description: PEPFAR programme data on the HIV index-testing cascade in 371 South African facilities; 2.6% of tests but 17.8% positivity, 1.0 contacts elicited per client, 51% of contacts tested.
author: Aheron et al.
published: 2024-05
resource: 10.1007/s10461-024-04269-3
local: raw/10.1007/s10461-024-04269-3
tags: [partner-notification, hiv]
updated: 2026-09-10 00:19
---

Descriptive analysis of routine PEPFAR monitoring data (quarterly MER indicators) from 371
public health facilities in 12 CDC-supported districts of South Africa, October 2019 to
September 2021. Index testing means offering an HIV test to the sexual, needle-sharing and
biological-child contacts named by a person newly diagnosed with HIV. The paper walks the
full cascade: offered, accepted, contacts elicited, contacts tested, contacts newly
positive. Aggregate programme data only, no individual-level records. Extracted text and
both cascade tables sit in `raw/10.1007/s10461-024-04269-3`.

## Relevance to project

canary-stis implements no partner-notification pathway, so this is a bound on what the
model leaves out, not a parameter for anything inside it. The cascade numbers say how much
of a partner-tracing arm would actually be realized in a routine African programme, and
they are low enough that omitting the pathway costs less than the intuition suggests:
of 316,220 clients who accepted index testing, only 319,680 contacts were named
(1.0 contact per client, 0.4 for female index clients aged 15+, 1.1 for males), and only
51.2% of those named were tested. Multiplying through, a newly diagnosed index client
yields roughly 0.5 contacts tested and 0.09 new diagnoses.

The yield figure is the comparator worth keeping: HIV positivity among tested contacts was
17.8% (29,118/163,633) against 4.1% for all non-index facility modalities, a 4.3-fold
difference, while index testing was 2.6% of the 6,385,172 tests conducted. A tracing
pathway concentrates diagnostic effort on high-prevalence contacts by a factor of about
four. That is the same mechanism the POC arm is meant to exploit through symptomatic
care-seeking rather than through partner tracing, so this sets a rough scale for how much
targeting gain a network-informed pathway can produce.

Not usable as a calibration target: South Africa, not Rakai, and the denominators are
facility throughput rather than a population cohort.

## Key points

Elicitation is the binding constraint, not acceptance. 85.2% of those offered index testing
accepted, but the elicitation ratio was 1.0 overall and 0.6 pediatric contacts per newly
diagnosed woman aged 15-49 (denominator 178,838). The authors attribute the low female
ratio (0.4) partly to intimate partner violence risk: providers screen with the WHO LIVES
protocol and withhold index testing from clients screening positive.

19.7% of contacts elicited (62,978/319,680) had already been diagnosed HIV-positive and
were ineligible for testing, which is a re-engagement opportunity rather than case finding.

Testing coverage of elicited contacts varied enormously by district, 91.9% in Zululand
against 11.2% in Dr Kenneth Kaunda, which the authors attribute to migration and the
inability to trace clients across facility catchment areas electronically.

Yield by age and sex crosses over: females aged 34 and under had higher index positivity
than males of the same age (25.3% for females 20-24), while males 35 and over had higher
positivity than same-age females (28.1% for males 35-39). Women aged 50+ reached 26.9%
against 3.3% from other modalities, the largest single ratio in the paper.

Among children under 15, index testing was 7.7% of pediatric tests but 25.0% of pediatric
diagnoses (positivity 2.8% versus 0.7%), and only 44.0% of elicited child contacts were
tested.

## Limitations

Testing modality may be misclassified in routine reporting. No costing data, though the
authors cite other work finding index testing more expensive per test than most modalities.
Public facilities only, excluding community sites, key-population venues and private
providers. Non-index modalities were pooled rather than assessed separately, so the 4.1%
comparator mixes antenatal, TB, VMMC and STI-clinic testing with very different prior
probabilities. Aggregate data prevents any individual-level or multivariable analysis, and
the period overlaps COVID-19 service disruption.
