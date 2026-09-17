# Canonical Figures in HIV Transmission Modeling: A Taxonomy with Named Examples

## TL;DR
- HIV modeling papers recycle roughly a dozen recognizable figure archetypes: calibration overlays (model line + ribbon over survey dots), counterfactual/averted-infection projections, care-cascade bars, transmission-attribution (tPAF) plots, cost-effectiveness planes/CEACs, sensitivity tornadoes/PRCC, compartment/network schematics, age-sex stratified panels, multi-model comparison grids, and subnational maps.
- The best canonical exemplars are named and reproducible: Granich 2009 (Lancet) elimination curve; Eaton 2012 (PLOS Medicine) 12-model comparison; Stone 2021 (JIAS) FSW/client tPAF; Akullian 2020 (Lancet HIV) EMOD eSwatini; Thembisa, Spectrum/Goals, Optima, Naomi, and DMPPT2 (VMMC).
- Conventions are stable: calibration targets shown as points with error bars while model output is a line with 50/80/95% credible ribbon; time horizons of 1990–2030/2040; status quo/no-ART drawn as a dashed or grey reference; the region between baseline and scenario shaded as "infections averted."

## Key Findings

The domain has a shared visual grammar. A reader can identify the figure type before reading the caption because axis choices, encodings, and reference-line styling are highly conventionalized. Below is the taxonomy, each entry giving axes, encoding, the scientific question, recognizability cues, and named examples with figure locations.

## Details

### 1. Model fit / calibration plots
- **Axes:** x = calendar year (typically 1990–2025); y = HIV prevalence (%) or incidence (per 100 or per 1000 person-years), or PLHIV/ART counts.
- **Encoding:** solid model line + shaded credible-interval ribbon; empirical calibration targets overlaid as discrete points with vertical error bars (survey CIs). Multi-panel by sex and age band is standard.
- **Question:** does the model reproduce observed epidemiology well enough to be trusted for projection?
- **Recognizability:** points-with-whiskers (data) sitting on top of a line-with-ribbon (model); paneled men vs women.
- **Named examples:** Thembisa provincial and national calibration panels (Johnson, Dorrington); EMOD-HIV calibration "(a) National HIV prevalence in women and men 15–49; (b) National HIV incidence" in Moolla et al. 2023 (BMC Public Health, five-model comparison). Naomi (Eaton et al. 2021, JIAS) shows model estimate as thick black dash with 95% CrI plus narrow 80% posterior predictive intervals against survey observations. Calibration targets in this domain are DHS, PHIA/ZIMPHIA, ANC sentinel surveillance, and Spectrum/EPP outputs.

### 2. Counterfactual / intervention-impact projections
- **Axes:** x = year (often extending to 2030/2040/2050); y = incidence, new infections, or cumulative infections.
- **Encoding:** baseline/status quo curve vs one or more scenario curves; the area between them shaded as "infections averted." Status quo styled as dashed or grey.
- **Question:** how many infections/deaths does an intervention avert versus doing nothing (or current practice)?
- **Recognizability:** two-plus diverging curves with a shaded wedge; a "no-ART counterfactual" or "constant 2016 coverage" reference.
- **Named examples:** Granich et al. 2009 (Lancet 373:48–57), the field's founding elimination figure, plotting universal test-and-treat driving incidence below the 0.1/100 person-year elimination threshold (both Granich and later Akullian use "an incidence of less than 0·1 per 100 person-years" as the epidemic-control threshold). Eaton et al. 2012 (PLOS Medicine 9:e1001245) Figure 1 = incidence/prevalence under no-ART counterfactual across 12 models; Figure 2 = intervention scenario (CD4≤350, 80% access, 85% retention). Optima global model (Lancet HIV 2018) plots status quo vs optimized-allocation new-infection trajectories to 2030.

