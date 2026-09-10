---
type: entry
title: Reductions in HIV incidence are likely to increase the importance of key population programmes for HIV control in sub-Saharan Africa
description: Commentary arguing that as HIV incidence falls, transmission concentrates in high-risk core groups, so acquisition-side risk factors misdirect prevention.
author: Geoff P Garnett
published: 2021-06
resource: 10.1002/jia2.25727
local: raw/10.1002/jia2.25727
tags: [hiv, sexual-networks, modeling]
updated: 2026-09-10 00:14
---

A five-page commentary in the Journal of the International AIDS Society by Garnett (Gates Foundation), reasoning from transmission-dynamic first principles rather than new data. Extracted text sits at `raw/10.1002/jia2.25727/content.md`. It carries one table defining R0, Rt, the incidence/mortality ratio, the core group, risk factors, and the population attributable fraction, each with how the quantity is expected to move as HIV comes under control in sub-Saharan Africa.

## Relevance to project

A structural justification for two choices the model already makes, and a warning about how its outputs should be read.

First, risk-structured mixing is not optional. The argument is that heterogeneity in contact rates and in per-contact transmission raises R0 while lowering the prevalence at which the epidemic saturates, and that as an epidemic is pushed down, remaining transmission chains persist only where the local reproduction number stays above one. In a model whose whole question is where POC diagnostics buy the most HIV prevention, the answer is driven by that structure: a homogeneous network would let any incidence reduction look like progress toward elimination, and would erase the high-transmission positions the project is trying to identify.

Second, it separates the two attribution questions the project needs to keep apart. Risk of acquisition and risk of transmission are different variables, and measuring who acquires HIV overstates acquisition risk and understates transmission risk; with heterogeneity, most people acquiring infection are of only moderate risk. The recommended measure is the transmission population attributable fraction (tPAF), computed by running the model with and without a risk factor and comparing epidemics over time. That is directly the counterfactual design for the project's decomposition of POC impact into direct STI treatment, prevention targeting, and network-position identification. The commentary also states that remaining risk factors carry a higher tPAF as HIV is better controlled, which bears on how the POC-versus-SOC contrast should be expected to move over a long simulated horizon rather than at one time point.

Third, a caution for interpretation. Rt below one with incidence declining does not imply elimination unless R0 is also below one, so a simulated incidence decline is not by itself evidence of a durable effect. Relaxing an intervention can restore Rt to one at a new, lower endemic steady state.

It supplies no calibration targets, no priors, and no diagnostic performance numbers. It is not evidence for the STI cofactor effect, which it does not discuss. The trend figures it quotes are UNAIDS regional aggregates cited in passing, not estimates of its own: new infections per year down 38% over the decade to 2019 in Southern and Eastern Africa and 25% in Western and Central Africa, with 2019 ART coverage among adults living with HIV of 78% of women and 65% of men in Southern and Eastern Africa and 67% and 49% in Western and Central Africa. Use those for orientation only.

## Key points

Categorizing sub-Saharan epidemics as "generalized" pushed resources into undifferentiated mass testing and treatment and let key populations (men who have sex with men, transgender women, people who inject drugs, sex workers, prisoners) go under-served; the systematic review Garnett cites found insufficient treatment-cascade data on these groups at all.

Aggregate ART coverage can mask untreated subpopulations, which the commentary offers as one explanation for the mismatch between model-predicted and observed HIV declines.

Mixing structure decides reach: if high-transmission-likelihood people mix freely with lower-likelihood people, infection spreads further; constrained mixing keeps it inside the high-risk group. As average transmission risk falls (for example through treatment), the core group shrinks and requires more extreme behaviour to sustain transmission.

Preventing infection in people with both high acquisition and high transmission risk can prevent infections among moderate-risk people. The worked example is age-disparate: young women in sub-Saharan Africa acquire HIV more but transmit less than the older men they partner with, so preventing acquisition in those men also protects the women.

Two empirical routes to establishing how much key populations drive ongoing spread: phylogenetics on representative virus samples, or detailed sexual-network models reconstructing observed trends. Both need reliable population-size and behaviour data from surveys or partner notification.

Cost-effectiveness comparison is between packages, not tools. Focused interventions can cost more per person reached and still be cheaper overall because fewer people need reaching; population-wide delivery is cheaper per person and better integrated but wasted if it misses or fails among those most at risk.

Integrating HIV into universal health coverage risks dropping exactly the services key populations need, naming pre-exposure prophylaxis and treatment-assisted management of drug use disorders.

## Limitations

A commentary, not a study: no data collection, no model runs, no quantitative estimates of its own. Every figure in it is cited from elsewhere.

Its key populations are the standard five, and it concedes directly that uncertainty remains about their role in the high-prevalence epidemics of rural sub-Saharan Africa for lack of data. The project's first calibration site is a rural population-based cohort, so the commentary's programmatic conclusions do not transfer there without local evidence.

The argument is qualitative throughout. It gives no functional form, no elasticity, and no parameter that could be lifted into the model. Its use here is to justify structure and to name the tPAF counterfactual, and no more than that.

It also notes that risk of acquiring or transmitting HIV is not the same thing as the social or cultural identity used to define a key population, and that members may be mischaracterized or misperceive their own risk. A model that indexes risk on network position rather than on group membership sidesteps that mismatch, but any comparison of its risk groups to programmatically defined key populations inherits it.
