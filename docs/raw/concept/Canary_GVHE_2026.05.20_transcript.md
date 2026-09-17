# Transcription — *Unlocking point-of-care STI diagnostics as platform for HIV/STI prevention: A mathematical modeling study*

**Source file:** `STI_diagnositc_modeling_proposal_v2_Adam_-_Emilia_edits.pptx`
**Slides:** 26 (slides 21 and 23 are marked *hidden* in the source deck — see notes below)
**Authors:** Adam Akullian & Emilia Simmons (IDM / Gates Foundation)

> **How to read this document.** Each slide section gives: the on-slide text, a description of any figure and what it is meant to communicate, the speaker notes where they exist in the file, and any ambiguities or apparent errors. A consolidated list of cross-deck ambiguities appears at the end.

---

## Narrative arc (overview)

The deck builds an argument in five movements:

1. **Context & portfolio (Slides 1–2).** The Foundation is already investing across the point-of-care (POC) STI diagnostics value chain in high-HIV-burden African settings.
2. **The biology and the gap (Slides 3–8).** STIs raise HIV risk both biologically and as a marker of network risk, but trials have been inconsistent and syndromic management misses most (asymptomatic) infection. No model has jointly quantified the biological + targeting pathways or the population-level HIV impact of POC diagnostics.
3. **Framework & questions (Slides 9–16).** A pathway diagram (A–E), epidemiological-context arguments, the three core model questions, the value proposition, and the empirical anchor (the INSTEP trial in Rakai, Uganda), plus the convening participants.
4. **The model (Slides 17–20).** STI/HIVsim — an agent-based, HIV-first model integrating HIV and STIs on one sexual network — its architecture, and a "counterfactual arm ladder" for isolating each pathway's contribution.
5. **Illustrative results & next steps (Slides 21–26).** Early, explicitly *illustrative / uncalibrated* results for Pathways C, D, the asymptomatic bottleneck, and network-hub findings, ending with next steps.

---

## Slide 1 — Title

**Title:** Unlocking point-of-care STI diagnostics as platform for HIV/STI prevention: A mathematical modeling study

**Authors:** Adam Akullian & Emilia Simmons

**Collaborators:** Kate Grabowski (Johns Hopkins), Jeff Imai-Eaton (Harvard University), Robyn Stewart + Software (IDM), Michelle O'brien (IDM)

**Figure / branding:** IDM (Institute for Disease Modeling) logo centered; "Gates Foundation" wordmark lower-left; a large faint "Foundation" watermark across the top.

**Notes file:** present but contains only the slide number ("1") — no narration.

**Ambiguities:**
- Source filename misspells "diagnostic" as "diagnositc" and is tagged "v2 … Adam - Emilia edits," indicating a collaborative working draft rather than a final deck.
- The collaborator list here differs from the participant list on Slide 16 (e.g., Yonatan Grad and Kirsten Oliveira Roster appear on Slide 16 but not here; "Robyn Stewart + Software" here is broken out into named software staff on Slide 16).

---

## Slide 2 — The Foundation is building a multi-layered POC STI diagnostics portfolio

**Subtitle:** Spans product development → market introduction, includes high HIV-risk geographies: Kenya, South Africa, Zimbabwe, Botswana

**Body (three numbered tiers):**

1. **Product development (EDGE team)** — Funding 4 manufacturers (Chembio, Detact, Aptitude, Pluslife) to develop low-cost POC molecular diagnostics for NG/CT/TV and syphilis; regulatory approval expected 2026–2027.
2. **Clinical evaluation & implementation science (WHI ~$6.4M across 4 studies)**
   - **Kenya — Jhpiego ($2.9M+):** public-sector field evaluation of Aptitude Metrix™ + MOH implementation of diagnostic-led STI management.
   - **Zimbabwe — PSI:** feasibility and costs of POC testing in private facilities and pharmacies.
   - **South Africa — Wits/RHI ($2.9M):** clinical performance + implementation research across AGYW and key populations.
   - **Botswana — Harvard Health Partnership ($150K):** STI prevalence and modeling cost-effectiveness among AGYW.
3. **Market access & health economics (~$786K across 2 investments)**
   - Market assessment across Kenya, Nigeria, South Africa, Zimbabwe — Eureka Idea Co. ($236K).
   - Health economic modeling for product introduction in Kenya + South Africa — Quantium Health ($550K).

**Figure:** none (text slide). Footer: "©Gates Foundation."

**Ambiguities:**
- Tier 2 is labeled "across 4 studies" and four country studies are listed — consistent.
- Dollar figures are abbreviated (e.g., "$2.9M+", "$150K"); precise amounts and the meaning of "+" are not specified.
- "AGYW" (adolescent girls and young women) and "MOH" (Ministry of Health) are used without definition.

---

## Slide 3 — STIs increase HIV risk through multiple mechanisms

**Subtitle (bold/underlined):** STIs are both **causal cofactors AND observable signals of network-level risk — two distinct levers for prevention**

**Body:**
- **Biological pathway:**
  - Mucosal disruption, genital inflammation increase HIV risk (increased susceptibility 4-fold).
  - Genital ulcers increase viral shedding (increased transmissibility 2–3 fold).
- **Epidemiologic signals:**
  - Empirical marker of high risk (useful for risk assessment and prevention prioritization).
  - Indicator of high-degree individuals on a sexual network (potential to break large transmission chains).

