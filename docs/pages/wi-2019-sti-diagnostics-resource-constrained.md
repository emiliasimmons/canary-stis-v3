---
type: entry
title: "Diagnosing sexually transmitted infections in resource-constrained settings: challenges and ways forward"
description: WHO-led review of syndromic management diagnostic accuracy vs POCTs for CT/NG/TV/syphilis, with absolute-effect tables at varying prevalence
author: Wi et al.
published: 2019-06-18
resource: 10.1002/jia2.25343
local: raw/10.1002/jia2.25343/content.md
tags: [sti, diagnostics]
updated: 2026-09-10 09:45
---

A review commissioned by WHO's Human Reproduction Programme that updates the Zemouri et al.
(2016) meta-analysis of vaginal discharge syndromic management and surveys POCTs
commercially available or in the pipeline for CT, NG, TV and syphilis. The raw extraction
is at `raw/10.1002/jia2.25343/content.md`.

## Relevance to project

The paper's core tables (Tables 2-4) give pooled sensitivity and specificity for four
vaginal discharge flowchart variants diagnosing CT/NG, and then compare the absolute
effects (true positives, missed treatments, overtreatment) of those flowcharts against
RDTs and molecular POCTs at 5%, 15% and 30% CT/NG prevalence. These numbers bound the diagnostic performance of the SOC arm (syndromic management) and
the POC arm in the model, and anchor the gap between them.

For the POC arm specifically: the Xpert CT/NG molecular assay (sensitivity 95-98%,
specificity 99.4-99.9% on vaginal/cervical swabs) is the benchmark near-patient NAAT. The
paper also tabulates lower-accuracy RDT scenarios (60-80% sensitivity, 90% specificity)
that bracket what a cheaper, more deployable test might achieve. The model's POC
sensitivity and specificity parameters can be drawn from these ranges.

For the SOC arm: pooled CT/NG sensitivity across flowchart types ranges from 28% (risk
assessment only) to 90% (with lab microscopy), with specificity moving inversely (57% down
to 35%). The most common field implementation, flowchart 2 (history + risk + speculum),
sits at 45% sensitivity and 74% specificity. These set the syndromic management diagnostic
performance the SOC arm should reproduce.

The paper does not model HIV transmission effects of improved STI diagnosis, and its
cost-effectiveness discussion draws on Vickerman et al. (2006) modelling rather than
producing new estimates.

## Key points

Urethral discharge syndrome in men has adequate diagnostic accuracy (sensitivity 84-95%)
and is cost-effective. The diagnostic gap is concentrated in women, where most CT, NG and
MG cervical infections are asymptomatic and never enter a syndromic pathway.

At 15% CT/NG prevalence using flowchart 2, syndromic management produces 219
overtreatments and 83 missed treatments per 1000 women. A molecular POCT at the same
prevalence produces 17 overtreatments and 8 missed treatments. RDTs at 70% sensitivity and
90% specificity fall between: 85 overtreatments and 45 missed treatments.

For TV, the OSOM lateral flow test (sensitivity 83-86%) and the Xpert TV assay (sensitivity
~96-97%) are commercially available. Syphilis RDTs (sensitivity 75-99%, specificity
92-99%) are already deployed at scale; the main limitation is distinguishing active from
previously treated infection.

NG POCTs lag behind CT POCTs. Most rapid NG tests have been validated only against culture
(not NAATs) and only in symptomatic patients. No gonorrhoea POCT has been evaluated for
extragenital sites.

Cost-effectiveness modelling (Vickerman et al.) suggests a POCT with 70-80% sensitivity,
95% specificity and a unit cost of US$1-2 would be cost-effective for reducing HIV
transmission and inappropriate treatment of CT/NG among female sex workers in
high-prevalence settings.

## Limitations

The updated meta-analysis pools studies across geographic settings and flowchart
implementations, so the pooled estimates may not reflect performance in any single site
(including Rakai). Study heterogeneity is acknowledged but not formally assessed with
I-squared or similar.

The POCT landscape described is a 2018 snapshot. Several assays listed as "in the
pipeline" (GeneXpert Omni, Atlas Genetics io, MobiNAAT) have since either launched,
stalled or been discontinued, so the pipeline section is dated.

The review does not address how diagnostic accuracy translates to population-level STI or
HIV incidence reduction, which is the question this project's model is built to answer.

## Methodology

Updated systematic review and meta-analysis of the vaginal discharge flowchart (Zemouri
et al. 2016 extended through September 2018). Pooled sensitivity and specificity calculated
with WINPEPI software. Literature reviews (PubMed, Medline, 2000-2018) for POCT
performance, provider preferences and cost-effectiveness. No eligibility criteria were
applied to the narrative review component beyond the syndromic management meta-analysis.
