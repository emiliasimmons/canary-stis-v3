---
type: entry
title: "The effect of 90-90-90 on HIV-1 incidence and mortality in eSwatini: a mathematical modelling study"
description: EMOD network model of eSwatini finds ART scale-up cut adult HIV incidence 43.6% over 2010-16 but no treatment scenario reaches epidemic control by 2030.
author: Akullian et al.
published: 2020-02-13
resource: https://doi.org/10.1016/S2352-3018(19)30436-9
local: raw/10.1016/s2352-3018(19)30436-9
tags: [hiv, modeling, sexual-networks]
updated: 2026-09-10 00:23
---

Source: [akullian-2020](https://doi.org/10.1016/S2352-3018(19)30436-9)

An individual-based network transmission model (EMOD, Institute for Disease Modeling) of the
HIV epidemic in eSwatini, calibrated to age- and sex-specific antiretroviral therapy (ART) and
voluntary medical male circumcision (VMMC) coverage, asking whether reaching the UNAIDS
90-90-90 targets can bring eSwatini to epidemic control (fewer than 1 infection per 1000
person-years) by 2030. Five scenarios: status quo, no ART/no VMMC, VMMC only, 90-90-90 attained
evenly within age and sex strata, and 100% ART initiation within an average of 6 months of
infection.

## Relevance to project

A comparator and an upper bound for the treatment-only arm of the argument this project makes.
The headline result is that the most aggressive ART scenario physically achievable (100%
initiation within 6 months, ART reducing infectiousness by 92%) still leaves adult incidence at
0.46 infections per 100 person-years by 2050, roughly five times the epidemic control threshold
of 0.1 per 100 person-years. That is the quantitative case for prevention modalities beyond
treatment, which is the space POC STI diagnostics occupy. If a POC arm here produces an
incidence reduction on top of a well-treated baseline, this paper gives the size of the gap that
remains to be filled.

Numbers usable as design references rather than as calibration targets, since the setting is
eSwatini and not Rakai:

- ART assumed to reduce infectiousness by 92%, with the transmission benefit growing linearly
  over the first 6 months after initiation. A defensible default if this model needs an ART
  efficacy parameter.
- By 2030 under status quo, acute infection (within 3 months) accounts for 18.8% (95% CrI
  13.7-22.4) of transmissions from men and 16.4% (12.8-21.8) from women; early infection (within
  1 year) accounts for 23.8% (18.8-28.0) from men and 20.8% (16.0-26.0) from women. A bound on
  how much of the residual transmission is unreachable by any test-and-treat door, including an
  STI-diagnostic door.
- By 2030 under status quo (>80% ART coverage), transmissions come from people never on ART
  (38.6%, 33.1-47.7), dropped out of ART (24.7%, 20.2-29.6), or on ART unsuppressed (35.9%,
  30.1-41.4).
- Status-quo adult (15-49) incidence 1.42 per 100 person-years in 2016, 1.09 (0.87-1.29) in
  2030, 0.74 (0.60-0.91) in 2050. Counterfactual with no ART and no VMMC: 4.46 (3.64-5.23) by
  2050.

The structural precedent matters as much as the numbers. The model's stated reason previous
test-and-treat models overpredicted incidence declines is missing age and sex structure in
coverage, simplistic sexual mixing, and unrealistic scale-up assumptions. It uses four
relationship types (marital, informal, transitory, commercial) with risk-group heterogeneity
driven by extra-partnership parameters, which is the same shape as the risk-structured network
this project builds on.

Not a source of STI parameters: no STI is in the model, and the cofactor effect on HIV
transmission is absent entirely.

## Key points

Historical ART scale-up (34.0% coverage in 2010 to 74.1% in 2016 among adults 15-49) reduced
cumulative incidence by 43.57% (39.71-46.36) and mortality by 56.17% (54.06-58.92) over 2010-16,
against a no-ART counterfactual. Incidence fell more in men, mortality more in women, both
attributed to higher treatment coverage in women.

Closing coverage gaps to 90-90-90 evenly across age and sex by 2020 adds little overall but
concentrates in the young: an extra 17.37% (7.33-26.12) incidence reduction in 15-24 year olds
over 2016-30, against 1.99% (-5.09 to 7.74) in 35-49 year olds.

VMMC's contribution is modest short-term and grows with horizon: 4.56% (1.24-8.56) cumulative
incidence reduction over 2010-16, 20.57% (18.51-23.90) over 2016-50, larger in men.

Epidemic control by 2050 appears only under a combination the authors call unrealistic:
cross-sectional ART coverage above 90%, ART efficacy 98% or more, and under 2 months from
acquisition to initiation.

Successful intervention ages the epidemic. The share of new adult acquisitions in 15-24 year
olds falls from 0.39 (0.34-0.44) in 2016 to 0.26 (0.22-0.30) by 2030 under status quo, and this
shift is absent from the no-intervention counterfactual, so it is caused by the reduction in
force of infection rather than by demography.

## Methodology

Calibration targets were demographics (age-specific fertility, age- and sex-specific mortality,
population age distribution), HIV prevalence by 5-year age bin, sex and year from three
population-based surveys (2007 SDHS, 2011 SHIMS, 2016 PHIA), and ART coverage by age, sex and
year. ART coverage was not observed directly; it was back-calculated from viral load suppression
(<1000 copies/mL) assuming 90% of people on ART are suppressed, then imputed for non-survey
years proportionally to annual changes in the crude number on ART.

Fitting used parallel simultaneous perturbation optimisation maximising a pseudolikelihood, run
to a likelihood plateau. 250 parameter sets were drawn from 23,100 simulations by roulette
resampling in proportion to likelihood; 25 parameters were fitted. All credible intervals are
the spread across those 250 sets, so they are fitting uncertainty and not posterior uncertainty
in a Bayesian sense.

Closed population, no migration, single country-level geography justified by prevalence varying
only 25.7% to 29.4% across the four provinces.

## Limitations

No pre-exposure prophylaxis and no layering of other prevention modalities, so the projections
describe a treatment-and-circumcision-only future. VMMC is held at 2016 levels with no further
scale-up, which the authors say likely understates future coverage. No behavioural change is
assumed following VMMC or ART uptake. Generalisability is claimed only to settings with similar
epidemic intensity and scale-up dynamics, and eSwatini has the world's highest HIV prevalence,
so the absolute incidence levels do not transfer to Rakai. Two of the seven authors are Gates
Foundation employees and the study was Gates- and Global Good-funded, disclosed in the paper.
