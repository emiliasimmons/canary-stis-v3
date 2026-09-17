---
type: entry
title: "Canary study concept: originating note and May 2026 convening deck"
description: The idea the project started from: the pathway decomposition proposed from STI diagnostics to HIV incidence, the counterfactual arm ladder meant to separate the pathways, and the empirical anchors named for it.
author: Akullian et al.
published: 2026-05-20
resource: raw/concept/
local: raw/concept/
tags: [study-concept, hiv, sti, diagnostics, modeling, sexual-networks, rakai, prep, coinfection, care-seeking, partner-notification, economics]
updated: 2026-09-17 10:58
---

Two internal documents set out the idea this repository grew from. `CN_adam.md` is Adam
Akullian's concept note, a prose proposal with four pathways and five key questions and no
results. `Canary_GVHE_2026.05.20_transcript.md` transcribes the 26-slide deck presented at
the 20 May 2026 convening, which expands the same idea into a five-pathway framework, a
counterfactual arm ladder, a model architecture with named parameters, and early figures
from runs the deck labels illustrative and uncalibrated. Both name the Rakai Community
Cohort Study as the calibration site and the INSTEP randomized trial as the empirical
anchor.

## Study concept

Both documents argue one premise, STI positivity as a marker of HIV risk rather than a
driver of HIV persistence, and between them they are the only place the project's opening
choices appear with a reason attached: the pathway taxonomy the analysis sets out to
decompose, the arm ladder the SOC and POC arms and `MagicCure` grew out of, and the
per-pathogen multipliers on HIV relative susceptibility the model started with (gonorrhoea
×1.2, trichomoniasis ×1.5, syphilis ×2.67, chlamydia none), which appear on the
architecture slide with no source given in either document.

Neither document supplies an empirical quantity. Every number the model produces in the
deck comes from an uncalibrated run on a network that had not been fitted to Rakai, and the
closing slide says so. They are not targets, priors, or bounds.

## The pathways

The deck's framework diagram enumerates five lettered pathways from a diagnostic result to
a population outcome.

- **A, treatment of asymptomatic infection.** Detection leads to treatment, a shorter
  infectious period, and less onward STI transmission.
- **B, partner treatment cascade.** Diagnosis leads to notification and referral, partner
  treatment, and interruption of a transmission chain.
- **C, biological susceptibility.** Infection causes genital inflammation and raises the
  per-act probability of HIV acquisition.
- **D, prevention targeting and risk awareness.** A positive STI result signals HIV
  exposure risk, raises perceived risk, and raises PrEP uptake and adherence.
- **E, network risk signal.** A positive result is evidence of position in a
  high-transmission network, identifying high-risk individuals and clusters.

A and B feed reduced STI transmission, C and D feed reduced HIV risk, and E feeds
interruption of transmission chains.

The same study is enumerated three different ways across the two documents, and no document
maps one enumeration onto another. The concept note lists four pathways: direct treatment
with reduced biological susceptibility, prevention of onward STI transmission,
identification of elevated-risk individuals for prevention delivery, and identification of
high-transmission networks. Slide 8 lists three, named biological, behavioral, and network.
The A to E scheme is the one used everywhere the proposal gets concrete, so it is the one to
work from.

## The counterfactual arm ladder

Five arms, each toggling syndromic treatment, POC screening, and how PrEP is allocated.

| Arm | Syndromic treatment | POC screening | PrEP |
|---|---|---|---|
| Baseline | yes | no | none |
| Full Screening | yes | yes | STI-diagnosis triggered |
| Screening, no PrEP | yes | yes | none |
| Risk-Group PrEP | yes | no | WHO behavioral screening |
| Magic Cure | instant cure | no | none |

Differences between arms are meant to isolate a pathway. Full minus Baseline gives the
total effect of the POC platform. Full minus Screening-no-PrEP gives D, the contribution of
PrEP targeting. Screening-no-PrEP minus Baseline gives A and C together, the direct effect
of STI treatment on HIV. STI-diagnosis-triggered PrEP minus Risk-Group PrEP gives the value
of a biomarker over behavioral screening, which the deck also labels D. Magic Cure minus
Baseline gives the upper bound on C, the maximum biological population attributable
fraction.

