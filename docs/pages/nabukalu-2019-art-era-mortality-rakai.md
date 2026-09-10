---
type: entry
title: Population-level adult mortality following the expansion of antiretroviral therapy in Rakai, Uganda
description: RCCS 2000-14 all-cause and HIV-positive mortality rates by sex and ART period, ages 15-49, across 30 communities
author: Nabukalu et al.
published: 2020
resource: https://doi.org/10.1080/00324728.2019.1595099
local: raw/10.1080/00324728.2019.1595099
tags: [hiv, rakai]
updated: 2026-09-10 00:31
---

Survival analysis of the Rakai Community Cohort Study over 2000-14, covering the 30 communities followed continuously across that window, published in Population Studies. Free ART reached the district in June 2004 through PEPFAR-funded Rakai Health Sciences Program clinics, and the paper splits its analysis at that date: pre-ART (Jan 2000 - May 2004) and ART (Jun 2004 - Dec 2014). It reports mortality rates by HIV status and sex, partial life expectancy between exact ages 15 and 50, and Weibull hazard models for people living with HIV. Extracted text sits in `raw/10.1080/00324728.2019.1595099`.

## Relevance to project

Supplies background (non-HIV) and HIV-attributable mortality rates for the RCCS calibration site, on the same population, age band, and calendar window the model targets. The HIV-negative death rate is close to flat across the whole 15-year period, 3.1 then 3.0 per 1,000 person-years for men and 2.3 then 2.2 for women, which makes it a clean non-AIDS background mortality rate for ages 15-49 in Rakai rather than something the model has to fit. The HIV-positive rates are the residual the model's HIV natural-history and ART modules have to reproduce: 101.0 (men) and 100.4 (women) per 1,000 pyo before ART, falling to 43.9 and 24.1 during 2004-14. Denominators are 20,924 and 22,822 person-years pre-ART and 67,403 and 72,432 during the ART period, for men and women.

The paper is about mortality only. It gives no STI data, no partnership structure, and no diagnostic performance, so it bears on the simulation's demography and the HIV death sink, not on the POC-versus-SOC comparison. One incidence number arrives secondhand: RCCS HIV incidence peaked in 2000 at 1.3 per 100 pyo and declined afterwards, cited from Grabowski et al. 2017 rather than estimated here, so use the original for a calibration target.

## Key points

58,871 individuals aged 15-49 contributed 183,581 person-years and 1,374 deaths. All-cause death rates fell from 11.9 to 6.4 per 1,000 pyo in men and 13.7 to 5.2 in women between the two periods.

Partial life expectancy between exact ages 15 and 50 (ceiling 35 years) rose from 26.4 to 33.5 years for women and 28.6 to 33.8 for men across 2000-14. Life-years lost to HIV, the gap between HIV-negative individuals and the whole population, fell from 8.1 years (95% CI 6.5-9.5) to 1.3 (0.3-2.5) in women and from 4.3 (2.9-5.7) to 0.4 (-0.4-1.3) in men.

Mortality among people living with HIV declined among those with no record of treatment as well as among the treated, reaching 16.8 per 1,000 pyo (untreated) and 10.5 (ever-treated) in 2013. Two mechanisms are offered: ART received at facilities the cohort could not link records with, and a progressively healthier untreated pool as eligibility widened (CD4 threshold 250 to 350 cells/uL in October 2011, then Option B+ lifelong ART for all HIV-positive pregnant women in September 2012).

Weibull hazard ratios per calendar year, 2004-08, are 0.72 (95% CI 0.67-0.77) for untreated women and 0.64 (0.57-0.71) for treated women, against 0.83 and 0.87 for the corresponding men. From 2009 the pattern reverses for the treated: 0.96 (0.79-1.16) for women, 0.73 (0.59-0.90) for men. The women-first advantage is attributed to earlier testing, earlier initiation, and PMTCT-driven eligibility.

Life-years lived began rising before ART arrived, partly from cotrimoxazole prophylaxis and partly because HIV incidence in Uganda peaked in the early 1990s, so AIDS mortality was already turning down by 2004. A model that attributes the whole 2000-14 mortality decline to treatment will overstate ART's effect.

## Limitations

Follow-up stops at age 50, so HIV mortality above that age is invisible. The authors expect this to bias the burden downward most for men, who acquire HIV at older ages.

Treatment status is ascertained only through record linkage to RHSP facilities. Other providers in the district could not be linked, so the "untreated" group contains an unknown share of people on ART, which compresses the treated-untreated contrast. Of HIV-positive RCCS participants, 7,436 (about 52%) were in RHSP care by December 2014, and 6,618 of those were known to be on ART.

Person-time before a first HIV test is a separate "status unknown" category, and time after a last negative test is imputed as HIV-negative for the interval over which 95% of that age group would be expected to remain uninfected. The unknown-status group's mortality tracks the whole population, which the authors read as evidence it is not strongly selected.

Estimates for people living with HIV are sensitive to when diagnosis happened, and the confidence intervals on their years lived are wide because of small annual death counts, around five deaths per year by 2014.
