

###### RESEARCH ARTICLE 

# **Evaluating the biomedical and behavioral drivers of HIV incidence decline in adolescent girls and young women in Uganda: A mathematical modeling study** 

**Adam Akullian 1** * **, Victor Ssempijja 2, Daniel Bridenbecker 1, Fred Nalugoda3, Gertrude Nakigozi 3, John Santelli 4, Philip Kreniske5, Larry W. Chang 6, Steven J. Reynolds 7, Robert Ssekubugu3, Ronald H. Gray6, Maria J. Wawer6, Thomas C. Quinn**<sup>**8**</sup> **, Ronald M. Galiwango**<sup>**3**</sup> **, William J. M. Probert 9, Jeffrey W. Imai-Eaton 10,11, Oliver Ratmann12, Christophe Fraser 13, Joseph Kagaayi3, Godfrey Kigozi**<sup>**3**</sup> **, Mary Kate Grabowski 14** ☯ **, David Serwadda3,15** ☯ 





###### OPEN ACCESS 

**Citation:** Akullian A, Ssempijja V, Bridenbecker D, Nalugoda F, Nakigozi G, Santelli J, et al. (2026) Evaluating the biomedical and behavioral drivers of HIV incidence decline in adolescent girls and young women in Uganda: A mathematical modeling study. PLoS Med 23(3): e1004993. <u>https://doi.org/10.1371/ journal.pmed.1004993</u> 

**1** Institute for Disease Modeling, Gates Foundation, Seattle, Washington, United States of America, **2** Clinical Monitoring Research Program Directorate, Frederick National Laboratory for Cancer Research, Frederick, Maryland, United States of America, **3** Rakai Health Sciences Program, Kalisizo, Uganda, **4** Population and Family Health and Pediatrics, Columbia University, New York, New York, United States of America, **5** Graduate School of Public Health and Health Policy, City University of New York, New York, New York, United States of America, **6** Johns Hopkins School of Medicine and Bloomberg School of Public Health, Baltimore, Maryland, United States of America, **7** Division of Intramural Research, National Institute of Allergy and Infectious Diseases, National Institutes of Health, Bethesda, Maryland, United States of America, **8** Department of Medicine, Johns Hopkins University School of Medicine, Baltimore, Maryland, United States of America, **9** University of Oxford, Oxford, United Kingdom, **10** Center for Communicable Disease Dynamics, Department of Epidemiology, Harvard T.H. Chan School of Public Health, Boston, Massachusetts, United States of America, **11** MRC Centre for Global Infectious Disease Infectious Disease Analysis, School of Public Health, Imperial College London, London, United Kingdom, **12** Department of Mathematics, Imperial College London, London, United Kingdom, **13** Li Ka Shing Centre for Health Information and Discovery, University of Oxford, Oxford, United Kingdom, **14** Departments of Pathology and Epidemiology, Johns Hopkins University, Baltimore, Maryland, United States of America, **15** Makerere University School of Public Health, Rakai Health Sciences Program, Kalisizo, Uganda 

☯ These authors contributed equally to this work. 

* <u>adam.akullian@gatesfoundation.org</u> 

**Academic Editor:** Alice Zwerling, University of Ottawa, CANADA 

**Received:** February 18, 2025 

## **Abstract** 

**Accepted:** March 3, 2026 

**Published:** March 25, 2026 

**Copyright:** This is an open access article, free of all copyright, and may be freely reproduced, distributed, transmitted, modified, built upon, or otherwise used by anyone for any lawful purpose. The work is made available under the <u>Creative Commons CC0 public domain</u> dedication. 

**Data availability statement:** Source code for mathematical modeling software (EMODHIV) used to run simulations can be found at https://github.com/EMOD-Hub/EMOD. The 

### **Background** 

HIV incidence among adolescent girls and young women (AGYW) in eastern and southern Africa has declined substantially over the past two decades. These declines are often attributed to biomedical HIV prevention strategies, though concurrent changes in sexual behavior may also contribute. We evaluated the contributions of biomedical and behavioral drivers to historical incidence decline in AGYW and projected their impact on incidence trajectories over the next 30 years. 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

1 / 18 



