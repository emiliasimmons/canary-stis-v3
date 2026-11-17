---
type: entry
title: "UNAIDS 2026 HIV estimates with uncertainty bounds, 1990-2025"
description: Country-year Spectrum estimates of HIV prevalence, ART coverage and viral suppression on ART, used for Zimbabwe's 2010 ART level and both countries' prevalence at 15-49 over time.
author: UNAIDS
published: 2026-07-27
resource: https://www.unaids.org/sites/default/files/2026-07/HIV_estimates_from_1990-to-present_1.xlsx
local: raw/unaids-2026-hiv-estimates/unaids-2026-hiv-estimates.xlsx
tags: [hiv]
updated: 2026-11-17 11:42
---

UNAIDS's annual release of national HIV estimates, produced by country teams with the Spectrum
model and fitted to surveys, antenatal surveillance and programme counts. Each estimate comes
with lower and upper bounds. The Zimbabwe and Eswatini rows used here are extracted to
`raw/unaids-2026-hiv-estimates/zimbabwe_eswatini_extract.csv`.

## Variables and coverage

- **HIV prevalence at 15-49** (sheet `HIV2026Estimates_ByArea`), 1990-2025.
  - Zimbabwe: 14.1% (2016), 12.1% (2020), 11.0% (2022), 9.3% (2025, bounds 9.2-9.5).
  - Eswatini: 30.2% (2016), 26.8% (2021), 22.4% (2025).
- **Percentage of people living with HIV aged 15+ on ART, by sex** (sheet
  `HIV-Test-&-Treat_ByArea`), from 2010. Zimbabwe, women/men:
  - 2010: 31/24 (bounds 26-36/19-29)
  - 2013: 52/49
  - 2016: 73/60
  - 2020: 91/85
  - 2025: above 98 / 90
- **Percentage on ART with suppressed viral load, by sex**, from 2016 for Eswatini and 2020
  for Zimbabwe.
  - Zimbabwe 2021: 94 (women), 93 (men).
  - Eswatini 2016: 92 (women), 91 (men).
  - Values above 98% are reported only as ">98".

## Denominator and population

All people living with HIV in the age band, as modelled by Spectrum. Coverage numerators are
national programme counts of people on treatment, so coverage inherits any double counting or
loss to follow-up in those registers. Values are published rounded to whole percentages.

## Relevance to project

The surveys give Zimbabwe ART coverage only for 2016 and 2020. UNAIDS's 2010 coverage (31%
women, 24% men aged 15+) sets the 2010 level of Zimbabwe's ART table. It is spread across age
bins with ZIMPHIA 2015-16's age pattern, as `src/data/coverage_construction.py` records. The
estimates agree with the surveys to within about 5%: ZIMPHIA 2015-16 gives 71% (women) and 63%
(men) at 15-64, and UNAIDS gives 73% and 60% for 2016.

The prevalence series answers what the medium-prevalence setting would see in Zimbabwe in 2026.
It extrapolates to about 9% at 15-49 in 2026, against the roughly 15% the
[settings decision](settings-prevalence-by-phase.md) asks for. Eswatini extrapolates to about
22%, against the high setting's roughly 25%.

## Limitations

These are model outputs fitted to the same surveys this project uses, so they are not
independent evidence for the survey years. Coverage before 2010 is not published. Sex-specific
coverage is reported for adults 15+ only, with no age split.
