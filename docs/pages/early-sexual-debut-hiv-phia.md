---
type: entry
title: Association Between Early Sexual Debut and New HIV Infections Among Adolescents and Young Adults in 11 African Countries
description: PHIA cross-sectional analysis putting the adjusted odds of recent HIV infection at 2.65x for sexual debut before age 18, ages 10-24.
author: He et al.
published: 2024-06-15
resource: https://doi.org/10.1007/s10461-024-04343-w
local: raw/10.1007/s10461-024-04343-w
tags: [hiv, sexual-networks]
updated: 2026-09-10 00:24
---

A pooled analysis of Population-Based HIV Impact Assessment (PHIA) household surveys run in
sub-Saharan Africa between 2015 and 2019, asking whether first sex before age 18 predicts
*recent* HIV infection rather than prevalent infection. Eleven countries, 99,672 records
aged 10-24 (55,249 female, 44,423 male), carrying 2,687 prevalent cases and 104 recent
infections. Recency comes from a limiting-antigen avidity assay converted to incidence by
the Kassanjee estimator. Extracted text sits in `raw/10.1007/s10461-024-04343-w`.

## Relevance to project

A prior on the risk gradient the model's age-mixing and debut-age structure should
reproduce, not a calibration target. The headline 2.65 odds ratio is an adjusted
cross-sectional association pooled across eleven national populations, so it cannot be read
as a per-act or per-partnership hazard multiplier for a Starsim network. It bounds how
strong the debut-age effect can plausibly be once education, wealth, residence and country
are controlled: the 95% CI [1.5, 4.7] is wide enough that a simulated gradient anywhere in
that band is defensible.

More directly usable are the sex and age coefficients from the same model, which are
structural facts the model's network should generate rather than assume. Males have 0.24
times the odds of recent infection of females (95% CI [0.12, 0.48]), and each additional
year of age multiplies the odds by 1.32 (95% CI [1.23, 1.40]) across 10-24. Those two
numbers say the young-female incidence excess in this age band is large, and that incidence
climbs steeply through adolescence, both of which a risk-structured network with age mixing
has to reproduce before its STI-HIV interaction results mean anything.

The Uganda arm is national PHIA, not Rakai, so it is a comparator for the RCCS calibration
site rather than a source of targets for it. Uganda's recent-infection count in this age
band is 14 out of 12,948, which is too thin to calibrate anything against.

Nothing here touches STIs, diagnostics, or care-seeking. The paper never measures a
non-HIV STI.

## Key points

- Adjusted OR 2.65 (95% CI [1.5, 4.7]) for recent HIV infection given debut before 18, ages
  10-24, from survey-weighted multivariate logistic regression with country fixed effects.
- Wealth quintile, education, and urban residence are not significant at 95% in the same
  model. The debut effect survives their adjustment.
- Country effects are large relative to Zambia: Eswatini OR 2.60 (95% CI [1.20, 5.66]),
  Ethiopia roughly 96% lower odds.
- Population attributable fractions are consistently higher for males than females, because
  early debut is more prevalent in males everywhere except Ethiopia. Lesotho tops the male
  PAF at 45.6% (95% CI [20.5, 66.4]); Uganda tops the female PAF at 34.9% (95% CI
  [13.9, 55.2]).
- Early-debut prevalence itself ranges widely: above 50% among Lesotho males, below 15% in
  Zimbabwe, Ethiopia, and Eswatini.
- Weighted HIV prevalence ages 10-24 spans 0.63% (Cote d'Ivoire) to 7.41% (Eswatini), female
  above male in every country.

## Methodology

Survey-weighted logistic regression with country as a fixed effect, fitted in R with the
`survey` package. Missing covariates filled by multiple imputation by chained equations
(5 sets, predictive mean matching). The design deliberately excludes mediators (partner
number, condom use, duration of sexual activity) from the adjustment set, on the argument
that early debut causes them, so controlling for them would block the pathway being
estimated. That choice is what makes the 2.65 a total effect of debut age and not a direct
one, and it is the reason the estimate is larger than analyses that adjust for partner
counts.

PAF is computed from the country-specific early-debut prevalence and the single pooled odds
ratio, with Monte Carlo propagation of uncertainty in both. The odds ratio is therefore
assumed constant across all eleven countries; only prevalence varies.

Nine sensitivity analyses (imputation count and algorithm, inclusion of 10-14 year olds,
debut cutoff at 16/17/18, sex-stratified fits, sex-by-debut interaction, country prevalence
as covariate, censoring, MICE vs Amelia) leave the conclusion intact.

## Limitations

Only 104 recent infections carry the entire estimate, which is why the confidence interval
spans a factor of three and why the sex-stratified fit finds significance in females but
not males. The authors attribute the male null to power.

Debut age is self-reported, with recall and social-desirability bias in both directions, and
misreporting here is not plausibly independent of HIV status. Missingness was large enough
to exclude Tanzania's and Rwanda's young adolescents entirely (above 93% missing on the
debut indicator), and Rwanda is dropped from modeling anyway for a different sampling-weight
scheme. Ethiopia and Cote d'Ivoire lack the indicator in the 10-14 band.

Education is dichotomized to any versus none, which is close to uninformative above age 15.

The cross-sectional design means the exposure is measured after the outcome window in some
respondents. Temporal ordering rests on debut preceding a recent infection, which is likely
but unverified per person.