**Figure:** none.

**Speaker notes (verbatim sense):** Observational data show strong associations between presence of an STI and HIV risk — a meta-analysis shows a ~4-fold increased risk of HIV acquisition with any lab-documented STI and a 2–3-fold increase in HIV shedding in genital secretions — with established causal mechanisms (mucosal disruption, HIV target-cell recruitment and activation, altered cytokine production, reduced CD4 counts, impaired HIV-specific cytotoxic lymphocyte function, enhanced HIV replication, increased HIV viral load in plasma/vaginal fluids/semen, and an imbalance of protective lactobacilli-dominated vaginal flora). Cites Hayes et al. (PMC3827743, introduction). Observational studies also show substantial declines in viral load within two weeks of treatment for gonorrhea, chlamydia, and trichomoniasis in men and women.

---

## Slide 4 — The missing link: population-level HIV impact of POC STI diagnostics

**Body (numbered gaps):**
1. **No rigorous estimate of population-level HIV impact** — implementation studies measure STI outcomes and care-cascade metrics, but cannot quantify HIV infections averted at the population level.
2. **Biological and targeting pathways never jointly quantified** — existing models only estimate the direct biological benefit of STI treatment on HIV risk and don't consider STI as a marker of high risk.
3. **No guidance on where to deploy STI dx for greatest HIV-prevention return** — which epidemic settings, populations, and delivery platforms maximize impact per diagnostic deployed remains unanswered.
4. **Sexual network effects unmodeled** — STI positivity as a signal of network connectivity and high-transmission clusters has not been quantified.

**Closing (red text):** **This modeling study aims to fill that gap** — providing the decision-relevant evidence needed to justify scaling the Foundation's STI diagnostics portfolio as a strategic HIV-prevention platform.

**Figure:** none.

**Ambiguities:**
- The extracted text lists four numbered gaps plus the closing statement; the on-slide closing line is styled in red but is not numbered. (The plain-text export folds the "Sexual network effects unmodeled" point in slightly different order than the rendered slide — content is identical.)

---

## Slide 5 — STI treatment trials show biological plausibility but inconsistent population impact

