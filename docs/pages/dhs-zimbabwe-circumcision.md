---
type: entry
title: "Zimbabwe DHS 2005-06, 2010-11 and 2015: men circumcised, by age"
description: Self-reported male circumcision by 5-year age group from three Zimbabwe DHS rounds, giving the pre-programme circumcision level for Zimbabwe's VMMC table.
author: DHS Program (ICF) and Zimbabwe National Statistics Agency
published: 2015
resource: https://api.dhsprogram.com/rest/dhs/data?indicatorIds=HA_MCRC_M_MCC&countryIds=ZW&breakdown=all
local: raw/dhs-zimbabwe-circumcision/HA_MCRC_M_MCC_age.csv
tags: [hiv]
updated: 2026-11-17 11:42
---

Values of DHS indicator `HA_MCRC_M_MCC` (percentage of men who report being circumcised) for
Zimbabwe, retrieved from the DHS Program API by 5-year age group for the ZW2005DHS, ZW2010DHS
and ZW2015DHS surveys. The retrieved rows are stored in the local CSV.

## Variables and coverage

The percentage circumcised, by 5-year age group from 15-19 to 50-54, with no split between
medical and traditional providers. Ages 15-49 overall:

- 2005-06: 10.3% (n = 6,849)
- 2010-11: 9.1% (n = 7,104)
- 2015: 14.3% (n = 8,018)

Before the programme the age profile is flat, at 8-14% in every group in 2005-06. By 2015 the
15-19 group has risen to 22.6%.

## Denominator and population

All men interviewed in the men's questionnaire, aged 15-54. No confidence intervals were
returned by the API.

## Provenance

Household surveys by the Zimbabwe National Statistics Agency with ICF. Fieldwork for 2005-06
and 2010-11 straddles the year boundary, and the API labels each round with its first year.

## Relevance to project

Sets the 2005 and 2010 rows of Zimbabwe's VMMC table, before and just after the national VMMC
programme began in 2009. The 2005 row is also carried back to 1990 as the pre-programme level.
DHS 2015 (14.3% at 15-49) matches ZIMPHIA 2015-16's medical plus non-medical total (14.3%), so
the DHS and PHIA instruments can be joined into one series.

## Limitations

Self-reported, and no survey age band covers boys 10-14 or men 55-64, so those bins are carried
from neighbouring bands. The roughly 10% circumcised before the programme is high next to
ZIMPHIA's 2.3% non-medical circumcision. Older men report a medical provider for circumcisions
done before the programme, so the provider split is not a clean programme measure.
