---
type: entry
title: sti_notification
description: Robyn Stuart's STIsim model of Zimbabwe testing partner notification, care-seeking and condom counseling layered on a point-of-care NG/CT/TV panel against syndromic management, and the source of the project's partner notification wiring.
author: Robyn Stuart
resource: https://github.com/starsimhub/sti_notification
local: raw/sti_notification
tags: [partner-notification, modeling, sti, diagnostics, care-seeking]
updated: 2026-11-17 13:50
---

An agent-based Starsim/STIsim model of HIV, syphilis, gonorrhoea (NG), chlamydia (CT),
trichomoniasis (TV) and bacterial vaginosis in Zimbabwe, from the starsimhub organisation
(read at commit 8b1f264, 2026-10-12). It asks whether three levers layered on a
point-of-care (POC) NG/CT/TV panel close the share of infections that go untreated:
partner notification, symptomatic care-seeking, and condom counseling for the newly
treated. It also asks whether POC cuts notifications triggered by an index whose own
treatment was a false positive. It is a companion to the group's `syph_dx_zim`
(overtreatment) and `stisim_vddx_zim` (VDS diagnostic accuracy) analyses, tested against
stisim 1.5.7 and starsim 3.3.2. A manuscript draft sits in `docs/sti_manuscript.md`.

## Architecture

`make_sim` in `model.py` starts in 1985 with 5,000 agents by default (the manuscript says
10,000), scaled to 8.7 million people. Networks are stisim's `StructuredSexual`,
`PriorPartners` and `MaternalNet`. Interventions run in list order: HIV testing in three
streams (female sex workers, everyone else, CD4 below 200), ART and VMMC by count, PrEP,
then NG/CT/TV detection followed by their treatments, then partner notification, then
syphilis testing ending in `syph_tx`. The order sets when attendees are treated
(`model.py:176-187`).

`run_scenarios.py` runs a syndromic standard-of-care (SOC) cell plus a 4 × 4 × 4 POC
factorial over the three levers, 65 cells, switched on at `intv_year` 2027 and run to 2040.
The current baseline is 10 posterior draws × 5 paired seeds per cell (3,250 sims). The
manuscript reports an earlier 5-draw run. Calibration (ZIMPHIA 2015-16 syphilis and HIV,
UNAIDS HIV series, NG/CT/TV prevalence) is a 500-draw Latin hypercube with the
best-fitting draws kept, documented under `calibration/`.

## Partner notification

`pn.py` is a local copy of an edge-stratified `PartnerNotification`, written because
stisim pull request 505 had not reached stisim 1.5.7. That class has since gone upstream
as stisim's `PartnerNotification`. One instance, named `pn`, serves all four diseases.

`baseline_pn_eligibility` (`interventions.py:472-490`) returns everyone whose
`ng_tx`, `ct_tx`, `metronidazole` or `syph_tx` treatment fired that step. Notified
partners who are treated become indices in turn.

`find_partners` walks edges of the current network with exactly one
index endpoint, so two indices never notify each other, and keeps each edge's type. Each
unique partner then gets one notify draw and one attend draw. `pn_rates` builds the
probability for each draw from a dict keyed by edge type, optionally split by partner sex,
summing over a partner's edges and capping at 1. Edge types left out of the dict get
probability 0, so one-off and sex-work partners are never notified. The repo sets
notification by edge type alone and attendance by edge type and partner sex. `make_pn`
sets the prior-partner channel to 0 (`interventions.py:528-529`). Duplicates are removed
within a step only. The class keeps no record of who notified whom, so a treated partner
can notify the person who notified them at a later step.

`SyndromicPN` (SOC) sends attending women to `syndromic_vds` and men to
`syndromic_uds`. `POCPN.notify_attendees` (`interventions.py:98-121`) does the same before
`intv_year`, and from then on calls the POC panel and `syph_pn_test` on every attendee,
regardless of symptoms, in the step the index is treated. `syph_pn_test` uses the
non-treponemal (RPR) product at test probability 1.0. The code comment gives two reasons
for picking it over the dual RDT: the dual has 0.20 sensitivity in primary syphilis, the
stage partners are most likely in, and 0.95 false-positive probability in the previously
cured (`interventions.py:328-341`). Attendees positive on the panel are treated the
following month, because NG/CT/TV treatments run before `pn`. Syphilis positives are
treated in the same month, because `syph_tx` runs after `pn` and reads
`ti_positive == ti`. Attendees get no HIV test.

