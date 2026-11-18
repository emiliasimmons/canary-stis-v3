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

Simulations start in 1985 and select their demographics with
`sim_pars(country=dict(name="eswatini"))` or `"zimbabwe"`: the 1985 age structure,
fertility, and mortality with HIV deaths removed, from UN WPP files in `src/data`
(`scripts/download_wpp.py`, `scripts/remove_hiv_mortality.py`). HIV is still seeded at the
simulation start.

Phase is judged from `sim.analyzers.hiv_incidence_15_49.annual()`: HIV incidence at ages
15-49 per 100 person-years by year, pooled and by sex. Prevalence at 15-49 is stisim's
`hiv.prevalence_15_49` result.

Before the first exploration: the per-pathogen STI-to-HIV multipliers (issue 12), the
model change that loads country ART and VMMC coverage and the four shared testing streams
(issue 18), and Zimbabwe's coverage data (issue 17).
