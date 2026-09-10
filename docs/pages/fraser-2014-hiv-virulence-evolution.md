---
type: entry
title: "Virulence and pathogenesis of HIV-1 infection: an evolutionary perspective"
description: Review arguing viral genotype explains ~33% of set-point viral load variance, with SPVL sitting near the value that maximizes transmission potential.
author: Fraser et al.
published: 2014-03-21
resource: https://doi.org/10.1126/science.1243727
local: ../raw/10.1126/science.1243727
tags: [hiv, modeling]
updated: 2026-09-10 00:35
---

A *Science* review of why untreated HIV-1 infection progresses fast in some people and
slowly in others, framed as a conflict between selection inside the host and selection
between hosts. Its organising quantity is set-point viral load (SPVL), the roughly stable
plasma viral load during asymptomatic infection, which ranges from under 20 to about 10^6
virions per mL and predicts both infectiousness and time to AIDS. The extracted text is at
`raw/10.1126/science.1243727/content.md`.

## Relevance to project

Context and a structural justification for what the HIV module leaves out, not a
calibration target.

The model treats HIV infectiousness as a function of stage and treatment status, with no
per-infection viral-genotype effect. This review is the argument that such an effect is
real and moderate: viral genotype explains 33% (95% CI 22-45%) of SPVL variance in
heterosexual couples in sub-Saharan Africa, against about 13% for host genome-wide
variants (22% adding age and sex). That is enough to say individual infectiousness carries
a heritable component the model does not represent, and small enough that a
network-and-stage model of HIV incidence is not obviously mis-specified by omitting it.
Treat it as a caveat on any claim about heterogeneity in per-act transmission, since some
of the spread the model attributes to behaviour and stage is viral-genetic.

Two secondary uses. The Rakai contribution to the pooled heritability estimate is
Hollingsworth et al. 2010, 97 transmission couples, 36% (6-66%), adjusted for age, sex,
subtype, and symptomatic genital ulcer disease; the adjustment set is a reminder that
symptomatic STI and GUD are treated as confounders of viral load in this literature. And
the paper's Figure 1C relationship, infectiousness rising with SPVL while time to AIDS
falls, is the shape behind stage-structured HIV infectivity generally, though the
numerical curves live in Fraser et al. 2007, not here.

Nothing here bears on STI diagnostics, syndromic versus etiological management, or the
POC/SOC contrast.

## Key points

Heritability of SPVL was disputed across an order of magnitude, from Yue et al.'s 2% to
Alizon et al.'s >50%. The authors attribute the spread to inconsistent definitions rather
than cohort differences, and re-analyse four sub-Saharan African transmission-couple
studies on one framework: Tang (Zambia, 115 couples) 36% (12-60%), Hollingsworth (Uganda,
97) 36% (6-66%), Lingappa (Partners in Prevention, 14 East and Southern African sites,
141) 44% (19-69%), Yue (Zambia, 195) 26% (8-44%). Weighted summary over 548 couples: 33%
(22-45%).

The 33% viral figure and the 13% host figure are not directly comparable. The viral
estimate is broad-sense heritability, capturing the total genotype effect including
interactions; the GWAS figure is narrow-sense, summing individual SNP contributions, and
broad-sense is always the larger of the two. Host-virus interaction variance may be
double-counted across the two.

SPVL as a life-history trait: infectiousness per contact rises with SPVL while
asymptomatic lifespan falls, so transmission potential (the product) peaks at an
intermediate value. The observed SPVL distribution clusters near that peak, which the
authors read as the virus having evolved to maximize onward infections.

Candidate viral virulence factors are replicative capacity and the capacity to induce CD4+
T-cell activation (*nef*, *vpr*, *tat*, *env*). Elite controllers in one cited study shared
only infection by low-replicative-capacity virus; compensatory mutations restoring
replicative capacity later in infection did not reliably raise viral load, which points to
early events fixing SPVL.

Three non-exclusive mechanisms reconcile fast within-host evolution with heritability
across transmissions: slow evolution of replicative capacity on a rugged fitness
landscape; viral load factors that are neutral within-host, such as systemic target-cell
activation acting as a public good no single strain profits from; and preferential
transmission of founder-like virus retrieved from the long-lived latent reservoir.

Widespread antiretroviral treatment shifts the transmission trade-off and could select for
higher virulence. Set-point viral loads have risen in some heavily treated populations,
though observations are inconsistent, and the authors judge any such increase slow, limited,
and no reason to change treatment or prevention priorities.

## Limitations

A review, so nothing here is a primary measurement made by these authors; the pooled 33%
comes from re-analysing four published couple studies, all heterosexual and all sub-Saharan
African, and heritability is population-dependent, so the number does not transfer to a
low-diversity or epidemiologically young epidemic.

Transmission-pair designs assume the presumed donor is the actual source, and viral load is
measured in blood while sexual transmission happens at the genital mucosa, a mismatch the
authors flag themselves.

No viral whole-genome association study has yet identified the virulence factors the
argument requires; the largest cited (N=698) found nothing significant and was powered only
for variants explaining 4% of SPVL variance.

All calculations exclude treatment effects, deliberately, so the transmission-potential
optimum describes untreated natural history and not a population on ART.
