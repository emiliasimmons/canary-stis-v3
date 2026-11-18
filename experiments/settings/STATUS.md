# Settings status

The parameter exploration closed on its third approach,
[38.3_seed_year_lower_sti_beta](38.3_seed_year_lower_sti_beta/SUMMARY.md). Its landing
draws fill both mature cells: 154 of 400 Zimbabwe draws land at 12-18% HIV prevalence at
15-49 in 2026, and 10 of 400 Eswatini draws at 22-28%. Neither expanding cell has a draw.
Seeding HIV in 1993-2000 instead of 1985 moved the median incidence peak only from about
2005 to 2008 (SUMMARY observation 2), and `seed_year` is dropped.

The lower STI ranges reach every STIPS band. Draws inside each band have chlamydia
`beta_m2f` 0.06-0.141, gonorrhoea 0.137-0.33, trichomoniasis 0.022-0.067 and syphilis
0.01-0.04 (SUMMARY observations 8-9).

The next experiment gives each setting its own HIV `beta_m2f` range. Eswatini lands only
at the top of 38.3's shared HIV `beta_m2f` range of 0.003-0.012, so its range extends
above HIV `beta_m2f` 0.012.
Reduced ART scale-up in the high-incidence setting may join the same experiment. Separate
HIV `beta_m2f` ranges depart from the
[settings decision](../../docs/pages/settings-prevalence-by-phase.md), which shares HIV
biology across the four settings, so the decision is revised alongside the issue.

Choices for the next experiment's design:

- Each setting's HIV `beta_m2f` range.
- Whether ART scale-up is reduced in the high-incidence setting, and by how much.

Figures follow the `figN_` naming in [experiments/CLAUDE.md](../CLAUDE.md). The
model-features figures (38.3's Fig 6 and 7) pool the network summary over landing draws
rerun with `run.py --network N`, in the six-panel layout of Emilia's "Select model
features" slide.
