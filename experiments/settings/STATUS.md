# Settings status

Two ensembles serve the four cells under an interim arrangement, from
[40.1_peak_year_ensembles](40.1_peak_year_ensembles/SUMMARY.md). Each country has five
draws, all kept after 10 seeds each: Eswatini's mean 2026 HIV prevalence at 15-49 is
24.1-25.6% and Zimbabwe's 14.3-16.2%. Each draw serves its mature cell with `intv_year`
2027 and its expanding cell with `intv_year` at the peak year of its seed-averaged
incidence, 2003-2006 in Eswatini and 2008-2010 in Zimbabwe. The draws and both
intervention years are in [ensembles.json](40.1_peak_year_ensembles/ensembles.json), for
the decomposition track to run its arms on.

The arrangement departs from the
[settings decision](../../docs/pages/settings-prevalence-by-phase.md) on three points:
phase is set by the intervention year, the expanding cells intervene before 2027, and
HIV `beta_m2f` differs by country (Eswatini 0.010-0.020, Zimbabwe 0.003-0.012). The
decision page is left unrevised while the arrangement is interim. At each draw's peak
year, prevalence is partly below its 2026 cell and ART is at or near 0, so a country's
peak-year cell differs from its 2027 cell in prevalence and ART coverage as well as
incidence.

[40.2_slower_art_ramp](40.2_slower_art_ramp/SUMMARY.md) tried keeping the intervention
in 2027 and slowing ART instead, stretching each country's ART table from 2004 by
`art_stretch` (`sim_pars` `art.stretch`) over 1-3. The stretch raises 2026 incidence
relative to the peak, to a seed-averaged 0.53-0.60 in Eswatini and 0.63-0.80 in Zimbabwe
for the best landing draws, against 0.27-0.48 in 40.1. But seed-averaged peaks stay in
2002-2007 and 2011-2016, so ART timing alone gives no expanding epidemic in 2027.

Issue 42 is the next experiment: what slows the epidemic's growth enough that incidence
peaks near 2027, with 2026 prevalence in each cell. ART timing is settled as a lever by
40.2. The draws with the highest 2026-to-peak proportion in 40.2 had low HIV `beta_m2f`
for their country and flatter epidemics (peak incidence 2.81-3.22 per 100 person-years in
Eswatini, 1.39-1.92 in Zimbabwe).

Choices for issue 42's design:

- Which levers to explore: HIV `beta_m2f`, `seed_year` later than 2000, the network's
  high-risk proportions, and whether `art_stretch` stays drawn alongside them.
- How a batch judges phase. Single-seed 2026-to-peak proportions overstated the seed
  average by up to 0.15 in 40.2, so a selection on phase needs a few seeds per draw.

Figures follow the `figN_` naming in [experiments/CLAUDE.md](../CLAUDE.md).
