# Settings status

No experiment has run. The first experiment sets the agent count and replicate count from
the model's measured run time and run-to-run variance, through calib's `model-setup`
(story 18 on issue 1).

Questions that depend on simulation results, and are settled by experiments on this
track:

- What produces a mature or an expanding epidemic at the same prevalence and country
  setup: the HIV seed year, the network, or both. ART, VMMC and HIV testing are fixed by
  the country setup and shared testing streams.
- Which network parameters separate the settings, condom use included. Risk-group
  proportions and concurrency are the first candidates. Issue 5 compares the Eswatini
  model's network inputs with this model's defaults.
- How HIV is seeded.
- Which setting the shared STI transmission parameters are first set on, given that the
  current values were set by hand on the default network and moving the network moves STI
  prevalence.
- Whether the shared biology and care parameters are fixed at single values or explored
  over the same ranges for every setting. Fixed is the current lean.

To watch: each country's simulations fill only that country's cells, so a Zimbabwe
simulation reaching high prevalence is discarded. If many are, letting either country fill
either cell (with country recorded on each simulation) may be the better rule.

Before the first exploration: the per-pathogen STI-to-HIV multipliers (issue 12), the
model change that loads Eswatini and Zimbabwe demographics from UN WPP and moves the
simulation start year to 1985, the year of their age structure (issue 16), the model change
that loads country ART and VMMC coverage and the four shared testing streams (issue 18),
and Zimbabwe's coverage data (issue 17).
