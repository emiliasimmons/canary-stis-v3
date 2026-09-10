---
type: entry
title: "The role of high-risk geographies in the perpetuation of the HIV epidemic in rural South Africa"
description: Phylogenetic transmission links in rural KwaZulu-Natal concentrate on one peri-urban high-prevalence cluster, quantifying how much of a generalized epidemic's network runs through a small high-risk core.
author: Cuadros et al.
published: 2022-02-22
resource: https://doi.org/10.1371/journal.pgph.0000105
local: raw/10.1371/journal.pgph.0000105
tags: [hiv, sexual-networks, modeling]
updated: 2026-09-10 00:16
---

Spatial molecular epidemiology of HIV in the Africa Health Research Institute's population surveillance area (PIPSA) in Hlabisa, northern KwaZulu-Natal: a 438 km2 rural area of roughly 90,000 people. The authors combined 2011-14 population HIV surveillance (18,295 tested adults 15+, 5,624 HIV-positive), a 2004-14 seroconversion cohort (17,984 people, 2,311 seroconversions), and 1,426 HIV-1 subtype C *pol* sequences to ask how much of the transmission network passes through the area's single statistically identified high-prevalence zone. Extracted text at `raw/10.1371/journal.pgph.0000105`.

## Relevance to project

A quantitative anchor for the third pathway the project separates: the value of identifying high-transmission positions in the network rather than treating infections one at a time. It supplies a size for the effect in a generalized African epidemic, on geography rather than on individual risk behaviour, and the numbers are usable as a comparator, not as a calibration target (wrong country, HIV only, no STI data).

The transferable figures: a zone holding 7.5% of the area and 32% of the sampled population carried 40.8% of HIV-positive people, prevalence 39.1% (95% CI 37.9-40.4) inside versus 26.8% (26.0-27.6) outside, incidence 4.33 versus 2.85 per 100 person-years. 254 of 350 phylogenetic transmission links (72.6%) had at least one endpoint inside it. Mean node degree on the 3 km grid was 20 inside versus 5 outside, a four-fold connectivity ratio that is the closest thing here to a prior on risk-group degree heterogeneity in a rural generalized-epidemic setting. Their gravity microsimulation reproduced the observed link distribution with a 20% higher per-person probability of forming a link inside the cluster, which reads as a modest attractiveness multiplier rather than a core-group structure.

The paper also bears directly on the project's Rakai calibration site by contrast. It notes that the Rakai fishing-community work found under 11% of transmission links crossing between high-prevalence fishing communities and lower-prevalence inland communities, against 72.6% connectivity here. The authors attribute the difference to scale and design: Rakai spanned 40 communities across a region and mapped a migration network, this study mapped a contact network within one local community. Treat the two as measuring different things, and do not carry the 72.6% into a Rakai-parameterized model.

## Key points

- The high-risk zone is peri-urban, near the N2 highway, wealthier households, more adults aged 25-34. Over 50% of external in-migrants to the surveillance area settled there, and its incidence stayed among the highest for 15 years while incidence elsewhere fell by more than 70%.
- Node degree on the 3 km grid correlated with cell HIV prevalence at Pearson r = 0.69 (p < 0.005). The highest-prevalence nodes (34.6% to 47.7%) were also the highest-degree ones (17 to 44 links).
- Community detection found one central module of 11 nodes, 6 of them inside the high-risk zone. Nodes outside the zone were sparsely connected and reached each other mostly through that module.
- Mean distance between genetically linked individuals was 6.4 km. Only 6 links (1.7%) were within a household, and 29 seroconcordant couples sharing a household were not genetically linked, so most partnerships bridging space are not the resident couple.
- A parallel analysis of stable partnership formation gave 76% of partnership links touching the same zone, matching the phylogenetic pattern from independent data.

## Limitations

- Only 1,426 of 5,624 HIV-positive people (25.4%) were sequenced, sequencing was prioritized for viral load above 10,000 copies/ml, and 333 of 1,222 geolocated sequences fell in a phylogenetic cluster. A phylogenetic link is not a direct transmission; an unsampled intermediate is likely in most pairs.
- Clustering can favour people diagnosed early or engaged in care. The authors test this weakly: median time from first positive test to sequencing was 1.84 years for clustered versus 2.24 years for non-clustered individuals.
- No mobility data, so the gravity interpretation (the zone attracts partners) is inferred from fit rather than observed.
- 60% of contacted participants ever consented to testing, and HIV status is the most recent test result, which understates prevalence among the untested.
- Nothing on STIs, on diagnostics, or on any intervention actually delivered. The targeting argument is a claim about where an intervention would land, untested here.
