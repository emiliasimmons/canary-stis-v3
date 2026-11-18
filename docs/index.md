# canary-stis

The evidence base for the HIV-prevention impact of point-of-care STI diagnostics: how much
of the HIV incidence reduction comes from direct STI treatment, how much from prevention
targeting, and how much from identifying high-transmission positions in the sexual network.
The model is a Starsim/STIsim agent-based simulation of HIV and four curable bacterial STIs
on a shared risk-structured network, with the Rakai Community Cohort Study as the first
calibration site.

> Compiled from frontmatter, overwritten on the next compile.

## Tags

- [care-seeking](tags/care-seeking.md) · 52 pages
- [coinfection](tags/coinfection.md) · 27 pages
- [diagnostics](tags/diagnostics.md) · 23 pages
- [economics](tags/economics.md) · 9 pages
- [hiv](tags/hiv.md) · 179 pages
- [immunity](tags/immunity.md) · 3 pages
- [modeling](tags/modeling.md) · 36 pages
- [partner-notification](tags/partner-notification.md) · 22 pages
- [phylogenetics](tags/phylogenetics.md) · 5 pages
- [prep](tags/prep.md) · 33 pages
- [rakai](tags/rakai.md) · 75 pages
- [sexual-networks](tags/sexual-networks.md) · 83 pages
- [sti](tags/sti.md) · 52 pages
- [study-concept](tags/study-concept.md) · 3 pages

## Syntheses

- [Partner notification and its omission from canary-stis](pages/partner-notification-pathway.md) -- Notification finds contacts at 4-14x general-testing positivity but reaches about half of those named, and both the concentration and the reinfection it interrupts are already represented in the model.
- [PrEP as delivered versus trial efficacy and the STI-test-to-PrEP prevention step](pages/prep-delivered-vs-efficacy.md) -- How far delivered PrEP coverage in Eastern and Southern Africa falls below trial efficacy, and what that bounds for routing STI-positive people into PrEP.
- [RCCS HIV incidence decline and its drivers](pages/rccs-incidence-decline-drivers.md) -- The RCCS incidence trajectory by age and sex from the 1990s to 2018, and how much of the decline ART, VMMC, and later sexual debut account for.
- [The STI-HIV cofactor and the HIV reduction achievable by clearing curable STIs](pages/sti-hiv-cofactor.md) -- Curable STIs raise per-act HIV transmission, but observational cofactor ratios overstate the incidence reduction from clearing the four bacterial STIs, and the attributable ceiling in a mature epidemic is 3-17%.
- [The syndromic door and the point-of-care panel](pages/syndromic-door-poc-panel.md) -- The curable-STI burden the symptomatic syndromic door reaches in Rakai, and the accuracy a point-of-care panel adds at the same door.
- [Targeting high-transmission network positions in a generalized epidemic](pages/targeting-network-positions.md) -- How much HIV prevention comes from identifying high-transmission network positions through STI diagnosis, and why the payoff is modest and setting-dependent in a Rakai-like generalized epidemic.

## Decisions

- [Partner notification implementation](pages/partner-notification-implementation.md) -- Current partners of every treated person are notified through upstream stisim PartnerNotification from intv_year, attendees get the POC panel, a syphilis test and an HIV test at one visit, and diagnosed partners join the same coverage-targeted ART as everyone else.
- [Pathway decomposition and arm design](pages/pathway-decomposition-arm-design.md) -- Four reporting pathways from eight model arms, behavioral PrEP as its own SOC arm sharing one oral PrEP cascade with STI-triggered PrEP, the network risk signal tested inside the POC arm, and comparisons between arms suggested for experiments to settle.
- [Settings are hypothetical epidemics crossed by prevalence and phase](pages/settings-prevalence-by-phase.md) -- Four settings cross high (about 25%) or medium (about 15%) HIV prevalence with a mature or expanding epidemic, each an ensemble of simulations selected on prevalence at ages 15-49 in 2026, with STI and HIV biology shared and STI burden left to the model.

## Stale

- [Pathway decomposition and arm design](pages/pathway-decomposition-arm-design.md) -- 1 newer dependency

## Recent

- 2026-11-17 [Settings are hypothetical epidemics crossed by prevalence and phase](pages/settings-prevalence-by-phase.md)
- 2026-11-17 [Pathway decomposition and arm design](pages/pathway-decomposition-arm-design.md)
- 2026-11-17 [Partner notification implementation](pages/partner-notification-implementation.md)
- 2026-11-17 [hivsim_eswatini: STIsim HIV model of Eswatini](pages/hivsim-eswatini.md)
- 2026-11-17 [sti_notification](pages/sti-notification-zimbabwe-model.md)
