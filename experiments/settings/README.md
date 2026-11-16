# Settings

The settings track builds the four hypothetical HIV epidemics the pathway decomposition
runs on: high (about 25%) or medium (about 15%) HIV prevalence at ages 15-49 in 2026, each
as a mature and as an expanding epidemic. The decomposition track runs its SOC and POC arms
on the ensembles this track selects.

A setting is the ensemble of simulations, selected from a parameter exploration, whose
prevalence and phase fall in its cell. Targets, tolerance and how phase is judged are in
the [settings decision](../../docs/pages/settings-prevalence-by-phase.md). STI biology,
HIV biology and STI care are meant to be shared across settings, with network structure
expected to drive most of the divergence between them. Each setting's curable-STI
prevalence is a reported check against sourced bands, starting from
[STIPS](../../docs/pages/grabowski-2022-stips-sti-burden-rakai.md) for Rakai.

Comparator epidemics for each cell are on issue 3, to be cataloged under issue 14.
