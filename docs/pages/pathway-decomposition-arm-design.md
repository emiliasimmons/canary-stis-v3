---
type: decision
title: Pathway decomposition and arm design
description: Four reporting pathways, three measured as prevented fractions from seven model arms, the canary signal tested as a hypothesis inside a run, and the STI cofactor PAF as their maximum.
tags: [study-concept, modeling, diagnostics, partner-notification, prep, hiv]
updated: 2026-11-15 22:51
---

The study reports four pathways from point-of-care STI diagnostics to HIV incidence:
direct treatment, partner notification, prevention targeting, and the canary signal. The
first three are each measured as a prevented fraction from comparisons among seven model
arms. The canary signal is a hypothesis about the epidemic, tested inside a run. The PAF of
the STI cofactor, from a separate SOC run with the Magic cure, sets the maximum that direct
treatment and partner notification can prevent together. Each experiment chooses its own
outcome and time horizon.

## Pathways

Direct treatment is pathways A and C of the [concept deck](canary-study-concept.md) taken
together. Pathway A changes HIV only by reducing how many people later carry the STI
cofactor, so comparing runs cannot separate its HIV effect from C's without a model switch
that ends the cofactor while leaving the STI transmitting. Direct treatment is split
instead by the infections the POC panel treats that syndromic management did not, into
symptomatic and asymptomatic. An analyzer supplies the split, with no extra arm.

Partner notification is pathway B. Notified partners are treated for curable STIs and
tested for HIV with linkage to ART, and the HIV testing part is reported as its own
sub-category. Most of the canon's notification evidence comes from HIV index testing
([partner-notification synthesis](partner-notification-pathway.md)), and reporting that
part separately keeps the STI part comparable with direct treatment. The synthesis argues
the model loses little by leaving notification out. Bringing it into scope measures that
loss instead of arguing it.

Prevention targeting is pathway D: a positive STI result leads an HIV-negative person into
prevention.

The canary signal is pathway E, restricted to acquisition: an STI infection in an
HIV-negative person predicts that the same person acquires HIV later. It describes the
epidemic and switches nothing on, so it has no prevented fraction. Its two requirements
are measured apart. Whether STIs precede HIV is measured inside one run over all STI
infections, diagnosed or not. Whether the platform reaches those people shows in the split
between diagnosed and undiagnosed infections, and in the prevented fraction of D. A measure
on diagnosed infections alone would give the same low value for a weak signal and for
a narrow care-seeking door. Under the SOC arm a diagnosis is a syndromic treatment, which
can fall on a person with no STI, so the analyzer records true infection status at each
treatment.

## Figures

Each pathway is reported as a prevented fraction: the proportion of incidence it averts,
out of the incidence that would occur without it. The PAF is kept for the STI cofactor,
which is an exposure. Gargiullo, Rothenberg and Wilson (1995, doi:10.1002/sim.4780140107)
separate the two, with the prevented fraction measuring an intervention's impact and the
attributable risk suited to etiology.

## Arms and comparisons

1. SOC
2. POC
3. POC + partner notification
4. POC + STI-triggered prevention
5. POC + STI-triggered prevention + partner notification
6. POC + prevention by behavioral eligibility, matched in amount to arm 4
7. POC + screening door at background HIV testing visits

Direct treatment is arm 2 against arm 1, so it measures what the POC arm adds over
syndromic management.

Arms 2 to 5 form a 2×2 over POC. Partner notification and prevention targeting are each
measured alone and added to the other, and the difference between the two values is their
interaction. A sequential ladder would assign that interaction to whichever pathway came
second, since sequential attributable fractions depend on the order of removal (Eide 2008,
doi:10.1111/j.1752-699x.2008.00091.x).

The canary signal's value is arm 4 against arm 6. Behavioral eligibility is what
prevention programmes use now, so the comparison asks whether the STI signal beats current
practice. The concept deck labelled this comparison D as well. It sits with E because it
measures the signal, with the amount of prevention held fixed.

The screening door is arm 7 against arm 2, and its effect falls in direct treatment's
asymptomatic sub-category. The door attaches to background HIV testing because that is the
only routine HIV contact present in every arm. An `include_men` switch restricts it to
women, matching the population of the INSTEP trial.

The cofactor PAF is SOC with the Magic cure against SOC, run apart from the seven arms. The
Magic cure clears gonorrhoea, chlamydia, trichomoniasis and syphilis at one instant, and
nothing in `src/` reintroduces them, so the removal lasts for the rest of the run. Whether
stisim reintroduces infections internally has not been checked, and a reintroduction would
make this run understate the PAF. The cure leaves BV in place, so the maximum covers the
four STIs only.
