# Settings status

The parameter exploration closed on its second approach,
[38.2_lower_hiv_beta_and_seed](38.2_lower_hiv_beta_and_seed/SUMMARY.md). Its landing
draws are the two mature settings, and the next experiment fills the two expanding ones.

The next experiment adds an HIV `seed_year`, the year HIV first enters the simulated
population. Every simulation now seeds HIV on 1 January 1985, so by 2026 each epidemic has
had 41 years to grow, peak and decline, and a mature epidemic is the default outcome.
Seeding later, say in 1998, gives a younger epidemic in 2026 that may still be rising or
only recently past its peak. 38.2 tried a smaller 1985 seed for the same purpose, and it
mostly let HIV die out (SUMMARY observations 4 and 7).

The other parameter ranges stay at 38.2's. Its late-starting epidemics reached Zimbabwe's
target of 12-18% HIV prevalence at 15-49 in 2026 inside them, but none reached Eswatini's
22-28% (observation 10), so the pilot checks that Eswatini draws with a late seed still
land.

Choices for the next experiment's design:

- Whether `seed_year` is drawn as a fourteenth explored parameter or fixed at a few values.
- The seed size at `seed_year`, large enough that HIV doesn't die out (observation 4).
- What counts as a recent peak. The settings decision leaves this to the experiments, and
  observation 7 has the closest draw so far.

Figures: settings experiments need a model-features figure for a few landing draws per
country, one figure file per country, covering age at sexual debut, risk-group
composition, condom use by partnership type, age pairing, lifetime partners and new
partners in the last year. 38.2's results don't record the network, so it has none. Ask
Emilia for the reference figure and its code before writing it.

Open: Zimbabwe's mature epidemic at 12-18% HIV prevalence at 15-49 in 2026 has 22 landing
simulations against the 30 planned. Either 22 is enough, or about 130 more Zimbabwe draws
on 38.2's ranges bring it to 30.
