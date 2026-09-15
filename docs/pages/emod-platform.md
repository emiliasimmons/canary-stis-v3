---
type: entry
title: "Implementation and applications of EMOD, an individual-based multi-disease modeling platform"
description: Design and software-process description of IDM's EMOD agent-based platform, including how HIV inherits from a generic STI transmission layer and how STI cofactors are configured.
author: Bershteyn et al.
published: 2018-07-06
resource: 10.1093/femspd/fty059
local: raw/10.1093/femspd/fty059
tags: [modeling, hiv, coinfection]
updated: 2026-09-10 00:28
---

Source: [bershteyn-2018](https://doi.org/10.1093/femspd/fty059)

A methods paper from the Institute for Disease Modeling describing EMOD, a C++ individual-based
modeling framework covering malaria, HIV, tuberculosis, dengue, polio and typhoid on one shared
codebase. It is a platform description, not an epidemiological study: no data, no fitted
parameters, no results.

The organising idea is an object-oriented inheritance chain. A generic layer (34,512 lines as of
February 2018) carries demographics, births, non-disease mortality, migration, socio-demographic
strata, SEIRS disease states, and generic interventions (a diagnostic with configurable
sensitivity and specificity, a vaccine with configurable take and efficacy). A transmission-mode
layer sits above it: the STI layer adds propensities to form and dissolve sexual relationships
and general STI interventions such as condoms. The HIV layer inherits that sexual-behaviour logic
and overwrites the generic SEIRS states with acute, chronic and symptomatic-AIDS states plus
CD4+ counts, ART and male circumcision. No single disease model exceeds 50,000 lines total; the
vector layer adds roughly 8,000 lines to the common framework and malaria a further 6,000, and
Notre Dame's dengue model needed about 1,000 lines on top of the existing vector code.

The second component is the "campaign" framework: a JSON file of blocks, each specifying who
(socio-demographic filter plus a random fraction), what (intervention and its parameters), when
(absolute simulation time), where (nodes), and optionally why (a trigger). Blocks broadcast
user-defined event names and listen for them, so cascades of decisions, delays, diagnostics and
interventions are assembled without recompiling. Triggers can also come from model-internal
events: birth, death, migration, pregnancy, new infection, formation of a new relationship. The
paper states that in the HIV model this same framework is what creates coinfections with other
STIs that raise HIV susceptibility or infectiousness, and what delivers STI treatment.

## Relevance to project

A design reference and a comparator, not a source of any number. canary-stis is built on
Starsim/STIsim, so nothing here is imported; what it supplies is the architectural precedent for
two choices the project already makes. First, that HIV and the curable STIs sit on a shared
sexual-network and demographic layer with disease-specific within-host state layered on top,
which is the same separation STIsim uses. Second, that the STI cofactor on HIV is implemented as
externally configured coinfection events modifying susceptibility and infectiousness rather than
as hard-coded biology.

The campaign framework is the closest published analogue to the project's SOC and POC arms: a
symptomatic care-seeking trigger routing to a diagnostic block with configurable sensitivity and
specificity, then to treatment, with the arm difference expressed as a swap of the diagnostic
block rather than a change to transmission code. Worth citing when justifying that arm design as
a recognised way to separate care-cascade structure from disease dynamics.

The paper's calibration discussion bears directly on the project's own plans. It names the
constraints as the number of free parameters, run time of minutes to tens of minutes per
simulation, and stochastic output requiring replicates to quantify, and calls automated
calibration an area of active development rather than a solved problem. It also states EMOD is
applied only in data-rich settings and is not re-fitted across all settings where a heuristic
might apply, which is the same posture as calibrating to Rakai first and generalising by argument.

## Limitations

Nothing here is evidence about HIV or STI epidemiology. The paper reports no parameter values,
no calibration targets, and no intervention effect sizes; every quantitative figure in it is a
line count or a test count (over 600 regression tests producing over 1,200 output files, over 140
scientific feature tests, as of March 2018). The line-count comparison is a proxy for development
effort, not for model fidelity.

It is also a self-description by the platform's own developers, published in 2018, so the code
structure it describes has moved on and the claims about testing discipline are unaudited. The
authors do concede that configurability costs usability, that becoming fluent in the model takes
weeks to months, and that EMOD is a poor choice where a compartmental model would do.
