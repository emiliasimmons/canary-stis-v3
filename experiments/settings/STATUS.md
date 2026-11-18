# Settings status

Two ensembles serve the four cells under an interim arrangement, from
[40.1_peak_year_ensembles](40.1_peak_year_ensembles/SUMMARY.md). Each country has five
draws, all kept after 10 seeds each: Eswatini's mean 2026 HIV prevalence at 15-49 is
24.1-25.6% and Zimbabwe's 14.3-16.2%. Each draw serves its mature cell with `intv_year`
2027 and its expanding cell with `intv_year` at the peak year of its seed-averaged
incidence, 2003-2006 in Eswatini and 2008-2010 in Zimbabwe. The draws and both
intervention years are in [ensembles.json](40.1_peak_year_ensembles/ensembles.json), for
the decomposition track to run its arms on.

Eswatini now has its own HIV `beta_m2f` range of 0.010-0.020, where 91 of 200 draws land
at 22-28% HIV prevalence at 15-49 in 2026. Zimbabwe's draws are the landing draws of
[38.3](38.3_seed_year_lower_sti_beta/SUMMARY.md), at HIV `beta_m2f` 0.0069-0.0113.

The arrangement departs from the
[settings decision](../../docs/pages/settings-prevalence-by-phase.md) on three points:
phase is set by the intervention year, the expanding
cells intervene before 2027, and HIV `beta_m2f` differs by country. The decision page is
left unrevised while the arrangement is interim.

At each draw's peak year (2003-2006 in Eswatini, 2008-2010 in Zimbabwe), seed-averaged
prevalence at 15-49 is 15.6-24.3% in Eswatini and 10.4-14.9% in Zimbabwe, partly below
the 2026 prevalence cells of 22-28% (Eswatini) and 12-18% (Zimbabwe), and the interventions start before
or early in ART scale-up (both country tables are 0 in 2004). A country's peak-year cell
therefore differs from its 2027 cell in prevalence and ART coverage as well as
incidence.

The next approach on the same question slows the ART ramp-up explicitly, with a scalar
on the timing of each country's ART coverage table, and keeps the intervention in 2027.
`sim_pars` has no such parameter yet: `art.coverage` only replaces the table.

Choices for the next approach's design:

- How the scalar stretches the table's years, and the year the stretch is anchored at.
- Whether the scalar is drawn in a new batch or applied to 40.1's kept draws.

Figures follow the `figN_` naming in [experiments/CLAUDE.md](../CLAUDE.md).
