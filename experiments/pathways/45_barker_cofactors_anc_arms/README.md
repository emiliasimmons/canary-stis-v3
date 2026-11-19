# Exp 45: HPrev mature arms under Barker 2022 cofactors, with ANC testing as an arm

**Question.** How much of SOC's HIV infections at 15-49 over 2027-2040 does each arm
prevent in the HPrev mature setting when the HIV acquisition cofactors are
[Barker 2022](../../../docs/pages/barker-2022-hiv-risk-nonviral-stis-meta-analysis.md)'s
pooled risk ratios for women, and ANC testing is an intervention from 2027 rather than
a baseline service? [44](../44_ensemble_prevented_fractions/SUMMARY.md) found that every
arm's prevented fraction scales with the Magic cure's, which the cofactors set. The model
ran stisim's defaults: gonorrhoea 1.2, chlamydia 1.2, trichomoniasis 1.5, syphilis 2.67.
Barker gives 2.81, 1.49, 1.54 and 1.67. This experiment answers issue 45.

**Plan.** The baseline changes in two ways for every arm. The acquisition cofactors take
Barker's values in both sexes (Barker pools a value for men only for syphilis, 1.77), and
the transmission cofactors for gonorrhoea and syphilis stay at 1.2. ANC HIV testing and
ANC syphilis screening are off for the whole run. Both changes move the epidemic before
2027, so stage 1 redraws the setting: 120 Eswatini draws from
[43](../../settings/43_delayed_epidemic_ensembles/SUMMARY.md)'s mature-cell ranges, each run
as SOC to the end of 2040 on 10,000 agents and one seed. The members are the first 30 draws
by index whose 2026 HIV prevalence at 15-49 lands within 25% ± 3, as 43 chose its own. At
43's landing fraction of 0.47 about 56 draws land. Stage 2 runs ten more arms on each
member:

- the POC panel
- the panel with partner notification at 54% notified and 50% attending, and at 90% and 90%
- the panel with PrEP offered on STI treatment at 30% uptake and 3-month courses, and at
  90% uptake and 6-month courses
- the panel with PrEP and notification, at 30% and 3 months with 54% and 50%
- the ANC arm: the panel, plus ANC HIV testing and ANC syphilis screening from 2027, with
  the panel offered to women at the ANC HIV test
- the ANC + HIV testing arm: the ANC arm, with the panel also offered to women at every
  other background HIV test
- the Magic cure
- Magic PrEP at 3-month courses

The ANC HIV test reaches only women not yet diagnosed with HIV, so diagnosed pregnant
women are never offered the panel at ANC. Starting ANC testing in a given year and
offering the panel at the ANC HIV test alone need changes to `src/sim.py`. That makes
120 + 10 × 30 = 420 simulations, about 25 minutes on zebra at 80 workers.

**Success criteria.** At least 20 of the 120 draws land, and the figure shows every arm's
prevented fraction against SOC and the contributions as differences between arms, with
members as dots over box plots. Fewer than 20 landing draws would mean the new baseline
shifted prevalence off the HIV beta range, to be moved before drawing again. The ANC + HIV
testing arm contains every ANC arm offer, so a prevented fraction below the ANC arm's by
more than seed noise, or a Magic PrEP fraction below the 30% PrEP arm's contribution,
would point to an error in the wiring.
