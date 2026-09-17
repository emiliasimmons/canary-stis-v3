---
type: entry
title: "Canonical figures in HIV transmission modeling: a taxonomy with named examples"
description: A research agent's taxonomy of the figure archetypes HIV modeling papers reuse, each with its axes, encoding, and named exemplars, plus the field's plotting conventions.
author: Claude research agent
published: 2026-09-17
resource: raw/canonical-hiv-modeling-figures.md
local: raw/canonical-hiv-modeling-figures.md
tags: [modeling, hiv, sexual-networks, phylogenetics, prep, economics]
updated: 2026-09-17 11:08
---

The output of a Claude research agent asked what the canonical figures are in HIV
transmission modeling. It answers with fifteen figure archetypes, each given its axes, how
the data are drawn, the question it answers, the cues that make it recognizable, and named
papers that exemplify it, followed by the field's plotting conventions, a split by audience,
and six recommendations. The premise it argues is that the domain has a shared visual
grammar stable enough that a reader identifies a figure's type before reading its caption.

## Relevance to project

This is a reporting reference and a reading list. It supplies the conventional form for
calibration output, for contrasts between scenarios, for attribution of transmission across
groups, and for sensitivity and uncertainty, along with the papers that established each
form. Matching a convention makes results legible to the modeling audience that reviews
them, and departing from one becomes a deliberate choice.

Nothing in it is evidence about HIV epidemiology. Every epidemiological number it quotes is
secondhand from a paper the agent read, and several of its sources are preprints it flags as
provisional. Use it to locate the primary source and take the number from there.

## The archetypes

**Model fit and calibration.** Calendar year on the x-axis, usually 1990 to 2025, against
prevalence as a percentage, incidence per 100 or per 1000 person-years, or counts of people
living with HIV and on treatment. The model is a solid line with a shaded credible-interval
ribbon, and the empirical targets sit on top as discrete points with vertical error bars
carrying the survey confidence intervals. Panels by sex, and often by age band. The question
is whether the model reproduces observed epidemiology closely enough to be trusted for
projection. Recognizable by points with whiskers sitting over a line with a ribbon, paneled
men against women. Exemplars are the Thembisa provincial and national panels (Johnson,
Dorrington) and the EMOD-HIV panels in Moolla et al. 2023 (BMC Public Health), a five-model
comparison. Naomi (Eaton et al. 2021, JIAS) draws the estimate as a thick black dash with a
95% credible interval plus a narrower 80% posterior predictive interval against the survey
observations. Calibration targets in this literature come from DHS, the PHIA and ZIMPHIA
surveys, antenatal clinic sentinel surveillance, and Spectrum or EPP output.

**Counterfactual and intervention-impact projections.** Year on the x-axis, often running to
2030, 2040, or 2050, against incidence, new infections, or cumulative infections. A baseline
or status quo curve runs against one or more scenario curves, with the area between them
shaded as infections averted and the reference drawn dashed or grey. Recognizable by two or
more diverging curves with a shaded wedge, and by a no-ART or frozen-coverage reference.
Granich et al. 2009 (Lancet 373:48-57) is the field's founding elimination figure, plotting
universal test-and-treat driving incidence below the 0.1 per 100 person-years elimination
threshold. Eaton et al. 2012 (PLOS Medicine 9:e1001245) gives the no-ART counterfactual
across twelve models in its first figure and an intervention scenario (treatment at CD4 350
or below, 80% access, 85% retention) in its second. The Optima global model (Lancet HIV
2018) plots status quo against optimized budget allocation to 2030.

**Infections averted and percent reduction.** Scenario or subgroup on the x-axis against
infections averted, percent incidence reduction, or infections averted per unit of resource,
drawn as grouped or stacked bars, often with confidence whiskers and disaggregated by sex or
country. Njeuhmeli et al. 2011 (PLOS Medicine 8:e1001132) shows infections averted by sex
and country for voluntary medical male circumcision scale-up over 2011 to 2025, with the
headline that reaching and holding 80% coverage across 13 countries would avert 3.36 million
infections through 2025 at a cost of US$2 billion against net savings of US$16.51 billion.
Eaton 2012 reports person-years of ART per infection averted, ranging 6.3 to 18.7 across
models over 2012 to 2020. The PopART costing paper (Thomas et al. 2021, Lancet Global
Health) reports cost per infection averted.

