---
type: entry
title: "Understanding the potential impact of a combination HIV prevention intervention in a hyper-endemic community"
description: Compartmental model of KwaZulu-Natal finds combined testing, risk reduction, circumcision and ART cuts HIV incidence 47% at 4 years and 52% at 15 years, with the full effect taking 10-15 years to accrue.
author: Alsallaq et al.
published: 2013-01-23
resource: https://doi.org/10.1371/journal.pone.0054575
local: raw/10.1371/journal.pone.0054575
tags: [hiv, modeling, care-seeking]
updated: 2026-09-10 00:25
---

Source: [alsallaq-2013](https://doi.org/10.1371/journal.pone.0054575)

A deterministic compartmental model of heterosexual HIV transmission in KwaZulu-Natal, South
Africa (adult prevalence about 23%), used to project the population-level incidence effect of
four prevention components delivered together: community home-based HIV testing reaching 90% of
adults in one year and repeated every four years, risk behaviour reduction after a first
positive test, medical male circumcision, and ART. The population is stratified by sex,
circumcision status, and sexual risk group, with staged infectiousness by CD4. It is fitted by
rejection sampling to antenatal and household HIV prevalence, one longitudinal incidence
estimate, and province-wide ART coverage; the uncertainty ranges quoted are interquartile
ranges across accepted parameter sets.

## Relevance to project

A comparator for the size and, more usefully, the time course of a combination-prevention effect
on HIV incidence, in a generalized epidemic of similar structure to Rakai. Combination I (90%
four-yearly testing, behaviour change, 70% circumcision of uncircumcised men over 2 years, ART
at CD4 350) reduces incidence 47% (43-50%) at 4 years, from 2.3 (2.1-2.6) to 1.2 (1.1-1.3) per
100 person-years, and 52% (45-60%) at 15 years. Combination II, identical but with ART on
diagnosis, gives 63% (60-65%) at 4 years and 76% (71-81%) at 15 years. Those numbers bound what
a package built on repeated community testing plus treatment can deliver without any STI
component, so a POC arm here has to show impact on top of that, not instead of it.

The mechanism decomposition is the part that transfers directly. Short-term impact is carried
almost entirely by post-diagnosis behaviour change and long-term impact by ART and circumcision:
removing behaviour change costs 4 percentage points at 4 years (47% to 43%) but almost nothing
at 15 years. Cutting testing uptake by a third in each round costs far more than any other
failure mode, taking Combination I from 52% to 33% and Combination II from 76% to 46% at 15
years, because ART initiation depends on being diagnosed. That is the same dependency a POC
test-and-treat arm has on the symptomatic care-seeking door, and it says the door, not the assay,
is where impact is lost.

Individual parameter values usable as priors or bounds, all from Table 1: ART reduces onward
transmission by 92%, circumcision reduces per-act female-to-male acquisition by 60%, condoms
reduce transmission by 90% both ways, female-to-male per-act transmission is half male-to-female,
acute infection multiplies baseline transmission probability by 27 and late symptomatic infection
by 7, mean untreated duration 11 years, ART dropout 14.5% per year. Behaviour change after
diagnosis in the intervention arms: men increase condom use 25% and reduce partner acquisition
25%, women 12.5% and 25%, sustained a mean 3 years.

The model has no STIs, so it says nothing about the cofactor pathway or about STI treatment as a
prevention modality. Use it for the counterfactual and the timescale, not for anything the STI
components of this project are meant to estimate.

## Key points

- The full impact of a combination package accrues over 10-15 years. Trials and programme
  evaluations reading out at 2-3 years will understate it, and the small relative differences
  between single components in the short term make stepped-wedge designs impractical for
  attributing effect to components.
- ART alone at CD4 350 gives 33% (32-34%) incidence reduction at 4 years; ART on diagnosis gives
  53% at 4 years, 66% at 10 years, 67% at 15 years. The ART-only projection never falls below
  0.5 per 100 person-years, which the authors attribute to the 92% (not complete) infectiousness
  reduction, 14.5%/year dropout, and the four-year gap between testing rounds.
- Combination II reaches 0.3 new infections per 100 person-years at 25 years and crosses the
  "AIDS transition" (new infections below AIDS deaths) within 6-8 years.
- Components are synergistic at almost all times, measured as incidence reduction beyond the sum
  of the individual reductions. Brief marginal redundancy appears before year 20 when many people
  are simultaneously on ART and reducing risk after diagnosis; dropout and behavioural waning
  restore synergy.
- Circumcision does comparatively little here because 27% of KZN men are already circumcised. In
  a lower-baseline setting the circumcision component would matter more.

## Limitations

Not age-structured and no explicit partnership formation or concurrency, so nothing about age
mixing or overlapping partnerships is represented; the authors say so. No PrEP, no risk
compensation on ART, no circumcision of HIV-positive men, no drug resistance, no behaviour change
in the wider uninfected population as incidence falls. Costs are not modelled. The model was not
fitted to sex-specific incidence. The single incidence data point used for calibration is thin
support for the baseline trajectory. Numbers are specific to KZN in the 2010s and the ART
guidelines of that period (CD4 350 was then current), so the current-standard comparator is
obsolete as a description of any present-day programme.
