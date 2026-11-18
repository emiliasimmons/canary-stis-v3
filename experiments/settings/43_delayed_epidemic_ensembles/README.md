# Exp 43: 30-draw ensembles for the four settings, with the high-incidence cells delayed

**Question.** Which 30 simulations make up each of the four settings, when every cell is
intervened in 2027 and the high-incidence cells come from an HIV epidemic started later?
[40.1](../40.1_peak_year_ensembles/SUMMARY.md) stood the expanding cells in by intervening
at each draw's 2003-2010 incidence peak, which put them at lower prevalence and near-zero
ART. [40.2](../40.2_slower_art_ramp/SUMMARY.md) slowed ART alone and left the peaks in
2002-2016. Here each high-incidence draw moves its HIV seed and its HIV programmes (ART,
VMMC and HIV testing) later by one drawn delay `d`, so it runs a 40.1-style epidemic and
response shifted in calendar time. PrEP is unaffected, since every PrEP arm starts with
the 2027 intervention.

**Plan.** One batch on zebra: one seed per draw, 10,000 agents, 1985 to the end of 2026,
SOC arm, over 40.1's ranges (HIV `beta_m2f` 0.010-0.020 in Eswatini and 0.003-0.012 in
Zimbabwe, `seed_year` 1993-2000, no ART stretch).

- Mature cells: no delay, 100 Eswatini and 125 Zimbabwe draws.
- High-incidence cells: `d` drawn uniformly over 17-23 years, 150 draws per country. The
  model gains a delay that adds `d` to `seed_year` and moves the ART, viral suppression
  and VMMC coverage tables and the HIV testing ramp years later by `d`.

A draw lands when its 2026 HIV prevalence at 15-49 is 22-28% (Eswatini) or 12-18%
(Zimbabwe). Each cell's ensemble is its first 30 landing draws by draw index, written to
`ensembles.json` as `sim_pars` overrides. Batch sizes give a 95% chance of 30 landing
draws per cell, from landing fractions of 0.46 (40.1, Eswatini), 0.35 (40.2 at
`art_stretch` 1-1.5, Zimbabwe), 0.27 (delayed, Eswatini) and 0.26 (delayed, Zimbabwe). The delayed
fractions come from reading 40.1's Eswatini batch and 38.3's Zimbabwe batch at 2026 − `d`.
At 40.1's 200 s per simulation with 80 workers, the 525 simulations take about 25 minutes.

**Success criteria.** 30 landing draws in every cell, with the high-incidence draws'
incidence peaks mostly in 2020-2028 and their 2026 incidence a higher proportion of peak
than the mature draws'. Demography and the STI programmes stay on calendar years, so
a high-incidence cell short of 30 means those inputs change the shifted epidemic more than
the estimate allows. A second batch sized from this one's landing fraction then fills it.
Peaks mostly before 2020 call for a longer delay.
