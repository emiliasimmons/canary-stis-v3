---
type: entry
title: "Likelihood-free estimation of model evidence"
description: ABC estimators for the marginal likelihood of each model separately, and the result that statistics sufficient for fitting two models need not be sufficient for comparing them.
author: Didelot et al.
published: 2011-03-01
resource: 10.1214/11-ba602
local: raw/10.1214/11-ba602
tags: [modeling]
updated: 2026-09-10 10:31
---

Statistical methods paper in Bayesian Analysis. It builds ABC estimators of model evidence
(the marginal likelihood) for each candidate model independently, so Bayes factors can be
formed as a ratio without a sampler that jumps between models, and then works out when a
summary statistic is safe to use for model comparison. Validated on a Poisson-versus-
geometric toy problem where the evidence is analytic, then applied to demographic models
fitted to human Y-chromosome microsatellite data. Extracted text sits in
`../raw/10.1214/11-ba602/`.

## Relevance to project

Bears on structural model comparison, if canary-stis ever asks which model variant the
Rakai data prefers rather than only what parameter values fit. It carries no
epidemiological content: no HIV, no STI, no rates, no targets.

The usable result is a warning about summary statistics. A statistic sufficient for
estimating the parameters of model M1 and also sufficient for model M2 can still be
insufficient for comparing M1 against M2, so a Bayes factor computed from it is wrong by
the ratio p(x | s(x), M1) / p(x | s(x), M2). Their worked case: with independent
observations from a Poisson and a geometric, the sum of the observations is sufficient for
each model on its own and useless for choosing between them, because it discards the
differing base measures. The remedy given is to embed both models in a larger model in
which they are nested; any statistic sufficient for that larger model is then sufficient
for the comparison. For exponential families this means the comparison statistic is the
concatenation of each model's sufficient statistics plus each base-measure term
`t_i(x)`.

Practically, any comparison the project makes between two versions of the STI-HIV model
using ABC-style distances over calibration targets is exposed to this, since prevalence and
incidence summaries chosen to fit each variant carry no guarantee of separating them. The
authors are candid that for realistic models, low-dimensional sufficient statistics for
comparison do not exist and one falls back on statistics believed informative.

## Key points

Model evidence under ABC is the normalising constant of the ABC-approximate posterior. It
can be estimated as the mean importance weight (Algorithm 4), which converges to the true
marginal likelihood as the tolerance goes to zero under mild continuity conditions.

Sampling parameters from the prior gives an unbiased evidence estimate whose variance is
dominated by a handful of large weights whenever the posterior is concentrated relative to
the prior. Their fix reuses an approximate posterior sample from ABC-MCMC, perturbs it
through a heavy-tailed kernel, and estimates the resulting proposal density from the
sample, at O(N^2) cost. In the SMC setting the evidence falls out of the sampler's own
normalising-constant estimate.

Estimating each model's evidence separately avoids the older approach of nesting all
candidates inside a metamodel with a model indicator and reading the Bayes factor off the
acceptance counts, which is stuck with rejection sampling and cannot exploit MCMC or SMC
exploration.

Jeffreys' reading of Bayes factors is quoted as the interpretation scale: 1-3 barely worth
a mention, 3-10 substantial, 10-30 strong, 30-100 very strong, above 100 decisive.

## Limitations

The population genetics application uses three summary statistics (number of distinct
haplotypes, mean variance in repeat number, mean effective heterozygosity) that the authors
state are sufficient neither for parameter estimation nor for model comparison, so their own
headline application does not meet the standard the paper sets.

Everything inherits the standard problems of Bayesian model comparison over a fixed finite
set of candidates, including sensitivity of the evidence to the priors on each model's
parameters.

No epidemic model appears anywhere in the paper.
