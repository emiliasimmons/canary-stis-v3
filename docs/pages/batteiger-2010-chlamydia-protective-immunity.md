---
type: entry
title: "Protective Immunity to Chlamydia trachomatis Genital Infection: Evidence from Human Studies"
description: Review of human evidence that genital chlamydia infection confers partial protective immunity, and that early treatment may blunt it.
author: Batteiger et al.
published: 2010-04
resource: 10.1086/652400
local: raw/10.1086/652400
tags: [sti, immunity, coinfection]
updated: 2026-09-10 00:12
---

Source: [batteiger-2010](https://doi.org/10.1086/652400)

Narrative review commissioned for the CDC Chlamydia Immunology and Control Expert Advisory
Meeting (April 2008), published in a *Journal of Infectious Diseases* supplement. It asks
whether humans acquire protective immunity to genital *Chlamydia trachomatis*, whether
prompt antibiotic treatment attenuates that immunity, and which laboratory measures track
it. An Ovid Medline search (1950 onward, English, ages 1-65) narrowed 1287 titles to 209,
then to 108 read in detail by four reviewers. No human challenge studies exist, so every
inference is indirect.

## Relevance to project

Two uses, both structural rather than numeric.

The first is a prior on untreated chlamydia duration and on whether the model needs any
immunity state at all. The clearance figures the review assembles (45-55% of untreated
asymptomatic infections in women cleared by 1 year, 94% by 4 years; 44% of infections in
pregnant women cleared within 2-3 months) put untreated duration on a months-to-years
scale, an order of magnitude longer than the weeks seen in mouse models. Whatever
immunity does develop is partial: reinfection is common, and prior infection is one of the
strongest predictors of the next one. That supports modelling chlamydia with full return
to susceptibility after clearance, at most a short partial reduction in per-act
acquisition, and treating any stronger immune protection as out of scope.

The second bears directly on the POC arm. The review's organising hypothesis is that
screen-and-treat programmes shorten infection duration, blunt the protective response, and
raise reinfection risk, offering an explanation for programmes (Vancouver, Finland) where
prevalence fell and then rebounded. If real, this is a mechanism working against the POC
arm: an etiological test-and-treat panel replacing syndromic management shortens
chlamydia episodes precisely as the hypothesis requires. The human evidence is not strong
enough to parameterise (see Limitations), so this belongs as a named sensitivity direction
on chlamydia rather than as a term in the base case. The only quantitative anchor is
animal: in mice, doxycycline started 0-10 days after inoculation lengthened post-rechallenge
shedding, worse the earlier treatment began.

Partnership concordance figures are usable as a soft comparator for the model's
within-partnership transmission, though the review reports them to argue about immunity, not
transmission probability. Across 494 STD-clinic partnerships screened by NAAT, both partners
were positive in 68% of those with at least one positive; 76% in a second clinic sample of
106 partnerships; 65% in a Boston contact-tracing study where direction was inferred
male-to-female, against 73% for gonorrhoea in the same study. In 1690 asymptomatic
community couples in German gynaecology practices, only 27 of 78 couples with a positive
partner (35%) were concordant, and concordance fell with age. The clinic-versus-community
gap is large enough that a model calibrated to one will miss the other.

Nothing here is a calibration target for the Rakai site, and the review supplies no
transmission probabilities, no HIV cofactor estimate, and no diagnostic performance data.

## Key points

Prevalence, organism load, and couple concordance all fall with age, the pattern usually
read as acquired immunity. The review is careful that age also tracks cervical ectopy and
partner numbers, and that gonorrhoea shows the same inverse age gradient while conferring
almost no immunity (extensive antigenic variation). One large STD-clinic study (n=14,605)
found age an independent inverse predictor of culture positivity in multivariate analysis,
holding even among people known to have been exposed, but serologic and PBMC blastogenic
responses did not correlate with age. In 1231 high-risk women, quantitative endocervical
culture load was inversely related to age with cervical ectopy not associated.

Repeat infection is the rule. Median time to recurrence 5-7 months; 26.3% cumulative
repeat infection at 1 year in school-based health centres, 59.6% at 18 months in
community-based centres, 13.4% at a mean 4.3 months when repeats were sought at scheduled
visits. Resumption of sexual activity was the strongest correlate in the last of these,
and baseline chlamydia infection was the strongest predictor of incident infection among
sex workers.

Serovar-specific immunity has little support. Same-serovar repeats ran 33.8% observed
against 18.4% expected from the serovar distribution in one clinic series, 44.8% in
adolescent women. Among Nairobi sex workers, 13 of 21 repeats (62%) within 1-6 months
were the same genotype versus 2 of 19 (11%) later, but a larger adolescent study found the
late different-genotype infections explained by partner change.

The one longitudinal marker of protection: in a Nairobi sex worker cohort of 299 women
followed for incident chlamydia, all 29 women with baseline IFN-gamma production by PBMCs
stimulated with chlamydial heat-shock protein 60 (cHSP60) remained uninfected over 24
months. IFN-gamma to whole elementary bodies carried no such protection, and neither serum
nor endocervical IgG/IgA to elementary bodies or cHSP60 was protective; antibody looks
like a marker of past infection, and high anti-cHSP60 titres track sequelae.

Population-level circumstantial evidence. Vancouver: among 33,917 infected individuals,
relative reinfection rates rose across 1989-2003 after a screening programme, most in
young people and women. Finland (8000 maternity-cohort sera): IgG seroprevalence in women
under 23 fell from 16.0% (1990-1996) to 10.6% (1997-2003), and in women 23-28 from 19.1%
to 12.5%, while reported cases rose from 8031 (1995) to 12,863 (2003).

Co-factors the review notes in passing: concurrent gonococcal infection is associated with
recurrent chlamydia and with higher endocervical chlamydial shedding; bacterial vaginosis
is a risk factor for acquiring both chlamydia and gonorrhoea, with hydrogen-peroxide-producing
lactobacilli protective. Among HIV-infected Nairobi sex workers, entry CD4 count below 400
cells/mm3 marked the highest risk of chlamydial PID, and HIV-infected women produced less
IFN-gamma on chlamydial stimulation. One cohort found HIV status associated with incident
chlamydia independent of CD4; a later cohort in the same population did not.

## Limitations

The review's own: some informative articles may have been missed, and it cites
representative rather than exhaustive examples of each evidence type.

Bearing on the uses above. No human study establishes the minimum infection duration
needed to confer protection, or the point in an infection after which treatment no longer
blunts the response, so the treatment-attenuates-immunity mechanism cannot be given a
functional form from this source. The Vancouver reinfection trend has an arithmetic
alternative explanation the authors concede: reinfections must accrue as a share of total
infections once a screened population is rescreened, and neither infection duration before
treatment nor the test-to-treatment interval was reported. Rising case counts alongside
falling seroprevalence are equally consistent with wider screening coverage and the switch
to NAATs. Most concordance and load studies are cross-sectional and clinic-based, where
partner numbers and exposure intensity are high and confounded with age. Sex worker
cohorts are the design most able to detect immunity because exposure is high and
sustained, and are the least generalisable to a general-population cohort. The trachoma
material rests on continuous ocular exposure among young children, a transmission process
unlike episodic sexual exposure, and the trachoma reinfection study treated at most 11% of
infected people in the intervention communes.
