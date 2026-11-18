---
type: decision
title: Pathway decomposition and arm design
description: Four reporting pathways from eight model arms, behavioral PrEP as its own SOC arm sharing one oral PrEP cascade with STI-triggered PrEP, the network risk signal tested inside the POC arm, and comparisons between arms suggested for experiments to settle.
tags: [study-concept, modeling, diagnostics, partner-notification, prep, hiv]
updated: 2026-11-18 15:10
---

The study reports four pathways from point-of-care STI diagnostics to HIV incidence:
direct treatment, partner notification, prevention targeting, and the network risk signal.
Eight model arms supply them. The network risk signal is a hypothesis about the epidemic,
tested inside the POC arm. Which arms are compared, the outcome, the time horizon, and how
pathway values relate to the total are left to each experiment. The comparisons below are
the ones the arms were built for.

## Pathways

Direct treatment is pathways A and C of the [concept deck](canary-study-concept.md) taken
together. Pathway A changes HIV only by reducing how many people later carry the STI
cofactor, so comparing runs cannot separate its HIV effect from C's without a model switch
that ends the cofactor while leaving the STI transmitting. Direct treatment is split
instead by the infections the POC panel treats that syndromic management did not, into
symptomatic and asymptomatic. An analyzer supplies the split, with no extra arm.

Partner notification is pathway B. Notified partners are referred to a testing visit,
where they receive the POC panel, treatment if positive, and an HIV test with linkage to
ART. The HIV testing part is reported as its own sub-category. Most of the canon's
notification evidence comes from HIV index testing
([partner-notification synthesis](partner-notification-pathway.md)), and reporting that
part separately keeps the STI part comparable with direct treatment. Referral is the one
delivery mode that tests partners: patient-delivered partner medication treated 74% of
partners against 34% under referral
([Alam 2010](alam-2010-partner-notification-developing-countries.md)), but no partner it
reaches is tested for HIV or becomes eligible for STI-triggered PrEP. The synthesis argues
the model loses little by leaving notification out. Bringing it into scope measures that
loss instead of arguing it.

Prevention targeting is pathway D: a positive STI result leads an HIV-negative person onto
PrEP. STI-triggered PrEP offers PrEP to a person in the step their STI treatment fires, at
whatever volume the diagnoses produce. Partner notification and STI-triggered PrEP act on
the diagnoses the POC panel produces, so neither runs on SOC.

The network risk signal is pathway E, restricted to acquisition: an HIV-negative person
who acquires one of the four curable STIs is more likely than average to acquire HIV
later. It describes the epidemic and switches nothing on, so it has no prevented fraction.
It is tested inside the POC arm, where no PrEP runs. In an arm with STI-triggered PrEP the
people the signal flags are put on PrEP, and their later HIV acquisition falls because
the PrEP works. That fall is prevention targeting's effect, the value of acting on the
signal, and it would weaken the signal being tested. The four STIs are gonorrhoea,
chlamydia, trichomoniasis and syphilis, the infections the POC panel detects. BV is left
out because the panel never detects it, and its HIV cofactor in stisim is a placeholder.

The test splits HIV-negative people in the POC arm by whether they acquire one of the four
STIs and compares their later HIV acquisition, over all STI infections, diagnosed or not.
A measure on diagnosed infections alone would give the same low value for a weak signal
and for a narrow care-seeking door. Infection times come from the infection log. The HIV
transmission logger's guess at the source partner plays no part, since only who acquired
HIV and when is read. An analyzer records every treatment, syndromic or POC, with the
person's true STI status, because a syndromic treatment can fall on a person with no STI.
That record splits infections into diagnosed and undiagnosed.

## Behavioral PrEP

Behavioral PrEP runs in one arm, SOC with behavioral eligibility, which is the concept
deck's Risk-Group PrEP arm. It stands for targeting prevention by behavior without buying
diagnostics, the strategy POC with STI-triggered PrEP competes against. Running it in
every arm would remove that comparison, would put PrEP in the POC arm where the network
risk signal is tested, and would not make the baseline more realistic, since each setting
is already selected on its HIV prevalence
([settings decision](settings-prevalence-by-phase.md)).

The screen is Uganda's national PrEP eligibility tool as applied in the RCCS
([Ssempijja 2022](ssempijja-2022-prep-eligibility-hiv-incidence-rakai.md)): any of more
than one partner of unknown HIV status, condomless sex outside marriage, transactional
sex, or genital ulcers, in the past 12 months. Each item is something a person could
report, so the screen sees what a real questionnaire sees and never the model's hidden
risk group. In the RCCS 29% of adults qualified, with HIV incidence of 0.91 per 100
person-years among them against 0.41 among the rest, which checks how many people the
model's version qualifies and how much risk it concentrates. The screen is asked at
background HIV testing visits and at STI clinic visits, the contacts where programmes
offer PrEP, of HIV-negative people aged 15 and over. HIV testing has no lower age limit,
and without the age limit children would fill the count of people screened. The screen
reports its counts for ages 15-49 as well, the RCCS age range. Offers run at the volume
the screen produces. The screen and its PrEP start in 2027, the intervention year of the
POC arms, so the two PrEP strategies run over the same years.

