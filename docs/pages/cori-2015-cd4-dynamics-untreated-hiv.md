---
type: entry
title: "CD4+ cell dynamics in untreated HIV-1 infection"
description: Dutch ATHENA seroconverter cohort, giving mean time spent in each CD4 category before treatment (3.32, 2.70, 5.50 and 5.06 years) and a threefold spread in progression by set-point viral load
author: Cori et al.
published: 2015
resource: https://doi.org/10.1097/QAD.0000000000000854
basis: abstract
tags: [hiv, modeling]
updated: 2026-09-10 10:36
---

Analysis of the AIDS Therapy Evaluation in the Netherlands (ATHENA) cohort, restricted to people whose seroconversion date could be placed within one year and who had intensive clinical follow-up before starting treatment. CD4 trajectories were fitted with a monotonic spline separating a smoothed underlying decline from measurement noise, then summarised as time spent in four categories. Written from the published abstract; no full text is held on this machine.

## Key points

- Mean time in each CD4 category among untreated individuals: above 500 cells/ul, 3.32 years; 350-500, 2.70 years; 200-350, 5.50 years; 200 or below, 5.06 years. Summing the first three gives roughly 11.5 years from seroconversion to CD4 below 200.
- Only 76% of individuals were in the above-500 category immediately after seroconversion, so a quarter enter the CD4 cascade already below 500 and a model starting everyone at the top overstates early time in high-CD4 states.
- Set-point viral load drives progression. Individuals with set-point viral load of at least 5 log10 copies/ml reached CD4 below 200 in 5.37 years, against 15.76 years for those below 4 log10 copies/ml, roughly a threefold difference in the pre-AIDS interval.
- The stated purpose is to supply these as directly usable model parameters, with the recommendation that models stratify progression by set-point viral load rather than using a single decline rate.

## Relevance to project

The natural-history parameter set for untreated HIV progression in the model: category residence times for a four-compartment CD4 structure, plus the initial distribution across categories at seroconversion. Both are the kind of value that would otherwise be assumed. The set-point viral load stratification matters for this project specifically, because per-act infectiousness scales with viral load, so a model that ties both progression speed and infectiousness to the same set-point is coupling two quantities that are otherwise fitted independently.

It supplies nothing on STIs, nothing on transmission directly, and nothing on care-seeking. Its use is confined to the HIV disease-progression component.

## Limitations

- Written from the abstract alone. Confidence intervals, the covariate model, and the observation model are not available here.
- Dutch cohort, largely a European epidemic with a different subtype distribution and different comorbidity background from Rakai. CD4 decline rates in sub-Saharan African cohorts are not necessarily the same, and this study cannot show whether they are.
- Restricted to people with a seroconversion date known to within a year and with intensive pre-treatment follow-up, which selects for people diagnosed early and monitored closely.
- The untreated observation window shrinks over calendar time as treatment guidelines moved earlier, so the later CD4 categories rest on people who remained untreated when guidelines said they need not have been.
