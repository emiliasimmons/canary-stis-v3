---
type: entry
title: "Multiplexed rapid technologies for sexually transmitted infections: a systematic review"
description: Diagnostic accuracy of commercialised multiplexed RNAAT platforms and immunochromatographic POC tests across CT, NG, TV, syphilis, and other STIs
author: Karellis et al.
published: 2022-04-01
resource: 10.1016/s2666-5247(21)00191-9
local: raw/10.1016/s2666-5247(21)00191-9/content.md
tags: [sti, diagnostics]
updated: 2026-09-10 09:45
---

Systematic review of 24 studies (26,126 individuals) evaluating 17 multiplexed rapid
nucleic acid amplification test (RNAAT) platforms and 7 immunochromatographic devices for
simultaneous detection of multiple STIs. Published in *Lancet Microbe*. Studies were
published between 2009 and 2020, conducted across Europe (9), Africa (6), Asia (3), North
America (3), South America (2), and Australia (1). All were observational.

## Relevance to project

The model's POC arm replaces syndromic management with an etiological test-and-treat panel.
This review supplies the real-world sensitivity and specificity envelope for the multiplexed
platforms that such a panel would use, specifically for the four curable STIs the model
tracks (CT, NG, TV, syphilis). The data inform the `sens` and `spec` parameters on each
pathogen in the intervention: what fraction of true infections a POC test detects (feeding
treatment probability) and what fraction of uninfected individuals it correctly excludes
(bounding overtreatment).

For the RNAAT platforms closest to point-of-care use (GeneXpert CT/NG in particular), the
review reports sensitivity and specificity both above 97% for CT and NG on vaginal and
urine specimens, consistent with the
[target product profiles](toskin-2017-sti-poct-target-product-profiles.md) optimal
thresholds. Immunochromatographic tests cover syphilis (SD Bioline HIV/Syphilis Duo)
with sensitivity 86-100% and specificity 99-100% depending on specimen and population.

The review does not report time-to-result distributions, cost per test, or operational
feasibility in low-resource clinics, so it cannot directly parameterise the care-seeking
delay or cost layers of the model.

## Key points

- RNAAT platforms: 66% of sensitivity entries were at least 95%, and 45% of specificity
  entries were 100%. Multiple platforms achieved 100%/100% for CT and NG on select specimen
  types.

- GeneXpert CT/NG (the device with the most field-based evidence for near-POC use)
  showed sensitivity and specificity both above 97% for CT and NG across studies in
  Australia, South Africa, and Zimbabwe, on vaginal and urine specimens.

- Immunochromatographic tests (handheld, no laboratory infrastructure): all 18 specificity
  entries exceeded 95%. The SD Bioline HIV/Syphilis Duo Test detected *T. pallidum* with
  sensitivity 86-100% and specificity 99-100% across four studies in pregnant women and
  outpatient populations.

- TV detection by RNAAT showed sensitivity 83-100% and specificity 90-100%, with BD Max
  CT/GC/TV on vaginal specimens at 96%/99%.

- Performance varied by pathogen, specimen type, population screened, and co-infection
  prevalence. The same device (Anyplex II STI-7) on the same reference test showed CT
  sensitivity of 85% in one population and 93-100% in another.

- No commercialised multiplexed RNAAT platform yet covers CT, NG, TV, and syphilis in a
  single cartridge. RNAAT platforms detect the bacterial trio (CT, NG, TV) while
  immunochromatographic tests handle syphilis and HIV.

## Limitations

- All 24 studies were observational. No RCTs assessed impact or cost-effectiveness of
  deployment.

- Wide confidence intervals on many entries due to small sample sizes and low prevalence of
  some pathogens in some study populations.

- Heterogeneity in reference standards across studies (culture, different NAAT assays, PCR
  variants) makes direct cross-device comparison imprecise.

- The review covers commercialised tests through April 2020. Newer multiplex cartridges
  (e.g., Cepheid CT/NG/TV, binx io CT/NG) post-date the search window.

- No sub-Saharan African study evaluated a full four-pathogen RNAAT panel, limiting direct
  applicability to the RCCS setting.

## Methodology

MEDLINE and Embase search, January 2009 to April 2020. Included commercialised multiplex
rapid tests (RNAAT or immunochromatographic) used on human participants in clinical care.
Excluded pre-collected specimens, case series, and case reports. Quality assessed with
QUADAS-2. Registered in PROSPERO (CRD4202179218). Sensitivity and specificity reported per
device, per pathogen, per specimen type, with 95% confidence intervals.
