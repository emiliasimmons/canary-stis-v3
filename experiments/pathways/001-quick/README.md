# Exp 001: All eight arms on six Zimbabwe draws

**Question.** What do the eight arms of the
[pathway decomposition](../../../docs/pages/pathway-decomposition-arm-design.md) look like
side by side in one setting, as material for a first set of pathway plots? The arms have
not yet been run together on settled settings. This is a quick look ahead of the settings
ensembles, with no experiment issue.

**Plan.** The mature Zimbabwe setting: the 6 of
[38.3](../../settings/38.3_seed_year_lower_sti_beta/SUMMARY.md)'s 154 landing Zimbabwe draws
whose 2026 HIV prevalence at 15-49 is closest to 15%, each with its 38.3 random seed. Each
draw runs all eight arms with the same seed, 10,000 agents, 1985 to the end of 2040, with
the POC arms, behavioral PrEP, and the Magic cure starting in 2027. Partner notification
reaches 54% of current stable and casual partners, the median for STI notification in
low- and middle-income countries
([Alam 2010](../../../docs/pages/alam-2010-partner-notification-developing-countries.md)),
and half of those notified attend
([partner notification synthesis](../../../docs/pages/partner-notification-pathway.md)).
Every other arm setting is the model default. Each simulation saves annual trajectories
over the whole run, at ages 15-49 and by sex: HIV and the four STIs' incidence,
prevalence and new infections, PrEP starts and users, and STI infections treated, split by
symptom status. 48 simulations at about 280 s each (38.3's 211 s to 2027, scaled to 2041)
take roughly 30 minutes on 8 cores.

**Success criteria.** All 48 simulations finish and the figures show each arm's HIV and
STI trajectories and each pathway's prevented fraction of HIV infections at 15-49 over
2027-2040, with the draw-to-draw spread. Six draws with one seed each cannot separate a
pathway smaller than seed noise from zero, so a prevented fraction whose draws straddle
zero is a reason for more seeds, not a null result.
