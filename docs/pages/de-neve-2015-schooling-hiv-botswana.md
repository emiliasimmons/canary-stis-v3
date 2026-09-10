---
type: entry
title: "Length of secondary schooling and risk of HIV infection in Botswana: evidence from a natural experiment"
description: Instrumental-variable estimate that one extra year of secondary schooling cuts cumulative HIV risk by 8.1 percentage points, with a cost per infection averted benchmarked against circumcision, treatment as prevention, and PrEP.
author: De Neve et al.
published: 2015
resource: 10.1016/S2214-109X(15)00087-X
local: raw/10.1016/s2214-109x(15)00087-x
tags: [hiv, prep]
updated: 2026-09-10 00:25
---

Natural-experiment study using Botswana's January 1996 secondary-school reform, which moved grade ten from senior to junior secondary and raised average attainment by about 0.79 years, as an instrument for years of schooling. Outcome is HIV serostatus at survey in the Botswana AIDS Impact Surveys II (2004) and III (2008), pooled analytic sample 7018 (3965 women, 3053 men), Botswana citizens aged 18 and over born in or after 1975 with a valid HIV test. Cohorts born in 1981 or later are treated as exposed. Extracted text and tables sit in `raw/10.1016/s2214-109x(15)00087-x`.

## Relevance to project

A cost-effectiveness comparator, and context on which structural gradient drives HIV risk in a generalised epidemic. The paper's Table 4 assembles cost per HIV infection averted across established interventions in southern Africa: medical male circumcision $551 and $1096, treatment as prevention at CD4 350 or above $8375, PrEP $12,500-20,000 and $6000-66,000, secondary schooling $27,753 (all US$, from the cited source years 2006-2012). That row set is the natural scale on which a POC STI test-and-treat panel's cost per HIV infection averted would be judged. The paper's own DALY arithmetic, an HIV infection at age 20 costing 16.3 lifetime DALYs without ART and 3.5 with ART, at a lifetime treatment cost of $12,400, gives a reusable conversion from infections averted to DALYs for this project's economic framing.

Not a calibration target and not a parameter source. The exposure is schooling, which the model does not represent, the setting is Botswana rather than Rakai, and the outcome is cumulative prevalence at survey rather than incidence. Its bearing on model structure is indirect: risk heterogeneity across a socioeconomic gradient in this population is large and causal, at 8.1 percentage points per school year against a 25.5% pre-reform baseline, which supports keeping a risk-structured network in the model even though this paper supplies no coefficient for it.

## Key points

Two-stage least squares, instrumenting years of schooling by reform-cohort membership, gives an 8.1 percentage point reduction in cumulative HIV risk per additional year of schooling (SE 3.1, p=0.008) in the pooled sample, against 25.5% prevalence in the pre-reform 1980 birth cohort. Women: 11.6 points (SE 5.8, p=0.046) against a 32.3% pre-reform baseline. Men: 5.0 points (SE 2.9, p=0.085) against 16.8%. The sex difference is not statistically distinguishable. First-stage effects of the reform on years of schooling were 0.64 (women), 1.01 (men), 0.79 (pooled), with 2SLS F statistics of 8.6, 9.5, and 18.0.

Intention-to-treat effects of reform-cohort membership on HIV status were -7.4 points in women (p=0.017), -5.0 in men (p=0.052), -6.4 pooled (p=0.002).

The crude cross-sectional association is non-monotonic: HIV prevalence peaks at 8-9 years of schooling and falls thereafter. Each year beyond 9 was associated with 3.6 points lower risk (SE 0.4); below 9 years there was no association (0.3 points, SE 0.2). The instrumented estimate is larger than the covariate-adjusted one, which the authors attribute to unobserved traits correlated with both attainment and risk biasing OLS downward.

Robustness checks on the pooled 8.1-point estimate stayed in the -5.2 to -9.1 band across sampling weights (-7.8), imputed HIV status (-9.1), IVProbit marginal effects (-5.2), quadratic and slope-change birth-year trends (-7.3, -7.9). A placebo restricted to respondents with fewer than 9 years of schooling, the group the reform could not have affected, gave -1.9 (SE 5.9), while the complementary group with 9 or more years gave -7.2 (SE 2.3).

## Limitations

Estimates are local in four ways the authors name: to grades 10-12, to compliers (people who would otherwise have left after ninth grade, a high-risk group), to a hyperendemic setting, and to risk exposure during the 1990s and early 2000s. Respondents are observed only to age 32, so infections averted cannot be separated from infections delayed. HIV test participation was 61% (2004) and 67% (2008), though consent rates did not vary with reform exposure and results survived imputation. The difference-in-differences specification returned a similar point estimate (-14.7) with a standard error of 23.1, so it corroborates direction only. The cost-effectiveness ratio charges the entire per-pupil cost of secondary schooling ($2248 per year, UNESCO 2005 and 2007) against HIV infections alone and excludes all other returns to education, and it excludes transmission spillovers to people outside the reform cohorts.