Two features of this table are worth carrying forward. Pathway D is assigned to two
different comparisons, which measure different things under one letter: the increment from
adding targeted PrEP to a screening programme, and the increment from choosing a biomarker
over a behavioral questionnaire. Pathways B and E are isolated by no arm at all, which the
deck's next-steps slide confirms as unimplemented work.

## Empirical anchors named

**INSTEP.** A randomized trial among 4,500 women, embedded in the Rakai cohort, testing
whether integrating curable-STI diagnostic testing into HIV prevention services improves
identification of women at elevated HIV risk and raises PrEP uptake and persistence. The
proposal expects it to supply STI test positivity, the symptomatic-to-asymptomatic split at
testing, the association between STI positivity and HIV positivity, PrEP uptake, adherence,
and persistence after an STI diagnosis, and changes in perceived risk and behavior after
diagnosis. Early findings reported in the deck: a high burden of undiagnosed curable STIs
among African women at high HIV risk, and that adding curable-STI testing to existing PrEP
eligibility screening would nearly double the number of PrEP-eligible women. The deck gives
no read-out date and describes the findings as early.

**Rakai incidence decline.** The deck cites Akullian et al., 2026, PLOS Medicine for an
incidence curve peaking near 2.1 per 100 person-years around 2000 and falling steeply after
2010 toward below 0.5, alongside rising ART and VMMC coverage and later sexual debut. The
argument made from it is that finding women at high HIV risk gets harder as incidence
declines, which is what motivates precision targeting tools.

**STI burden.** Curable STI point prevalence among women in high HIV burden African
settings, from the WHO STI prevalence atlas, with study-group medians of roughly 3% for
syphilis, 5% for gonorrhoea, 10% for trichomoniasis, and 12% for chlamydia, and study-level
estimates scattered from about 1% to above 40%. These mix symptomatic and asymptomatic
detection across study designs.

**Trial evidence the study is built against.** A forest plot of nine STI-treatment trials,
of which only Grosskurth 1995 in Mwanza shows a significant protective effect on HIV
(RR 0.58, 95% CI 0.42 to 0.79, N = 12,537). The other eight straddle RR 1. The deck's
reading is that Mwanza was an early-epidemic setting with high genital-ulcer prevalence, and
that the inconsistency elsewhere reflects the untreated asymptomatic reservoir rather than
absent biology.

## Strategic and funding context

The deck opens on the Foundation's POC STI diagnostics portfolio, which is the reason the
modeling question is being asked. Product development funds four manufacturers (Chembio,
Detact, Aptitude, Pluslife) for low-cost molecular diagnostics covering gonorrhoea,
chlamydia, trichomoniasis, and syphilis, with regulatory approval expected 2026 to 2027.
Clinical evaluation and implementation science runs about $6.4M across four country studies:
Kenya with Jhpiego ($2.9M and above), Zimbabwe with PSI, South Africa with Wits/RHI
($2.9M), and Botswana with Harvard Health Partnership ($150K). Market access and health
economics is about $786K across two investments. The stated value proposition is evidence
for integrated investment across the STI and HIV portfolios, better risk prioritization for
HIV prevention delivery, and guidance on where to deploy diagnostics.

The convening brought together the software and modeling platform team, the SRH team, the
INSTEP investigators (Kate Grabowski at Johns Hopkins, Jeff Imai-Eaton and Yonatan Grad at
Harvard), the STI diagnostics and strategic direction group, and Rakai in-country
investigators listed as to be determined.

Both files are working drafts. The source deck filename misspells "diagnostic", one slide's
numbered list skips item 5, slide 19 duplicates slide 9, the two quantitative pathway
slides (21 and 23) are marked hidden in the source and do not appear in normal playback,
and the concept note's co-author list is marked to be determined. The deck's map caption
gives the Rakai cohort as 34 communities, against the 30 used elsewhere in this project.