In the model every genital ulcer is a syphilis chancre, since the non-syphilitic ulcer
background (`gudp`) stays at zero. The ulcer item therefore marks a curable STI every time
it fires, which real self-reported ulcers do not, and this gives behavioral PrEP a sharper
STI signal than real screening has.

## PrEP

Both PrEP arms share one delivery cascade, so comparing them measures who each rule
selects. The product is daily oral PrEP, the only product with delivered uptake and
persistence data from Eastern and Southern Africa in the
[PrEP synthesis](prep-delivered-vs-efficacy.md). Uptake is set at 0.30, the routine
uptake measured in SEARCH (27%, [Koss 2020](koss-2020-prep-uptake-adherence-search.md))
and a Kampala AGYW cohort (30.6%, [Mayanja 2022](mayanja-2022-prep-uptake-agyw-kampala.md)).
The model applies it as a coverage target, the way [hivsim_eswatini](hivsim-eswatini.md)
runs PrEP: each month the people offered PrEP that month are topped up until 30% of them
are on PrEP, starting those with the highest score on a fixed random willingness. Offered
people already partway through a course count toward the 30%, and the target rounds down,
so about 20-27% of offered people start and a month with 3 or fewer offers starts nobody.
Experiments report uptake as the proportion of offered people who start. A course lasts 3
months and then ends, and a person restarts only at a new offer. Efficacy while on PrEP is
0.75.

The model runs PrEP through stisim's `sti.Prep`, and the course length is its default,
kept for simplicity. A 3-month course sits near the 2.5-month median time on drug in
Kampala and the 20% still on PrEP at 6 months in POWER
([Celum 2022](celum-2022-power-prep-agyw.md)). An efficacy of 0.75 sits near the 73%
reduction at adherence of 70% or more and above the 54% pooled across real adherence levels
([Chou 2019](chou-2019-prep-systematic-review.md)), so both PrEP arms give each user the
protection of good adherence, and by the same factor. Because willingness
is random and fixed for life, uptake is unrelated to risk and a person who declines once
tends to decline again. Uptake, persistence, and
uptake that varies with risk are left for exploration (issue 22).

## Figures

Each pathway is reported as a prevented fraction: the proportion of incidence it averts,
out of the incidence that would occur without it. The PAF is kept for the STI cofactor,
which is an exposure. Gargiullo, Rothenberg and Wilson (1995, doi:10.1002/sim.4780140107)
separate the two, with the prevented fraction measuring an intervention's impact and the
attributable risk suited to etiology.

## Arms

1. SOC
2. SOC + behavioral PrEP, from 2027
3. POC
4. POC + partner notification
5. POC + STI-triggered PrEP
6. POC + STI-triggered PrEP + partner notification
7. POC + STI screening at HIV testing
8. SOC + Magic cure

STI screening at HIV testing offers the POC panel to people without STI symptoms at a
background HIV testing visit, the only routine HIV contact present in every arm. It
screens women by default, matching the population of the INSTEP trial, and an
`include_men` switch adds men. Everyone offered accepts by default. Experiments can lower
acceptance to test how much the arm depends on it.

The Magic cure clears gonorrhoea, chlamydia, trichomoniasis and syphilis at one instant,
and nothing in `src/` reintroduces them, so the removal lasts for the rest of the run.
Whether stisim reintroduces infections internally has not been checked, and
a reintroduction would make arm 8 understate the cofactor PAF. The cure leaves BV in place,
so the PAF covers the four STIs only.

## Suggested comparisons

Direct treatment is POC against SOC (3 against 1), what the POC panel adds over syndromic
management.

Partner notification and STI-triggered PrEP can each be measured alone (4 or 5 against 3)
and with the other present (6 against 5 or 4). The difference between the two values is
their overlap, mostly notified partners who test STI-positive and so become eligible for
STI-triggered PrEP. Reporting it as its own term avoids a sequential ladder, which would
assign the overlap to whichever pathway came second, since sequential attributable
fractions depend on the order of removal (Eide 2008, doi:10.1111/j.1752-699x.2008.00091.x).

The two PrEP strategies compare as 5 and 2, each against its own diagnostic baseline or
both against SOC, by total infections averted and by infections averted per PrEP user. The
concept deck labelled this comparison D, alongside adding targeted PrEP to POC (5 against
3). Because volumes are left free, STI-triggered PrEP can come out ahead by enrolling more
people as well as by choosing higher-risk ones. An experiment that raises the volume of
behavioral PrEP separates the two.

STI screening at HIV testing is 7 against 3, and its effect falls in direct treatment's
asymptomatic sub-category.

The cofactor PAF is 8 against 1, the maximum that direct treatment and partner
notification can prevent together.