The class records the funnel (indices, notified, attending) by sex, an index
false-alarm count (index treated for NG, CT or syphilis with every one of those
treatments unnecessary, metronidazole excluded because it also treats bacterial
vaginosis), and the count of notified and attending partners with no current STI.

Partner notification runs at baseline rates from 1985 in both
arms, and the calibration ensemble includes it (`calibration/assumptions.md:16`). For
cells above baseline, `PNIntensitySwitch` swaps in the scenario's probability functions at
`intv_year` (`interventions.py:956-1007`), so every cell shares its pre-2027 trajectory.

## Intensity ladder

`PN_INTENSITY` in `scenarios.py:31-48` co-varies notification and attendance along one
axis. The repo calls every level provisional and round for slide use
(`scenarios.py:26-27`), and cites no source for any value. Probabilities are per current
partner of a treated index.

| Level | Notify stable / casual | Attend, female partner, stable / casual | Attend, male partner, stable / casual |
|---|---|---|---|
| baseline | 0.20 / 0.10 | 0.80 / 0.50 | 0.50 / 0.25 |
| low | 0.35 / 0.25 | 0.85 / 0.60 | 0.60 / 0.40 |
| moderate | 0.55 / 0.45 | 0.90 / 0.70 | 0.70 / 0.55 |
| high | 0.75 / 0.65 | 0.92 / 0.80 | 0.80 / 0.70 |

The other two ladders are a multiplier of 1.0, 1.25, 1.5 or 1.8 on NG/CT/TV symptomatic
care-seeking (female care-seeking clips at 1.0 near 2), and condom counseling covering 0,
25, 50 or 75% of the newly treated, each enrolled person's susceptibility to NG, CT and TV
reduced 50% for 6 months.

## Findings

Reported over 2027-2040 against SOC, as medians across draws. The POC panel alone cuts
cumulative new curable-STI infections about 10-15%, and the highest-intensity combination
of all three levers about 50-60%. Care-seeking is the largest lever for NG, CT and TV, and
partner notification for syphilis, with smaller gains from moderate to high notification.
Unnecessary NG, CT, TV and syphilis treatments fall 75-85% under POC whatever the lever
levels. Among female indices notifying male partners at baseline levers, the share with an
unnecessary index treatment falls from 44% under SOC to 31% under POC, a floor the
manuscript attributes to 95% per-pathogen specificity at Zimbabwe's low true prevalence.
HIV is modelled as background, and no HIV outcome is reported.

## Relevance to project

A design reference for the project's partner notification arms, which follow this repo's
wiring as recorded in [Partner notification implementation](partner-notification-implementation.md).
The project takes from it notification of current partners only, with probabilities set
by partnership type (stable, casual) and partner sex through `pn_rates`, every treated
person as an index, and one visit at which attendees get the POC panel and a syphilis test
in the index's treatment month (`POCPN.notify_attendees`). The project uses upstream
stisim's `PartnerNotification` (stisim 1.7.2) in place of the local `pn.py`.

The intensity ladder is the range of notification and attendance this repo explores. Its
values are round and unsourced, usable as a span to test across. They estimate
notification and attendance in no setting. The repo gives no evidence on
partner notification's effect on HIV, since attendees get no HIV test and HIV outcomes are
not reported. Its calibrated parameters are specific to Zimbabwe and stisim 1.5.x, and
`calibration/recalibration_guide.md` states they do not carry across stisim minor
versions.

## Limitations

Code and prose disagree in places, and the code is what ran. The manuscript
(`docs/sti_manuscript.md:57`) and docstrings (`interventions.py:21`, `:74`, `:474-477`,
`:510`) say a notified partner cannot notify the index back, via a `last_notifier` check
in the upstream class. The local `pn.py` that runs has no such check. The design note
`docs/baseline_pn_design.md` describes three instances, one per index pathway, with
independent draws per edge and attendees routed to syndromic management. The code uses one
shared instance, one draw per partner, and POC routing after 2027. Notification and
attendance probabilities are assumptions with no cited data.
