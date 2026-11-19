# Exp 45: HPrev mature arms under Barker 2022 cofactors, with ANC testing as an arm

**Question.** How much of SOC's HIV infections at 15-49 over 2027-2040 does each arm
prevent in the HPrev mature setting when the HIV acquisition cofactors are
[Barker 2022](../../../docs/pages/barker-2022-hiv-risk-nonviral-stis-meta-analysis.md)'s
pooled risk ratios for women, and ANC testing is an intervention from 2027 rather than
a baseline service? [44](../44_ensemble_prevented_fractions/SUMMARY.md) found that every
arm's prevented fraction scales with the Magic cure's, which the cofactors set. In 44 the
acquisition cofactors were `connectors.hiv_ng.rel_sus_hiv_ng` = 1.2, `hiv_ct.rel_sus_hiv_ct` = 1.2,
`hiv_tv.rel_sus_hiv_tv` = 1.5 and `hiv_syph.rel_sus_hiv_syph` = 2.67 (stisim defaults, with
chlamydia raised from 1). Barker's pooled risk ratios of HIV
acquisition in women are gonorrhoea 2.81, chlamydia 1.49, trichomoniasis 1.54 and syphilis
1.67. This experiment answers issue 45.

**Plan.** The baseline changes in two ways for every arm. The acquisition cofactors take
Barker's values for women in both sexes (Barker's only pooled risk ratio for men is
syphilis's 1.77), and the transmission cofactors `hiv_ng.rel_trans_hiv_ng` and
`hiv_syph.rel_trans_hiv_syph` stay at 1.2. ANC HIV testing and
ANC syphilis screening are off for the whole run. Both changes move the epidemic before
2027, so stage 1 redraws the setting: 120 Eswatini draws from
[43](../../settings/43_delayed_epidemic_ensembles/SUMMARY.md)'s mature-cell ranges, each run
as SOC to the end of 2040 on 10,000 agents and one seed. The members are the first 30 draws
by index whose 2026 HIV prevalence at 15-49 lands within 3 points of the HPrev mature setting's 25% target, as 43 chose its own. 43
landed 66 of its 140 mature Eswatini draws (0.47), and at that proportion about 56 of 120
land. Stage 2 runs eleven more arms on each
member, with Magic PrEP at 12-month courses added after the first run:

- the POC panel
- the panel with partner notification at 54% notified and 50% attending, and at 90% notified and 90% attending
- the panel with PrEP offered on STI treatment at 30% uptake and 3-month courses, and at
  90% uptake and 6-month courses
- the panel with PrEP and notification, at 30% uptake and 3-month courses with 54% notified and 50% attending
- the ANC arm: the panel, plus ANC HIV testing and ANC syphilis screening from 2027, with
  the panel offered to women at the ANC HIV test
- the ANC + HIV testing arm: the ANC arm, with the panel also offered to women at every
  other background HIV test
- the Magic cure
- Magic PrEP at 3-month courses, and at 12-month courses

The ANC HIV test reaches only women not yet diagnosed with HIV, so diagnosed pregnant
women are never offered the panel at ANC. Starting ANC testing in a given year and
offering the panel at the ANC HIV test alone need changes to `src/sim.py`. That makes
120 + 11 × 30 = 450 simulations, about 25 minutes on zebra at 80 workers.

**Success criteria.** At least 20 of the 120 draws land, and the figure shows every arm's
prevented fraction against SOC and the contributions as differences between arms, with
members as dots over box plots. Fewer than 20 landing draws would mean the new baseline
shifted prevalence off the HIV beta range, to be moved before drawing again. The ANC + HIV
testing arm contains every ANC arm offer, so a prevented fraction below the ANC arm's by
more than seed noise, or a Magic PrEP fraction below the 30% PrEP arm's contribution,
would point to an error in the wiring.
