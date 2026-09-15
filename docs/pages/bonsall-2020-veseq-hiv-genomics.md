---
type: entry
title: A Comprehensive Genomics Solution for HIV Surveillance and Clinical Monitoring in Low-Income Settings
description: veSEQ-HIV, a 30 GBP whole-genome HIV sequencing assay validated on 1,620 Zambian plasma samples, giving viral load, drug resistance, and directed transmission networks from one test.
author: Bonsall et al.
published: 2020-09-22
resource: https://doi.org/10.1128/JCM.00382-20
local: raw/10.1128/jcm.00382-20
tags: [hiv, diagnostics, sexual-networks]
updated: 2026-09-10 00:15
---

Source: [bonsall-2020](https://doi.org/10.1128/JCM.00382-20)

A laboratory and computational protocol paper describing veSEQ-HIV: probe-based bait capture
of HIV RNA from leftover plasma, Illumina short-read sequencing, and a pipeline (shiver for
consensus and minority variants, phyloscanner for contaminant removal and transmission
inference, Stanford HIVdb for resistance calls). Validated on 1,620 plasma samples from
adults aged 18+ attending 10 urban clinics in 9 Zambian communities of the HPTN 071 (PopART)
trial, using residual blood drawn for routine CD4 counts.

## Relevance to project

Context and a cost comparator, not a parameter source. Nothing here is an STI diagnostic
and nothing feeds a calibration target.

Two concrete uses. First, a price anchor for what molecular testing costs in a
sub-Saharan field programme: 30 GBP per sample in 2020 for reagents, consumables, and
technician labour, excluding laboratory setup, which the authors put at roughly a third of
the 2015 WHO budgeted cost for HIV pol sequencing. That sits far above any point-of-care STI
panel price the POC arm would assume, and is useful mainly to bound the "molecular testing in
an LMIC clinic" end of the cost range.

Second, a methods reference for the network-position pathway. The project asks how much HIV
impact comes from identifying high-transmission positions in the sexual network. This paper
is the empirical instrument behind directed transmission-pair inference in that literature
(phyloscanner ancestral-state reconstruction over 373 overlapping 340-bp windows, giving
transmitter/recipient direction), so it explains what an observed transmission network
in these settings can and cannot resolve. It supplies no network statistics of its own:
no degree distribution, no partnership durations, no cluster sizes.

## Key points

- Whole genomes (>8,000 bp at read depth >=5) from 1,297/1,424 samples (91%) with sequence-derived
  viral load >1,000 copies/ml, and from all 1,204 samples above 10,000 copies/ml. Lowest viral load
  yielding a whole genome was 4,300 copies/ml.
- Sequence-derived viral load tracks the clinical assay (Roche AmpliPrep/TaqMan) with R-squared 0.89
  on 146 samples, mean squared prediction error 0.324 log10 copies/ml, detection limit around
  50 copies/ml.
- Probe capture rather than HIV-specific PCR keeps it unbiased across subtypes: 86% (1,282/1,498)
  of subtype C samples gave complete genomes, with A, D, G, and J also recovered.
- Contaminant read removal ("phyloscanner clean") blacklisted 1.2% of HIV reads; in spike-in
  experiments sensitivity was 95.6% (262/274) and specificity over 99.9% (291,742/291,815).
- Throughput of 350-360 samples per technician per week.

## Limitations

- Not licensed for clinical viral load, genotyping, or resistance testing. Concordance evidence
  comes from a separate HPTN 078 validation, which recovered complete resistance information in
  93.3% of samples above 5,000 copies/ml.
- Sequencing was done in the UK, not in Zambia; only extraction and transport happened in country.
  Reagent supply chains and maintenance are named as the barrier to LMIC deployment.
- The 30 GBP figure excludes capital: equipment, ground rent, and maintenance.
- Sampling frame is people not currently on ART who consented to an ancillary phylogenetic
  study, so the viral load distribution is not representative of the treated population.
