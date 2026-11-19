# Settings status

The four settings have 30-member ensembles, from
[43_delayed_epidemic_ensembles](43_delayed_epidemic_ensembles/SUMMARY.md), in
[ensembles.json](43_delayed_epidemic_ensembles/ensembles.json). Every cell intervenes in
2027. The mature cells use 40.1's ranges unchanged. The high-incidence cells move each
draw's HIV seed, ART and viral suppression tables, VMMC table and HIV testing ramps later
by the drawn `hiv_delay`, 17-23 years. Members' incidence at 15-49 peaks in 2017-2026 in
the Eswatini high-incidence cell and 2019-2026 in the Zimbabwe one. Members' median 2026
incidence as a proportion of peak is 0.82 (Eswatini high-incidence), 0.98 (Zimbabwe
high-incidence), 0.29 (Eswatini mature) and 0.36 (Zimbabwe mature). These
ensembles replace 40.1's interim arrangement of intervening at each draw's peak year.

The decomposition track runs its arms on the four ensembles with
`setting_pars(draw, country, sim=dict(stop=2040), intv_year=2027)`.

Each member ran on one seed. In 40.1, a draw's single-seed 2026 HIV prevalence at 15-49
sat up to 1.2 percentage points from its 10-seed mean, so members near a cell edge may leave it on other seeds.

The [settings decision](../../docs/pages/settings-prevalence-by-phase.md) still describes
phase as judged from the incidence curve and HIV biology as shared. It needs revising on
three points: phase is set by `hiv_delay`, the drawn `hiv_beta_m2f` range differs by
country (Eswatini 0.010-0.020, Zimbabwe 0.003-0.012), and the high-incidence cells intervene at ART coverage
of 0-0.23 among women aged 25-34 with HIV, against 0.80-0.89 in the mature cells.

Open threads:

- RPR-positive syphilis prevalence at 15-49 in 2026 is 19.6-21.8% (cell medians), above
  the STIPS band of 0.8-11.5%.
- If behavioral PrEP becomes a baseline from 2017 (issue 29), its start in the
  high-incidence cells moves by `hiv_delay`.

Figures follow the `figN_` naming in [experiments/CLAUDE.md](../CLAUDE.md).
