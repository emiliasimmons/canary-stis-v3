---
type: synthesis
title: The STI-HIV cofactor and the HIV reduction achievable by clearing curable STIs
description: Curable STIs raise per-act HIV transmission, but observational cofactor ratios overstate the incidence reduction from clearing the four bacterial STIs, and the attributable ceiling in a mature epidemic is 3-17%.
tags: [coinfection, hiv, sti]
updated: 2026-09-14 21:35
---

Curable STIs raise the per-act risk of HIV transmission. The observational risk ratios,
which compare HIV acquisition in STI-positive against STI-negative people, do not measure
the HIV incidence reduction that clearing the four curable bacterial STIs the model tracks
(gonorrhoea, chlamydia, trichomoniasis, syphilis) would produce. The achievable reduction
is smaller than those ratios imply: three of the four pathogens are non-ulcerative and
carry little or no per-act effect once genital ulcer disease is separated out, the ratios
mix the biological effect with the higher-transmission network position an STI-positive
person already occupies, viral load dominates transmission and absorbs the STI signal when
it is adjusted for, and in a mature epidemic most transmission occurs in partnerships
where clearing an STI changes little. The direct-treatment channel of the POC arm should
be bounded accordingly.

## Measured cofactor estimates

The largest per-act estimate is for ulcerative disease. [Boily
2009](boily-2009-heterosexual-per-act-hiv-risk.md) puts genital ulcer disease in the
susceptible partner at a 5.29-fold (1.43-19.58) increase in per-act infectivity, against
a cofactor-free asymptomatic value near 0.07% per act, while non-ulcerative STI without
ulceration gives 1.11 (0.30-4.14), indistinguishable from no STI. [Patel
2014](patel-2014-per-act-hiv-transmission-risk.md) gives GUD 2.65 (1.35-5.19) and is
explicit that this is ulceration as a syndrome, covering HSV-2 and syphilis, saying
nothing about the discharge-causing pathogens. Of the four STIs the model carries, only
syphilis is ulcerative, and it is the least prevalent of the four in Rakai (high-titre
1.4% inland, [Grabowski 2022 STIPS](grabowski-2022-stips-sti-burden-rakai.md)).

The per-pathogen ratios that exist for the non-ulcerative STIs are incidence-rate ratios
over months of follow-up, not per-act probabilities, and come mostly from female sex
worker cohorts. [Barker 2022](barker-2022-hiv-risk-nonviral-stis-meta-analysis.md), which
required the STI diagnosis to precede HIV, pools women's risk ratios at gonorrhoea 2.81,
trichomoniasis 1.54 and chlamydia 1.49 over follow-up averaging 5.5 months in a population
that is 84% non-OECD and mostly female sex workers. [Jia
2022](jia-2022-hiv-risk-scores-ssa.md) pools an adjusted hazard ratio of 1.45 for curable
STIs in all-age women and 2.14 in adolescent girls and young women, and states these are
prognostic associations confounded by shared risk behaviour. [Hayes
2010](hayes-2010-sti-treatment-hiv-prevention.md) gives the older meta-analytic figure, an
adjusted odds ratio of 3.9 for any laboratory-documented STI, ulcerative (2.8) above
non-ulcerative (1.7), and notes these per-follow-up estimates understate the per-contact
effect.

| Source | Cofactor estimate | What it measures | Population |
|---|---|---|---|
| [Boily 2009](boily-2009-heterosexual-per-act-hiv-risk.md) | GUD 5.29 (1.43-19.58); non-ulcerative 1.11 (0.30-4.14) | per-act infectivity | pooled, mostly pre-2001, not general-population SSA |
| [Patel 2014](patel-2014-per-act-hiv-transmission-risk.md) | GUD 2.65 (1.35-5.19) | per-act, GUD as syndrome | high-income-weighted |
| [Barker 2022](barker-2022-hiv-risk-nonviral-stis-meta-analysis.md) | GC 2.81, TV 1.54, CT 1.49 (women) | incidence-rate ratio, ~5.5-month windows | mostly FSW, SSA |
| [Jia 2022](jia-2022-hiv-risk-scores-ssa.md) | curable STI aHR 1.45 (women), 2.14 (AGYW) | prognostic hazard | SSA, mostly women / RCT screens |
| [Hayes 2010](hayes-2010-sti-treatment-hiv-prevention.md) | any STI aOR 3.9; GUD 2.8, non-ulcerative 1.7 | per-follow-up | 31 longitudinal studies |
| [Quinn 2000](quinn-2000-viral-load-heterosexual-transmission.md) | no significant cofactor after viral-load adjustment | per-partnership | Rakai discordant couples |
| [Grabowski 2022](grabowski-2022-stips-sti-burden-rakai.md) | any curable STI PRR 1.51 (1.27-1.78) | cross-sectional co-occurrence | Rakai, population-based |
| [Wawer 1999](wawer-1999-rakai-std-mass-treatment-trial.md) | ~17% of acquisition (curable four) | trial-based PAF | Rakai, mass treatment |
| [Wand 2012](wand-2012-coital-debut-hiv-durban.md) | 5% prevalent / 3% incident (curable four) | cross-sectional attributable risk | Durban, 41% prevalence, high HSV-2 |

## Network position, viral load, and epidemic maturity

An STI-positive person tends to occupy a higher-transmission position in the sexual
network, so an incidence-rate ratio between STI-positive and STI-negative people conflates
the biological cofactor with that position. The population-based measure of that
shared-position effect at the calibration site is modest: [Grabowski 2022
STIPS](grabowski-2022-stips-sti-burden-rakai.md) gives an adjusted prevalence risk ratio
of 1.51 (1.27-1.78) for any curable STI among people living with HIV, a cross-sectional
co-occurrence rather than an acquisition hazard. The model's shared network reproduces
that overlap of about 1.5 without any cofactor term.

