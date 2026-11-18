# Settings status

The first approach to the parameter exploration closed on its 60-draw pilot
([38_explore_parameters](38_explore_parameters/SUMMARY.md)). On the network, HIV and STI
ranges in its [config.yaml](38_explore_parameters/config.yaml), 9 of 30 Eswatini draws
land in the high cell, all as mature epidemics, and no Zimbabwe draw falls below 18.9%
HIV prevalence at 15-49 in 2026. Every draw carries 2026 syphilis prevalence at 15-49 of
25-45%, including at the lowest syphilis beta. Issue 38 stays open for the next approach.

What the next approach needs settled before it draws:

- An HIV `beta_m2f` range reaching down to Zimbabwe's target of 15% HIV prevalence at
  15-49 in 2026. The pilot's lowest `beta_m2f`, 0.0086, gave 19% in a Zimbabwe draw, and
  HIV `beta_m2f` drives 2026 prevalence more than any other parameter (rank correlation
  0.77 over the 60 draws).
- What can produce an expanding epidemic. HIV incidence at 15-49 takes off within three years of 1985
  in nearly every pilot draw, and `rel_init_prev` over 0.1-1.5 moves the peak earlier but
  barely moves 2026 prevalence.

Measured for planning: a simulation at 10,000 agents from 1985 to the end of 2026 takes
about 165 s, so 60 run in about 10 minutes on the laptop's 18 workers. A batch sized by
the issue's rule (about 30 landing draws in the hardest cell) goes to Coiled. The
experiment workflow covers VM runs only, so `run.py`'s dispatch and the return of results
to `outputs/` still have to be adapted for it.

The tools the next approach reuses are in `src/settings.py`: `setting_pars` builds a
draw's simulation with HIV seeded from the risk-group table, and `summarize` returns its
2026 outcomes and annual curves. STI prevalence at 15-49 is the `sti_prevalence_15_49`
analyzer.

To watch: each country's simulations fill only that country's cells, so a Zimbabwe
simulation reaching high prevalence is discarded. 3 of the pilot's 30 Zimbabwe draws
landed in the high cell.
