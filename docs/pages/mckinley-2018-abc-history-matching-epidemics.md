---
type: entry
title: "Approximate Bayesian Computation and Simulation-Based Inference for Complex Stochastic Epidemic Models"
description: Review of ABC variants and a worked failure of ABC-SMC on a 22-parameter, 18-output individual-based HIV model in Uganda, against history matching on the same model.
author: McKinley et al.
published: 2018-02-01
resource: 10.1214/17-sts618
local: raw/10.1214/17-sts618
tags: [modeling, hiv]
updated: 2026-09-10 10:29
---

Source: [mckinley-2018](https://doi.org/10.1214/17-sts618)

Review article in Statistical Science covering simulation-based Bayesian inference for
epidemic models: classic ABC with rejection, MCMC and SMC samplers, tolerance schedules,
summary statistics, generalised ABC, indirect inference and synthetic likelihood, then
emulation and history matching. The methodological argument is carried by a case study on
Mukwano, an individual-based stochastic microsimulation of heterosexual partnership
formation, sexual activity and HIV transmission fitted to a 25-year open cohort of about
18,000 people in rural Uganda. The two supplements (the tolerance bisection method, and
the ABC posteriors against the history matching depth plots) are not included.

## Relevance to project

A method-choice reference for calibrating a slow stochastic agent-based model against many
stratified targets at once, which is the situation canary-stis is in at Rakai. The case
study is the closest published analogue available: an individual-based HIV model on a
Ugandan cohort, 22 free inputs, 18 outputs matched simultaneously, 5-10 minutes per
simulation in the well-supported region and over 3 hours in poorly supported regions.

Three usable results. ABC-SMC on that model consumed 800,319 simulations over 11
generations and still did not reach the target tolerance: the per-generation acceptance
rate fell from 0.78 to 0.15, the final generation took nearly two days on a cluster, and
one output (`m1s`) sat far below the data with its tolerance asymptoting well above target.
History matching on the same model reached better fits in about 355,000 runs, under half
the ABC budget, and the wave-9 design points would have been accepted at 0.48 (mean
outputs) or 0.41 (individual replicates) under the generation-11 ABC tolerances, against
0.15 for ABC itself.

Second, the design guidance on matching multiple outputs. An intersection metric requires
every output inside its own tolerance and so rejects at a rate scaling with the number of
outputs; a union metric collapses them into one distance and lets some outputs fit badly
while the aggregate passes. Combining metrics defined on different scales is the hard part.
The paper's semi-automatic scheme sets each initial tolerance at the 50th percentile of the
simulated distances for that output, then picks the next generation's tolerances by
bisection so about half of the current particles would be accepted.

Third, the argument for running history matching before any posterior method. Implausibility
is on a meaningful scale because the denominator is the sum of emulator variance,
observation error variance and model discrepancy variance, so a cutoff of 3 has a
justification the ABC tolerance does not. It also gives a stopping rule: either the emulator
variance falls below the other uncertainty terms, or the whole input space is ruled
implausible, which says the model cannot fit the data.

The paper supplies no epidemiological parameters, priors or targets. Mukwano's own priors
and outputs sit in Andrianakis et al. (2015), not here.

## Key points

Under Wilkinson's reading, ABC with a fixed metric and tolerance is exact inference under
an assumed model error, so the tolerance ought to be specified in epidemiologically
meaningful terms in advance. Doing that requires committing to a form and magnitude for
model discrepancy, which the paper treats as the neglected uncertainty in calibration.

On replicates per particle, theory says convergence does not depend on the number of
simulations n. Bornn et al. show n=1 costs at most a factor of 2 against the optimum for
ABC-MCMC with uniform matching, and is optimal for plain rejection ABC, but that rests on
roughly constant run times, which epidemic simulators violate. ABC-MCMC chains at low n get
stuck; ABC-SMC tolerates low n better, which is why the case study used SMC with n=1.

History matching remembers: every wave reuses the emulators and implausibility cuts from
earlier waves, so ruled-out space is never retested. Most ABC implementations have no such
memory.

An output only needs to enter history matching at the wave where it can be emulated
accurately, so erratic outputs can be deferred until later waves shrink the space around
them.

In the Mukwano history match, the non-implausible region was about 10^-11 of the original
input volume, and no single simulation matched all 18 outputs simultaneously at target
tolerance even after 9 waves.

## Limitations

One case study, one model, one cohort. The ABC run was not taken to convergence, so the
comparison is between an unfinished ABC and a finished history match, which the authors
acknowledge: it is unclear whether ABC would have reached the same region given more
generations.

History matching returns no posterior. The authors position it as a precursor that seeds or
bounds a later inferential run, not a replacement, so a project needing credible intervals
still has to do the posterior step afterwards.

The depth plots and ABC posteriors disagree on several parameters (`mhag`, `fchc3`,
`hacr3`) and the paper cannot say which is right.

Emulation carries its own labour: design points, training, diagnosing emulator accuracy, and
enough user judgement that the authors call it harder to implement than vanilla ABC.
