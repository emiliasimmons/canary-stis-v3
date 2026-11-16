# Settings status

No experiment has run. The first experiment sets the agent count and replicate count from
the model's measured run time and run-to-run variance, through calib's `model-setup`
(story 18 on issue 1).

Questions that depend on simulation results, and are settled by experiments on this
track:

- What produces a mature or an expanding epidemic at the same prevalence: the HIV seed
  year, HIV programme timing and coverage (ART, VMMC, HIV testing), the network, or a
  combination.
- Which network parameters separate the settings. Risk-group proportions and concurrency
  are the first candidates. Issue 5 compares the Eswatini model's network inputs with this
  model's defaults.
- Which setting the shared STI transmission parameters are first set on, given that the
  current values were set by hand on the default network and moving the network moves STI
  prevalence.
- Whether the shared biology and care parameters are fixed at single values or explored
  over the same ranges for every setting. Fixed is the current lean.

Before the first exploration: the per-pathogen STI-to-HIV multipliers (issue 12), and the
model change that loads Eswatini and Zimbabwe demographics from UN WPP and moves the
simulation start year to 1985, the year of their age structure (settled on issue 6).
