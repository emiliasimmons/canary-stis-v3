---
type: entry
title: "Zimbabwe Population-based HIV Impact Assessment 2020 (ZIMPHIA 2020): Final Report"
description: Zimbabwe's second national household HIV survey with biomarkers, giving 2020 ART coverage including a 50+ band, viral suppression on ART, circumcision and prevalence at 15-49.
author: Ministry of Health and Child Care, Zimbabwe (PHIA Project, ICAP at Columbia University)
published: 2023-09
resource: https://phia.icap.columbia.edu/wp-content/uploads/2023/09/010923_ZIMPHIA2020-interactive-versionFinal.pdf
local: raw/zimphia-2020-final-report/zimphia-2020-final-report.pdf
tags: [hiv]
updated: 2026-11-17 11:41
---

The final report of ZIMPHIA 2020, a nationally representative household survey of adults aged
15 and older run from November 2019 to March 2020. It measured HIV status, viral load and
detectable antiretrovirals (ARVs) in blood. Of 22,751 eligible adults, 19,535 were interviewed
and tested. The version held here is the September 2023 revision, which corrected Table 11.5
and the related estimates in the executive summary.

## Findings

All values are survey-weighted percentages.

- **HIV prevalence at 15-49** (Table 6.1): 8.6% in men (n = 5,946), 14.8% in women
  (n = 9,088), 11.8% overall.
- **ART coverage among all people living with HIV** (Table 9.1.A). Diagnosis and treatment
  count self-report or detectable ARVs.
  - Men: 68.8% at 15-24, 58.0% at 25-34, 84.4% at 35-49, 90.1% at 50+, 80.9% at 15+.
  - Women: 73.4%, 79.7%, 89.5% and 92.5% in the same bands, 86.2% at 15+.
- **Viral suppression (below 1,000 copies/mL) among those on ART** (Table 9.1.B): 89.0% of men
  (n = 748) and 91.0% of women (n = 1,799) aged 15+. It runs from 71.5% in men aged 15-24
  (n = 44) to 97.2% in women aged 50+.
- **Male circumcision at 15+** (Table 12.5, self-reported): 19.2% medical, 3.9% non-medical.
  Medical circumcision reaches 37.4% at 15-19 and 30.8% at 20-24, and is 3.6% at 65+.
  Non-medical circumcision rises with age, to 10.0% at 65+.

## Relevance to project

Gives the 2020 rows of Zimbabwe's ART and VMMC coverage tables and Zimbabwe's 2020 suppression
among people on ART. Its 50+ ART band fills the [45,100) bin directly, the way SHIMS3's 50+
band fills Eswatini's. `src/data/coverage_construction.py` holds the transcriptions.

The prevalence at 15-49 (11.8% in 2020) is below the roughly 15% target that the
[settings decision](settings-prevalence-by-phase.md) sets for medium-prevalence settings, and
UNAIDS's series ([UNAIDS 2026 estimates](unaids-2026-hiv-estimates.md)) continues downward
past 2020.

## Limitations

Self-reported circumcision status. No ART age band between 35-49 and 50+, so the [45,100) bin
treats 45-49-year-olds as if they were 50+. Fieldwork ended as COVID-19 restrictions began.
