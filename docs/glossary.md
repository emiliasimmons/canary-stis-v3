# Glossary

- **POC arm**. The intervention arm: point-of-care. An etiological test-and-treat panel
  that replaces syndromic management at the same symptomatic care-seeking door, switched
  on at `pars.intv_year`. Not an asymptomatic screening programme.
- **Screening door**. The POC panel offered to people without STI symptoms at an HIV
  prevention contact, in addition to the symptomatic care-seeking door.
- **SOC arm**. The comparator. Syndromic management for the whole run, selected by
  `pars.intv_year = None`.
- **Syndromic management**. Treating on the presenting syndrome with a drug mix covering
  the likely causes, without identifying the pathogen. The WHO standard where laboratory
  testing is unavailable, and the origin of both overtreatment and missed infection.
- **Etiological diagnosis**. Identifying the pathogen before treating, so the drug matches
  the infection.
- **VDS / UDS**. Vaginal discharge syndrome and urethral discharge syndrome, the two
  syndromic pathways. VDS covers gonorrhoea, chlamydia, trichomoniasis and bacterial
  vaginosis; UDS the first three.
- **Magic cure**. `MagicCure` in `src/interventions.py`. Clears every bacterial STI from
  every agent at one instant, bounding the largest HIV incidence reduction that STI
  clearance alone could produce.
- **RCCS**. Rakai Community Cohort Study, an open population-based cohort of adults aged
  15-49 across 30 communities in Rakai, Uganda. The first planned calibration site.
- **AGYW**. Adolescent girls and young women, conventionally aged 15-24.
- **NAAT**. Nucleic acid amplification test, the laboratory reference standard that
  point-of-care STI tests are measured against.
- **STI cofactor**. The raised per-act probability of HIV acquisition or transmission while
  a curable STI is present.
- **Pathway A**. Onward STI transmission: treating an STI shortens the infection, so fewer
  partners acquire it and fewer people later carry the STI cofactor.
- **Pathway B**. Partner treatment cascade: partners of a diagnosed person are notified and
  treated for curable STIs, and tested for HIV with linkage to ART. Every effect on HIV of
  what partners receive belongs to this pathway, with the HIV testing part reported as its
  own sub-category.
- **Pathway C**. Biological susceptibility: treating an STI ends the STI cofactor in the
  treated person.
- **Pathway D**. Prevention targeting: a positive STI result leads the person into
  prevention (PrEP, condoms, counseling), and every effect of that prevention on HIV
  belongs to this pathway.
- **Pathway E**. Network risk signal: the hypothesis that a positive STI result in an
  HIV-negative person marks someone more likely than average to acquire HIV later.
- **Behavioral eligibility**. Qualifying for PrEP on self-reported sexual behavior, the
  screen prevention programmes use, without an STI result.
- **Direct treatment**. Pathways A and C together, the HIV effect of treating curable STIs
  at the care-seeking door, reported separately for symptomatic and asymptomatic
  infections.
- **Prevented fraction**. The proportion of incidence that an intervention, or one pathway
  of it, averts, out of the incidence that would occur without it.
- **PAF**. Population attributable fraction: the proportion of incidence caused by a risk
  factor, which would disappear if every exposure to it were removed.
- **Target product profile**. A specification of what a test must achieve to be useful,
  agreed by expert consensus and given as a minimal and an optimal value per
  characteristic. See
  [pages/toskin-2017-sti-poct-target-product-profiles.md](pages/toskin-2017-sti-poct-target-product-profiles.md).
- **Setting**. A hypothetical HIV epidemic defined by an HIV prevalence level and an
  epidemic phase, represented by the ensemble of simulations, selected from a parameter
  exploration, whose prevalence and phase fall in its cell.
- **Country setup**. The country-specific inputs a simulation is built on: demography and
  ART and VMMC coverage, taken from one real country.
- **Mature epidemic**. An HIV epidemic long past its incidence peak, with incidence flat
  or declining. Rakai is the standard example.
- **Expanding epidemic**. An HIV epidemic whose incidence is still rising or peaked
  recently, so its decline cannot yet be told apart from a temporary dip.

## Tags

- **care-seeking**: Who presents for STI or HIV services, when, and why, including symptomatic clinic visits, testing uptake, and barriers to access.
- **coinfection**: Biological interaction between concurrent infections, particularly the cofactor effect of curable STIs on HIV acquisition and transmission.
- **diagnostics**: Test performance, platforms, and deployment for identifying STI and HIV infections, from syndromic algorithms to point-of-care molecular assays.
- **economics**: Costing, cost-effectiveness, and the resource constraints under which a diagnostic or prevention intervention is decided.
- **hiv**: HIV epidemiology, incidence, prevalence, transmission dynamics, treatment, and prevention in the populations and settings relevant to the model.
- **immunity**: Acquired protection after infection or clearance, its strength and duration, and what it implies for reinfection and return to susceptibility.
- **modeling**: Mathematical and computational modeling methods, including agent-based simulation, network models, calibration, and validation.
- **partner-notification**: Tracing and notifying sexual partners of diagnosed individuals, its effectiveness, coverage, and role in STI and HIV control.
- **phylogenetics**: Viral sequence analysis used to infer who infects whom, the direction and rate of transmission between groups or places, and the structure of the transmission network.
- **prep**: HIV pre-exposure prophylaxis: efficacy, uptake, adherence, retention, and interaction with STI diagnostics as background prevention.
- **rakai**: Data, studies, and parameters from the Rakai Community Cohort Study and surrounding communities in south-central Uganda.
- **sexual-networks**: Partnership structure, concurrency, mixing patterns, degree distributions, and extra-couple contacts that shape STI and HIV transmission.
- **sti**: Epidemiology, natural history, treatment, and prevalence of the four curable bacterial STIs the model tracks: gonorrhoea, chlamydia, trichomoniasis, and syphilis.
- **study-concept**: Proposals, protocols, and trial designs: the pathways a study sets out to separate, the arms meant to separate them, and what each contrast is intended to isolate.