Viral load is the dominant determinant of transmission, and adjusting for it removes the
STI association in the Rakai discordant-couple cohort. [Quinn
2000](quinn-2000-viral-load-heterosexual-transmission.md) found the per-partnership
transmission rate rose 2.45-fold per log10 of the index partner's viral load, and no STI
cofactor survived that adjustment: syphilis, gonorrhoea, chlamydia, trichomoniasis,
bacterial vaginosis, ulcer, discharge and dysuria all spanned 1 in both directions. The
unadjusted symptom signals that did reach significance, discharge and dysuria in the
transmitting partner, track the same viral load. At partnership level, [Baggaley
2013](baggaley-2013-hiv-infectiousness-art-discordant-couples.md) found no substantial
difference in transmission when its discordant-couple studies were stratified by reported
STI prevalence, a second failure to corroborate the per-act cofactor, on weak study-level
data.

The direct trial test in the calibration population found no effect. [Wawer
1999](wawer-1999-rakai-std-mass-treatment-trial.md), home-based mass STD treatment
reaching over 80% of Rakai residents every 10 months, left HIV incidence at 1.5 per 100
person-years in both arms (adjusted rate ratio 0.97, 0.81-1.16). Its contrast with
Mwanza's positive syndromic-management trial (RR 0.58) is significant at p<0.01, and
[Hayes 2010](hayes-2010-sti-treatment-hiv-prevention.md) attributes the difference to
epidemic phase: Mwanza was expanding (prevalence-to-incidence ratio 4.6) with high-titre
syphilis at 5-6%, Rakai was mature (ratio 10-15) with syphilis at 1-2%, and in a mature
epidemic most transmission runs on stable partnerships where curable STIs are less common
and the cumulative transmission probability is already high. One of the nine trials Hayes
reviews found an HIV effect.

## Maximum PAF estimates

Two population estimates bound the HIV acquisition that complete clearance of the four
curable STIs could prevent, and both fall far below the per-pathogen ratios. [Wawer
1999](wawer-1999-rakai-std-mass-treatment-trial.md) puts the population attributable
fraction, the share of HIV acquisition removed if the exposure were eliminated, at about
17% for complete control of syphilis, trichomoniasis, gonorrhoea, chlamydia and chancroid
in Rakai, with a further ~20% on bacterial vaginosis and HSV-2 ulcers that neither arm of
the model treats. [Wand 2012](wand-2012-coital-debut-hiv-durban.md), in a 41%-prevalence
Durban cohort, puts the attributable risk for the same four curable STIs at 5% of
prevalent and 3% of incident HIV, against 82% and 21% for HSV-2. The two disagree on level
because of method and setting: Wawer builds a community-trial PAF from cofactor risk
ratios and Rakai prevalences, Wand computes a cross-sectional attributable risk in
a high-HSV-2 population where HSV-2 carries most of the burden. Both describe instant
complete clearance, and both fall far below a per-act multiplier of 1.5-2.8 applied
directly. Much of the burden the literature attributes to STIs sits on HSV-2 and bacterial
vaginosis, which the model does not carry.

## Mechanism and the chlamydia exception

The cofactor acts through genital inflammation, and that inflammation is present in
asymptomatic infection. [Mtshali
2021](mtshali-2021-genital-inflammation-hiv-susceptibility.md) reports roughly a 3-fold
higher HIV acquisition risk with raised genital pro-inflammatory cytokines, shows each of
gonorrhoea, chlamydia and trichomoniasis raises that same cytokine set, and finds similar
cytokine concentrations and cervicitis in women with and without symptoms. Because the
cofactor tracks inflammation and inflammation does not track symptoms, an asymptomatic
infection carries HIV risk comparable to a symptomatic one, so the model should not scale
the cofactor down for asymptomatic cases, and the infections an etiological panel finds
beyond the syndromic door carry the same per-infection risk. The 3-fold figure is
inflammation as the exposure rather than any single pathogen, so it anchors an upper bound
on a per-pathogen cofactor rather than a prior for one.

Chlamydia behaves differently from the other three and the model should carry it
separately. Partial protective immunity after infection ([Batteiger
2010](batteiger-2010-chlamydia-protective-immunity.md)) shows up at the calibration site
as an inverse HIV association (adjusted PRR 0.82 in [Grabowski 2022
STIPS](grabowski-2022-stips-sti-burden-rakai.md)) and weaker cross-pathogen clustering
([Moffa 2026](moffa-2026-sti-couples-stips.md)). Batteiger also raises the possibility
that shortening episodes through screen-and-treat blunts that protection, a sensitivity
direction against the POC arm rather than a base-case term.

## Bound on the direct-treatment channel

The direct-treatment channel of the POC arm, the HIV incidence averted by clearing curable
STIs at the symptomatic door, should be bounded so that complete instant clearance of all
four sits near the 3-17% acquisition range above, not near what the 1.5-2.8 per-pathogen
ratios imply as per-act multipliers. A realistic panel at partial care-seeking coverage
and imperfect sensitivity delivers a fraction of that range. The `MagicCure` intervention,
which clears every bacterial STI from every agent at one instant, reads that upper bound
directly, and the evidence here puts it low.

## Open questions

No per-act cofactor multiplier for the non-ulcerative curable STIs exists for
a general-population setting. The model has to set it from mechanism, with the roughly
3-fold inflammation figure as an upper anchor, and calibrate, rather than lift a value.
Most estimates are acquisition-side, measured in the susceptible partner, so the
infectiousness-side cofactor, an STI in the transmitting partner, is weakly constrained.
Whether clearing chlamydia faster raises reinfection enough to matter is untested in
humans.
