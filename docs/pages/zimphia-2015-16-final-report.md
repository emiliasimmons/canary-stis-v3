---
type: entry
title: "Zimbabwe Population-based HIV Impact Assessment (ZIMPHIA) 2015-2016: Final Report"
description: Zimbabwe's first national household HIV survey with biomarkers, giving 2016 ART coverage, viral suppression on ART, circumcision and prevalence at 15-49 by sex and age.
author: Ministry of Health and Child Care, Zimbabwe (PHIA Project, ICAP at Columbia University)
published: 2019-08
resource: https://phia.icap.columbia.edu/wp-content/uploads/2019/08/ZIMPHIA-Final-Report_integrated_Web-1.pdf
local: raw/zimphia-2015-16-final-report/zimphia-2015-16-final-report.pdf
tags: [hiv]
updated: 2026-11-17 11:41
---

The final report of ZIMPHIA 2015-16, a nationally representative household survey run from
October 2015 to August 2016. It interviewed and tested adults aged 15-64 and children, and
measured HIV status, viral load, CD4 count and detectable antiretrovirals (ARVs) in blood, so
treatment status does not rest on self-report alone. About 8,400 men and 10,200 women aged
15-49 were tested.

## Findings

All values are survey-weighted percentages. The unweighted denominators are in the report's
tables.

- **HIV prevalence at 15-49** (Table 6.3.A): 10.7% in men, 15.9% in women, 13.4% overall.
- **ART coverage among all people living with HIV**, as the product of the two conditional
  steps in Table 10.3.B. Diagnosed means self-reported positive or ARVs detected, and on
  treatment means self-reported ART or ARVs detected.
  - Men: 53.3% at 15-24, 45.6% at 25-34, 66.7% at 35-49, 63.4% at 15-64.
  - Women: 52.0% at 15-24, 62.7% at 25-34, 79.4% at 35-49, 71.0% at 15-64.
  - Men aged 25-34 have lower coverage than men aged 15-24, because 59.9% of HIV-positive men
    aged 25-29 were unaware of their status (Table 8.3.A).
- **Self-reported ART among all people living with HIV in 5-year bands** (Tables 8.3.A, 8.3.B).
  This is the only age split above 49.
  - Men: 74.4% at 50-54, 70.1% at 55-59, 84.4% at 60-64.
  - Women: 85.4%, 83.7% and 68.9% in the same bands.
  - At 15-64, self-report gives 58.9% (men) and 66.4% (women), about 7% below the
    ARV-adjusted values.
- **Viral suppression (below 1,000 copies/mL) among those on ART** (Table 10.3.B): 82.5% of men
  (n = 770) and 87.0% of women (n = 1,637) aged 15-64. It is lowest among men aged 15-24, at
  75.2% (n = 54).
- **Male circumcision at 15-64** (Table 15.5.A, self-reported): 11.8% medical, 2.3% non-medical,
  82.7% uncircumcised, 3.2% unknown. Medical circumcision is highest at 15-19 (22.9%) and falls
  to 2.6% at 60-64, which is where the national VMMC programme started in 2009 shows.

## Relevance to project

Gives the 2016 rows of Zimbabwe's ART and VMMC coverage tables for the medium-prevalence
settings, and Zimbabwe's 2016 suppression among people on ART. Table 10.3.B's age bands
(15-24, 25-34, 35-49) are the ones Eswatini's ART table uses, so the two countries' tables are
built the same way. The [45,100) band is not in Table 10.3.B. It is built from the self-reported
50-64 bands, scaled up by each sex's ARV-adjusted to self-reported ratio at 15-64.
`src/data/coverage_construction.py` records every transcription and step.

The prevalence at 15-49 is a survey value for 2016, ten years before the 2026 selection year in
the [settings decision](settings-prevalence-by-phase.md).

## Limitations

The survey stops at age 64, so nothing describes people aged 65 and older. Circumcision is
self-reported, and men misreport partial or traditional procedures. Treatment estimates for
men aged 20-24 rest on 37 unweighted cases. Fieldwork spans ten months, and the tables built
from it label the survey 2016.
