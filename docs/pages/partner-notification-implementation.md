---
type: decision
title: Partner notification implementation
description: Current partners of every treated person are notified through upstream stisim PartnerNotification from intv_year, attendees get the POC panel, a syphilis test and an HIV test at one visit, and diagnosed partners join the same coverage-targeted ART as everyone else.
tags: [partner-notification, modeling, hiv, sti]
updated: 2026-11-17 13:39
---

Partner notification (pathway B) runs only in the two arms that include it, POC with
partner notification and POC with STI-triggered PrEP and partner notification, switched on
at `intv_year`. It is implemented as stisim's `sti.PartnerNotification`, following the
wiring of the sti_notification model (a colleague's Zimbabwe partner notification model,
not cataloged). Notification and attendance levels are left to experiments.

## Who is notified

Only current partners are notified, read from the active sexual network each month.
Notification and attendance probabilities are set separately for stable and casual
partnerships and by the partner's sex, through stisim's `pn_rates`. One-off and sex-work
partners are never notified. The look-back channel through `PriorPartners` stays off: our
sim does not build that network, and `pn_rates` cannot stratify it by partnership type.
The [partner notification synthesis](partner-notification-pathway.md) gives about 1.1
contacts named per index, close to what current partnerships supply.

## Index

An index is everyone whose `ng_tx`, `ct_tx`, `metronidazole` or `syph_tx` treatment fires
that month. That includes women treated after a positive antenatal syphilis test and
notified partners who are treated in turn, so notification passes along chains. A treated
partner can notify back the person who notified them, which costs that person an extra
visit and test a month later. stisim removes duplicate notifications only within a month,
and sti_notification behaves the same, so the model keeps their behaviour.

## Visit

Each partner gets one notify draw and one attend draw. An attendee receives the POC panel,
the syphilis notification test, and an HIV test in the month the index is treated, and
STI treatment fires the following month, as in sti_notification. The wait to testing in
Siaya had a median of 14.5 days
([Wekesa 2020](wekesa-2020-time-to-test-partner-services-siaya.md)), which the monthly
timestep cannot resolve more finely.

Upstream `notify_attendees` schedules a single test, and three separate notification
instances would draw attendees independently, so one partner could get the panel without
the HIV test. A subclass overrides `notify_attendees` to call the three tests on the same
attendees. It keeps only the post-switch part of sti_notification's `POCPN`. The
pre-switch routing to syndromic management is dropped, because the intervention starts at
`intv_year` and the arms match SOC before it.

## ART after an HIV diagnosis

A partner diagnosed with HIV at the visit starts ART through the same `sti.ART` as
everyone else, with coverage targets by age and sex, as in the hivsim_eswatini model (an
Eswatini HIV model, not cataloged). Each month `sti.ART` starts diagnosed people only into
places below the coverage target and stops people to bring numbers down to it. A partner
diagnosis therefore raises the number on ART only in age and sex groups where too few
people are diagnosed to fill the target. Where the diagnosed pool already fills it, the
HIV testing sub-category of partner notification comes out near zero by construction of
the coverage target. Read that sub-category alongside how full each group's target is.
