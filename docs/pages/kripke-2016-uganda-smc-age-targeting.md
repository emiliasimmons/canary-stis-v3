---
type: entry
title: "Modeling the Impact of Uganda's Safe Male Circumcision Program: Implications for Age and Regional Targeting"
description: DMPPT 2.0 compartmental model of age- and region-targeted male circumcision scale-up in Uganda, giving circumcisions and cost per HIV infection averted.
author: Kripke et al.
published: 2016-07-13
resource: 10.1371/journal.pone.0158693
local: raw/10.1371/journal.pone.0158693
tags: [hiv, modeling]
updated: 2026-09-10 00:22
---

A PLOS ONE modeling exercise run with Uganda's Ministry of Health to re-set national targets
for safe male circumcision (SMC, Uganda's term for voluntary medical male circumcision). The
tool is DMPPT 2.0, a compartmental Excel model that tracks circumcised males by five-year age
group through ageing and mortality, driven by population, mortality, and age-specific HIV
incidence exported from the country's Spectrum/AIM file (validated version of 17 May 2014).
Each scenario raises circumcision coverage to 80% in one age band or combination between 2014
and 2018 by linear interpolation from 2013 baseline coverage, then holds it, and is compared
against a baseline where circumcision prevalence stays put. Outputs are compiled over 2014-2028
and discounted at 3% per year. Extracted text at `raw/10.1371/journal.pone.0158693`.

## Relevance to project

Context and a comparator for the prevention-targeting arm of the argument, not a calibration
target. It is the clearest available worked example of the question canary-stis asks of
point-of-care STI diagnostics, posed for a different intervention in the same country: given a
fixed prevention tool, how much HIV incidence reduction does targeting buy over untargeted
scale-up, and what does each averted infection cost. The efficiency numbers set the scale a POC
diagnostic strategy would be judged against in Uganda: 12 circumcisions per HIV infection
averted in men 20-24 and 25-29, 13 in men 30-34, and $1,100 per infection averted for the
15-34 strategy at an $80 unit cost and $497 per person-year of antiretroviral therapy.

It also supplies the background prevention environment the Rakai calibration must sit inside.
Uganda's national circumcision programme was scaling toward 80% coverage in men 15-49 over the
model's window, from a 2011 baseline of 26% circumcised among men 15-49 with regional values
from 2% (Mid Northern) to 53% (Mid Eastern), and roughly 450,000 circumcisions per year would
be needed just to hold 80% once reached. An HIV model of Rakai over 2014 onward that ignores
rising circumcision coverage will misattribute the resulting incidence decline. The paper takes
the trial-based 60% reduction in male HIV acquisition as given rather than re-estimating it.

What it cannot supply: no STI content of any kind, no sexual-network structure, no individual
heterogeneity. DMPPT 2.0 has no transmission model inside it, so the incidence trajectory is
imported from Spectrum/AIM rather than generated, and infections averted follow from applying
circumcision protection to that imported incidence. Nothing here constrains a network or
cofactor parameter.

## Key points

- Immediacy and efficiency both favour men 20-34: fastest five-year incidence decline and the
  fewest circumcisions per infection averted.
- Magnitude over 15 years favours the young: 10-19 gives the largest incidence reduction by
  2028, because boys 10-14 reach exposure inside the window. Average age of sexual debut for
  men is 18.4 years and peak HIV incidence falls between 25 and 39.
- Total infections averted 2014-2028: 479,558 for the current 15-49 strategy, 485,000 for
  10-49, 402,000 for 10-34 (85% of the 15-49 figure), 257,000 for 10-24, 242,000 for 15-24.
- Cost per infection averted: $1,100 for 15-34, the same as for 15-49; roughly $2,100 for
  10-24, the worst of the set, since 10-14 year olds spend part of the window unexposed.
- Circumcisions needed by 2018 to hit 80%: 2,160,553 for 20-34 ($291M), 3,311,676 for 15-34
  ($428M), 4,565,828 for 15-49 ($523M).
- Regional cost-effectiveness varies little. Uncertainty bounds overlap the national estimate
  everywhere except West Nile, where projected incidence is low and the Spectrum fit is
  questionable. Scale-up among 10-34 is cost-saving in every region, and stays cost-saving at a
  $160 unit cost.
- Mid Northern (1.6% of men circumcised) and North East (6.7%) lag; every other region is on or
  ahead of target pace.
- Programme data were the binding constraint on the analysis: before April 2015 Uganda's health
  information system reported circumcisions in bands of 0-<2, 2-<5, 5-<15, 15-49, >49, so
  five-year age distributions of programme output did not exist.

## Limitations

Inputs are national and regional aggregates, so the projections inherit whatever bias sits in
baseline circumcision prevalence, unit costs, and the Spectrum/AIM incidence forecast; the
authors say long-term incidence cannot be projected accurately. The $80 unit cost is fixed
across age, region, implementation model, and scale-up phase, which matters here because demand
creation for older men is the expensive part, so the age ranking on cost-effectiveness could
shift. The authors state total cost figures are for relative comparison only and not for
budgeting. Social, cultural, and logistical barriers to uptake sit outside the model entirely.
