---
type: entry
title: "Geospatial and phylogenetic clustering of acute and recent HIV infections in Lilongwe, Malawi"
description: STI-clinic-anchored detection of 141 acute HIV infections, with 30% of cases resident in 0.8% of the catchment area and only two-person phylogenetic clusters.
author: Bell et al.
published: 2025-11-05
resource: 10.1371/journal.pgph.0005420
local: raw/10.1371/journal.pgph.0005420
tags: [hiv, sexual-networks, sti]
updated: 2026-09-10 00:17
---

Secondary analysis of the iKnow randomised trial (NCT02467439), which ran combination HIV
detection in two Lilongwe STI clinics from 2015 to 2019, nearly all enrolment at Bwaila,
the only free STI clinic in Lilongwe District. Participants were STI clinic attendees aged
18+, plus sexual partners and social contacts they referred. Acute HIV infection (AHI) was
a negative or discordant rapid serological test with HIV RNA above 5,000 copies/ml on PCR;
recent infection (RHI, roughly 4 months since acquisition) came from a Sedia LAg-avidity
assay among seropositives; everyone else seropositive was chronic (CHI). Household GPS
points came off locator forms, which were only collected for seronegative and serodiscordant
attendees, so people with post-acute infection have no location. PANGEA deep sequencing
gave whole genomes assembled with shiver. Extracted text in `raw/10.1371/journal.pgph.0005420`.

## Relevance to project

This is a comparator and a structural argument for the clinic door the POC arm sits behind,
not a source of parameters for the Rakai calibration. The design is exactly the geometry
canary-stis models: a symptomatic-STI care-seeking door used as the point of contact for
finding HIV. It supplies the yield side of that door in absolute terms: 823 people with HIV
among the STI clinic study population, of whom 141 acute and 30 recent, so 21% of HIV
detected at the clinic was early infection. That fraction is the reason the STI clinic door
matters for HIV prevention beyond the cofactor effect, and it is the number to hold against
whatever early-infection yield the model produces at the same door.

It also bounds one mechanism the project separates out. The paper's phylogenetics found no
cluster larger than two people, 14 pairs total, and zero phylogenetic linkage inside any
geospatial cluster. So the "identify high-transmission network positions" pathway is not
supported here as local, rapidly propagating chains discoverable from a clinic population:
of eight people with AHI phylogenetically linked to an opposite-sex partner, only one was
linked to another acute or recent case. Treat this as a caution on how much the network
targeting pathway can deliver from clinic-based detection alone, not as an estimate of the
early-infection contribution to incidence, which the study explicitly did not attempt.

Partner referral is the one place the numbers bear on a pathway the model omits. Nine of ten
male-female pairs were clinic-referral pairs, and those nine were every referral pair in
which both members had sequence data, so referral in this setting identified genuine
transmission partners with essentially no false positives. That is evidence about the value
of a partner-notification pathway, which canary-stis does not implement.

## Key points

- 141 AHI, 30 RHI, 652 CHI among 823 participants with HIV, 2015-2019, Bwaila STI clinic.
- 135/141 (96%) of AHI cases had household geolocation. Four spatial clusters (flexible scan
  statistic, alpha 0.1, ~500x500 m cells, denominator = residents aged 15-64 from a
  high-resolution settlement layer) held 40/135 (30%) of AHI residences in 1.2-1.7 km2 each,
  totalling 0.8% of the populated catchment and 31,000 people, 3.5% of the 15-64 population.
- 70% (94/135) of AHI cases lived in or within 250 m of five traditional authorities
  (Areas 23, 24, 36, 56, 57).
- Six spatial clusters of HIV-negative clinic attendees; four overlapped or abutted three of
  the four AHI clusters, read by the authors as shared risk and shared care-seeking rather
  than anything HIV-specific.
- Clusters held only 36/721 (5.0%) of mapped venues where people meet new partners, but all
  four sat within 500 m of the M1, S124, or Lilongwe Bypass, which connect to the two areas
  holding 128 venues.
- Space-time clustering was weak: 11/141 (8%) of AHI cases in 0.25% of populated land over
  111 days, despite a permissive alpha of 0.5.
- 14 phylogenetic clusters, all of size two, at <2% distance in gag or pol (or <4.5%
  whole-genome where gag-pol overlap was under 50%). Ten male-female, of which 9 referral
  pairs; four same-sex pairs with no referral link, possibly missing intermediaries.
  Referred partners attended within 23 days of each other.
- Sequences were essentially all subtype C.

## Limitations

Sampling is one STI clinic plus referred contacts, a partial slice of Lilongwe's sexual
network, and the authors say the study cannot quantify the contribution of acute infection
to city-wide incidence. Sequencing was prioritised toward AHI/RHI and referred partners
(237 samples attempted, 222 usable), so unreferred partners are systematically under-sampled
and the absence of long chains is partly a sampling result. Household location stands in for
transmission location, and the venue-and-road pattern suggests the two differ. Post-acute
cases have no household location at all, so the spatial analysis compares AHI against
HIV-negative attendees only. Cluster detection at 3-16 cases per cluster is low-powered, and
the ~1x1 km sensitivity analysis lost one of the four clusters. Malawi, subtype C, 2015-2019:
transporting the spatial efficiency numbers to Rakai's 30 rural and fishing communities is
not warranted.
