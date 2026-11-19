# Exp 44: Prevented fractions of HIV infections on the four settings' ensembles

**Question.** How much of SOC's HIV infections at 15-49 over 2027-2040 does each arm
prevent in each of the four settings, and how wide is the spread across each setting's 30
ensemble members? [001-quick](../001-quick/SUMMARY.md) ran the arms on six Zimbabwe draws
with one seed each, too few to separate contrasts of about 3% from zero.
[43](../../settings/43_delayed_epidemic_ensembles/SUMMARY.md) has since built 30-member
ensembles for the four settings. This experiment answers issue 44.

**Plan.** Every member of the four ensembles in
[ensembles.json](../../settings/43_delayed_epidemic_ensembles/ensembles.json), on its exp 43
random seed, runs eight arms: 10,000 agents, 1985 to the end of 2040, interventions from
2027. Seven arms are 001-quick's with idealized behavioral PrEP dropped: SOC, the POC panel
alone, with partner notification, with STI-triggered PrEP, with both, with STI screening at
HIV testing, and the Magic cure. Partner notification keeps 001-quick's 54% of partners
notified and 50% attending. The eighth arm, Magic PrEP, runs on SOC: every HIV-negative
person who acquires gonorrhoea, chlamydia, trichomoniasis or syphilis from 2027 on starts
PrEP the month after they are infected, whether or not the infection is ever diagnosed. It
uses STI-triggered PrEP's course (75% efficacy, full adherence, 3 months per start, a new
course on the next infection after one ends) with uptake raised from 30% to 100%. Magic PrEP needs a new PrEP
eligibility rule in `src/sim.py`. The experiment runs in two stages. Stage 1 runs these
eight arms with STI-triggered PrEP at 30% uptake (`prep.coverage` 0.30) and 3-month
courses (`prep.dur_months` 3): 4 x 30 x 8 = 960 simulations, about an hour on zebra at 80
workers (001-quick's 284 s per simulation). Stage 2 crosses STI-triggered PrEP's
`prep.coverage` 0.10, 0.30 and 0.90 with `prep.dur_months` 3 and 6 in both STI-triggered
PrEP arms, and adds Magic PrEP at `prep.dur_months` 6: 11 new arms and 1,320 more
simulations, appended to the same results. Each setting gets one figure in
the layout of 001-quick's Fig 4: each arm's prevented fraction against SOC, and the pathway
contributions as differences between arms, with members as dots over a box plot.

**Success criteria.** All 960 simulations finish and each setting's figure shows all eight
arms and the five pathway contributions. Thirty members with one seed each mix
member-to-member differences with seed noise, so a box that straddles zero says the
contribution is small against that spread, not that it is zero. Magic PrEP bounds what
routing STI-infected people into PrEP could prevent if every infection were found and every
offer accepted. A Magic PrEP fraction below STI-triggered PrEP's contribution in any setting
would point to an error in the new rule.