**Transmission attribution.** Four sub-types: a stacked area or bar of the fraction of new
infections contributed by each risk group over time, a bar chart of the transmission
population attributable fraction by partnership type over 10-year and 30-year windows, a
matrix of transmitter age against recipient age, and a breakdown of sources by care-cascade
state (undiagnosed, diagnosed but not on treatment, on treatment but unsuppressed). The
question is which populations, ages, or cascade states drive onward transmission, which is
a different question from who acquires infection. Stone et al. 2021 (J Int AIDS Soc
24:e25650), the Key-Pop Model for South Africa, gives population and partnership
contributions to new infections and then 10-year and 30-year attributable fractions by
partnership type with 95% credible intervals: sex between female sex workers and their
paying clients contributed 6.9% (4.5% to 9.3%) of new infections in South Africa over 2010
to 2019, and sex between those clients and their non-paying partners contributed 41.9%
(35.1% to 53.2%). Maheu-Giroux et al. 2017 (JAIDS 75:517-527) decomposes Côte d'Ivoire the
same way, with female sex workers contributing 95% (91% to 97%) of infections over 1976 to
1985 falling to 19% (11% to 27%) over 2005 to 2015. Akullian et al. 2020 (Lancet HIV
7:e348-e358, EMOD-HIV for eSwatini) renders sources of transmission by treatment status and
by acute or early stage, alongside a figure of the shift in transmitter age, and reports
that even 100% treatment coverage within six months of infection would leave adult incidence
at 0.73 (95% CI 0.55 to 0.92) per 100 person-years in 2030 and 0.46 (0.33 to 0.59) in 2050.
Mishra et al. 2014 (Sex Transm Infect 90:19-25) is the methods reference that separates
acquisition from transmission. Phylogenetic work (Ratmann, Xi and colleagues) produces
visually similar age-source flows, estimating for example that 91.8% of infections in
15-year-old women came from men more than five years older.

**Care cascade and 95-95-95.** Cascade step on the x-axis (diagnosed, then on treatment,
then virally suppressed) against a percentage, drawn as a descending staircase of bars.
UNAIDS documents the denominator convention explicitly, where each 95's numerator becomes
the next 95's denominator. Cascades over time use stacked areas or grouped bars per year.
UNAIDS publishes the reference version in "Understanding measures of progress towards
95-95-95". Thembisa produces the South African national cascade, reaching 90-68-88 by
mid-2018. Ehrenkranz et al. 2021 (PLOS Medicine 18:e1003651) proposes a cyclical revolving
door cascade as a critique of the linear form.

**Structure schematics.** Boxes and arrows for natural history, running susceptible to
acute to chronic stratified by CD4 to AIDS, with diagnosed, on-treatment, and suppressed
care states alongside. Agent-based versions layer the within-host scale, the
disease-progression scale, and the sexual network. The question is simply which states and
transitions the model represents. Exemplars are the EMOD-HIV network diagram in the idmod
documentation, which shows per-agent disease states plus a contact network, Granich 2009's
first figure with infectivity by stage and Weibull survival, a multi-scale model for men who
have sex with men in PLOS One that panels the within-host, health-state, and network scales,
and the Starsim and STIsim presentation of an agent matrix with modular disease and network
components.

**Cost-effectiveness planes and acceptability curves.** On the plane, incremental effect
(quality- or disability-adjusted life years, or infections averted) runs against incremental
cost as a scatter of probabilistic draws, with a willingness-to-pay threshold line drawn
across it. On the acceptability curve, the willingness-to-pay threshold runs against the
probability that an option is cost-effective, one curve per comparator, summing to 1 across
mutually exclusive options. Exemplars are a Markov model of PrEP for men who have sex with
men in Japan (Scientific Reports 2022), which gives the plane, the curve, and a time-horizon
variation in one figure, a cost-effectiveness analysis of long-acting cabotegravir PrEP
(PharmacoEconomics Open 2025) against a $100,000 per QALY threshold, and a Thai PrEP
analysis (JIAS) showing 80% of scenarios cost-effective once restricted to higher-risk men.

