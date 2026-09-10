---
type: entry
title: "Preexposure Prophylaxis for HIV Infection among African Women (FEM-PrEP)"
description: Null trial of daily oral TDF-FTC in 2120 high-risk African women, with placebo-arm HIV incidence of 5.0 per 100 person-years and baseline curable STI prevalence
author: Van Damme et al.
published: 2012-07-11
resource: 10.1056/NEJMoa1202614
local: raw/10.1056/nejmoa1202614
tags: [prep, hiv, sti, sexual-networks]
updated: 2026-09-10 00:38
---

FEM-PrEP was a randomised, double-blind, placebo-controlled trial of once-daily oral tenofovir disoproxil fumarate plus emtricitabine (TDF-FTC) in 2120 HIV-negative women aged 18-35 at four sites in Kenya (Bondo), South Africa (Pretoria, Bloemfontein) and Tanzania (Arusha), enrolled June 2009 to April 2011 and stopped early for futility on 18 April 2011. Eligibility required at least one vaginal sex act in the previous 2 weeks or more than one partner in the previous month, so the cohort is a general-risk rather than a formally defined key population, with 12.6% reporting sex for money or gifts with a non-primary partner in the previous 4 weeks. Extracted text sits in `raw/10.1056/nejmoa1202614`.

## Relevance to project

Two numbers travel into the model. The placebo-arm HIV incidence of 5.0 per 100 person-years (35 infections, 1407.4 person-years across both arms) bounds what "high-risk East and southern African woman aged 18-35" means as a force of infection, and sits well above the community-wide female incidence the Rakai calibration targets, so it is an upper comparator for the model's high-activity female stratum rather than a population target. The baseline curable STI prevalences give the co-infection burden a woman in that risk stratum carries at a single cross-section: chlamydia 14.0% (264/1887), gonorrhoea 5.7% (108/1887), trichomoniasis 5.8% (109/1893), syphilis 1.7% (36/2118), all in HIV-negative women at enrolment. Since the model carries all four of these pathogens on one network, that set is a joint prior for prevalence in a high-activity female stratum, and the sample is large enough that the pairwise proportions are usable together rather than one at a time.

The trial also supplies the null result that shapes how PrEP enters the SOC and POC arms. TDF-FTC as delivered here did nothing (hazard ratio 0.94, 95% CI 0.59 to 1.52), and the drug-level data say why: fewer than 40% of uninfected controls in the TDF-FTC arm had plasma tenofovir at or above 10 ng/mL, the threshold for a dose in the previous 48 hours. Efficacy is therefore not a property of the drug alone in this project, and a PrEP arm parameterised at trial-protocol efficacy without an adherence layer would be inconsistent with this evidence. Use the paper as the low anchor on effective PrEP coverage in women, paired with the Partners PrEP figures cited here (81-83% detectable drug in uninfected controls) as the high anchor.

What it cannot supply: no STI incidence, since fewer than half of participants agreed to a pelvic examination after randomisation, and end-of-study STI testing covered only the subset who presented. No partner data, no network structure, and no HIV-STI co-infection cross-tabulation beyond the pre-specified subgroup split below.

## Key points

- No efficacy signal in any analysis. Primary hazard ratio 0.94 (0.59-1.52, P = 0.81); censoring at last drug availability gave 0.82 (0.49-1.36); including all post-randomisation infections gave 0.87 (0.55-1.38). Cumulative probability of infection at 12 months 0.049 (TDF-FTC) versus 0.046 (placebo).
- Adherence measured three ways diverged sharply. Self-report 95% "usually or always", pill counts consistent with ingestion on 88% of available days, plasma tenofovir at target in 24-37% of uninfected controls depending on the visit. Self-report and pill counts are uninformative here.
- A pre-specified subgroup on baseline gonorrhoea, chlamydia or syphilis gives HIV incidence 4.7 per 100 person-years in TDF-FTC and 8.0 in placebo among the STI-positive (small: 6 and 8 events on 186 and 156 participants), versus 4.6 and 4.1 among the STI-negative (722 and 771 participants). The direction is consistent with an STI cofactor effect on HIV acquisition, but the event counts are too small to carry a magnitude.
- Bacterial vaginosis prevalence at baseline was 41.8% (785/1877), higher than any of the four curable STIs; the model does not represent it.
- Side effects were modest and consistent with low uptake: nausea 4.9% vs 3.1%, vomiting 3.6% vs 1.2%, any ALT elevation 11.4% vs 8.6%. Lab abnormality prompting drug interruption or discontinuation 4.7% vs 3.0% (P = 0.05).
- Emtricitabine resistance appeared in 4 of 33 seroconverters in the TDF-FTC arm (M184V or M184I) and 1 of 35 in placebo. No tenofovir-resistance mutations (K65R, K70E) in either arm.
- No risk compensation. Reported partners, vaginal sex acts, and condomless sex all fell modestly by the last visit, and end-of-study STI prevalence did not differ between arms.

## Limitations

Low adherence makes this an uninformative test of the drug and an informative test of the delivery model. The trial was powered on 72 infections assuming 70% risk reduction and 3% annual placebo-arm infection; observed incidence was higher than assumed but enrolment stopped at 2120 of a planned 3900, so no efficacy conclusion survives. 12.5% were lost to follow-up and another 5.3% discontinued early, leaving 82.1% in the primary end-point analysis, and the missing final HIV tests admit a differential-acquisition explanation that cannot be excluded.

Contraception was mandated and non-barrier: 66.1% on injectables and 30.1% on oral pills at enrolment, an unusual profile that also drove the oral-contraceptive imbalance between arms and a pregnancy rate of 29.0 per 100 person-years among oral-pill users. Any transfer of the incidence figure to a modelled population should note that the cohort was selected for willingness to use non-barrier contraception.

The STI prevalences are single-cross-section, syndromic-independent laboratory diagnoses at enrolment among women who passed screening for hepatitis B surface antigen and normal hepatic and renal function, so they describe a screened trial population, not a clinic or community denominator.
