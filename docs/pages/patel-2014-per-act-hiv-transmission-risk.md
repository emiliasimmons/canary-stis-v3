---
type: entry
title: "Estimating per-act HIV transmission risk: a systematic review"
description: CDC synthesis of per-act HIV acquisition probabilities by exposure route, 8 per 10,000 receptive and 4 per 10,000 insertive penile-vaginal, plus relative risks for genital ulcer disease, viral load, stage, condoms, circumcision and ART
author: Patel et al.
published: 2014-06-19
resource: https://doi.org/10.1097/QAD.0000000000000298
local: raw/10.1097/qad.0000000000000298/
tags: [hiv, coinfection, prep]
updated: 2026-09-10 10:34
---

CDC's update of its 2005 per-act HIV transmission risk estimates, drawing mainly on published meta-analyses rather than pooling primary studies afresh, with new fixed-effects inverse-variance pooling only where no current meta-analysis existed (anal intercourse, needle sharing). Searches covered 2008 to 2012 for transmission risk and 2008 to May 2013 for modifying factors. Estimates were deliberately weighted toward high-income-country data to match the US epidemic. Extracted content in [raw/10.1097/qad.0000000000000298/](../raw/10.1097/qad.0000000000000298/).

## Key points

- Per-act acquisition risk from an infected source, per 10,000 exposures, assuming no condom: receptive penile-vaginal 8 (95% CI 6-11), insertive penile-vaginal 4 (1-14), receptive anal 138 (102-186), insertive anal 11 (4-28), receptive and insertive oral low with an upper bound of 4 (no transmissions in 8,965 receptive oral acts). Blood transfusion 9,250 (8,900-9,610), mother-to-child 2,260 (1,700-2,900), needle sharing 63 (41-92), percutaneous needle stick 23 (0-46).
- The penile-vaginal estimates come from a meta-analysis of 10 high-income-country studies, nine of them pre-HAART, and describe the asymptomatic phase of infection. Meta-regression adjusting for cofactors attenuates the two-fold receptive-versus-insertive difference toward parity.
- Cofactors raising per-act risk, as relative risks: genital ulcer disease 2.65 (1.35-5.19); each log10 copies/ml of plasma viral load 2.89 (2.19-3.82); acute versus asymptomatic stage 7.25 (3.05-17.3); late versus asymptomatic stage 5.81 (3.00-11.4). The stage multipliers are from the Rakai per-coital-act study.
- Cofactors lowering it: condom use 0.20 (0.08-0.47); ART in the infected partner 0.08 (0.00-0.57) for treated versus untreated and 0.04 (0.01-0.27) for early versus delayed; oral PrEP 0.29 (0.17-0.47) in heterosexual couples, 0.56 (0.37-0.85) in MSM, 0.52 (0.28-0.90) in people who inject drugs; male circumcision 0.50 (0.34-0.72) when the uninfected partner is the man, and 0.80 (0.53-1.36), not significant, when she is the woman.
- Condoms and ART together were estimated to cut per-act risk by up to 99.2%, computed by multiplying the two relative risks and treating their covariance as zero.
- Receptive anal risk rose 1.8-fold against the 2005 CDC figure of 50 per 10,000, which had been extrapolated as five times the receptive vaginal risk rather than measured.

## Relevance to project

The default per-act transmission probability for the HIV component: 8 per 10,000 for receptive and 4 per 10,000 for insertive penile-vaginal contact in the asymptomatic phase, with 95% intervals wide enough (1-14 for insertive) to serve directly as calibration bounds rather than fixed values.

The cofactor table is the more useful half. Genital ulcer disease at RR 2.65 (1.35-5.19) is a prior for the syphilis cofactor on HIV acquisition, and the stage multipliers (acute 7.25, late 5.81 against asymptomatic) set the infectiousness profile the model needs over the course of untreated infection. Male circumcision at 0.50 and ART at 0.08 are the background prevention effects that have to be in the SOC arm before the POC arm can be credited with anything.

Two limits on that use. The cofactor is genital ulcer disease as a syndrome, so it covers HSV-2 and syphilis and says nothing about the discharge-causing STIs (gonorrhoea, chlamydia, trichomoniasis) that make up most of the model's STI burden. And these are relative risks lifted from separate primary studies, each with its own adjustment set, then multiplied together, so stacking several of them in a model compounds assumptions the review did not test.

## Methodology

Pooling used fixed-effects inverse-variance models on the log scale, back-transformed. Combined-effect estimates (condoms plus ART) multiply independent relative risks and assume zero covariance to first order. The authors note they used efficacy for treatment and effectiveness for condoms interchangeably, which overstates the treatment effect.

## Limitations

- Built for the US epidemic. Low-income-country data were judged too heterogeneous to pool with high-income data for penile-vaginal and vertical transmission and were excluded, so nothing here is calibrated to sub-Saharan African populations.
- The penile-vaginal estimates rest on pre-HAART partner studies from the late 1980s and 1990s, where exposure counts came from self-reported coital frequency and partners' HIV status was often unknown.
- Per-act risk is not a fixed biological constant. The authors state these estimates may not reflect true infectivity, because they average over viral load, stage, and coinfection within each study population.
- No point estimate for oral sex was possible.
- Confidence intervals overlap heavily across sexual exposure routes, so ordering the routes by point estimate carries more precision than the data support.
