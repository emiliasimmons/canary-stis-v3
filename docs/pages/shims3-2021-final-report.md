---
type: entry
title: "Eswatini Population-based HIV Impact Assessment 3 2021 (SHIMS3 2021): Final Report"
description: Eswatini's third national household HIV survey with biomarkers, giving 2021 viral suppression among people on ART, ART coverage including a 50+ band, and prevalence at 15-49.
author: Ministry of Health, Eswatini (PHIA Project, ICAP at Columbia University)
published: 2024-11
resource: raw/shims3-2021-final-report/shims3-2021-final-report.pdf
local: raw/shims3-2021-final-report/shims3-2021-final-report.pdf
tags: [hiv]
updated: 2026-11-17 11:42
---

The final report of SHIMS3, a nationally representative household survey of adults in Eswatini
in 2021. It measured HIV status, viral load and detectable antiretrovirals (ARVs) in blood, and
reports the UNAIDS 95-95-95 cascade both conditionally and as proportions of all people living
with HIV. The PDF is the copy shipped with hivsim_eswatini.

## Findings

- **HIV prevalence at 15-49**: 15.6% in men (n = 3,771), 31.6% in women (n = 4,915), 23.7%
  overall.
- **Viral suppression (below 1,000 copies/mL) among those on ART** (Table 9.1.B, ages 15+):
  95.9% of women (n = 1,885) and 96.7% of men (n = 775). Among young people aged 15-24 it is
  90.4% (women) and 86.5% (men).
- **ART coverage among all people living with HIV** (Table 9.1.A, ages 15+): 93.1% of women,
  87.8% of men. At 50+: 96.6% (women) and 95.3% (men).

## Relevance to project

Gives the 2021 row of Eswatini's suppression among people on ART in
`src/data/eswatini_vls.csv`, for the high-prevalence settings. The 2016 row (91.8% women, 90.5%
men, SHIMS2 Table 10.3.B, ages 15+) is carried over from hivsim_eswatini's transcription,
because the SHIMS2 report is not held here. UNAIDS's 2016 estimate for Eswatini (92% and 91%,
[UNAIDS 2026 estimates](unaids-2026-hiv-estimates.md)) matches it to within 1%. The 50+ ART
band is the measured value that hivsim_eswatini already put in the [45,100) cell of Eswatini's
2021 ART coverage.

## Limitations

Suppression among those on ART is published by sex and broad age band only. Both rows of the
table count people as treated by self-report or detectable ARVs. SHIMS2's self-report-only
estimates differ from them by less than 1% at ages 15+.