**Sensitivity analysis.** Three distinct figures. A tornado ranks horizontal bars by
influence on the incremental cost-effectiveness ratio or another outcome, each bar spanning
the low-to-high range of one parameter around a base-case vertical line. A partial rank
correlation plot shows coefficients from Latin hypercube sampling as bars or dots, often
with a significance threshold, and sometimes traced over time. Probabilistic sensitivity
analysis appears as the scatter on the cost-effectiveness plane and as the acceptability
curve. Exemplars are a South African HIV vaccine tornado that colors bars by parameter
direction and shades the region that is not cost-effective at three times GDP per capita,
tornado diagrams on the cost-effectiveness ratio in the Thai and Kenyan PrEP analyses, and
correlation convergence plots in compartmental control-theory papers.

**Age-sex stratified incidence and prevalence.** Paneled lines or bars by five-year age band
and sex, sometimes age-sex pyramids of people living with HIV. Female curves peaking at a
younger age than male curves is the recognizable signature in generalized epidemics.
Exemplars are Thembisa's age-specific prevalence, which put 31% of South African women aged
25 to 49 as living with HIV in 2022, the age and sex output of Spectrum and AIM, and Naomi
output stratified by district, sex, and five-year age group.

**Uncertainty representation.** Credible intervals as shaded ribbons at 50, 80, or 95%, with
a posterior predictive interval sometimes added as a wider band, as Naomi does. Ensembles of
posterior trajectories drawn as spaghetti, and fan charts widening into the future. Models
calibrated by approximate Bayesian computation, such as HIV Synthesis and PopART-IBM, plot
the full ensemble of accepted parameter sets. The ten-model validation in Eaton et al. 2015
(Lancet Global Health) shades a 95% credible interval only for those models that produced
statistical uncertainty at all.

**Multi-model comparison.** One panel per output indicator, covering prevalence, incidence,
treatment coverage, AIDS deaths, proportion diagnosed, proportion suppressed, and proportion
circumcised, with one colored line per model over a common horizon under a shared status quo
scenario. Uncertainty ribbons are frequently dropped for readability, and the structural
spread between models stands in for uncertainty instead. Exemplars are Eaton 2012 with
twelve models for South Africa, Eaton 2015 validating ten models against a 2012 survey
(all ten under-projected the 18.8% prevalence the survey measured, and eight fell below its
95% confidence interval of 17.5% to 20.3%), Moolla et al. 2023 comparing EMOD, Goals, HIV
Synthesis, Optima, and Thembisa over 1990 to 2040 with the coefficient of variation as the
consistency metric, Taramusi et al. 2025 (African Journal of AIDS Research) running five
models for Zimbabwe to 2040 and spanning a 2023 incidence range of 2.0 to 3.3 per 1000
person-years, and Bansi-Matharu et al. 2025 (PLOS Medicine) comparing seven models on a
cascade of death for Zimbabwe, Malawi, and South Africa.

**Elimination and target tracking.** An incidence trajectory, or the ratio of incidence to
prevalence, against a horizontal threshold line: 0.1 per 100 person-years for elimination, a
90% incidence reduction against 2010, or a 2030 target marker. Granich 2009 established the
form. A Lancet HIV commentary asking how universal universal test-and-treat has to be
juxtaposes Granich's epidemic-control curve against Akullian's eSwatini curve, which reaches
no control for decades, both drawn on the same threshold. Stover et al. 2021 (PLOS Medicine,
the Goals model) projects the UNAIDS 2025 targets forward to 2030.

**Key-population stratified figures.** Separate calibration and impact panels for female sex
workers, men who have sex with men, people who inject drugs, and adolescent girls and young
women, usually on much higher prevalence axes than the general population. Thembisa's 2022
estimates put prevalence at 59% among female sex workers and 30% among men aged 18 and over
who have sex with men. Exemplars are the Stone 2021 panels, Mukandavire et al. 2018 (J Int
AIDS Soc 21:e25126) on key-population contribution in Dakar, and an individual-based model
comparison for people who inject drugs in New York. The DREAMS evaluations (Birdthistle et
al. 2022, PLOS Medicine) plot incidence in adolescent girls and young women over time with
95% confidence intervals, though those are empirical cohort trends.

**Geographic maps.** Choropleths of prevalence, incidence, treatment coverage, or unmet need
by district or PEPFAR planning unit, frequently in pairs, such as prevalence against
circumcision coverage, or the three 95s shown clustering geographically. Exemplars are the
Naomi district maps, the official UNAIDS and PEPFAR subnational estimation tool since 2020,
the paired prevalence and circumcision maps across 13 countries in Njeuhmeli 2011, and a
geospatial k-means clustering of the 95s in Zambia.

