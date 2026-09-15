---
type: entry
title: Male-Partner Treatment to Prevent Recurrence of Bacterial Vaginosis (StepUp)
description: Randomized trial in Australian couples where treating the male partner cut 12-week bacterial vaginosis recurrence from 63% to 35%, the strongest partner-treatment effect size available.
author: Vodstrcil et al.
published: 2025-03-06
resource: 10.1056/NEJMoa2405404
local: raw/10.1056/nejmoa2405404
tags: [partner-notification, sti, sexual-networks]
updated: 2026-09-10 00:14
---

Source: [vodstrcil-2025](https://doi.org/10.1056/NEJMoa2405404)

StepUp, an open-label randomized controlled trial at two sexual health services and three
family-planning services across three Australian states, enrolled 164 couples in which the
woman had symptomatic bacterial vaginosis (BV) and a regular male partner of at least 8
weeks. Both arms gave the woman first-line therapy (metronidazole 400 mg twice daily for 7
days, or intravaginal clindamycin or metronidazole where contraindicated). The intervention
arm added treatment of the male partner: oral metronidazole 400 mg twice daily plus 2%
clindamycin cream applied to the glans and upper shaft, both for 7 days. The control arm
left the man untreated.

## Relevance to project

This is a partner-treatment effect size, and the model has no partner-notification pathway,
so it cannot enter the simulation as a parameter. Its use here is as a bound on what the
project is leaving on the table: in a monogamous-couple design with a 7-day dual-site
regimen, treating the male partner cut female recurrence within 12 weeks from 63% to 35%
(hazard ratio 0.37, 95% CI 0.22 to 0.61). If a reviewer asks how much of an STI-control
gain the SOC and POC arms forgo by omitting partner services, this is the largest
well-powered estimate available, though on BV rather than on any of the four curable
bacterial STIs the model carries.

It is also a structural argument for the shared-network representation of a couple. The
trial's premise, and its result, is that the male genital tract sustains reinfection of the
female partner, which is the same mechanism the model uses for the four modeled STIs. The
result is evidence that within-partnership reinfection is a large fraction of what looks
like treatment failure, in a setting where the woman was fully treated and adherent (all
women took at least 70% of doses).

Not usable as a calibration target. The population is urban Australian sexual health clinic
attendees, not Rakai, BV is not in the model, and the outcome is 12-week recurrence under
directly observed monogamy rather than population incidence.

## Key points

Recurrence within 12 weeks (modified intention-to-treat, women meeting at least three Amsel
criteria plus Nugent score 4 to 10): 24 of 69 (35%) with partner treatment, 43 of 68 (63%)
with standard care. Recurrence rates 1.6 per person-year (95% CI 1.1 to 2.4) against 4.2 per
person-year (95% CI 3.2 to 5.7), an absolute difference of -2.6 per person-year (95% CI -4.0
to -1.2, P<0.001). Mean time to recurrence 73.9 against 54.5 days over the 84-day window.

The data and safety monitoring board stopped the trial at the 150-couple interim analysis,
against a planned 342, because standard care was inferior under a Peto-Prentice rule of
P<0.001. Recurrence in the control arm ran far above the 40% assumed for the power
calculation.

Imputing all missing week-12 data as treatment failure still gives 2.2 against 4.1 per
person-year; imputing as cure gives 1.2 against 3.1. The direction survives either
assumption.

Earlier partner-treatment trials used oral agents alone and were read as evidence against
sexual transmission of BV. The authors attribute the difference to also clearing cutaneous
and subpreputial penile carriage, which oral therapy does not reach.

Male adherence was the main leak: 8 of 56 men reporting adherence took under 70% of doses,
missing clindamycin more often than metronidazole. Recurrence was lowest (1.3 per
person-year, 95% CI 0.7 to 2.6) among partners of fully adherent men, which the authors
concede may be adherence bias rather than dose-response.

Tolerability in men was acceptable: 26 of 56 (46%) reported any adverse event, mostly
nausea, headache, and metallic taste; 4 of 56 reported penile skin irritation. No serious
adverse events.

## Limitations

Open-label, with no placebo cream for men, though the microscopists scoring the primary
outcome were blinded. Stopping at 150 couples leaves the effect size imprecise and likely
overstated relative to a completed trial.

Eligibility excluded anyone with a partner outside the couple, sex workers, and people
known to be living with HIV, and required monogamy through follow-up. That is the opposite
of the risk structure the model's transmission dynamics rest on, and it makes the trial
silent on partner treatment where concurrency is common. Nine couples reported an outside
partner during the trial; undisclosed concurrency is plausible.

Baseline risk was high: 87% of women had a prior BV diagnosis, 80% of male partners were
uncircumcised, and 28 to 33% used an IUD. Effects did not differ by IUD use or circumcision
status, but the trial was not powered for either stratum. Most participants came from a
single sexual health service in urban Australia.
