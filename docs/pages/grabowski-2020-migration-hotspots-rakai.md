---
type: entry
title: "Migration, hotspots, and dispersal of HIV infection in Rakai, Uganda"
description: RCCS census data on migration rates, HIV prevalence by migration status, and the finding that fishing-community hotspots receive rather than export infection.
author: Grabowski et al.
published: 2020-02-13
resource: https://doi.org/10.1038/s41467-020-14636-y
local: raw/10.1038/s41467-020-14636-y
tags: [rakai, hiv, sexual-networks]
updated: 2026-09-10 00:34
---

Source: [grabowski-2020](https://doi.org/10.1038/s41467-020-14636-y)

Analysis of two consecutive Rakai Community Cohort Study rounds, R15 (Aug 2011 to May 2013)
and R16 (Aug 2014 to Jan 2015), covering 38 communities: 27 agrarian, 7 trading, and 4 Lake
Victoria fishing. It characterizes who migrates, how far, what their HIV status is, and
whether the high-prevalence fishing communities seed infection into the surrounding inland
population.

The headline result reverses the usual hotspot assumption. Migrants moving *into* fishing
communities carry high HIV prevalence, while out-migration from those communities is
geographically scattered and contributes almost nothing to the inland burden.

## Relevance to project

The main use here is context and a bound on the closed-population assumption. The model
runs a single risk-structured network with no in- or out-migration, and this paper puts a
number on what that leaves out at the intended calibration site: 29% of the 22,901
participating adults aged 15-49 migrated into or out of a study community over roughly two
years, at 10.9 out-migrations and 10.1 in-migrations per 100 person-years. In-migrants
accounted for 685 of 1,197 (57%) newly detected HIV cases at R16, against 162 (14%) true
incident cases with a prior negative test. A closed model calibrated to RCCS *newly
detected* cases would badly overstate local incidence, so incidence targets must come from
the seroconverter denominator, not from first-positive tests.

Second, it is a source of community-stratified HIV prevalence for setting the model's
risk-group structure. Prevalence runs 9-26% in agrarian communities, 11-21% in trading, and
38-43% in fishing, with methods giving means of ~12%, ~14%, and ~42%. If the network gets a
high-activity stratum standing in for fishing communities and sex work, this is the
prevalence contrast that stratum has to reproduce.

Third, a caution on where a POC diagnostic arm would find people. HIV-positive in-migrants
of both sexes report ART use less often than long-term residents: 27% vs 43% in men
(adjusted PRR 0.74, 95% CI 0.56-0.97) and 36% vs 61% in women (adjusted PRR 0.67, 95% CI
0.57-0.78) at R16. Care contact is systematically worse in exactly the mobile group that
carries the most undiagnosed infection, which argues against assuming uniform care-seeking
across risk groups.

It gives no STI data at all, and no partner-level or sexual-network structure. It is not a
calibration target for anything the model tracks directly.

## Key points

Migration peaks in the early 20s and is more common in women: 25% of women out-migrated
between rounds vs 22% of men, and 24% of R16 women were in-migrants vs 19% of men. In-migration
rates by community type (median per 100 person-years): trading 16 (IQR 11-18), fishing 13
(IQR 12-15), agrarian 7.2 (IQR 6.4-8.6).

HIV prevalence is elevated among female migrants, not male. Age-adjusted prevalence among
female in-migrants was 1.64 times that of long-term residents in agrarian communities (95%
CI 1.39-1.92), 1.25 in trading (0.95-1.65), and 1.08 in fishing (0.93-1.26). No significant
migrant-resident difference in men. HIV-positive women were 1.33 times more likely to
out-migrate than HIV-negative women after adjusting for age and community type (95% CI
1.19-1.49); HIV-positive men were not (adjusted PRR 0.97, 0.83-1.13).

Hotspots absorb rather than export. Out-migrants from the two fishing sub-districts
accounted for at most 1.3% of HIV cases in any of the nine inland sub-districts (median
0.4%, IQR 0-1.1%). In-migrants arriving at fishing sub-districts had 35.0% prevalence if
they came from inland and 30.6% if from another fishing sub-district, against 34.0% among
resident adults there.

Prevalence among female in-migrants to fishing communities does not rise with time since
arrival, implying they arrived infected. Among male in-migrants it rises from 18% to 39%
over two years (p = 0.006), implying acquisition after arrival.

Migrants into fishing communities come from further away: median 48 km from origin (IQR
33-84) vs 18 km for both trading (IQR 6-44) and agrarian (IQR 7-42).

## Limitations

Migration is measured from household census at two points three years apart, so short-term
and circular mobility is invisible, and the community boundaries are RCCS-defined, meaning
some counted "migrations" are hyperlocal moves. In-migrants have unknown infection duration,
so the 57% figure is newly *detected*, not newly acquired. ART use is self-reported;
validation against plasma drug levels gave 99% specificity and 76% sensitivity. Survey
participation was lower among out-migrants (59%) than residents (64%) or in-migrants (67%),
though inverse-probability weighting did not move the prevalence or ART estimates. The
authors do not claim generalizability beyond the Lake Victoria basin.