individual-level data used in this study are not publicly available due to ethical and legal restrictions imposed by the Rakai Health Sciences Program and relevant Ugandan research ethics committees. Aggregated number of seroconversions, person-years, and incidence point estimates from cohort models used to generate incidence plots are provided in the <u>Supporting information (Table A in S1 File). Code used to run cohort models and plot</u> output from mathematical models is available at GitHub (https://github.com/aakullian/ <u>RakaiAnalysisPlosMed2026/tree/main). Access</u> to individual-level cohort data needed as inputs to run this code can be requested from the Rakai Health Sciences Program Data Access Committee (datarequests@rhsp.org). 

**Funding:** This work was supported by the National Institute of Allergy and Infectious Diseases (NIAID) <u>https://www.niaid.nih.gov/,</u> National Institutes of Health (NIH) <u>https:// www.nih.gov/</u> (grant numbers U01AI100031 [RG], U01AI075115 [RG], R01AI110324 [RG], and K01AI125086 [MKG]); the Division of Intramural Research, National Institute of Allergy and Infectious Diseases, National Institutes of Health <u>https://www.niaid.nih.gov/ about/dir</u> (AI001040 [TQ]); and with federal funds from the National Cancer Institute, National Institutes of Health <u>https://www.cancer.gov/, under Contract No. 75N91019D00024</u> (VS). This publication is also based on research funded in part by the Gates Foundation <u>https:// www.gatesfoundation.org/, including models</u> and data analysis performed by the Institute for Disease Modeling <u>https://www.idmod.org/.</u> AA is a Senior Research Scientist and DB is a Principal Software Engineer at the Institute for Disease Modeling within the Gates Foundation. The funders had no other role in study design, data collection and analysis, decision to publish, or preparation of the manuscript beyond the involvement of these authors. 

**Competing interests:** The authors have declared that no competing interests exist. 

**Abbreviations:** AGYW, adolescent girls and young women; ART, antiretroviral therapy; CIs, confidence intervals; GAMs, generalized additive models; GLMs, generalized linear models; PFA, pair formation algorithm; PrEP, preexposure prophylaxis; RCCS, Rakai Community Cohort Study; SES, socio-economic status; STIs, sexually transmitted infections; VMMC, voluntary medical male circumcision. 

### **Methods and findings** 

We conducted a mathematical modeling study using data from the Rakai Community Cohort Study (RCCS), an open, population-based cohort of adults aged 15–49 years in 30 communities in Rakai, Uganda. We used an agent-based HIV-1 transmission model calibrated to cohort data to estimate HIV incidence trends among AGYW, aged 15–24, and to quantify the independent and combined effects of antiretroviral therapy (ART), voluntary medical male circumcision (VMMC), and changes in age at first sex (AFS). 

HIV incidence among women aged 15–24 declined by 71% between 2000 and 2019, from 1.57 to 0.45 per 100 person-years, representing the largest decline across female age groups in the cohort. Increasing AFS over the study period (by approximately 3 years in women and 2 years in men) was the largest contributor to incidence declines among adolescent women aged 15–19, averting 17% of cumulative infections between 2000 and 2020 and 37% between 2000 and 2050. Among women aged 20–24, ART scale-up had the greatest impact, averting 13% of infections by 2020 and 43% by 2050. VMMC contributed modestly to historical declines but had larger projected effects over longer time horizons. ART, VMMC, and delays in AFS acted additively to reduce HIV incidence among AGYW. Study limitations include reliance on self-reported sexual behavior and the use of a mathematical model that cannot capture all real-world sexual network dynamics. 

### **Conclusions** 

Both biomedical HIV interventions and broader behavioral changes contributed to declines in HIV incidence among AGYW. Sustaining continued incidence declines in young women will require maintaining both the protective changes in sexual behaviors and effective biomedical interventions. 

### Author summary 

### **Why was this study done?** 

- Adolescent girls and young women in eastern and southern Africa have historically faced the highest risk of acquiring HIV. 

- Over the past two decades, HIV infections among young women in Uganda have declined sharply, but the reasons for this decline are not fully understood. 

- Both biomedical interventions (such as HIV treatment and male circumcision) and changes in sexual behavior (such as later age at first sex) occurred during this period, making it important to understand their individual and combined effects. 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

2 / 18 



### **What did the researchers do and find?** 

- We used a mathematical model calibrated to long-term population data from southern Uganda to examine changes in HIV incidence between 2000 and 2019. 

- HIV incidence among young women aged 15–24 declined by more than 70%, with the largest reductions occurring among adolescents aged 15–19. 

- Delays in the age at which young people first had sex, along with expanded access to HIV treatment and male circumcision, each contributed to these declines, and their effects were largely additive. 

### **What do these findings mean?** 

- Our results show that both biomedical HIV interventions and broader social and behavioral changes have played important roles in reducing HIV infections among young women. 

- Sustaining progress toward HIV epidemic control will likely require continued investment in HIV treatment and prevention alongside efforts that support education and social conditions associated with delayed sexual debut. 

- This study relied on self-reported sexual behavior and mathematical modeling, which may not capture all real-world complexities, and future changes in HIV programs or social conditions could alter long-term projections. 

#### **Introduction** 

Adolescent girls and young women (AGYW) in east and southern Africa have experienced among the highest rates of HIV acquisition in the world [1–3]. Several behavioral, biological, and socio-economic factors put young women at disproportionately high risk of HIV acquisition [4,5]. These factors include higher per-sex-act risk of acquisition from increased biological susceptibility to HIV infection [6,7], limited ability to negotiate safer sex and condom use [8], poverty and school dropout [3–5], gender-based violence [9], and higher prevalence of unsuppressed viral load in older male partners [10–12]. 

Uganda has experienced substantial declines in HIV incidence and prevalence since the late 1990s, driven by early national responses [13] and later expansion of biomedical interventions such as voluntary medical male circumcision (VMMC) and widespread antiretroviral therapy (ART) coverage [14,15]. The HIV epidemic remains generalized, with marked geographic and age/sex heterogeneity; incidence tends to be highest among young women and in high-burden districts along major transport corridors and fishing communities [16]. 

Over the last decade, HIV incidence has declined substantially in AGYW across communities in southern and eastern Africa [17,18], especially compared to that of older women, whose incidence has remained relatively stable in certain settings [18–21]. Multiple factors, including the scale-up of biomedical interventions [18,22–25] and reductions in sexual behaviors that increase HIV risk [19], are likely contributors to incidence decline among AGYW [26], but no study has disentangled the independent effects of these hypothesized drivers. 

Age at first sex (AFS) marks the initiation of exposure to sexually transmitted infections (STIs), including HIV, and is associated with alarmingly high HIV risk in young African women [27]. Earlier initiation of sex is associated with higher risk of HIV acquisition [9,28–32] via several socio-behavioral [9] and biological [33] pathways. Consequently, delaying sex protects against HIV infection by reducing the time spent sexually active, lowering the overall number of sexual partners, and reducing biological and behavioral susceptibility to infection. Rising AFS in young adults has been observed across sub-Saharan Africa [34], driven by several social and structural factors, including rising socio-economic status (SES) and expanded educational opportunities for adolescents [35,36]. It is unclear, however, to what extent recently observed 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

3 / 18 



delays in AFS in young adults contribute to population-level declines in incidence among AGYW in the context of largescale expansion of biomedical interventions like ART and VMMC. 

Because biomedical and behavioral drivers act on HIV risk via conceptually distinct pathways, understanding their relative contributions has programmatic importance for funding and intervention prioritization. Biomedical interventions directly reduce biological susceptibility and infectiousness, while behavioral shifts modify the probability of exposure. These components can act synergistically, where, for example, reductions in partner numbers amplify the population-level impact of ART-driven decreases in community viral load [37], but may also operate redundantly when they target similar segments of the population. 

Here, we use a mathematical model calibrated to data from the Rakai Community Cohort Study (RCCS), a populationbased cohort in southern Uganda, to quantify the independent and combined contributions of ART, VMMC, and secular changes in AFS to historical and projected declines in HIV incidence among AGYW. 

#### **Methods** 

##### **Study data** 

The RCCS is one of the longest-standing population-based HIV surveillance programs, following an open cohort of adolescents and adults (15–49 years of age) from 30 continuously surveyed communities over a 20-year period between 1999 and 2019 (with continued follow-up to date). Approximately 40,000 adult residents enrolled in the RCCS, who were present for at least one survey round, provided data over the length of follow-up. While the focus of our study is on AGYW, we include all adults 15–49 in our analysis to provide epidemiological context for our results. 

Details of the RCCS and survey methods are found elsewhere [19,38]. Briefly, participants 15–49 years of age from a complete household census of 30 semi-urban and agrarian communities in four districts of southern Uganda were invited to participate in the longitudinal study. Participants were recruited into the open cohort throughout the study period and those who provided written informed consent were interviewed every 1–2 years between 1999 and 2019, constituting 14 survey rounds. Adolescents 15–17 years of age required assent with parental consent. Self-reported data on demographics, SES, sexual risk behaviors, partnership attributes, ever ART use, and circumcision status (for men), were collected at each survey round. Sexual behavior was captured through interviewer-administered surveys in private settings. Core questions (e.g., AFS, partnership status) remained consistent over time. HIV testing was offered to all adult participants (ages 15–49), and venous blood was obtained from those consenting to HIV testing (including 15–17-year-olds who assented with parental consent). Laboratory methodology for HIV testing is described elsewhere [19]. The analysis was restricted to residents at the time of survey. The mean participation rate among adults eligible for the survey ranges from 59% to 67% across survey rounds, with most non-participation due to an individual not being in the community at time of survey. Uptake of HIV testing among those reached is high across survey rounds [21]. Participants in the study completed, on average, 3.5 survey rounds. Self-reported ART coverage (percent of respondents who report ever having been on ART) was found to be similar in models adjusted for attributes associated with survey response [21], indicating low potential for selection bias. 

##### **Estimation of key outputs** 

HIV incidence was estimated from directly observed seroconversion among ~20,000 participants with an HIV–negative test followed by at least one HIV test during a subsequent survey round. For those testing positive at a subsequent survey round, a seroconversion round was imputed randomly between the last negative and the first positive testing round, a method that reduces precision but introduces minimal bias into estimates [39]. Follow-up was right censored at either the seroconversion round (for those testing positive) or last negative test round (for those who remained serially negative). Individuals with missing HIV status between two non-missing survey rounds with the same status (e.g., two negatives or two positives) had their missing HIV status filled in using the two non-missing rounds. For example, an individual with 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

4 / 18 



positive status at rounds 6 and 10 and missing status in between had positive status filled in for rounds 7, 8, and 9, with a similar method applied to those with missing test data between two negative tests. We excluded records where the first observed positive was on/before the last negative (i.e., no valid seroconversion window), which occurred rarely in the dataset. 

Person-years of follow-up and crude numbers of incident infections were calculated for each survey round for individuals included in the incidence cohort. Smoothed Poisson generalized additive models (GAMs) [40] with an offset for person-years at risk [41] were used to estimate sex-specific smoothed incidence rates and 95% confidence intervals. Age and survey round were specified as a smooth function with a main effect and interaction. GAMs were fit with penalized, thin plate regression splines [40], (isotropic, locally weighted regression smoothers). The expected number of seroconversions _E_ ( _yi_ ) was estimated as the product of the Poisson-distributed seroconversion rate _λi_ and person-time at risk _Ti_ . Linear combinations of 1- and 2-dimensional smooth terms, _f_ 1, _..._ , _fp_ were included as main effects in the model: 





where _β_ 0 is an intercept, _εi_ are identically distributed and independent (i.i.d.) errors, and _f_ 1, _..._ , _fp_ are smooth regression splines, defined as the sum of piece-wise polynomial basis functions _bj_ and regression coefficients _Zj_ with basis dimension _J_ : 



Generalized linear models (GLMs) were also fit with categorical terms for survey round and age group to estimate sex, age group, and round-specific incidence rates and 95% confidence bounds to compare with smoothed GAMs. 



HIV prevalence was estimated cross-sectionally at each survey round using binomial GAMs with a logit link function: 



ART coverage (% on ART), male circumcision coverage (% circumcised), and prevalence of having initiated sex (% reporting ever having sex), were similarly estimated cross-sectionally at each survey round for all individuals with non-missing data on each indicator using binomial GAMs with the sames specification as the HIV prevalence models. 

##### **Mathematical modeling** 

Micro-simulation modeling was implemented using the epidemiological modeling software EMOD-HIV, an agent-based, stochastic, network transmission model described in detail at <u>https://docs.idmod.org/projects/emod-hiv/en/latest</u> and elsewhere [42]. EMOD simulates the natural history of HIV progression, considering the variable health states of individuals, such as CD4 cell count and WHO disease stage. A diagram of model structure can be found at <u>https://docs.idmod.org/ projects/emodpy-hiv/en/latest/emod/hiv-model-overview.html.</u> 

EMOD uses data on age-specific fertility, mortality, and sexual relationship formation [43], and models the cyclical flow of people living with HIV through the HIV care cascade. ART and VMMC were allocated based on age, sex, and 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

5 / 18 



year-specific coverage estimates from cohort data. We estimated a per-contact ART efficacy of 92% [44], to reflect “realworld” barriers to suppression like adherence and undetected drug resistance. Other factors in our model that modify the transmission probability include condom usage, circumcision status of the male HIV–negative partner, age of the female HIV–negative partner (to capture increased biological susceptibility of younger women), and presence of an STI. 

EMOD simulates the age, gender, and risk-group-specific sexual network using a sexual partner pair formation algorithm (PFA) described previously [43]. The PFA provides a detailed representation of the age-specific structuring of heterosexual networks—a phenomenon that contributes to the age- and gender-specific patterns of HIV transmission [27,43]. We capture the effects of delayed age at sexual debut on relationship formation by matching to survey data the percentage of individuals by age and sex available to form relationships on the network. In this way, changes in the proportion of individuals reaching sexual debut over time affect both the person-time exposed to HIV and the biological risk of acquisition among those delaying sex to older ages. The PFA allows redistribution of partnerships within the network and therefore partnership replacement can occur in response to changes in sexual debut. In this way, older male partners who would otherwise form relationships with younger women instead form partnerships with similarly aged women. 

Models were calibrated to age-, gender-, and year-specific HIV prevalence and age-, gender-, and year-specific population numbers from the RCCS between 1999 and 2019. Cohort-based estimates of ART coverage, VMMC coverage, and proportion having initiated sex by age, sex, and round were specified as modeled inputs. Pre-exposure prophylaxis (PrEP) was not included in the model because of its limited availability in the population and the uncertainty around its future scale-up in the population. A total of 100 best-fitting parameter sets were sampled from 6,600 simulations using roulette resampling in proportion to the likelihood. Uncertainty was incorporated into modeled estimates using a range of model parameters calibrated to observed epidemiologic trends. A summary of calibrated and static model parameter values and descriptions can be found in (Tables B and C in <u>S1 File).</u> 

##### **Model scenarios and outcomes** 

For historical (2000–2020) and future projections (2000–2050), we modeled HIV incidence per 100 person-years, cumulative infections averted, and cumulative % of infections averted. We compare several counter-factual scenarios to a baseline scenario, which captures the historical scale-up of ART/VMMC and the observed increases in AFS between 2000 and 2019. The four counterfactual scenarios are as follows: (1) a scenario with no ART scale-up (ART coverage set at zero), (2) a scenario with no VMMC scale-up (VMMC coverage set at zero), (3) a scenario with no changes in AFS (set at baseline levels estimated at the start of the cohort study), and (4) a scenario with no interventions (including no changes in AFS). For each scenario, we held levels of each intervention and AFS constant from 2020 to 2050 for projected impacts. 

##### **Ethics** 

Ethical approval for the RCCS was obtained from the Uganda Virus Research Institute’s Research Ethics Committee (No: GC/127/19/11/137) and the Uganda National Council for Science and Technology (HS 540). Approval was also obtained from IRBs of collaborating institutions, including the Committee for Human Research at the Johns Hopkins University School of Public Health and School of Medicine (JHU NA_00069085) and the Western University Institutional Review Board. All participants provided written informed consent for the broader protocol under the RCCS. 

#### **Results** 

##### **Study population** 

The population of adult residents ages 15–49 enrolled in the RCCS who participated in at least one of the 14 survey rounds between 1999 and 2019 included 40,800 participants (17,800 men and 23,000 women). Mean age at first survey 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

6 / 18 



visit was 23.7 years in women and 24.1 years in men. Among women 15–24 included in the analysis of AGYW, mean age at first survey visit was 18.8 years, 48.3% had ever been married, mean AFS was 15.7 years, and mean number of sex partners among those sexually active in the last year was 1.2. 

##### **HIV incidence** 

The cohort providing data to estimate HIV incidence (those with a negative test followed by a subsequent test) included 22,017 participants aged 15–49, among whom 1,317 incident infections were observed (795 in women and 522 in men) in 141,537 person-years of follow-up, (76,056 person-years of follow-up in women and 65,481 person-years of follow-up in men), resulting in a crude incidence rate of 0.93/100 py (0.88–0.98) overall, and 1.05/100 py (0.97–1.12) in women and 0.80/100 py (0.73–0.87) in men over the 20-year study period. A full enumeration of incident infections, person-years, incidence/100py, and 95% confidence intervals (CIs) by age group and year for both men and women can be found in Table A in <u>S1 File.</u> 

Among women 15–24 years of age, 283 incident infections were observed in 22,827 person-years, a crude incidence rate of 1.24 per 100 py (1.10–1.39) (Fig 1). Based on smoothed GAM models, HIV incidence in women 15–24 declined by 71% (from 1.57 per 100 py in 2000 to 0.45 per 100 py in 2019), with most of the decline occurring after 2014 and a marked drop between 2016 and 2017. Older age groups of women also experienced declines in incidence, though less than that of the youngest women: incidence declined by 52% among women 25–34 (from 1.35 per 100 py in 2000 to 0.65 per 100 py in 2019) and by 44% among women 35–49 (from 0.81 per 100 py in 2000 to 0.45 per 100 py in 2019). The larger relative decline among younger versus older women resulted in a shift toward an older incidence age distribution in 2019 compared with 2000, with the highest incidence shifting from the 15–24 group in 2000 to the 25–34 group in 2019 <u>(Fig 2). The age group with the highest incidence increased by about 10 years over the 20-year study period, peaking</u> among women 20–24 years in 2000 and among women 30–34 years of age in 2019. 



**Fig 1. Age-specific HIV incidence in the Rakai Community Cohort Study over time (2000-2019) among women 15–49, estimated from cohort data.** Point estimates and 95% confidence intervals (error bars) estimated from categorical generalized linear models (GLMs); smoothed incidence curves and 95% confidence intervals (ribbons) estimated from smoothed generalized additive models (GAMs). Note incidence is on a log2 scale. 

<u>https://doi.org/10.1371/journal.pmed.1004993.g001</u> 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

7 / 18 





**Fig 2. Smoothed continuous age distributions of HIV incidence among women 15–49 comparing the first (year 2000) and last (year 2019) survey rounds.** Incidence estimated from cohort data using smoothed generalized additive models (GAMs). Note incidence is on a log2 scale. <u>https://doi.org/10.1371/journal.pmed.1004993.g002</u> 

##### **ART coverage, VMMC coverage, and percent ever initiating sex** 

<u>Fig 3</u> shows temporal trends in ART coverage (% on ART), VMMC coverage (% circumcised), and the % of young men and women who reported ever initiating sex. ART began to scale-up after 2004 and steadily increased to 2019 and increased earlier and to higher coverage in older men and women. By 2019, the highest coverage was in women 45–49 years of age, 94% (92%–96%) and the lowest ART coverage in men 20–24 years of age, 32% (17%–52%). 

The percentage of circumcised men increased steadily over the study period. VMMC scaled up slowly from 1999 to 2009, after which it climbed more steeply to 2019. VMMC coverage was similar across all ages prior to 2010 and increased more rapidly in younger men thereafter. By 2019, 80% (79%–82%) of men 15–19 were circumcised compared to 60% (56%–63%) of men 45–49 years of age (Fig 3). 

The proportion of men and women 15–24 years of age who reported ever having initiated sex declined over the course of the study. Among women 15–19 years of age, half as many reported having initiated sex in 2019 compared to 1999 (from 80% to <40%). Similar declines were reported by young men. By 2019, similar proportions of young men and women reported having initiated sex (Fig 3). 

##### **Mathematical modeling** 

Calibrated model fits to observed HIV prevalence by age, sex, and year are shown in (Figs A and B in <u>S1 File). Modeled</u> HIV incidence among women 15–24 years of age had a similar trend between 2000 and 2020 as that of directly observed incidence estimated from the RCCS, though modeled estimates tended to be slightly higher than observed incidence <u>(Fig 4). Modeled incidence declined from 2.1/100 py (1.6–2.6/100 py) in year 2000 to 0.47/100 py (0.29–0.64/100 py) in</u> year 2020 and is projected to continue to decline to 0.2/100 py (0.07–0.39/100 py) by 2040 assuming stable rates of ART, VMMC, and AFS over that time horizon. 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

8 / 18 





**Fig 3. Antiretroviral (ART) coverage (by age-group and sex), voluntary medical male circumcision (VMMC) (by age-group), and prevalence of having initiated sex among 15–19 and 20–24 (by sex).** Point estimates and 95% confidence bounds estimated from smoothed generalized additive models (GAMs) with an interaction between year and age-group. 

<u>https://doi.org/10.1371/journal.pmed.1004993.g003</u> 



**Fig 4. Comparison of modeled HIV incidence and estimated yearly incidence observed in the Rakai Community Cohort Study (RCCS) among women 15–24 years of age.** Purple curve with ribbon shows range of 100 simulations from modeled incidence. 

<u>https://doi.org/10.1371/journal.pmed.1004993.g004</u> 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

9 / 18 



HIV incidence and cumulative infections averted are shown over time for women aged 15–19 and 20–24 for each counterfactual scenario relative to the baseline scenario (Fig 5). Modeled increases in AFS (by 2 years in men and 3 years in women) (Fig 6a) had the largest effect on incidence in women 15–19 years of age, averting 17% of cumulative infections between 2000 and 2020 and 37% of cumulative infections between 2000 and 2050 (Fig 5). The incidence rate among 15–19 year olds in 2020 was 69% lower in the baseline, 0.26/100 py (0.15–0.40/100 py) versus the counterfactual scenario with no change in AFS, 0.83/100 py (0.51–1.27/100 py), and in 2050 the incidence rate is projected to be 75% lower in the baseline, 0.08/100 py (0.01–0.17/100 py) versus the counterfactual scenario with no change in AFS, 0.31/100 py (0.08–0.77py) (Table 1). Among women 20–24 years of age, increases in AFS had no effect on cumulative incidence between 2000 and 2020, and averted 13% of cumulative infections by 2050. In women 20–24 years of age, incidence in 2050 is projected to be 45% lower in the baseline scenario, 0.21/100 py (0.05–0.53/100 py) compared to the AFS counterfactual scenario, 0.38/100 py (0.11–0.73/100 py) among women 20–24 years of age. 



**Fig 5. Modeled counterfactual scenarios compared to baseline among women 15-24.** (Top panel) mean incidence rates and (bottom panel) mean cumulative infections averted among women 15–19 and 20–24 by scenario. The percentage of cumulative infections averted is the percent reduction in cumulative infections between the counterfactual scenario and the baseline scenario. 

<u>https://doi.org/10.1371/journal.pmed.1004993.g005</u> 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

10 / 18 





**Fig 6. Modeled age at first sex and changes in numbers of partners from baseline. (a)** Median age at first sex (AFS) by year in the baseline scenario (solid black lines) compared to no change in AFS scenario (dotted lines). **(b)** Distribution of AFS by year. **(c)** Crude number of sexual relationships formed by age, sex, and scenario (baseline vs. no change in AFS). **(d)** Difference in crude number of sexual relationships formed between baseline scenario and no change in AFS scenario. Numbers to the left of zero indicate fewer relationships formed in the baseline scenario and numbers to the right of zero indicate more relationships in the baseline scenario relative to the no change in AFS scenario. 

<u>https://doi.org/10.1371/journal.pmed.1004993.g006</u> 

ART scale-up to date had a more moderate effect on incidence in women 15–19 years of age and the largest effect of any intervention on incidence in women 20–24 years of age. ART scale-up averted 7% of infections in women 15–19 years of age and 13% of infections in women 20–24 years of age between 2000 and 2020. By 2050, ART scale-up is projected to avert 28% of infections in women 15–19 years of age and 43% of infections in women 20–24 years of age. In 2020 incidence in women 15–19 years of age was 54% lower in the baseline scenario, 0.26/100 py (0.15–0.40/100 py) compared to the scenario without ART, 0.57/100 py (0.38–0.79/100py), and by 2050 incidence in women 15–19 years of age is projected to be 78% lower in the baseline, 0.08/100 py (0.01–0.17/100 py) compared to incidence in the scenario without ART, 0.36/100 py (0.19–0.55/100 py). VMMC scale-up to date (Fig 3) had a small impact on incidence reduction in young women to date, averting 4% of cumulative infections in women 15–19 years of age and 5% of cumulative infections in women 20–24 years of age between 2000–2020, and a larger impact over longer time horizons: 13% of cumulative infections averted in women 15–19 years of age and 22% of cumulative infections averted in women 20–24 years of age between 2000 and 2050. 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

11 / 18 



**Table 1. Modeled age and year-specific incidence rates by scenario among women 15-24.** 

|**Scenario**|**Age**|**Year**|**Incidenceper 1**|**00py**||
|---|---|---|---|---|---|
||||Mean|lb|ub|
|Baseline|15–19|2020|0.26|0.15|0.40|
|||2050|0.08|0.01|0.17|
||20–24|2020|0.73|0.44|1.01|
|||2050|0.21|0.05|0.53|
|No ART|15–19|2020|0.57|0.38|0.79|
|||2050|0.36|0.19|0.55|
||20–24|2020|1.66|1.13|2.29|
|||2050|1.03|0.54|1.54|
|No change in AFS|15–19|2020|0.83|0.51|1.27|
|||2050|0.31|0.08|0.77|
||20–24|2020|0.95|0.55|1.33|
|||2050|0.38|0.11|0.73|
|No VMMC|15–19|2020|0.36|0.22|0.56|
|||2050|0.17|0.05|0.33|
||20–24|2020|0.96|0.62|1.32|
|||2050|0.52|0.16|0.92|
|No Interventions|15–19|2020|2.31|1.60|3.27|
|||2050|2.70|1.65|3.98|
||20–24|2020|2.61|1.65|3.71|
|||2050|3.09|1.63|4.63|



Mean and 95% credible intervals. Antiretroviral therapy <u>(ART), age at first sex (AFS), voluntary medical male circumcision (VMMC) https://doi.org/10.1371/journal.pmed.1004993.t001</u> 

Combined, all three scenarios (ART, VMMC, and increased AFS) reduced cumulative infections by 32% in women 15–19 years of age and by 19% in women 20–24 years of age between 2000 and 2020 and reduced cumulative infections by 74% in women 15–19 years of age and 65% in women 20–24 years of age between 2000 and 2050. The combined effect of the three scenarios when modeled together was similar to the sum of the individual effects of each scenario for women 15–19 years of age over both time horizons and for women 20–24 years of age between 2000 and 2020, indicating largely additive effects of both interventions and increases in AFS. For women 20–24 years of age between 2000 and 2050, the combined effect for all scenarios was less than the sum of individual effects of each scenario, indicating some redundancy between ART, VMMC, and increasing AFS in that age group. 

Modeled mean AFS increased by 2 years in men and 3 years in women between 2000 and 2020 (Fig 6a), shifting the modeled age distribution of first sex to older ages (Fig 6b). Increases in AFS changed the modeled structure of the sexual network. Under the baseline scenario, where AFS was delayed, men of all ages formed fewer total sexual relationships due to fewer sexual partnerships available with younger women. However, in women, only younger women (<23 years of age) formed fewer relationships. Older women (23–31 years of age) formed _more_ relationships, as men who were unable to form relationships with young women replaced those relationships with older women (Fig 6d). 

#### **Discussion** 

Through retrospective analysis of cohort data and mathematical modeling, we found that increasing AFS (by 2–3 years between 2000 and 2019), ART scale-up, and VMMC scale-up had substantial impacts on reducing HIV incidence among AGYW. Increasing AFS was the largest contributor to incidence decline in women 15–19 years of age, whereas ART 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

12 / 18 



alone contributed the most to incidence decline in 20–24 years of age. The scale-up of VMMC impacted incidence over a longer time horizon, with a modest effect on historical incidence declines. These interventions and observed changes in sexual behavior, for the most part, acted additively, where their combined effects were equivalent to the sum of their independent effects. Our results suggest that sustained levels of ART, VMMC, and AFS will continue to reduce incidence in AGYW over the next 25–30 years. 

Considerable investments have been made in behavioral and biomedical HIV prevention in AGYW [45,46]. The measured impact of these interventions on HIV risk in AGYW, however, has been mixed [47,48]. The effectiveness of PrEP for HIV prevention in women under age 25 has been suboptimal due to numerous barriers in product uptake and adherence [49–51]. The efficacy of oral PrEP measured in clinical trials, for example, underperformed expectations due to low adherence in AGYW [52,53]. Behavior change interventions have also demonstrated mixed effectiveness in promoting safer sexual behaviors and reducing HIV risk [54]. Sexual behavior in young adults is complex and often negotiated in the context of imbalanced social, economic, and gender-based power dynamics within partnerships, including the potential for coercion and gender-based violence, thus challenging interventions that target individual-level behaviors. 

Despite the mixed effectiveness of behavioral interventions targeted at AGYW at high risk of HIV acquisition, long-term trends in SES and educational attainment may reduce social and behavioral vulnerability to HIV over their life course. Educational attainment is proximally associated with several behavioral risk factors including older age at sexual debut, older age at first marriage, fewer lifetime number of partners, lower probability of having an older male partner, lower frequency of sex with a partner, and less frequent unprotected sex [28,32,55–57]. Rising SES and lower prevalence of orphanhood, (resulting from an overall decline in HIV mortality), in the RCCS were associated with increases in school enrollment between 1994 and 2013, which in turn were associated with lower prevalence of HIV, lower adolescent pregnancy rates, higher use of modern contraception [58], and lower marriage rates [59], translating into increasing age at first marriage over time. The expansion of universal secondary education in Uganda in 2007 [60], which removed the barrier of school fees, may have also contributed to secular changes in sexual behavior, and, in turn, to declining HIV risk in our study [36]. Whether this trend is observed in other settings can add to an evidence base supporting expanded access to secondary education for young women as part of HIV prevention programs. 

We found a disproportionately larger decline in incidence in women 15–24 years of age compared to older women, resulting in an age shift in incidence, a finding that has been confirmed from epidemiological [20] and phylogenetic data [21]. Reasons for age-heterogeneity in incidence decline are varied but include aging of HIV prevalence [20], targeted primary prevention to younger cohorts [61,62], and disproportionately larger reductions in sexual risk behaviors observed in younger cohorts [34]. Still, young adults in high-burden settings face challenges in achieving high coverage and effectiveness of treatment and prevention interventions that reduce risk in those populations. In our study, most men living with HIV under the age of 25 and nearly 40% of young women living with HIV (20–24 years of age) reported no ART use, even under universal test and treat, a pattern consistently observed across populations in sub-Saharan Africa [63]. Given the importance of ART as secondary prevention to reduce incidence in AGYW, targeted interventions towards increasing ART coverage in men, could contribute to additional reductions in HIV transmission [21]. 

There are several epidemiological and model-based assumptions that may limit the interpretation of our analysis. Self-reported sexual behavior is subject to social desirability bias, especially in the ‘Abstinence-First’ era in Uganda, which emerged in the early 2000’s as part of the abstinence, be faithful, use condoms approach, and may add some degree of error to our estimates of the proportion initiating sex in the population. Studies from East Africa have documented under-reporting of sexual activity in similar contexts [64]. Reporting bias alone, however, is unlikely to explain the large changes in AFS in our study. First, we observed a similar change in AFS in young men, who may experience less reporting pressures than their female peers. Second, abstinence-first programs have existed in Uganda prior to the start of the Rakai cohort, and thus any bias in reporting in the era following the introduction of abstinence-first would not be expected to change over time. Finally, national demographic indicators, such as rising age at marriage and first birth, corroborate 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

13 / 18 



real delays in sexual initiation [57]. We also rely on self-report of circumcision status and ART use to parameterize our model, both of which are subject to bias in level and trend over time, though previous analysis has also shown high specificity of self-reported ART when validated against clinically observed ART use [19]. 

In modeling delays in AFS over time, we assume that older male partners who would otherwise form relationships with younger women (who are delaying sex) are replacing those relationships with older women. This can, in turn, increase the number of older women forming relationships on the network, potentially offsetting some of the incidence reduction from young women delaying sex. Previous modeling has shown that the effects of delaying sexual debut are sensitive to whether partnership replacement is assumed [65]. It is plausible that the demand from men on the sexual network will draw more partners from similarly aged women as young women delay sex. In addition to commonly forming partnerships with younger women, a phenomenon observed consistently over time in the Rakai cohort [66] and elsewhere [27], older men also tend to partner with similarly aged women [67]. Further study is needed to understand how increasing AFS over time affects the structure of the sexual network, including any compensation for fewer young people available to form sexual relationships. These assumptions, however, likely result in a lower impact of delayed AFS in our model, and our findings should thus be interpreted as a conservative estimate of those effects. 

Second, model-based incidence estimates for some years in our model tended to be slightly higher than cohort-based estimates, especially in the early years of the study period (pre-2010). The implications of this are that modeled changes in incidence over the study period may be overstated. Our model may not have fully captured the risk distribution of the study population earlier in the epidemic. One hypothesis is that higher-risk individuals have been systematically missing from the population from which incidence was estimated, especially in the earlier part of the study period. Incidence can only be directly observed in a resident population (who are present at multiple survey rounds). Mobile individuals, who tend to have higher HIV prevalence, would therefore be systematically excluded from the longitudinal cohort if they came into the cohort already positive. This would lead to a lower incidence in the population compared to our modeled estimates. Methods exist to correct for this bias by considering both left and right censoring using mechanistic modeling [68], though there are also limitations to this approach compared to directly observed methods. Furthermore, we projected estimated impacts of interventions/behavioral changes to 2050, and those estimates are subject to substantial uncertainty given future programmatic/funding shifts and other unforeseen dynamics. 

Strengths of our analysis include the ability to disentangle the hypothesized drivers of HIV incidence decline in AGYW, providing evidence that existing interventions and behavioral changes act synergistically to impact both short and longterm incidence trajectories. We also dynamically model changes in sexual risk behavior over time to match observed longitudinal trends, something that previous models have only done theoretically [65]. Our model shows that both protective changes in risk behavior and scale-up of ART have contributed to historical declines in HIV incidence in AGYW (with VMMC acting over a longer time horizon), and if sustained, have the potential to continue to drive down infections in high-burden settings. 

#### **Supporting information** 

**S1 File. Table A. Incidence in the Rakai Community Cohort Study (RCCS) from 2000 to 2019.** Person-years (py), incident infections, and incidence (per 100 py) estimates and 95% confidence intervals (CI) using generalized linear models (GLMs) by age group, sex, and survey round (with corresponding year). **Table B. Model parameters used in calibration.** Median and interquartile range (IQR) from 100 best-fitting parameter sets. **Table C. Select static model parameters used to fit the EMOD HIV transmission model to Rakai survey data** . Models fit to population, HIV prevalence, and anti-retroviral therapy (ART) coverage. **Fig A. Modeled year-specific prevalence and 95% credible interval by sex for adults aged 15–49.** Modeled prevalence (red curve) fit to observed adult HIV prevalence in the Rakai cohort (black points with 95% confidence intervals). **Fig B. Modeled sex-, age-, and year-specific prevalence fit to observed prevalence in the Rakai cohort.** Point estimates and 95% credible intervals from model (lines with shaded ribbons) and 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

14 / 18 



observed prevalence (points and 95% confidence intervals). Note point estimates from Rakai cohort data are by round and thus are not available for some years. 

(DOCX) 

#### **Acknowledgments** 

We thank the participants of the Rakai Community Cohort Study for contributing their time, survey responses, and biological specimens. We also thank the Rakai Health Sciences Program field staff, data collectors, and community mobilizers whose dedication, care, and sustained engagement made the collection of high-quality longitudinal data possible. We additionally acknowledge the Institute for Disease Modeling for software and modeling infrastructure support. 

The content of this publication does not necessarily reflect the views or policies of the Department of Health and Human Services, nor does mention of trade names, commercial products, or organizations imply endorsement by the U.S. Government. 

#### **Author contributions** 

- **Conceptualization:** Adam Akullian, Victor Ssempijja, John Santelli, William J. M. Probert, Oliver Ratmann, Christophe Fraser, Mary Kate Grabowski. 

- **Data curation:** Victor Ssempijja, Fred Nalugoda, Gertrude Nakigozi, Robert Ssekubugu, Ronald M. Galiwango, Joseph Kagaayi, Godfrey Kigozi, Mary Kate Grabowski, David Serwadda. 

**Formal analysis:** Adam Akullian, William J. M. Probert, Mary Kate Grabowski. 

- **Funding acquisition:** Gertrude Nakigozi, Larry W. Chang, Robert Ssekubugu, Ronald H. Gray, Maria J. Wawer, Thomas C. Quinn, Godfrey Kigozi, Mary Kate Grabowski, David Serwadda. 

**Investigation:** Mary Kate Grabowski, David Serwadda. 

**Methodology:** Adam Akullian, John Santelli, Jeffrey W. Imai-Eaton, Mary Kate Grabowski. 

**Project administration:** Victor Ssempijja, Fred Nalugoda, Joseph Kagaayi. 

**Resources:** Gertrude Nakigozi, Joseph Kagaayi. 

**Software:** Daniel Bridenbecker. 

**Supervision:** Fred Nalugoda, John Santelli, Larry W. Chang, Steven J. Reynolds, Christophe Fraser, Joseph Kagaayi, Mary Kate Grabowski, David Serwadda. 

**Validation:** William J. M. Probert, Oliver Ratmann. 

**Visualization:** Adam Akullian. 

**Writing – original draft:** Adam Akullian, Mary Kate Grabowski. 

- **Writing – review & editing:** Adam Akullian, Victor Ssempijja, Daniel Bridenbecker, Fred Nalugoda, Gertrude Nakigozi, John Santelli, Philip Kreniske, Larry W. Chang, Steven J. Reynolds, Robert Ssekubugu, Ronald H. Gray, Maria J. Wawer, Thomas C. Quinn, Ronald M. Galiwango, William J. M. Probert, Jeffrey W. Imai-Eaton, Oliver Ratmann, Mary Kate Grabowski. 

#### **References** 

**1.** Karim QA, Kharsany ABM, Frohlich JA, Werner L, Mashego M, Mlotshwa M, et al. Stabilizing HIV prevalence masks high HIV incidence rates amongst rural and urban women in KwaZulu-Natal, South Africa. Int J Epidemiol. 2011;40(4):922–30. https://doi.org/10.1093/ije/dyq176 PMID: <u>21047913</u> 

**2.** Mabaso M, Sokhela Z, Mohlabane N, Chibi B, Zuma K, Simbayi L. Determinants of HIV infection among adolescent girls and young women aged 15-24 years in South Africa: a 2012 population-based national household survey. BMC public health. 2018;18(1):183. 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

15 / 18 



**3.** Harrison A, Colvin CJ, Kuo C, Swartz A, Lurie M. Sustained high HIV incidence in young women in southern africa: social, behavioral, and structural factors and emerging intervention approaches. Curr HIV/AIDS Rep. 2015;12(2):207–15. <u>https://doi.org/10.1007/s11904-015-0261-0</u> PMID: <u>25855338</u> 

**4.** Santelli JS, Edelstein ZR, Mathur S, Wei Y, Zhang W, Orr MG, et al. Behavioral, biological, and demographic risk and protective factors for new HIV infections among youth in Rakai, Uganda. J Acquir Immune Defic Syndr. 2013;63(3):393–400. <u>https://doi.org/10.1097/QAI.0b013e3182926795</u> PMID: <u>23535293</u> 

**5.** Birdthistle I, Tanton C, Tomita A, de Graaf K, Schaffnit SB, Tanser F, et al. Recent levels and trends in HIV incidence rates among adolescent girls and young women in ten high-prevalence African countries: a systematic review and meta-analysis. Lancet Glob Health. 2019;7(11):e1521–40. <u>https://doi.org/10.1016/S2214-109X(19)30410-3 PMID: 31607465</u> 

**6.** Yi TJ, Shannon B, Prodger J, McKinnon L, Kaul R. Genital immunology and HIV susceptibility in young women. Am J Reprod Immunol. 2013;69 Suppl 1:74–9. <u>https://doi.org/10.1111/aji.12035</u> PMID: <u>23157424</u> 

**7.** Mtshali A, Ngcapu S, Mindel A, Garrett N, Liebenberg L. HIV susceptibility in women: the roles of genital inflammation, sexually transmitted infections and the genital microbiome. J Reprod Immunol. 2021;145:103291. <u>https://doi.org/10.1016/j.jri.2021.103291 PMID: 33647576</u> 

**8.** Mathur S, Wei Y, Zhong X, Song X, Nalugoda F, Lutalo T, et al. Partner characteristics associated with HIV acquisition among youth in Rakai, Uganda. J Acquir Immune Defic Syndr. 2015;69(1):75–84. <u>https://doi.org/10.1097/QAI.0000000000000539</u> PMID: <u>25622058</u> 

**9.** Pettifor A, O’Brien K, Macphail C, Miller WC, Rees H. Early coital debut and associated HIV risk factors among young women and men in South Africa. Int Perspect Sex Reprod Health. 2009;35(2):82–90. <u>https://doi.org/10.1363/ifpp.35.082.09</u> PMID: <u>19620092</u> 

**10.** Grobler A, Cawood C, Khanyile D, Puren A, Kharsany ABM. Progress of UNAIDS 90-90-90 targets in a district in KwaZulu-Natal, South Africa, with high HIV burden, in the HIPSS study: a household-based complex multilevel community survey. Lancet HIV. 2017;4(11):e505–13. https://doi. <u>org/10.1016/S2352-3018(17)30122-4</u> PMID: <u>28779855</u> 

**11.** Agolory S, de Klerk M, Baughman AL, Sawadogo S, Mutenda N, Pentikainen N, et al. Low case finding among men and poor viral load suppression among adolescents are impeding Namibia’s ability to achieve UNAIDS 90-90-90 targets. Open Forum Infect Dis. 2018;5(9):ofy200. <u>https://doi. org/10.1093/ofid/ofy200</u> 

**12.** Huerga H, Van Cutsem G, Ben Farhat J, Puren A, Bouhenia M, Wiesner L, et al. Progress towards the UNAIDS 90-90-90 goals by age and gender in a rural area of KwaZulu-Natal, South Africa: a household-based community cross-sectional survey. BMC Public Health. 2018;18(1):303. <u>https:// doi.org/10.1186/s12889-018-5208-0</u> PMID: <u>29499668</u> 

**13.** Stoneburner RL, Low-Beer D. Population-level HIV declines and behavioral risk avoidance in Uganda. Science. 2004;304(5671):714–8. <u>https://doi. org/10.1126/science.1093166</u> PMID: <u>15118157</u> 

**14.** Loevinsohn G, Kigozi G, Kagaayi J, Wawer MJ, Nalugoda F, Chang LW, et al. Effectiveness of voluntary medical male circumcision for human immunodeficiency virus prevention in Rakai, Uganda. Clin Infect Dis. 2021;73(7):e1946–53. <u>https://doi.org/10.1093/cid/ciaa1533</u> PMID: <u>33043978</u> 

**15.** Kong X, Kigozi G, Ssekasanvu J, Nalugoda F, Nakigozi G, Ndyanabo A, et al. Association of medical male circumcision and antiretroviral therapy scale-up with community HIV incidence in Rakai, Uganda. JAMA. 2016;316(2):182–90. <u>https://doi.org/10.1001/jama.2016.7292</u> PMID: <u>27404186</u> 

**16.** Chang LW, Grabowski MK, Ssekubugu R, Nalugoda F, Kigozi G, Nantume B, et al. Heterogeneity of the HIV epidemic in agrarian, trading, and fishing communities in Rakai, Uganda: an observational epidemiological study. Lancet HIV. 2016;3(8):e388–96. https://doi.org/10.1016/S2352- <u>3018(16)30034-0</u> PMID: <u>27470029</u> 

**17.** Birdthistle I, Kwaro D, Shahmanesh M, Baisley K, Khagayi S, Chimbindi N, et al. Evaluating the impact of DREAMS on HIV incidence among adolescent girls and young women: a population-based cohort study in Kenya and South Africa. PLoS Med. 2021;18(10):e1003837. <u>https://doi. org/10.1371/journal.pmed.1003837</u> PMID: <u>34695112</u> 

**18.** Vandormael A, Akullian A, Siedner M, de Oliveira T, Bärnighausen T, Tanser F. Declines in HIV incidence among men and women in a South African population-based cohort. Nat Commun. 2019;10(1):5482. <u>https://doi.org/10.1038/s41467-019-13473-y</u> PMID: <u>31792217</u> 

**19.** Grabowski MK, Serwadda DM, Gray RH, Nakigozi G, Kigozi G, Kagaayi J, et al. HIV prevention efforts and incidence of HIV in Uganda. N Engl J Med. 2017;377(22):2154–66. <u>https://doi.org/10.1056/NEJMoa1702150</u> PMID: <u>29171817</u> 

**20.** Akullian A, Vandormael A, Miller JC, Bershteyn A, Wenger E, Cuadros D, et al. Large age shifts in HIV-1 incidence patterns in KwaZulu-Natal, South Africa. Proc Natl Acad Sci U S A. 2021;118(28):e2013164118. <u>https://doi.org/10.1073/pnas.2013164118</u> PMID: <u>34244424</u> 

**21.** Monod M, Brizzi A, Galiwango RM, Ssekubugu R, Chen Y, Xi X, et al. Longitudinal population-level HIV epidemiologic and genomic surveillance highlights growing gender disparity of HIV transmission in Uganda. Nat Microbiol. 2024;9(1):35–54. <u>https://doi.org/10.1038/s41564-023-01530-8</u> PMID: <u>38052974</u> 

**22.** Akullian A, Morrison M, Garnett GP, Mnisi Z, Lukhele N, Bridenbecker D. The effect of 90-90-90 on HIV-1 incidence and mortality in eSwatini: a mathematical modelling study. The Lancet HIV. 2020;7(5):e348–58. 

**23.** Borgdorff MW, Kwaro D, Obor D, Otieno G, Kamire V, Odongo F, et al. HIV incidence in western Kenya during scale-up of antiretroviral therapy and voluntary medical male circumcision: a population-based cohort analysis. Lancet HIV. 2018;5(5):e241–9. <u>https://doi.org/10.1016/S23523018(18)30025-0</u> PMID: <u>29650451</u> 

**24.** Kripke K, Vazzano A, Kirungi W, Musinguzi J, Opio A, Ssempebwa R, et al. Modeling the impact of Uganda’s safe male circumcision program: implications for age and regional targeting. PLoS One. 2016;11(7):e0158693. <u>https://doi.org/10.1371/journal.pone.0158693 PMID: 27410234</u> 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

16 / 18 



**25.** Kripke K, Okello V, Maziya V, Benzerga W, Mirira M, Gold E, et al. Voluntary medical male circumcision for HIV prevention in swaziland: modeling the impact of age targeting. PLoS One. 2016;11(7):e0156776. https://doi.org/10.1371/journal.pone.0156776 PMID: <u>27410687</u> 

**26.** Grilo SA, Thompson J, Chen IS, Nalugoda F, Lutalo T, Wei Y, et al. Declines in HIV incidence and prevalence and predictors among adolescents and young adults: an observational cohort study, Rakai, Uganda, 2005-2020. medRxiv. 2025. <u>https://doi.org/2025.01.07.25320118</u> 

**27.** Akullian A, Bershteyn A, Klein D, Vandormael A, Bärnighausen T, Tanser F. Sexual partnership age pairings and risk of HIV acquisition in rural South Africa. AIDS. 2017;31(12):1755–64. https://doi.org/10.1097/qad.0000000000001553 

**28.** Pettifor AE, van der Straten A, Dunbar MS, Shiboski SC, Padian NS. Early age of first sex: a risk factor for HIV infection among women in Zimbabwe. AIDS. 2004;18(10):1435–42. https://doi.org/10.1097/01.aids.0000131338.61042.b8 PMID: <u>15199320</u> 

**29.** Wand H, Ramjee G. The relationship between age of coital debut and HIV seroprevalence among women in Durban, South Africa: a cohort study. BMJ Open. 2012;2(1):e000285. <u>https://doi.org/10.1136/bmjopen-2011-000285</u> PMID: <u>22223838</u> 

**30.** Stöckl H, Kalra N, Jacobi J, Watts C. Is early sexual debut a risk factor for HIV infection among women in sub-Saharan Africa? A systematic review. Am J Reprod Immunol. 2013;69 Suppl 1:27–40. <u>https://doi.org/10.1111/aji.12043</u> PMID: <u>23176109</u> 

**31.** Hallett TB, Lewis JJC, Lopman BA, Nyamukapa CA, Mushati P, Wambe M, et al. Age at first sex and HIV infection in rural Zimbabwe. Stud Fam Plann. 2007;38(1):1–10. <u>https://doi.org/10.1111/j.1728-4465.2007.00111.x</u> PMID: <u>17385378</u> 

**32.** He J, Flaxman A, Imai-Eaton JW, Aravkin A, Zheng P, Sorensen R, et al. Association between early sexual debut and new HIV infections among adolescents and young adults in 11 African countries. AIDS Behav. 2024;28(7):2444–53. <u>https://doi.org/10.1007/s10461-024-04343-w PMID: 38878135</u> 

**33.** Hughes SM, Levy CN, Calienes FL, Martinez KA, Selke S, Tapia K, et al. Starting to have sexual intercourse is associated with increases in cervicovaginal immune mediators in young women: a prospective study and meta-analysis. Elife. 2022;11:e78565. <u>https://doi.org/10.7554/eLife.78565</u> PMID: <u>36281966</u> 

**34.** Nguyen VK, Eaton JW. Trends and country-level variation in age at first sex in sub-Saharan Africa among birth cohorts entering adulthood between 1985 and 2020. BMC Public Health. 2022;22(1):1120. <u>https://doi.org/10.1186/s12889-022-13451-y</u> PMID: <u>35659216</u> 

**35.** De Neve J-W, Fink G, Subramanian SV, Moyo S, Bor J. Length of secondary schooling and risk of HIV infection in Botswana: evidence from a natural experiment. Lancet Glob Health. 2015;3(8):e470–7. <u>https://doi.org/10.1016/S2214-109X(15)00087-X PMID: 26134875</u> 

**36.** Santelli JS, Edelstein ZR, Wei Y, Mathur S, Song X, Schuyler A. Trends in HIV acquisition, risk factors and prevention policies among youth in Uganda, 1999-2011. AIDS. 2015;29(2):211–9. 

**37.** Alsallaq RA, Baeten JM, Celum CL, Hughes JP, Abu-Raddad LJ, Barnabas RV, et al. Understanding the potential impact of a combination HIV prevention intervention in a hyper-endemic community. PLoS One. 2013;8(1):e54575. <u>https://doi.org/10.1371/journal.pone.0054575 PMID: 23372738</u> 

**38.** Wawer MJ, Sewankambo NK, Serwadda D, Quinn TC, Paxton LA, Kiwanuka N, et al. Control of sexually transmitted diseases for AIDS prevention in Uganda: a randomised community trial. Rakai Project Study Group. Lancet. 1999;353(9152):525–35. <u>https://doi.org/10.1016/s01406736(98)06439-3</u> PMID: <u>10028980</u> 

**39.** Vandormael A, Tanser F, Cuadros D, Dobra A. Estimating trends in the incidence rate with interval censored data and time-dependent covariates. Stat Methods Med Res. 2020;29(1):272–81. <u>https://doi.org/10.1177/0962280219829892</u> PMID: <u>30782096</u> 

**40.** Wood S. Generalized additive models: an introduction with R. CRC Press; 2006. 

**41.** Webster T, Vieira V, Weinberg J, Aschengrau A. Method for mapping population-based case-control studies: an application using generalized additive models. Int J Health Geogr. 2006;5:26. https://doi.org/10.1186/1476-072X-5-26 PMID: <u>16764727</u> 

**42.** Bershteyn A, Gerardin J, Bridenbecker D, Lorton CW, Bloedow J, Baker RS, et al. Implementation and applications of EMOD, an individual-based multi-disease modeling platform. Pathog Dis. 2018;76(5):fty059. <u>https://doi.org/10.1093/femspd/fty059</u> PMID: <u>29986020</u> 

**43.** Bershteyn A, Klein DJ, Eckhoff PA. Age-dependent partnering and the HIV transmission chain: a microsimulation analysis. J R Soc Interface. 2013;10(88):20130613. <u>https://doi.org/10.1098/rsif.2013.0613</u> PMID: <u>23985734</u> 

**44.** Donnell D, Baeten JM, Kiarie J, Thomas KK, Stevens W, Cohen CR, et al. Heterosexual HIV-1 transmission after initiation of antiretroviral therapy: a prospective cohort analysis. Lancet. 2010;375(9731):2092–8. <u>https://doi.org/10.1016/S0140-6736(10)60705-2 PMID: 20537376</u> 

**45.** Abdool Karim Q, Kharsany ABM, Frohlich JA, Werner L, Mlotshwa M, Madlala BT, et al. HIV incidence in young girls in KwaZulu-Natal, South Africa--public health imperative for their inclusion in HIV biomedical intervention trials. AIDS Behav. 2012;16(7):1870–6. <u>https://doi.org/10.1007/ s10461-012-0209-y</u> PMID: <u>22618892</u> 

**46.** Dellar RC, Dlamini S, Karim QA. Adolescent girls and young women: key populations for HIV epidemic control. J Int AIDS Soc. 2015;18(2 Suppl 1):19408. <u>https://doi.org/10.7448/IAS.18.2.19408</u> PMID: <u>25724504</u> 

**47.** Floyd S, Mulwa S, Magut F, Gourlay A, Mthiyane N, Kamire V, et al. DREAMS impact on HIV status knowledge and sexual risk among cohorts of young women in Kenya and South Africa. AIDS. 2022;36(Suppl 1):S61–73. <u>https://doi.org/10.1097/QAD.0000000000003157</u> PMID: <u>35766576</u> 

**48.** Lavoie M-CC, Blanco N, Lascko T, Baumhart C, Verbeek J, Stoebenau K, et al. The effects of the Determined, Resilient, Empowered, AIDS-free, Mentored, and Safe (DREAMS) program on HIV incidence and other health-related outcomes among adolescent girls and young women: a systematic review and meta-analysis. EClinicalMedicine. 2025;82:103176. <u>https://doi.org/10.1016/j.eclinm.2025.103176 PMID: 40242566</u> 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

17 / 18 



**49.** Ziraba A, Orindi B, Muuo S, Floyd S, Birdthistle IJ, Mumah J, et al. Understanding HIV risks among adolescent girls and young women in informal settlements of Nairobi, Kenya: lessons for DREAMS. PLoS One. 2018;13(5):e0197479. <u>https://doi.org/10.1371/journal.pone.0197479 PMID: 29851988</u> 

**50.** Laga M, Schwärtlander B, Pisani E, Sow PS, Caraël M. To stem HIV in Africa, prevent transmission to young women. AIDS. 2001;15(7):931–4. <u>https://doi.org/10.1097/00002030-200105040-00014</u> PMID: <u>11399966</u> 

**51.** Singh K, Sambisa W, Munyati S, Chandiwana B, Chingono A, Monash R, et al. Targeting HIV interventions for adolescent girls and young women in Southern Africa: use of the PLACE methodology in Hwange District, Zimbabwe. AIDS Behav. 2010;14(1):200–8. https://doi.org/10.1007/s10461- <u>009-9572-8</u> PMID: <u>19452272</u> 

**52.** Baeten JM, Palanee-Phillips T, Brown ER, Schwartz K, Soto-Torres LE, Govender V, et al. Use of a vaginal ring containing dapivirine for HIV-1 prevention in women. N Engl J Med. 2016;375(22):2121–32. <u>https://doi.org/10.1056/NEJMoa1506110</u> PMID: <u>26900902</u> 

**53.** Delany-Moretlwe S, Lombard C, Baron D, Bekker L-G, Nkala B, Ahmed K, et al. Tenofovir 1% vaginal gel for prevention of HIV-1 infection in women in South Africa (FACTS-001): a phase 3, randomised, double-blind, placebo-controlled trial. Lancet Infect Dis. 2018;18(11):1241–50. <u>https://doi.org/10.1016/S1473-3099(18)30428-6 PMID: 30507409</u> 

**54.** McCoy SI, Kangwende RA, Padian NS. Behavior change interventions to prevent HIV infection among women living in low and middle income countries: a systematic review. AIDS Behav. 2010;14(3):469–82. <u>https://doi.org/10.1007/s10461-009-9644-9</u> PMID: <u>19949847</u> 

**55.** Hargreaves JR, Morison LA, Kim JC, Bonell CP, Porter JDH, Watts C, et al. The association between school attendance, HIV infection and sexual behaviour among young people in rural South Africa. J Epidemiol Community Health. 2008;62(2):113–9. https://doi.org/10.1136/jech.2006.053827 PMID: <u>18192598</u> 

**56.** Stoner MCD, Pettifor A, Edwards JK, Aiello AE, Halpern CT, Julien A, et al. The effect of school attendance and school dropout on incident HIV and HSV-2 among young women in rural South Africa enrolled in HPTN 068. AIDS. 2017;31(15):2127–34. <u>https://doi.org/10.1097/ QAD.0000000000001584</u> PMID: <u>28692544</u> 

**57.** Ariho P, Kabagenyi A. Age at first marriage, age at first sex, family size preferences, contraception and change in fertility among women in Uganda: analysis of the 2006-2016 period. BMC Womens Health. 2020;20(1):8. <u>https://doi.org/10.1186/s12905-020-0881-4</u> PMID: <u>31948426</u> 

**58.** Santelli J, Mathur S, Song X, Huang TJ, Wei Y, Lutalo T, et al. Rising school enrollment and declining HIV and pregnancy risk among adolescents in Rakai district, Uganda, 1994-2013. Glob Soc Welf. 2015;2(2):87–103. <u>https://doi.org/10.1007/s40609-015-0029-x</u> PMID: <u>26075159</u> 

**59.** Spindler E, Hoffman S, Nalugoda F, Chen IS, Samari G, Lutalo T, et al. What’s driving girls’ adolescent marriage decline in Rakai, Uganda? The interplay between adolescent pregnancies and social determinants, 1999 - 2018. Int J Adolesc Youth. 2024;29(1):2384863. https://doi.org/10.1080/ <u>02673843.2024.2384863 PMID: 39308642</u> 

**60.** Kakuba C, Nzabona A, Asiimwe JB, Tuyiragize R, Mushomi J. Who accesses secondary schooling in Uganda; was the universal secondary education policy ubiquitously effective?. Int J Educ Dev. 2021;83:102370. <u>https://doi.org/10.1016/j.ijedudev.2021.102370</u> 

**61.** Zaidi J, Grapsa E, Tanser F, Newell M-L, Bärnighausen T. Dramatic increase in HIV prevalence after scale-up of antiretroviral treatment. AIDS. 2013;27(14):2301–5. <u>https://doi.org/10.1097/QAD.0b013e328362e832</u> PMID: <u>23669155</u> 

**62.** Bhavan KP, Kampalath VN, Overton ET. The aging of the HIV epidemic. Curr HIV/AIDS Rep. 2008;5(3):150–8. <u>https://doi.org/10.1007/s11904-0080023-3</u> PMID: <u>18627664</u> 

**63.** Green D, Tordoff DM, Kharono B, Akullian A, Bershteyn A, Morrison M, et al. Evidence of sociodemographic heterogeneity across the HIV treatment cascade and progress towards 90-90-90 in sub-Saharan Africa – a systematic review and meta-analysis. J Int AIDS Soc. 2020;23(3):e25470. <u>https://doi.org/10.1002/jia2.25470</u> PMID: <u>32153117</u> 

**64.** Woolf-King SE, Muyindike W, Hobbs MM, Kusasira A, Fatch R, Emenyonu N, et al. Vaginal prostate specific antigen (PSA) is a useful biomarker of semen exposure among HIV-infected Ugandan women. AIDS Behav. 2017;21(7):2141–6. <u>https://doi.org/10.1007/s10461-016-1433-7</u> PMID: <u>27224979</u> 

**65.** Hallett TB, Gregson S, Lewis JJC, Lopman BA, Garnett GP. Behaviour change in generalised HIV epidemics: impact of reducing cross-generational sex and delaying age at sexual debut. Sex Transm Infect. 2007;83 Suppl 1:i50-54. <u>https://doi.org/10.1136/sti.2006.023606</u> PMID: <u>17314125</u> 

**66.** Mwinnyaa G, Gray RH, Grabowski MK, Ssekasanvu J, Ndyanabo A, Ssekubugu R. Brief report: Age-disparate relationships and HIV prevalence among never married women in Rakai, Uganda. J Acquir Immune Defic Syndr. 2018;79(4):430–4. 

**67.** de Oliveira T, Kharsany ABM, Gräf T, Cawood C, Khanyile D, Grobler A, et al. Transmission networks and risk of HIV infection in KwaZulu- Natal, South Africa: a community-wide phylogenetic study. Lancet HIV. 2017;4(1):e41–50. <u>https://doi.org/10.1016/S2352-3018(16)30186-2 PMID: 27914874</u> 

**68.** Risher KA, Cori A, Reniers G, Marston M, Calvert C, Crampin A, et al. Age patterns of HIV incidence in eastern and southern Africa: a modelling analysis of observational population-based cohort studies. Lancet HIV. 2021;8(7):e429–39. https://doi.org/10.1016/S2352-3018(21)00069-2 PMID: <u>34197773</u> 

PLOS Medicine | <u>https://doi.org/10.1371/journal.pmed.1004993 March 25, 2026</u> 

18 / 18 

