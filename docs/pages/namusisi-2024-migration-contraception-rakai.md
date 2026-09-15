---
type: entry
title: "The intersection between migration, HIV, and contraceptive use in Uganda"
description: RCCS round 15 cross-section of 3,417 sexually active women 15-49, giving condom-use prevalence by HIV serostatus and recent in-migrant status.
author: Namusisi et al.
published: 2024-05-17
resource: https://doi.org/10.1186/s12978-024-01796-z
local: raw/10.1186/s12978-024-01796-z
tags: [rakai, hiv, care-seeking]
updated: 2026-09-10 00:35
---

Source: [namusisi-2024](https://doi.org/10.1186/s12978-024-01796-z)

A cross-sectional analysis of Rakai Community Cohort Study survey round 15 (July 2011 to
May 2013, 30 agrarian and semi-urban trading communities in south-central Uganda), asking
whether recent in-migration and HIV serostatus interact to shape unmet demand for modern
contraception. The analytic sample is 3,417 sexually active women aged 15-49 who did not
intend to become pregnant in the next 12 months, drawn from 6,083 women in 10,960 R15
participants.

The primary outcome is unsatisfied contraceptive demand: non-use of pill, condom,
Depo-Provera, IUD, implant, or tubal ligation among women who wish to avoid pregnancy.
Poisson regression with robust variance, adjusted for age, education, marital status,
socio-economic status, religion, and occupation.

## Relevance to project

The usable output for this project is condom-use prevalence in the RCCS female population,
disaggregated in a way most Rakai papers do not report. Among sexually active women 15-49
with no pregnancy intention in R15, current condom use was 13.7% overall (468/3,417), and
split by serostatus and mobility: 12.7% in HIV-seronegative long-term residents, 20.8% in
seropositive long-term residents, 11.0% in seronegative in-migrants, 16.5% in seropositive
in-migrants. That is a prior for the condom-use fraction in the female half of the
partnership model, and a bound on how much protection to assume: even the highest stratum
is a fifth of women, on a yes/no survey question that carries no frequency or partner-type
information, so condom coverage cannot be treated as consistent use.

Second, it quantifies the mobility gradient in service contact for the calibration site.
Recent in-migrants (arrival within roughly 1.5 years, identified at household census) were
17.4% of the sample (595/3,417) and had 14% higher prevalence of unsatisfied demand
(adjPRR 1.14, 95% CI 1.02-1.27). Among women living with HIV, ART use was 40.8% in
long-term residents versus 16.5% in in-migrants. This supports treating recent in-migrancy
as a marker of reduced health-system contact when parameterising who reaches the
symptomatic care-seeking door that the SOC and POC arms share, though the paper gives no
STI-specific care-seeking rate.

Third, context on the population's composition in the R15 window: 17.3% of the sample were
living with HIV (591/3,417), 54% of those reported current ART use, and 70.6% were
currently married. Numbers are from 2011-2013 and the paper itself notes ART coverage in
this cohort later rose above 70%, so none of these should be carried forward to a
present-day baseline.

It supplies no STI outcome, no incidence, and no partnership-level data. It is not a
calibration target.

## Key points

- Unsatisfied contraceptive demand was 43.9% overall (1,500/3,417) including condoms, and
  57.2% excluding them.
- Women living with HIV had 20% lower unsatisfied demand than seronegative women (adjPRR
  0.80, 95% CI 0.70-0.90), an effect entirely produced by higher condom use: excluding
  condoms, the association disappears.
- Highest unsatisfied demand was in in-migrants living with HIV (48.7%), lowest in
  long-term residents living with HIV (36.6%). The migration-by-serostatus interaction was
  in the expected direction but not significant (adjusted 1.23, 95% CI 0.96-1.57, p =
  0.096), on 115 in-migrant women living with HIV.
- Depo-Provera was the most-used method at 29.4%, ahead of condoms at 13.7%; pill and
  implant were each about 5%.
- Among women living with HIV, unsatisfied demand did not differ by ART use (35.2% on ART
  versus 33.2% not, adjPRR 0.91, 95% CI 0.68-1.23).

## Limitations

Cross-sectional, so nothing here separates whether migration causes reduced service
contact or whether the women who migrate differ beforehand. Migration is binary and
internal, with no origin-destination detail and no cross-border movement; destinations are
predominantly rural RCCS communities. Contraceptive use was collected as yes/no per method
at the time of survey, which is why the condom figures cannot be read as coital-act
coverage. The in-migrant-and-seropositive cell has 115 women, which is what the null
interaction rests on. R15 was the last RCCS round with comprehensive fertility-intention
and contraceptive data, so the values are fixed at 2011-2013 and are already known to be
out of date on ART coverage.
