---
type: entry
title: "What's driving girls' adolescent marriage decline in Rakai, Uganda? The interplay between adolescent pregnancies and social determinants, 1999-2018"
description: RCCS trends in marriage, pregnancy, and sexual debut among girls 15-17 across 13 rounds, with the education-pregnancy-marriage mediation behind them.
author: Spindler et al.
published: 2024-07-29
resource: https://doi.org/10.1080/02673843.2024.2384863
local: raw/10.1080/02673843.2024.2384863
tags: [rakai, sexual-networks]
updated: 2026-09-10 00:29
---

Repeat cross-sectional and panel analysis of 15- to 17-year-old girls in the Rakai Community
Cohort Study (RCCS), 13 survey rounds spanning 1999-2018 across the 30 continuously followed
communities: 6,998 observations from 5,169 girls for the trend and association models, and a
1,104-girl panel (two or three rounds each) for a causal mediation analysis of pregnancy as
the pathway from education to marriage. Extracted text at `../raw/10.1080/02673843.2024.2384863/`.

## Relevance to project

Context and a bound on the youngest age band the model represents, not a calibration target.
Two things it supplies concretely.

Sexual debut in the 15-17 female band moved a long way over the calibration window: the share
ever having had sex fell from 62% (round 6, 1999-2000) to 23% (round 18, 2016-2018), pooled
40.8% never had sex, 19.1% debut at 12-14, 21.9% debut at 15-17 across all 6,998 observations.
A network model that holds debut age fixed while simulating 1999 through 2018 will misplace the
entry rate of adolescent girls into partnerships by roughly a factor of two over that span. Same
window, marriage under 18 fell 24% to 6% and pregnancy under 18 fell 28% to 8%. Whether the
model needs a time-varying debut hazard here is a scope call, but the size of the drift is the
number to weigh it against.

The RCCS design figures bear on any target drawn from this cohort: ~95% of those present at
survey participate, but ~25% of censused residents are absent at each round for work, school, or
travel, and adolescents typically stay in the open cohort for only one to three rounds (77% of
these girls appear in one round only). Absence and short residence are not random with respect
to partnership formation, and the authors note newly married 15-19-year-olds often move to a
different community, so this cohort loses them.

It gives no STI or HIV incidence figures, no partnership-count or concurrency distributions, and
no adult-age behaviour. It cannot support a network parameter directly.

## Key points

Education dominates the marriage association. Girls with lower secondary schooling or above had
91% lower odds of being married than girls with lower primary or none (aOR 0.09, 95% CI
0.07-0.12), adjusted for age and time, and the estimate is unchanged in the full multivariable
model. Secondary schooling rose from 35% to 54% of the band over the period.

Pregnancy and marriage are near-inseparable in these data (aOR 39.59, 95% CI 31.12-50.36,
adjusted for age and time), and the conditional probability of being married given a current or
prior pregnancy stayed between 68% and 52% across rounds with no trend. Marriage declined
because pregnancies declined, not because pregnancy stopped leading to marriage.

The mediation puts 31.5% of the education effect (risk ratio scale) through lower pregnancy:
natural direct effect aOR 0.28 (95% CI 0.11-0.61), natural indirect effect aOR 0.55 (95% CI
0.42-0.72).

Orphanhood was above 50% before 2004 and fell to 21% by 2018 after the regional HIV treatment
rollout, but carried no independent association with marriage in the multivariable model.

## Limitations

Marriage is measured from self-report by 15-17-year-olds rather than the standard
retrospective report from 20-24-year-old women, so the series is right-censored: a girl
interviewed at 15 and not seen again contributes no information about marrying at 16 or 17.
Prevalence is therefore an underestimate and is not comparable to DHS child-marriage figures for
Uganda. Under-reporting may also have grown over time, since Uganda's 2007 age-of-consent reform
criminalised sex with a minor.

The panel restricts to girls followed across rounds with unambiguous pregnancy-then-marriage
ordering, which selects against exactly the girls who out-migrate to marry. Pregnancy was not
measured in round 17 (2015-2016), so that round drops from the multivariable models.