### 3. Infections-averted / cumulative-impact bar charts and percent-reduction plots
- **Axes:** x = scenario or subgroup; y = infections averted, % incidence reduction, or infections averted per unit resource.
- **Encoding:** grouped/stacked bars, often with CI whiskers; sometimes disaggregated by sex or country.
- **Question:** which scenario or targeting strategy yields the most impact, and how efficiently?
- **Named examples:** Njeuhmeli et al. 2011 (PLOS Medicine 8:e1001132) VMMC scale-up, Figure 2 = HIV infections averted by male/female by country 2011–2025; the paper's headline is that reaching and maintaining 80% VMMC coverage across 13 countries would avert 3.36 million new HIV infections through 2025, costing US$2 billion but yielding net savings of US$16.51 billion. Eaton 2012 reports person-years of ART per infection averted (efficiency metric, range 6.3–18.7 over 2012–2020). PopART cost paper (Thomas et al. 2021, Lancet Global Health) shows cost per infection averted.

### 4. Transmission attribution ("who infects whom")
- **Axes/encoding:** several sub-types — (a) stacked-area or stacked-bar of the fraction of new infections contributed by each risk group over time; (b) transmission population attributable fraction (tPAF) bar charts by partnership type over 10- and 30-year windows; (c) age-of-transmitter × age-of-recipient mixing matrices/heatmaps; (d) sources of infection by cascade stage (undiagnosed / diagnosed-not-on-ART / on-ART-unsuppressed).
- **Question:** which populations, ages, or care-cascade states drive onward transmission (distinct from who acquires infection)?
- **Named examples:** Stone et al. 2021 (J Int AIDS Soc 24:e25650, CC BY), the "Key-Pop Model" for South Africa: Figure 4 = population/partnership contributions to new infections; Figure 5 = 10- and 30-year tPAF by partnership type with 95% CrI. Verbatim finding: "Sex between FSWs and their paying clients, and between clients with their non-paying partners contributed 6.9% (95% credibility interval 4.5% to 9.3%) and 41.9% (35.1% to 53.2%) of new HIV infections in SA over 2010 to 2019 respectively." Maheu-Giroux et al. 2017 (JAIDS 75:517–527) Côte d'Ivoire "who acquired and transmitted" decomposition: FSW contributed 95% (91–97) of infections in 1976–1985, falling to 19% (11–27) in 2005–2015. Akullian et al. 2020 (Lancet HIV 7:e348–e358, CC BY, EMOD-HIV eSwatini) renders sources of transmission by ART status and by acute/early stage, plus the age-shift-in-transmission figure; the paper's firmest headline is that even 100% ART coverage within 6 months of infection "would reduce adult HIV incidence to 0·73 (95% CI 0·55–0·92) per 100 person-years by 2030 and 0·46 (0·33–0·59) per 100 person-years by 2050—still far off the epidemic control target." Foundational methods reference: Mishra et al. 2014 (Sex Transm Infect 90:19–25) distinguishing acquisition vs transmission. Phylogenetic analogues (Ratmann/Xi et al., arXiv/PLOS) render age-source flows for young women, e.g. at age 15 an estimated 91.8% of infections came from men >5 years older.

### 5. HIV care cascade / 95-95-95 bars
- **Axes:** x = cascade step (diagnosed → on ART → virally suppressed); y = % (of PLHIV or of prior step).
- **Encoding:** descending bar staircase; the denominator convention (each 95's numerator becomes the next 95's denominator) is documented explicitly by UNAIDS. Cascade-over-time uses stacked areas or grouped bars per year.
- **Named examples:** UNAIDS "Understanding measures of progress towards 95-95-95" (Figure 1 = progress bars; Figure 2 = country cascade). Thembisa produces the South Africa national cascade (e.g., 90-68-88 by mid-2018). Ehrenkranz et al. 2021 (PLOS Medicine 18:e1003651) proposes a cyclical "revolving door" cascade as a critique of the linear archetype.

### 6. Compartmental / agent-based structure schematics
- **Encoding:** boxes-and-arrows of natural history (susceptible → acute → chronic by CD4 → AIDS; plus diagnosed/on-ART/suppressed care states); for ABMs, layered diagrams of within-host + disease-progression + sexual-network scales.
- **Question:** what states and transitions does the model represent?
- **Named examples:** EMOD-HIV network diagram (idmod.org docs) showing SI/SEIRS states pushed inside agents plus contact network; Granich 2009 Figure 1 (infectivity-by-stage schematic, Weibull survival, secondary-case timing). Multi-scale MSM model schematic in PLOS One (within-host + health-state + contact-network panels A/B/C). Starsim/STIsim (Kerr et al.) present the agent-matrix + modular disease/network architecture.

