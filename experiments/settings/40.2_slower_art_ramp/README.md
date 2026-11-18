# Exp 40.2: Ensembles for the expanding settings, with a slower ART ramp-up and the intervention in 2027

**Question.** Which simulations make up the two expanding settings when ART scales up more
slowly than in the country tables, so that the intervention can stay in 2027?
[40.1](../40.1_peak_year_ensembles/SUMMARY.md) filled all four cells by intervening at
each draw's incidence peak, which left the expanding cells at lower prevalence (15.6-24.3%
in Eswatini, 10.4-14.9% in Zimbabwe) and with ART at or near 0. In 40.1's kept draws, 2026
incidence at 15-49 is 0.27-0.35 of its peak in Eswatini and 0.38-0.48 in Zimbabwe. This
approach to issue 40 keeps 40.1's draws for the mature cells and looks for expanding
epidemics in 2026 by stretching each country's ART coverage table in time.

Each table year becomes `2004 + s × (year − 2004)`, with coverage values unchanged, so ART
still starts from 0 in 2004 and `s` sets how fast it ramps. At `s = 2`, Eswatini's 2021
coverage (0.89 of women aged 25-34 with HIV) moves to 2038 and Zimbabwe's 2020 coverage
(0.80) to 2036. Eswatini's seed-averaged incidence peaked in 2003-2006, before most ART, so
a slower ramp is expected to raise incidence after the peak and prevalence in 2026 more
than to move the peak itself, and to change Zimbabwe's epidemics (peaks in 2008-2010) more
than Eswatini's.

This departs from the
[settings decision](../../../docs/pages/settings-prevalence-by-phase.md) as 40.1 does on
HIV `beta_m2f` differing by country, and on one more point: the two phases at one
prevalence level no longer share an ART table. A difference between a country's mature
and expanding cells then carries 2026 ART coverage as well as phase.

**Plan.** `sim_pars` gets the stretch as an ART parameter, through `tdd` then
`code-review`, with `s = 1` reproducing the country table. Two stages, both run on zebra.

1. Batch: 200 draws per country with `s` drawn uniformly over 1-3, alongside 40.1's
   ranges (Eswatini at HIV `beta_m2f` 0.010-0.020, Zimbabwe at 38.3's 0.003-0.012, and
   `seed_year` over 1993-2000 in both). At `s = 3` the 2011 and 2010 table rows fall in
   2025 and 2022, so 2026 ART coverage of women aged 25-34 with HIV is about 0.35 in both
   countries.
2. Replicates: among each country's draws landing within 3 points of its 2026 prevalence
   target (25% Eswatini, 15% Zimbabwe), the 5 with the highest 2026 incidence as
   a proportion of peak incidence, 10 seeds each, SOC arm, 10,000 agents, run to the end
   of 2026. A draw is kept when its seed-averaged 2026 prevalence is within 3 points of
   the target, and its phase is judged from its seed-averaged incidence curve.

At 40.1's mean of about 200 s per simulation with 80 workers on zebra, the batch of 400
simulations takes about 17 minutes and the replicates stage of 100 about 7 minutes. The
result is a table of kept draws, each written as `sim_pars` overrides with its `s` and
`intv_year` 2027.

**Success criteria.** At least 3 kept draws per country whose seed-averaged 2026 incidence
is at least 0.75 of its peak, against 0.27-0.48 in 40.1's kept draws. If Zimbabwe reaches
this and Eswatini does not, ART timing cannot slow a high-prevalence epidemic that peaked
before ART, and Eswatini's expanding cell needs issue 42's levers (a later seed or lower
HIV `beta_m2f`, with the prevalence that costs). If no draw in either country gets above
about 0.6 at `s = 3`, ART timing is too weak a lever on phase by itself.
