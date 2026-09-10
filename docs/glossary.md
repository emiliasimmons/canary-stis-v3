# Glossary

- **POC arm**. The intervention arm: point-of-care. An etiological test-and-treat panel
  that replaces syndromic management at the same symptomatic care-seeking door, switched
  on at `pars.intv_year`. Not an asymptomatic screening programme.
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
- **Target product profile**. A specification of what a test must achieve to be useful,
  agreed by expert consensus and given as a minimal and an optimal value per
  characteristic. See
  [pages/toskin-2017-sti-poct-target-product-profiles.md](pages/toskin-2017-sti-poct-target-product-profiles.md).

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