### 7. Cost-effectiveness planes and acceptability curves
- **CE plane:** x = incremental effect (QALYs/DALYs averted or infections averted); y = incremental cost; scatter of PSA draws with a willingness-to-pay threshold line.
- **CEAC:** x = WTP threshold; y = probability the intervention is cost-effective; one curve per comparator, summing to 1 across mutually exclusive options.
- **Named examples:** Japan MSM PrEP Markov model (Sci Rep 2022) Fig 6a CE plane / 6b CEAC / 6c time-horizon variation. Cabotegravir LA-PrEP CEA (PharmacoEconomics Open 2025) CE plane vs $100,000/QALY + CEAC. Thailand PrEP CEA (JIAS) CEACs showing 80% of scenarios cost-effective when restricted to higher-risk MSM.

### 8. Sensitivity analysis figures
- **Tornado:** horizontal bars ranked by influence on ICER/outcome, each spanning low-to-high parameter value around a base-case vertical line.
- **PRCC:** bar/dot plot of partial rank correlation coefficients (LHS sampling), often with significance thresholds; sometimes PRCC-over-time.
- **PSA:** scatter on the CE plane and CEAC.
- **Named examples:** HIV vaccine CEA South Africa tornado (green=low, blue=high, grey=not cost-effective region at 3×GDP). PrEP Thailand and Kenya tornado diagrams on ICER. PRCC convergence plots in compartmental HIV control-theory papers.

### 9. Age-sex stratified incidence/prevalence
- **Encoding:** paneled line plots or bars by 5-year age band and sex; sometimes age-sex pyramids of PLHIV; female curves peaking younger than male curves is the recognizable signature in generalized epidemics.
- **Named examples:** Thembisa age-specific prevalence — 31% of women aged 25–49 in South Africa were living with HIV in 2022 (Thembisa 2022 estimates, reported via Spotlight, 31 May 2023); Spectrum/AIM age-sex outputs; Naomi outputs stratified by district, sex, and five-year age group.

### 10. Uncertainty representation
- **Conventions:** credible/uncertainty intervals as shaded ribbons (50/80/95%); posterior predictive intervals shown as an additional wider band (Naomi); spaghetti/"draws" plots of many posterior trajectories; fan charts widening into the future. ABC-calibrated models (HIV Synthesis, PopART-IBM) plot ensembles of accepted parameter-set runs.
- **Named examples:** Naomi's dual-band convention (thick dash = estimate, 95% CrI, plus narrow 80% posterior predictive). Lancet Global Health ten-model validation (Eaton et al. 2015) shades 95% CrI only for the models that produced statistical uncertainty.

### 11. Multi-model / consortium comparison
- **Encoding:** one panel per output indicator (prevalence, incidence, ART coverage, AIDS deaths, % diagnosed, % suppressed, % circumcised), each with one colored line per model, spanning a common horizon and a shared "status quo" scenario. Uncertainty ribbons frequently omitted for readability, with structural spread across models serving as the uncertainty proxy.
- **Named examples:** Eaton et al. 2012 (PLOS Medicine, 12 models, South Africa); Eaton et al. 2015 (Lancet Global Health, 10-model validation against 2012 survey — all models under-projected the 18.8% survey prevalence, eight below the survey 95% CI 17.5–20.3); Moolla et al. 2023 (BMC Public Health, EMOD/Goals/HIV-Synthesis/Optima/Thembisa, 1990–2040, coefficient of variation as the consistency metric); Taramusi et al. 2025 (African Journal of AIDS Research, five models — EMOD-HIV, Goals, HIV Synthesis, Optima, PopART-IBM — for Zimbabwe to 2040, 2023 incidence range 2.0–3.3/1000 PY); Bansi-Matharu et al. 2025 (PLOS Medicine, seven-model cascade-of-death comparison for Zimbabwe/Malawi/South Africa).

