---
type: entry
title: The Role of Viral Introductions in Sustaining Community-Based HIV Epidemics in Rural Uganda
description: RCCS round 13 partitions HIV incidence into household, intra-community and extra-community sources, and gives per-partnership transmission probabilities over an 18-month interval.
author: Grabowski et al.
published: 2014-03-04
resource: 10.1371/journal.pmed.1001610
local: ../raw/10.1371/journal.pmed.1001610
tags: [hiv, rakai, sexual-networks]
updated: 2026-09-10 00:34
---

Three independent analyses of the same Rakai Community Cohort Study survey round (RCCS R13, June 2008 to December 2009, 14,594 participants aged 15-49 in 8,899 households across 46 communities) asking where new HIV infections come from geographically: spatial clustering of seropositive households, phylogenetics of *gag* and *env* sequences from 1,099 ART-naive seropositive participants, and an egocentric transmission model fitted to self-reported partner locations. Extracted text and tables in `../raw/10.1371/journal.pmed.1001610`.

Overall HIV seroprevalence was 12.2% (1,786/14,594) and incidence 1.2 per 100 person-years (95% CI 1.0-1.3, 189 incident cases), with 70% coverage of the censused eligible population.

## Relevance to project

Two uses here, both for the Rakai calibration site.

Per-partnership HIV acquisition probabilities over an 18-month interval, usable as priors or as a check on the model's per-act transmission and partnership-duration parameters once discordant partnerships are aggregated to a partnership-level risk: 26.0% (95% CI 13.4%-43.0%) from an ART-naive HIV-incident partner, 15.3% (10.9%-20.6%) from an ART-naive seroprevalent partner, 1.1% (0.7%-1.7%) from a household partner of unknown serostatus, 1.3% (0.8%-2.0%) from a community partner of unknown serostatus, and from an extra-community partner of unknown serostatus 4.2% (3.0%-5.9%) for women versus 0.9% (0.3%-1.8%) for men. The incident-partner figure rests on nine household pairs, so treat it as a wide prior rather than a target.

Partnership mix as a network structure target. Of 11,992 recent partners reported by 9,520 participants HIV-seronegative at a prior visit, 63.0% were household partners, 19.5% intra-community extra-household, and 17.5% extra-community. Household partnerships were 99% marital or long-term consensual; extra-household partnerships were 95% non-stable. Reporting is sharply sex-asymmetric: 96.2% of women reported exactly one partner in the last 12 months versus 59.5% of men. 65.2% of extra-household partners were reported by unmarried people. These are directly comparable to the model's partnership-count and concurrency distributions on the risk-structured network.

The source of incidence decomposition (39.0% household, 39.5% extra-household, 21.4% unknown source) bounds how much of the HIV epidemic an intervention delivered inside one community can reach, which matters for interpreting the POC arm's effect size: an appreciable share of transmission arrives from partners the simulated population does not contain. The model has no explicit spatial or community structure and no mobility, so this is context, not a target: it tells you that a closed-population estimate of the STI-diagnostic effect on HIV incidence is an upper bound on what a community-scale rollout would achieve.

Nothing here bears on STIs. The paper measures HIV only, and there is no coinfection, care-seeking, or diagnostic content to draw on.

## Key points

Household clustering is strong and everything beyond it is weak. Living with a seropositive participant raised your own probability of being seropositive 3.2-fold (95% CI 2.7-3.7); living with an incident case raised your probability of being incident 10.8-fold (2.3-23.6). Outside the household the effect was 1.22 (1.14-1.29) at 10-250 m and 1.08 (1.00-1.17) at 250-500 m, with nothing significant beyond 500 m and no significant extra-household clustering of incident cases at all.

Transmission chains cross community lines. Of 95 phylogenetic clusters, 42 (44.2%) were pairs sharing a household; of the 53 that spanned households, 38 (71.7%) crossed community boundaries and 18 of those 38 also crossed geographic regions. Only 19.0% (209/1,099) of sequenced participants clustered with any other participant.

Among people infected by extra-household partners, 62.1% (95% CI 54.9%-69.7%) were infected by a partner living outside their community. Where the location was known (68% of cases), half of those partners lived outside Rakai District entirely. Women reporting an extra-community partner had 5.0-fold higher odds (2.2-14.1) of acquiring HIV from that partner than men who reported one.

ART on the index partner eliminated measurable risk. Among 29 at-risk people whose seroprevalent household partner was on ART for at least half the risk interval, one seroconverted; among the 27 whose partner was on ART for at least 60% of the interval, none did.

## Limitations

Partner locations and counts are self-reported, and the model attributes 21.4% of infections to unnamed sources, which is direct evidence of underreporting. The authors note that if unreported sources were split evenly between community and extra-community partners instead of following the observed distribution, the community share of extra-household transmission would rise from 38% to 45%. Simulated 10% underreporting and 10% misreporting of partner community status both produced median bias under 10% of the CI width.

Attrition was 30.9% in the interval before R13, and the people lost were younger, more often unmarried, and marginally more often male and seropositive, so the cross-community fraction is likely underestimated. Newly enrolling seropositives were counted as prevalent, understating the contribution of early infection. Male circumcision prevalence in RCCS (39.4%) exceeded the 2011 Uganda DHS figure (26.8%), so per-partnership risks may run low relative to the general population.

Phylogenetic clustering was sparse enough that transmission chains could not be reconstructed; the cluster counts describe genetic relatedness, not confirmed transmission events. Sequence yield fell with age (RR 0.988 per year, 95% CI 0.980-0.995).