**Coverage against impact, and thresholds.** Coverage or effort on the x-axis against
infections averted, percent reduction, circumcisions per infection averted, or cost per
infection averted, with turning points marked. The DMPPT2 circumcision tool (Kripke and
colleagues, for eSwatini, Zimbabwe, and Zambia) plots circumcisions per infection averted by
age group, finding ages 20 to 29 and 20 to 34 the most efficient and the lowest cost per
infection averted, $870 in eSwatini, when circumcising ages 15 to 34. A model of long-acting
PrEP following HPTN 083 (Mitchell et al. 2023, Lancet Regional Health Americas) gives
infections averted by switching from oral tenofovir to cabotegravir among men who have sex
with men in Atlanta, with oral PrEP at roughly 28% usage averting 36.3% of infections over
2022 to 2026 against no PrEP. The easy-access PrEP analysis of Cambiano and Phillips (Lancet
2022) spans 3000 setting-scenarios keyed to the prevalence of viraemia above 1000 copies per
millilitre.

Probert et al. 2022 (Lancet HIV 9:e771-e780), the PopART-IBM analysis of HPTN 071, is
offered as a single paper carrying many of these archetypes at once. It is an individual-based
stochastic model calibrated by approximate Bayesian computation to 1000 accepted parameter
sets, and it shows predicted against observed trial effect (arm A predicted a 27% incidence
reduction, 6% to 42%, against 7% observed, while arm B predicted 29%, 10% to 43%, against
30% observed), four scenario trajectories to 2030 (continued PopART giving 58% lower
incidence in 2030 than the counterfactual, nationwide rollout 66%, discontinuation 11%),
panels by community and sex, cascade fit panels, the proportion of incidence arising from
acute and early infection, and the reproduction number by community. No scenario reached the
0.1 per 100 person-years threshold by 2030.

## Conventions

Empirical survey data are discrete points with error bars and model output is a continuous
line with a shaded interval, never the reverse. Credible intervals are shaded ribbons at 50,
80, or 95%, and multi-model plots sometimes drop the ribbons and let the spread between
models stand in for uncertainty, a substitution Bansi-Matharu 2025 states outright.
Prevalence axes are essentially always linear, and log scales appear only for quantities with
a wide dynamic range, such as viral load or incidence approaching elimination. Calibration
windows commonly run 1990 to 2025 and projections to 2030, 2040, or 2050, occasionally to
2100. Reference scenarios are dashed or grey and intervention scenarios saturated, with the
region between them shaded. Horizontal threshold lines mark 0.1 per 100 person-years for
elimination, the willingness-to-pay level on a cost-effectiveness plane, or three times GDP
per capita. Multi-panel grids are organized by indicator against scenario or setting, or by
sex and age band.

Audience changes the figure. Peer-reviewed figures are dense multi-panel calibration plus
counterfactual plus sensitivity, with explicit credible intervals and grayscale-safe
encoding, exemplified by Eaton, Stone, and Probert. Funder and donor figures are
single-message charts, color-forward with few intervals: cascade bars, infections-averted
bars, before-and-after budget splits from allocation optimization, and subnational maps for
PEPFAR planning. Internal diagnostics are calibration traces, posterior predictive checks,
correlation and tornado plots, and network-structure diagnostics, and they mostly live in
supplements and repositories rather than in papers.

## Standing

The taxonomy is the agent's own construction, and the conventions it states are inferred
from the papers it read rather than written down anywhere as a standard. Both are useful on
that basis. The named exemplars and their journal locations are the checkable part, and the
agent marks which of those it verified: figure numbers were confirmed for Stone 2021,
Granich 2009, Eaton 2012, and Njeuhmeli 2011, while for Akullian 2020 and Probert 2022 the
figure contents are described from full text with the figure labels unverified. Some cited
estimates come from preprints. Confirm any figure reference against the open-access version
before citing it.

The agent draws two distinctions that guard against misreading its own examples.
Phylogenetic source-attribution figures look like mechanistic attribution figures, answer a
different question, and rest on sequence data. And several evaluation figures that circulate
in the modeling literature are empirical cohort incidence trends with no model behind them.