### 12. Elimination / target-tracking against UNAIDS goals
- **Encoding:** incidence or incidence:prevalence ratio trajectory with a horizontal threshold line (0.1/100 PY elimination; 90% incidence reduction vs 2010; 2030 target markers).
- **Named examples:** Granich 2009 (elimination threshold); the Lancet HIV "How universal does UTT have to be?" figure juxtaposing Granich's epidemic-control curve against Akullian's eSwatini no-control-for-decades curve, both on the 0.1/100 PY threshold. Stover et al. 2021 (PLOS Medicine, Goals model) projects UNAIDS 2025 targets to 2030.

### 13. Key-population / risk-group stratified figures
- **Encoding:** separate calibration and impact panels for FSW, MSM, PWID, AGYW; often much higher prevalence axis ranges — Thembisa 2022 estimated 59% prevalence among female sex workers and 30% among men 18+ who have sex with men (Spotlight, 31 May 2023).
- **Named examples:** Stone 2021 (FSW/client/MSM panels); Mukandavire et al. 2018 (Dakar KP contribution, J Int AIDS Soc 21:e25126); PWID individual-based model comparison for New York (PMC5322479). DREAMS AGYW evaluations (Birdthistle et al. 2022, PLOS Medicine 1003837) plot AGYW incidence over time with 95% CIs, though these are largely empirical-cohort rather than transmission-model outputs.

### 14. Geographic / spatial maps
- **Encoding:** choropleth of prevalence, incidence, ART coverage, or unmet need by district/PSNU; frequently paired maps (prevalence vs circumcision, or the "95s" clustered geographically).
- **Named examples:** Naomi district-level maps (official UNAIDS/PEPFAR subnational tool since 2020); Njeuhmeli 2011 paired maps (HIV prevalence vs % circumcised across 13 countries); Zambia geospatial 95-95-95 k-means clusters (medRxiv/PMC10168516).

### 15. Coverage-vs-impact / threshold analyses (PrEP, ART, VMMC)
- **Encoding:** x = coverage or effort; y = infections averted, % reduction, VMMCs/infection averted, or cost per infection averted; threshold/turning points highlighted.
- **Named examples:** DMPPT2 VMMC age-targeting (Kripke et al., eSwatini/Zimbabwe/Zambia) — VMMCs per infection averted by age group, with ages 20–29/20–34 most efficient; lowest cost per infection averted circumcising ages 15–34 ($870 in eSwatini). HPTN 083 LA-PrEP model (Mitchell et al. 2023, Lancet Regional Health Americas) — infections averted by switching TDF/FTC to cabotegravir among Atlanta MSM (TDF/FTC at ~28% usage averting 36.3% of infections over 2022–2026 vs no PrEP). Cambiano/Phillips easy-access PrEP (Lancet 2022) — cost-effectiveness across 3000 setting-scenarios keyed to prevalence of viraemia >1000 copies/mL.

### PopART-IBM / HPTN 071 (a template intervention-modeling paper)
Probert et al. 2022 (Lancet HIV 9:e771–e780, open access; PopART-IBM stochastic individual-based model, ABC-calibrated, 1000 accepted parameter sets) illustrates several archetypes at once: model-prediction-vs-observed effect (arm A predicted 27% [6–42] reduction vs 7% observed; arm B 29% [10–43] vs 30% observed); four-scenario incidence trajectories to 2030 (continued PopART = 58% lower incidence in 2030 vs counterfactual; nationwide rollout = 66%; discontinuation = 11%); community- and sex-disaggregated panels; cascade-fit panels; proportion of incidence from acute/early infection; and reproduction-number-by-community. No scenario reached the 0.1/100 PY elimination threshold by 2030.

## Audience Differentiation