**Figure:** A forest plot (relative risk of HIV with 95% CI) of STI-treatment trials, grouped into three categories:
- **Community RCTs:** Grosskurth 1995 (Syndromic STI mgt, N=12,537, RR 0.58 [0.42, 0.79]); Wawer 1999 (Mass STI treatment, N=15,127, RR 0.97 [0.81, 1.16]); Kamali 2003 (Syndromic STI mgt, N=14,554, RR 1.00 [0.63, 1.58]); Gregson 2007 (Syndromic STI mgt, N=9,454, RR 1.27 [0.92, 1.75]).
- **Individual RCTs among FSW:** Ghys 2001 (Intensive STI mgt, N=542, RR 0.70 [0.25, 1.90]); Kaul 2004 (Presumptive STI treatment, N=466, RR 1.20 [0.60, 2.50]).
- **Individual RCT of HSV-2 therapy:** Watson-Jones 2007 (Acyclovir suppr'n, N=821, RR 1.08 [0.64, 1.83]); Celum 2008 (Acyclovir suppr'n, N=3,172, RR 1.16 [0.83, 1.62]); Celum 2009 (Acyclovir Suppr'n, N=3,408, RR 0.92 [0.60, 1.41]).
- X-axis 0.2–5 (log), with "← Favours intervention | Favours control →".
- A **gold star annotation** points at the Grosskurth 1995 (Mwanza) row — the single trial showing a significant protective effect.

**Source citation on slide:** Hayes et al., 2013 — https://pmc.ncbi.nlm.nih.gov/articles/PMC3827743/

**Figure context / point:** Only the Mwanza trial (Grosskurth, early-epidemic, high genital-ulcer prevalence) showed a clear protective effect; all other trials straddle RR = 1. This sets up the "biological plausibility but inconsistent population impact" thesis.

**Speaker notes:** "8 of 9 clinical trials of STI treatment on HIV risk failed to show association. Mwanza trial showed efficacy — early epidemic — STIs more important, high prevalence of genital ulcers — creates high susceptibility."

**Ambiguities:**
- Speaker notes say "8 of 9 … failed" but the plot shows nine trials (one significant). The exact count vs. plotted rows should be reconciled (the note appears to mean 8 of 9 were non-significant).

---

## Slide 6 — Population impact attenuated by real-world conditions

**Banner:** Biological efficacy → Individual risk reduction → Population impact

**Two columns:**

*Left — Individual-level: does treating STIs reduce a person's HIV risk?*
1. Frequent re-infection under intermittent treatment.
2. Most infections asymptomatic and untreated.
3. STIs are one of many competing risk factors (viral load, partner count, condom use).
4. High HIV exposure frequency offsets per-act risk reduction.

*Right — Population-level: does treating STIs in a population reduce HIV transmission?*
1. Impact depends on epidemic stage — generalized epidemics dilute core-group effects.
2. Requires reaching core transmission groups.
3. Trial contamination underestimates true effect.

**Figure:** none (two-column layout). Several phrases are underlined for emphasis.

**Speaker notes:** "Point-of-care or lab testing can reveal both active infection and risk information that would not be captured by syndromic management alone." (Note appears to be a generic recurring note — see Slides 9/12/19.)

---

## Slide 7 — Syndromic management misses the majority of STI infections

**Body (bullets):**
- Most STIs are asymptomatic: large fraction undiagnosed under syndromic management (40–70%).
- Relies on care-seeking versus population-based screening.
- Persistent reservoir of infection.
- Inconsistent RCT results reflect the untreated asymptomatic reservoir.

**Figure:** none.

**Speaker notes:** "Not only are these infections common, but the majority are asymptomatic. This means they are largely missed by syndromic management and persist as a hidden reservoir of infection. And importantly, we still don't fully understand what happens if we systematically identify and treat these asymptomatic infections."

---

## Slide 8 — POC STI diagnostics can amplify HIV prevention across three distinct pathways

**Subtitle:** Moving beyond syndromic management unlocks biological, behavioral, and network-level impact:

**Body (numbered):**
1. Detect more asymptomatic infections (biological pathway).
2. Identify higher-risk individuals and increase PrEP use in those groups (behavioral pathway).
3. Reach more network-connected individuals (network pathway).

**Figure:** none.

**Ambiguities:**
- The slide names **three** pathways (biological, behavioral, network), but the framework diagram (Slides 9/19) enumerates **five** lettered pathways (A–E). The mapping between the "three distinct pathways" here and the A–E scheme is implicit, not stated.

---

## Slide 9 — Potential pathways from STI diagnostics to HIV/STI risk and burden reduction

**Caption:** Color-coded to show where INSTEP provides evidence and where modeling can add value.

**Figure:** A left-to-right flow diagram in three columns.

- **Column 1 — Diagnostic input:** "STI diagnostics" splitting into two sub-boxes, **Infection detection** and **Risk information**.
- **Column 2 — Pathways (five color-coded boxes):**
  - **Pathway A — Treatment of asymptomatic infection:** Detection → treatment → reduced infectious period → reduced STI transmission. *(blue)*
  - **Pathway B — Partner treatment cascade:** STI diagnosis → partner notification/referral → partner treatment → transmission chain interruption. *(blue)*
  - **Pathway C — Biological susceptibility:** STI infection → genital inflammation → increased HIV acquisition probability. *(orange)*
  - **Pathway D — HIV prevention targeting + risk awareness:** STI positivity → signal of HIV exposure risk → increased perceived risk → PrEP uptake/adherence. *(orange/tan)*
  - **Pathway E — Network risk signal:** STI positivity → evidence of high-transmission network → identification of high-risk individuals/clusters. *(purple)*
- **Column 3 — Population outcomes (three boxes), with colored arrows from the pathways:**
  - **Reduced STI transmission:** Direct treatment and partner services lower prevalence and onward spread. *(fed by A, B)*
  - **Reduced HIV risk:** Better identification of who can benefit from prevention and reduce biologic susceptibility. *(fed by C, D)*
  - **Interrupt chains of transmission:** Targeting high-impact networks can improve prevention efficiency per test deployed. *(fed by E)*

**Speaker notes:** "Point-of-care or lab testing can reveal both active infection and risk information that would not be captured by syndromic management alone."

**Ambiguities / defects:**
- In the rendered diagram, the body text of the "Interrupt chains of transmission" box **overlaps its header** ("…transmission" sits on top of "Targeting high-impact networks…"), a visual layout defect.
- The "color-coded to show where INSTEP provides evidence vs. where modeling adds value" claim is asserted, but the diagram's legend for that color meaning is not visible — the reader cannot tell which colors map to "INSTEP evidence" vs. "modeling value."

---

## Slide 10 — STI burden is high and heterogeneous across HIV epidemic settings

**Subtitle:** Prevalence varies 3–5 fold across pathogens and settings — heterogeneity demands precision deployment.

**Figure:** A boxplot-with-overlaid-points chart titled "Prevalence of curable STIs among women in high HIV burden African settings — Study-group estimates; boxplots show median and IQR." Y-axis "Point prevalence (%)" on a log-like scale (1%–40%+). Four pathogen columns, left to right: **Syphilis** (lowest median, ~3%), **Gonorrhea** (~5%), **Trichomonas** (~10%), **Chlamydia** (highest median, ~12%). Each column shows wide scatter of study-level points spanning roughly 1% to >40%.

**Footnotes on slide:** "These estimates include a mix of symptomatic and asymptomatic infections across study designs." Data from: https://data.who.int/dashboards/sti-prevalence-atlas/database-explorer

**Speaker notes:** "Large STI prevalence and high degree of heterogeneity across high-burden HIV settings. Mixed asymptomatic and symptomatic detection approaches."

---

## Slide 11 — Impact of a POC dx platform will depend on epidemiological context

**Figure:** Three side-by-side sexual-network diagrams under the heading "HIV Transmission Events Over One Year (n=100 nodes, 50 transmissions each)." Each shows nodes (black = HIV only; red = HIV + STI) connected by edges (= transmission events in the past year), with a large red callout percentage and supporting math beneath:

| Panel | Scenario label | Parameters | % transmissions attributable to STI | Supporting numbers |
|---|---|---|---|---|
| Left | A — Homogeneous, low STI | 10% STI \| RR:4 mix:20 BB:26 (50 edges) | **39%** | weighted events = 82.0, baseline = 50.0, excess = 32.0 |
| Center | A — Homogeneous, high STI | 20% STI \| RR:10 mix:38 BB:2 (50 edges) | **57.6%** | weighted events = 118.0, baseline = 50.0, excess = 68.0 |
| Right | B — Heterogeneous, high STI | 20% STI \| RR:36 mix:14 BB:0 (50 edges) | **70.9%** | weighted events = 172.0, baseline = 50.0, excess = 122.0 |

**Legend on slide:** "HIV+ nodes: ● HIV only ● HIV + STI. Each edge = one transmission event in the past year. Relative risk: black–black = 1, red–black = 2, red–red = 4. PAF = (weighted events − baseline events) / weighted events."

**Figure context / point:** A schematic population-attributable-fraction (PAF) illustration: as STI prevalence rises and the network becomes more heterogeneous (more red–red, high-RR transmissions), the fraction of HIV transmission attributable to STIs rises from ~39% to ~71%.

**Notes file:** none for this slide. (The "Large STI prevalence and heterogeneity… Mixed asympt and sympt" speaker note is attached to this slide's notes XML in the file but reads as a carryover from Slide 10.)

**Ambiguities:**
- "mix" and "BB" in the parameter strings (e.g., "mix:20 BB:26") are not defined on the slide. "BB" likely denotes black–black (HIV-only to HIV-only) edges given the RR legend, and "mix" likely the red–black mixed edges, but this is inferred, not stated.
- The scenario labels reuse "A" for both homogeneous panels and "B" for the heterogeneous panel; the relationship to the Pathway A/B labels elsewhere is unrelated (here A/B are network archetypes).
- Numbers are schematic/illustrative (n=100, 50 transmissions) — not empirical.

---

## Slide 12 — Three core questions the model will answer

**Body:**

**Q1 (header, bold):** Do STI diagnostics provide an additional cost-effective investment for HIV prevention?
1. How much of the impact of scaling STI diagnostics arises from:
   i. Direct treatment of infections
   ii. Improved targeting of PrEP to high-risk individuals
   iii. Increased uptake and adherence of PrEP
2. To what extent does STI positivity identify individuals connected to high-transmission sexual networks?
   i. How sensitive is impact to variability in network structure and care-cascade metrics?
3. In which epidemic contexts should STI diagnostic testing be deployed for cost-effective impact?
   i. STI/HIV prevalence and incidence
   ii. Network topology (risk heterogeneity)

**Figure:** none.

**Speaker notes:** "Point-of-care or lab testing can reveal both active infection and risk information that would not be captured by syndromic management alone."

**Ambiguities:**
- The slide title says "Three core questions," and the bold line ("Do STI diagnostics provide an additional cost-effective investment…") reads as an overarching framing rather than one of the three. The three numbered items are the actual sub-questions, so the structure (1 framing + 3 numbered) is slightly inconsistent with the "three core questions" heading.

---

## Slide 13 — Value proposition for Foundation investments

**Body (numbered):**
1. **Cross-PST leverage:** Provides an evidence base for integrated investment strategies across STI and HIV portfolios, rather than siloed program design.
2. **Improve risk prioritization for HIV delivery:** Demonstrates how STI diagnostics can identify individuals at highest risk and high-transmission nodes, improving precision of prevention efforts.
3. **Provide decision-relevant guidance for deployment strategies:** In which populations to deploy diagnostics for most cost-effective impact.
4. **Fills key evidence gap:** existing models consider either biological or targeting pathways, but not both.
6. **Additional value of STI surveillance efforts:** Supports investments in monitoring STI prevalence in priority populations.

**Figure:** none.

**Notes file:** present but contains only the slide number ("13").

**Ambiguities / errors:**
- **Numbering error:** the list jumps from 4 to **6** (there is no item 5). Likely a deleted/renumbered bullet.
- "PST" (Program Strategy Team) and "Cross-PST leverage" are used without definition.

---

## Slide 14 — INSTEP trial provides empirical foundation for model development

**Subtitle:** RCT among 4,500 women to evaluate whether **integrating cSTI diagnostic testing into HIV prevention services** can improve identification of women at elevated HIV risk and increase uptake and persistence of PrEP.

**Left column — Empirical estimates from trial:**
- cSTI test positivity
- Distribution of symptomatic vs asymptomatic infections at testing
- Association between cSTI positivity and HIV positivity
- PrEP uptake, adherence, and persistence following cSTI diagnosis
- Changes in perceived HIV risk and behavior following cSTI diagnosis

**Left column — Early findings:**
- High burden of undiagnosed cSTIs among African women at high risk for HIV.
- Adding cSTI diagnostic testing to existing PrEP eligibility screening would nearly double the number of PrEP-eligible women.
- Women with cSTI symptoms more likely to perceive themselves as high HIV risk; women diagnosed with cSTIs more likely to use PrEP.

**Right column — Figure:** A map captioned "Rakai community cohort study communities in south-central Uganda (n=34)." Main panel plots study-community locations (green dots) by latitude (≈ −0.4 to −1.0) and longitude (≈ 31.3 to 31.8) near Lake Victoria, with an inset Africa map (Uganda circled in red) and a legend: green = Inland area, pink = Lakeside area.

**Notes file:** present but contains only the slide number ("14").

**Ambiguities:**
- "cSTI" = curable STI (not spelled out on the slide).
- Subtitle states "RCT among 4,500 women"; the figure caption says the Rakai cohort comprises **n=34 communities** — the two "n" values describe different things (participants vs. communities) and could be confused.
- "Early findings" implies the trial is ongoing / interim; the slide does not state read-out status or dates.

---

## Slide 15 — HIV incidence is rapidly declining in young women in Rakai

**Subtitle:** Finding and providing prevention to women at high HIV risk will become more difficult as incidence declines | Precision tools needed in declining epidemics.

**Figure (two parts):**
- **Left:** A line-with-uncertainty-band plot — "Incidence (per 100 person-years)" vs. "Year" (~1980 to ~2040+). HIV incidence rises to a peak (~2.1 per 100 PY) around 2000, then declines steeply after ~2010 toward a low plateau (<0.5) projected forward; point estimates with error bars (~2005–2018) track the modeled curve.
- **Right:** A small-multiples panel of intervention/behavioral trends over 2000–2020 by age group: **ART (Female)**, **ART (Male)**, **VMMC**, **Ever had sex (Female)**, **Ever had sex (Male)**. ART and VMMC coverage rise toward 50–100% over the period; "Ever had sex" declines, especially in younger female groups. Color legend by age band: 15–19, 20–24, 25–29, 30–34, 35–39, 40–44, 45–49.

**Source on slide:** Akullian et al., 2026 *PLOS Medicine*.

**Figure context / point:** Sharply declining incidence and rising treatment/prevention coverage make high-risk individuals harder to find, motivating "precision tools" (the diagnostic-targeting thesis).

**Notes file:** none.

**Ambiguities:**
- "VMMC" (voluntary medical male circumcision) is not spelled out on the slide.
- The cited paper is dated 2026 — consistent with the deck being a current/forward-dated draft.

---

## Slide 16 — Convening participants & meeting details

**Subtitle:** Align modeling design, trial data, and strategic priorities to quantify the population-level impact of STI diagnostics on HIV prevention.

**Layout:** Five labeled cards.

- **Software & Modeling Platform:** Robyn Stewart, Cliff Kerr, Clark Kirkman, Paul Saxman — Provide technical orientation to the Starsim platform and the STIsim/HIVsim integration.
- **SRH Team:** Adam Akullian, Emilia Simmons, Michelle O'Brien, Kirsten Oliveira Roster — Provide scientific framing and serve as connective tissue across all groups; align on model assumptions, structural needs (incl. AMR), and sensitivity analyses.
- **INSTEP Trial Investigators:** Kate Grabowski (Johns Hopkins), Jeff Imai-Eaton (Harvard), Yonatan Grad (Harvard) — Connect INSTEP trial design and Rakai cohort data to the modeling framework.
- **STI Diagnostics & Strategic Direction:** Lori Newman's team (WHI), HIV PST representatives, additional WHI collaborators — Ensure the analysis is oriented toward maximum strategic impact across SRH priorities.
- **Rakai Community Cohort Study:** In-country investigators (TBD) — Anchor calibration and interpretation in local context from the Rakai Community Cohort Study.

**Figure:** none (card grid).

**Ambiguities:**
- "SRH" (sexual & reproductive health), "WHI", "PST", and "AMR" (antimicrobial resistance) are used without definition.
- In-country Rakai investigators are listed as "TBD."

---

## Slide 17 — STI/HIVsim

**Right-column body (bullets):**
- Dominant models in the HIV space treat STIs as a static risk multiplier or time-varying prevalence input — unable to trace individual-level correlation between STI and HIV risk.
- There hasn't been an **HIV-first** well-calibrated model that integrates HIV and STI dynamics on the same network.
- To contrast with compartmental models, we also gain:
  - Co-infection status, Network position, Diagnosis history.
- Can answer: 'Does diagnosing *this person* with an STI tell us something about their HIV risk?'

**Left-column figure — conceptual architecture:**
- **Agents** (top): individual people with age, sex, risk group, care-seeking behavior, disease states.
- **Structured Sexual Network:** stable / casual / sex-work partnerships; age-assortative mixing · concurrency · risk stratification. (Edge label to diseases: "per-act transmission.")
- **Modular Interventions:** testing · treatment · prevention; "plug in without modifying disease logic." (Edge label: "diagnose · treat · prevent.")
- **Co-Circulating Diseases:** HIV · NG · CT · Syphilis · TV, each with independent natural history.
- **Connectors:** STI infection modifies HIV susceptibility (and vice versa) — emergent co-dynamics. (Edge labels: "cofactor effects," "modify rel_sus / rel_trans.")

**Notes file:** none.

**Ambiguities:**
- NG = *Neisseria gonorrhoeae*; CT = *Chlamydia trachomatis*; TV = *Trichomonas vaginalis*; "Syphilis" = *Treponema pallidum* (TP elsewhere). Abbreviations are not defined on the slide.
- `rel_sus` / `rel_trans` are model code parameter names (relative susceptibility / relative transmissibility) used without explanation for a general audience.

---

## Slide 18 — HIVsim instep model architecture

**Figure:** A detailed flow/architecture diagram (no separate body text). Boxes and their descriptors:

- **Agents:** demographics · risk groups · care-seeking.
- **Syndromic Testing:** symptom-driven care-seeking; current standard of care.
- **POC Screening:** asymptomatic detection; high-sensitivity diagnostics.
- **Partner Notification** (dashed box — i.e., not-yet-implemented / optional): trace & treat contacts of diagnosed cases.
- **Structured Sexual Network:** stable / casual / sex-work · age mixing; concurrency · condom use (disease-specific efficacy).
- **STI Treatment:** pathogen-specific; NG · CT · Syph · TV.
- **Bacterial STIs** (center): NG · CT · Syphilis · TV; symptomatic & asymptomatic.
- **STI–HIV Connectors:** NG ×1.2 · TV ×1.5 · Syph ×2.67; each modifies HIV `rel_sus` per-agent.
- **STI-dx → PrEP:** STI diagnosis triggers PrEP enrollment.
- **HIV Testing + ART:** diagnosis → treatment initiation; CD4-prioritized coverage.
- **HIV** (bottom): acute → latent → AIDS · CD4 · ART.

**Edge labels (arrows):** referral (Syndromic Testing → STI Treatment); referral (POC Screening → STI Treatment); trace contacts (Partner Notification, dashed); detection (symptomatic); detection (asymptomatic); clears (STI Treatment → Bacterial STIs); risk signal (POC Screening → STI-dx→PrEP); transmission (Network → Bacterial STIs); transmission (Network → HIV); cofactor (Bacterial STIs → STI–HIV Connectors); ↑ susceptibility (Connectors → HIV); reduces risk (STI-dx→PrEP → HIV); diagnosis + ART (HIV Testing + ART → HIV).

**Figure context / point:** The implementable version of Slide 17's concept. Note the per-pathogen cofactor multipliers on HIV susceptibility (NG ×1.2, TV ×1.5, Syphilis ×2.67) and that Partner Notification is drawn as dashed (consistent with Slide 26 listing it as a next step).

**Ambiguities:**
- The per-pathogen multipliers (×1.2, ×1.5, ×2.67) appear only here; their source/citation is not given on the slide. CT has no multiplier shown.
- Title uses lowercase "instep" (vs. "INSTEP" elsewhere).
- The title text very slightly overlaps the top of the diagram in the render (a layout nicety, not a content issue).

---

## Slide 19 — Potential pathways from STI diagnostics to HIV/STI risk and burden reduction (repeat)

**Content:** Identical to Slide 9 — same caption ("Color-coded to show where INSTEP provides evidence and where modeling can add value"), same A–E pathway diagram, same three population-outcome boxes, and the same "Interrupt chains of transmission" header/body **overlap defect**.

**Speaker notes:** "Point-of-care or lab testing can reveal both active infection and risk information that would not be captured by syndromic management alone."

**Ambiguities:**
- Slide 19 is a **duplicate** of Slide 9. In the working-draft context this is likely an intentional "recap before results" placement or an editing artifact; the deck does not flag which.

---

## Slide 20 — Counterfactual Arm Ladder

**Subtitle:** Isolating each pathway's contribution.

**Table 1 — model arms:**

| Arm | Syndromic Treatment | POC Screening | PrEP |
|---|---|---|---|
| Baseline | yes | – | – |
| Full Screening | yes | yes | STI-dx triggered |
| Screening, no PrEP | yes | yes | – |
| Risk-Group PrEP | yes | – | WHO behavioral screening |
| Magic Cure | instant cure | – | – |

**Table 2 — comparisons and the pathway each isolates:**

| Comparison | Pathway isolated |
|---|---|
| Full − Baseline | Total effect of POC platform |
| Full − Screening no PrEP | **D:** PrEP targeting contribution |
| Screening no PrEP − Baseline | **A + C:** direct STI treatment effect on HIV |
| STI-dx PrEP − Risk-Group PrEP | **D:** value of biomarker targeting vs behavioral screening |
| Magic Cure − Baseline | **C:** maximum biological PAF (upper bound) |

**Figure:** none (two tables).

**Figure context / point:** A factorial/counterfactual design where each arm toggles screening and PrEP-targeting strategy so that differences between arms isolate individual pathway contributions (A, C, D) and an upper bound (Magic Cure → maximum biological PAF).

**Ambiguities:**
- Pathway **D** is named as the isolated pathway for **two** different comparisons ("Full − Screening no PrEP" and "STI-dx PrEP − Risk-Group PrEP"); the two are described slightly differently ("PrEP targeting contribution" vs "value of biomarker targeting vs behavioral screening") but share the same letter.
- Pathways **B** (partner notification) and **E** (network signal) are not isolated by any arm here — consistent with Slide 26 listing both as still-to-implement.

---

## Slide 21 — Pathway C: Biological Susceptibility  *(HIDDEN in source deck)*

> This slide is marked `show="0"` (hidden) in the file; it does not appear in normal slideshow playback. Transcribed here for completeness.

**Left body (bullets):** Given a Magic Cure of bacterial STIs:
- What is the maximum possible contribution of biological STIs in these scenarios?
- We can get an exact value with the use of a 'magic cure' introduced at a timepoint.
- In this uncalibrated network, it hovers around 10%.

**Figure:** A combo bar + line chart titled "HIV infections averted by STI cure (2-year window)." X-axis: "Year STI cure introduced" (2000–2018, biennial). Left y-axis: "HIV infections averted" (0–60), shown as purple bars. Right y-axis: "Baseline HIV new infections" (~100–500), shown as a black line with markers. Both the bars (infections averted) and the baseline incidence line decline steeply over time — i.e., the later the STI cure is introduced, the fewer HIV infections it averts, tracking the declining baseline epidemic.

**Notes file:** none.

**Ambiguities:**
- Slide explicitly states results are from an **uncalibrated** network and the ~10% figure is illustrative. This ~10% maximum biological contribution contrasts with the much higher schematic PAFs on Slide 11 (39–70.9%); the difference (calibration, network archetype, definition) is not reconciled on-slide.

---

## Slide 22 — Asymptomatic Detection

**Subtitle:** The STI care cascade bottleneck is asymptomatic infection.

**Left body:**
- **The care cascade bottleneck is asymptomatic infection.**
- Under syndromic management:
  - Up to 70% of STI infections are asymptomatic.
  - All asymptomatic infections go undiagnosed and untreated.
- Introducing a POC diagnostic, we can directly measure the difference of the asymptomatic screened population.

**Figure:** A Sankey (flow) diagram of the STI care cascade. Flows (with on-figure counts/percentages):
- **Pathogen sources (left):** TV 13,900 (41%), NG 10,886 (32%), CT 5,380 (16%), Syphilis 4,060 (12%).
- **Symptom status:** Asymptomatic 22,881 (67%); Symptomatic 11,345 (33%).
- **Care-seeking / screening:** Screened 7,163 (21%); Care-seeking 6,993 (20%); Not care-seeking 4,352 (13%).
- **Cascade outcomes (right):** Diagnosed 14,156 (41%); Treated 14,156 (41%); Untreated 20,070 (59%).

**Figure context / point:** Visualizes that the large asymptomatic pool (67%) is the leak in the cascade; under syndromic management most of it ends "Untreated" (59%), whereas adding POC screening converts part of the asymptomatic pool into "Screened → Diagnosed → Treated."

**Notes file:** none.

**Ambiguities:**
- Diagnosed (14,156) equals Treated (14,156), implying 100% treatment-once-diagnosed in this illustrative run — an assumption, not stated.
- Whether this Sankey is illustrative or calibrated is not labeled here (Slide 26 states all results today are illustrative).

---

## Slide 23 — Pathway D: PrEP Targeting Efficiency  *(HIDDEN in source deck)*

> This slide is marked `show="0"` (hidden) in the file. Transcribed here for completeness.

**Left body (bullets):**
- Current PrEP targeting in Rakai relies on behavioral self-report: reporting multiple partners, transactional sex, recent STI symptoms, or belonging to a key population.
- STI diagnosis is objective.
- Under these regimes, we can examine NNT to avert one HIV infection comparing STI-dx to Risk-Group assigned PrEP distribution.

**Figure:** A two-bar chart titled "PrEP Targeting: STI Diagnosis Identifies Higher-Risk Individuals." Y-axis: "NNT to avert one HIV infection (1 year)." Bars: **Random PrEP = 179** (gray; annotated "HIV inc. 0.8%/yr") vs. **STI-targeted PrEP = 89** (green; annotated "HIV inc. 1.6%/yr"). A "**2.0× more efficient**" arrow spans the two bars.

**Footnote on slide:** "Illustrative | HIV inc. 0.8%/yr | STI prev. 25% | RR(HIV|STI+) = 3 | PrEP eff. 70%."

**Figure context / point:** Targeting PrEP by STI diagnosis roughly halves the number-needed-to-treat (179 → 89) because STI-positive individuals have ~2× the HIV incidence — making STI-targeted PrEP ~2× more efficient.

**Notes file:** none.

**Ambiguities:**
- Left-axis label reads "Random PrEP" annotated with "HIV inc. 0.8%/yr" while the STI-targeted bar is annotated "1.6%/yr"; the relationship to the footnote's single "HIV inc. 0.8%/yr" baseline is implicit (0.8% = population/random; 1.6% = STI-positive subgroup).
- Explicitly labeled "Illustrative."

---

## Slide 24 — STIs mark network hubs

**Subtitle:** STI positivity predicts HIV positivity.

**Figure:** Two large force-directed sexual-network graphs (left and right), each ~1,000 nodes, color-coded by infection status (per the legend on Slide 25: black = uninfected, blue = STI, red = HIV, purple = both). Co-infected/infected nodes cluster as central, high-degree **hubs**, with sparse black (uninfected) nodes toward the periphery. A timestamp "**2001.67**" appears centered at top; a partial stats readout appears top-right of the right panel ("HIV: 32 STI: 100 Both: … / ART: 9 PrEP: …").

**Figure context / point:** Snapshots from the agent-based simulation (later time points than Slide 25) showing infected individuals concentrated in the densely connected core — visual evidence for the "STIs mark network hubs / STI positivity predicts HIV positivity" claim.

**Notes file:** none.

**Ambiguities / defects:**
- The figure **overlaps the title and subtitle** — the subtitle "STI positivity predicts HIV positivity" is partially obscured by the network image, and the top-right stats readout ("Both: …", "PrEP: …") is **cut off**, so some counts are unreadable.
- This slide appears to be a frame (or pair of frames) from an animation whose legend/full stats live on Slide 25; standing alone it lacks a legend.

---

## Slide 25 — (Network animation frame; no PowerPoint text)

> This slide contains **no editable text** in the file (the text-extract returned it empty); all labels are baked into the image. It is almost certainly an embedded animation/GIF frame paired with Slide 24.

**Figure:** A single large force-directed network graph (~1,015 nodes). On-image annotations:
- Timestamp (top-left): **1995.00**
- Stats (top-right): **HIV: 29 | STI: 299 | Both: 49 | ART: 0 | PrEP: 263**
- Total (lower-right): **N = 1015**
- **Legend (bottom):** ● Uninfected (black) · ● STI (blue) · ● HIV (red) · ● Both (purple)

**Figure context / point:** The **t = 1995.00 starting state** of the same agent-based simulation shown on Slide 24. Together they illustrate the network's evolution over time (1995 → 2001+), with infection concentrating into central hubs.

**Ambiguities:**
- No title or caption; the slide relies entirely on the embedded figure. Its relationship to Slide 24 (earlier timepoint vs later) is inferable from the timestamps but not stated in text.
- At 1995 there are already 263 on PrEP and 299 STI cases but 0 on ART — plausible as a model initialization choice, but unexplained on-slide.

---

## Slide 26 — Next Steps

**Body (bullets):**
- **Implement Partner Notification (Pathway B):** trace and treat contacts of diagnosed cases.
- **Implement risk-group PrEP (Pathway D):** model WHO behavioral screening as the comparator.
- **Quantify Pathway E:** degree-infection correlation, formal network position metrics.
- **Finish implementation:** multiple analyzers needed for complete analysis.
- **Calibrate to Rakai:** **all results shown today are illustrative.**
- **Cost-effectiveness analysis:** which epidemic settings and populations yield the greatest HIV prevention return per diagnostic deployed?

**Figure:** none.

**Notes file:** none.

**Key caveat (important for interpreting Slides 11, 21, 22, 23, 24, 25):** the deck states plainly here that **all results shown are illustrative** and the model is **not yet calibrated to Rakai**.

---

## Cross-deck ambiguities, errors, and things to verify

1. **Filename / draft status.** `STI_diagnositc_modeling_proposal_v2_Adam_-_Emilia_edits.pptx` — "diagnositc" is a typo; "v2 … Adam - Emilia edits" marks this as an in-progress collaborative draft.
2. **Hidden slides.** Slides **21** (Pathway C) and **23** (Pathway D) are marked hidden (`show="0"`) and will not appear in normal playback, even though they carry the only quantitative Pathway C/D result figures. Worth confirming whether hiding was intentional.
3. **Duplicate slide.** Slide **19** is identical to Slide **9** (pathway diagram), including the same layout defect.
4. **Layout defect (Slides 9 & 19).** In the "Interrupt chains of transmission" outcome box, the body text overlaps the header.
5. **Layout/overflow defect (Slide 24).** The network figure overlaps and obscures the subtitle, and the top-right stats readout is cut off.
6. **List numbering error (Slide 13).** Numbered list runs 1, 2, 3, 4, **6** — item 5 is missing.
7. **"Three pathways" vs "five pathways" (Slides 8 vs 9/19).** Slide 8 describes three pathways (biological/behavioral/network); the diagram enumerates five lettered pathways (A–E). The mapping is implicit.
8. **Pathway D double-counted (Slide 20).** Two different arm comparisons are both labeled as isolating Pathway D.
9. **Magnitude inconsistency (Slides 11 vs 21).** Schematic STI-attributable fraction on Slide 11 is 39–70.9%; the "magic cure" maximum biological contribution on Slide 21 "hovers around 10%." Both are illustrative/uncalibrated, but the gap is not reconciled.
10. **Illustrative-only results.** Slides 11, 21, 22, 23, 24, 25 all rest on uncalibrated/illustrative model runs (stated explicitly on Slide 26). Numbers should not be cited as findings.
11. **Undefined parameters/acronyms.** Used without definition somewhere in the deck: AGYW, MOH, RHI, WHI, PST, SRH, AMR, VMMC, NNT, PAF, RR, cSTI, NG, CT, TV, TP/Syphilis, `rel_sus`, `rel_trans`, and the Slide-11 network strings "mix" and "BB."
12. **Per-pathogen cofactor multipliers (Slide 18).** NG ×1.2, TV ×1.5, Syphilis ×2.67 are given without a source; CT has no multiplier shown.
13. **Author/collaborator lists differ (Slide 1 vs 16).** Slide 16 adds Yonatan Grad and Kirsten Oliveira Roster and names individual software staff; Slide 1's collaborator line is shorter.
14. **Trial status (Slide 14).** "Empirical estimates" + "Early findings" imply the INSTEP RCT is ongoing/interim; no read-out date is given. "n = 4,500 women" (participants) vs "n = 34 communities" (Rakai cohort) are different denominators.
15. **Recurring speaker note.** The note "Point-of-care or lab testing can reveal both active infection and risk information that would not be captured by syndromic management alone" appears attached to multiple slides (6, 9/12, 19) and reads as a reusable framing line rather than slide-specific narration. Several other notes slides contain only a stray slide number.
16. **Forward-dated citation.** Slide 15 cites "Akullian et al., 2026 *PLOS Medicine*" — consistent with a current draft, but worth verifying publication status.