- **Peer-reviewed publication figures:** dense multi-panel calibration + counterfactual + sensitivity; explicit credible intervals; grayscale-safe. Eaton, Stone, Probert exemplify.
- **Funder/donor presentation figures (Gates/IDM, PEPFAR, Global Fund, UNAIDS, Avenir):** simplified single-message charts — cascade bars, infections-averted bars, allocation-optimization "before/after budget" splits (Optima), and subnational maps (Naomi for PEPFAR PSNU planning). Color-forward, few CIs.
- **Internal model-diagnostic figures:** calibration spaghetti/trace plots, posterior-predictive checks, PRCC/tornado, network-structure diagnostics (Starsim network analyzers). Rarely published in full; live in supplements and repos — e.g., the Starsim/STIsim Eswatini repo's calibration figure of prevalence, infections, ART, PLHIV, deaths, and population, supporting single-sim line or multi-sim median+band.

## Domain Conventions and Unwritten Norms

- **Targets vs output:** empirical survey data are almost always discrete points with error bars; model output is a continuous line with a shaded interval. Never the reverse.
- **Uncertainty:** shaded ribbons for CrIs; some journals/papers drop ribbons in multi-model plots and let inter-model spread stand in for uncertainty (stated explicitly in Bansi-Matharu 2025).
- **Scales:** incidence often on linear axes; log scales appear for wide-dynamic-range quantities (e.g., viral load, or incidence approaching elimination). Prevalence essentially always linear.
- **Time horizons:** calibration windows commonly 1990–2025; projections to 2030 (UNAIDS target year), 2040, 2050, occasionally 2100 (Thembisa long-run testing paper, Lancet Public Health 2024).
- **Reference scenario styling:** status quo / no-ART / counterfactual drawn dashed or grey; intervention scenarios in saturated colors; the between-curve region shaded for "averted."
- **Thresholds:** horizontal lines at 0.1/100 PY (elimination), WTP (CE plane), or 3×GDP (cost-effectiveness).
- **Layout:** multi-panel grids organized by indicator (rows) × scenario or setting (columns), or by sex (men/women panels) and age band.

## Recommendations

1. **For a Starsim/STIsim HIV paper in Zimbabwe/South Africa, lead with the two-panel calibration figure** (prevalence and incidence, men vs women, model line+95% ribbon over ZIMPHIA/PHIA and ANC points). This is the entry ticket for credibility and mirrors EMOD/Thembisa/Naomi conventions. Benchmark: if your ribbon misses survey CIs systematically, recalibrate before projecting.
2. **Pair every counterfactual projection with an infections-averted wedge and a percent-reduction-by-scenario bar.** Report an efficiency metric (infections averted per person-year of ART/PrEP, or per VMMC) as Eaton and DMPPT2 do, since funders read efficiency, not just totals.
3. **If your contribution is mechanistic transmission attribution, use the Stone 2021 tPAF template** (10- and 30-year tPAF by partnership/risk group with CrI) rather than an acquisition-only breakdown; explicitly separate "who acquires" from "who transmits" per Mishra 2014.
4. **For policy audiences, produce the 95-95-95 cascade bar and a Naomi-style subnational map**; these translate directly into PEPFAR/Global Fund planning.
5. **Always include a sensitivity figure** (tornado for CE outcomes, PRCC for dynamical outcomes) and a diagnostic uncertainty representation (posterior draws or fan chart). Thresholds that change conclusions (WTP, elimination line, coverage turning points) should be drawn, not just described.
6. **When multiple models exist for your setting, show a consortium-style comparison grid**; structural spread across Zimbabwe's five-model exercise (2023 incidence range 2.0–3.3/1000 PY) is a more honest uncertainty statement than any single model's ribbon.

## Caveats

- Some cited estimates come from preprints not yet peer-reviewed (a 15-model priority-populations comparison, medRxiv 2025; a Thembisa FSW-assumptions analysis, medRxiv 2026); treat their figures as provisional.
- Exact figure numbers were confirmed for Stone 2021, Granich 2009, Eaton 2012, and Njeuhmeli 2011, but for Akullian 2020 and Probert 2022 the figure contents are described from full text while precise "Figure N" labels should be verified against the open-access PMC versions (PMC7221345, PMC9646978).
- Phylogenetic source-attribution figures (age-flow plots) are visually similar to mechanistic attribution figures but answer a different question and rest on sequence data; do not conflate them with compartmental/ABM tPAF outputs.
- Several DREAMS "impact" figures are empirical cohort incidence trends, not transmission-model projections, despite appearing in the modeling literature.