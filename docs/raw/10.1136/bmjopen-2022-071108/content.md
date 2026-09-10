To cite: Khalifa A, Ssekubugu R, Lessler J, et al .  Implications of rapid population growth on survey design and HIV estimates in the Rakai Community Cohort Study (RCCS), Uganda. BMJ Open 2023; 13 :e071108. doi:10.1136/ bmjopen-2022-071108

► Prepublication history and additional supplemental material for this paper are available online. To view these files, please visit the journal online (http://dx.doi.org/10.1136/ bmjopen-2022-071108).

Received 15 December 2022 Accepted 10 July 2023

<!-- image -->

© Author(s) (or their employer(s)) 2023. Re-­ use permitted under CC BY-­ NC. No commercial re-­ use. See rights and permissions. Published by BMJ.

For numbered affiliations see end of article.

Correspondence to Aleya Khalifa; ak4598@ cumc. columbia. edu

<!-- image -->

## Implications of rapid population growth on survey design and HIV estimates in the Rakai Community Cohort Study (RCCS), Uganda

<!-- image -->

Aleya Khalifa , 1,2 Robert Ssekubugu , 3,4 Justin Lessler, 5,6 Maria Wawer, 3,7 John S Santelli , 8 Susie Hoffman, 9,10 Fred Nalugoda, 3 Tom Lutalo, 3 Anthony Ndyanabo, 3 Joseph Ssekasanvu, 3,7 Godfrey Kigozi, 3 Joseph Kagaayi, 3 Larry W Chang, 3,7,11 Mary Kathryn Grabowski 3,7,12

## ABSTRACT

Objective Since rapid population growth challenges longitudinal population-­ based HIV cohorts in Africa to maintain coverage of their target populations, this study evaluated whether the exclusion of some residents due to growing population size biases key HIV metrics like prevalence and population-­ level viremia.

Design, setting and participants Data were obtained from the Rakai Community Cohort Study (RCCS) in south central Uganda, an open population-­ based cohort which began excluding some residents of newly constructed household structures within its surveillance boundaries in 2008. The study includes adults aged 15-49 years who were censused from 2019 to 2020.

Measures We fit ensemble machine learning models to RCCS census and survey data to predict HIV seroprevalence and viremia (prevalence of those with viral load &gt;1000 copies/mL) in the excluded population and evaluated whether their inclusion would change overall estimates.

Results Of the 24 729 census-­ eligible residents, 2920 (12%) residents were excluded from the RCCS because they were living in new households. The predicted seroprevalence for these excluded residents was 10.8% (95% CI: 9.6% to 11.8%)-somewhat lower than 11.7% (95% CI: 11.2% to 12.3%) in the observed sample. Predicted seroprevalence for younger excluded residents aged 15-24 years was 4.9% (95% CI: 3.6% to 6.1%)-significantly higher than that in the observed sample for the same age group (2.6% (95% CI: 2.2% to 3.1%)), while predicted seroprevalence for older excluded residents aged 25-49 years was 15.0% (95% CI: 13.3% to 16.4%)-significantly lower than their counterparts in the observed sample (17.2% (95% CI: 16.4% to 18.1%)). Over all ages, the predicted prevalence of viremia in excluded residents (3.7% (95% CI: 3.0% to 4.5%)) was significantly higher than that in the observed sample (1.7% (95% CI: 1.5% to 1.9%)), resulting in a higher overall population-­ level viremia estimate of 2.1% (95% CI: 1.8% to 2.4%). Conclusions Exclusion of residents in new households may modestly bias HIV viremia estimates and some age-­ specific seroprevalence estimates in the RCCS. Overall, HIV seroprevalence estimates were not significantly affected.

## STRENGTHS AND LIMITATIONS OF THIS STUDY

- ⇒ This  study  leveraged  data  from  a  large  sample  of individuals  participating  in  a  population-­ based  cohort study.
- ⇒ Using  an  ensemble  model  to  predict  an  outcome maximises efficiency and minimises predictive error.
- ⇒ Prediction using ensemble models may yield moderate model performance for rare outcomes.
- ⇒ The methods used in this research assume that predictors of HIV seropositivity and viremia are the same for the included and excluded survey population.

## INTRODUCTION

Over the last  30  years,  longitudinal  population-­ based  cohorts  in  sub-­ Saharan  Africa  (SSA) have provided critical surveillance data on the determinants of HIV acquisition and transmission, and evolving HIV epidemic trends. 1 An important challenge these studies face is rapid population growth 2-4 often within the context of fixed budgets and resource constraints. 5-7 For  example,  the  Rakai  Community  Cohort Study (RCCS)-established in 1994 in south-­ central Uganda-has seen a more than 200% increase in population size within its surveillance  boundaries  over  the  last  20  years. 8 Most of this population increase in the RCCS catchment  area  is  attributable  to  Uganda's reduction  in  all-­ cause  mortality  and  high fertility rate, 2 but some growth is also due to in-­ migration. 9 This  rapid  population growth may  prevent  ongoing  open  cohort  studies like the RCCS from representatively sampling the growing target population.

In  resource-­ limited  settings,  studies  may address this challenge in two ways: they may prioritise  longitudinal  follow-­ up  of  existing residents by excluding new residents or they  may  scale  down  longitudinal  follow-­ up efforts in order to expand the sampling frame to one that includes new residents. Both options attempt to minimise total survey error, 10 but which one is more fitting depends on  local  context  and  research  priorities.  For  example, one demographic surveillance site in Burkina Faso prioritised  enrolling  new  in-­ migrants  over  the  longitudinal follow-­ up of out-­ migrants. 11 In contrast, a cohort study in Malawi prioritised the follow-­ up of out-­ migrants instead of enrolling new in-­ migrants. 12 In the case of the RCCS, rapid population growth and resource constraints led to the decision in 2008 to begin excluding residents of new households  in  newly  built  physical  structures  predominately comprised of in-­ migrating families.

Exclusion  of  new  households  from  open  population-­ based  cohorts  like  the  RCCS  may  bias  estimates  of community-­ level HIV seroprevalence if in-­ migrating members of new households have higher or lower rates of  HIV  than  local  residents, 13 (the  latter  because  of  a 'healthy  migrant  effect'). 14-16 Similarly,  population-­ level estimates of viremia may be biased by the exclusion of new households, and most evidence in SSA suggests worse HIV outcomes  for  migrants  living  with  HIV  compared  with non-­ migrants  living  with  HIV  due  to  gaps  in  the  continuity of care. 17-19 Since HIV serostatus and viremia can be in part predicted from sociodemographic data like age, gender, socioeconomic status (SES) and other individual or household-­ level characteristics, 20 21 machine learning can be used to predict the prevalence of these outcomes among excluded groups for which we have some information.  However,  employing one single learner can result in  unreliable  results  if  the  learner  is  weak.  Ensemble machine learning algorithms simultaneously implement multiple learners, weighing the most optimal learner(s) highest  and  securing  a  more  accurate  prediction  when little  is  known about which learner would perform best for  predicting  a  given  outcome. 22  23 Ensemble  models have  been  used  for  prediction  across  a  range  of  disciplines, including for public health. 24-28

This study aimed to assess and quantify the potential bias in population-­ level HIV seroprevalence and viremia estimates, caused by exclusion of in-­ migrating residents arriving  into  new  households  in  the  RCCS  surveillance area. To achieve this aim, the first objective was to describe characteristics of residents in new household structures (the excluded population), comparing them to residents in existing household structures (the observed sample). The second objective was to predict HIV seroprevalence and viremia in the excluded population to assess whether their  inclusion  in  the  observed  sample  might  alter currently observed values.

## METHODS The RCCS

The  RCCS  is  an  open  population-­ based  HIV  surveillance cohort study in the Rakai region of South-­ Central, Uganda, established in 1994. 29 At approximately 18-­ month  intervals,  the  RCCS  conducts  a  census  of  all residents, whether permanent or transient and regardless of age, in every household (old and new) within cohort community boundaries. The census collects sociodemographic data on each household member, including age, gender,  marital  status,  residence  status,  each  member's relationship to the household head and household assets.

Approximately  2 weeks  after  the  census,  the  RCCS administers  a  survey  interview  to  each  consenting  resident aged 15-49 years residing in old households. The survey  collects  sociodemographic,  behavioural,  health and HIV service utilisation data and a blood sample for the  assessment  of  HIV  prevalence,  incidence  and  HIV viremia among persons with HIV. Approximately 95% of eligible persons present in the household agree to both the interview and the blood draw. 20 All  participants  are offered  HIV  results  and  post-­ test  counselling  on  site. Enrolled participants are eligible for follow-­ up in future RCCS surveys  if  they  continue  to  meet  study  eligibility criteria.

For this analysis, we used data from 33 inland rural and peri-­ urban  communities  surveyed  in  RCCS  round  19, conducted between June 2018 and November 2020.

## Patient and public involvement

Patients and the public were not involved in the design, conduct,  reporting,  or  dissemination  planning  of  this research.

## Household classification

The RCCS defines a household as 'an individual or group of individuals who eat their primary meals together and live together'. 20 Households exist within 'structures'-the physical  building  in  which  members  of  the  household reside. During each census, the RCCS identifies individuals living in newly identified structures who are members of entirely new households not previously censused in the RCCS. Since 2008, these individuals are included in the RCCS household census but are not eligible to participate in the survey.

Based  on  the  household  census,  residents  in  the RCCS  surveillance  area  were  categorised  according  to whether they resided in a new or old physical structure and whether they were members of a newly established or  old  household.  Old  structures  and  old  households were defined as being recorded on the census since any year prior to 2008. New structures and new households were defined as being recorded for the first time in year 2008 or after. Using new and old categorisations for both household and structure, the four categories of residents in the RCCS surveillance area are as follows:

1.  Residents of old households in old structures: household censused prior to 2008 and members eligible to participate in the survey.
2.  Residents of new households in old structures: household censused in 2008 or after and members eligible to participate in the survey.
3.  Residents of old households in new structures: household censused prior to 2008 and members eligible to participate in the survey.

4.  Residents of new households in new structures: household censused in 2008 or after and members not eligible to participate in the survey.

Since  residents  of  new  households  in  new  structures (herein referred to as 'new household residents' or 'residents of new households') have been excluded since 2008, we  sought  to  compare  them  with  the  observed  sample of residents in old structures (herein referred to as 'old household residents' or 'residents of old households').

Residents  of  old  households  in  new  structures  were excluded from the analysis because only 339 (56%) of the 601 residents were eligible, present and surveyed (others were absent at the time of survey, had out-­ migrated, had already  been  seen  at  another  residence  or  were  ineligible for other reasons at the time of survey like being unable to provide informed consent due to illness). The 339 participating residents comprised 1% of the analytic sample and were similar to other residents of old households with regards to seroprevalence and viremia, so their exclusion was not expected to influence the results.

## Primary outcomes

Primary  outcomes  included  population-­ level  HIV  seroprevalence  and  viremia.  HIV  seropositivity  among  residents  in  old  households  was  assessed  using  a  validated three rapid test algorithm, while the probability of seropositivity  was  predicted-as  described  below-among residents in new households. 30 HIV seroprevalence in the observed sample was calculated as the proportion of the total population who were HIV positive, and for residents of new households, as the mean of predicted probabilities of HIV seropositivity. Individual viremia was defined as having an HIV viral load of 1000 copies/mL or more (ascertained via viral load testing on stored serum/plasma among residents in old households who were HIV seropositive). We assigned a viral load of zero to all residents in old households who tested HIV seronegative. Among residents in new households, the probability of having an HIV viral load of 1000 copies/mL or more was predicted using the model described below. Population-­ level prevalence of HIV viremia among residents of old households was calculated as the proportion of the total population who were viremic. Among residents of new households, viremia was calculated as the mean of predicted probabilities of being viremic. All outcomes were calculated or predicted by gender (men and women) and age group (15-24 and 25-49 years).

## Predictors

Census data were used to assess potential predictors of HIV  seroprevalence  and  viremia.  Individual  predictors included  gender,  5-­ year  age  group  (starting  at  15-19), marital status, relationship to the household head, residence  status  (permanent,  &gt;6  months  spent  at  household/year or transient, &lt;6 months spent at household/ year) and new in-­ migration (migrated into the study area between the last and current survey round). Household-­ level predictors included region of residence, SES, land ownership, household size, gender of the household head and youth dependency ratio. SES was measured using a weighted nine-­ item asset-­ based index based on the availability of household-­ level assets like radio, electricity and latrines. 20 Youth  dependency  ratio  was  defined  as  the number of household members under age 18 divided by the number of members aged 18 and above. 31

## Descriptive analysis

We first measured the number of residents in new households and the number of new households in each survey round, excluding those who had out-­ migrated or died by round 19. We then characterised residents in new and old households  using  the  predictors  described  above,  with differences  assessed  using χ 2 tests.  Analyses  were  additionally stratified by age (15-24 and 25-49) and by round in  which  new  household  was  identified  on  the  census (pre-­ 2018  census or during the 2018 census) (reported in online supplemental tables 1 and 2). Among residents in  old  households  who  participated  in  the  survey,  each predictor  was  assessed  for  its  bivariate  association  with each outcome using a χ 2 test of significance (reported in online supplemental table 3).

To assess whether new in-­ migrants in new households were different from new in-­ migrants in old households, the  analysis  was  repeated  among  new  in-­ migrants  only. New in-­ migrants were individuals who have moved into the  RCCS  study  area  between  the  last  survey  round (August  2016-May  2018)  and  this  survey  round  (May 2018-June 2020).

## Prediction model

To predict seroprevalence and viremia among residents in  new  households,  an  ensemble  prediction  model  was built for each outcome. Ensemble models often employ bagging,  boosting  or  stacking  approaches  to  combine multiple machine learners, maximising performance of the prediction model when little is known about which single  learner  best  predicts  a  given  outcome. 32 Super Learner-a stacking-­ type  ensemble  prediction  modelhas been used in a variety of health outcome prediction models  and  is  generally  robust  to  model  misspecification. 33-36 Performance and architecture of Super Learner has  been  described  elsewhere. 37  38 Super  Learner  uses cross validation to evaluate and weight the performance of  multiple  machine  learning  algorithms  to  build  one ensemble model, thus maximising efficiency while minimising predictive error. 39 In the first step of 10-­ fold cross-­ validation, each Super Learner weighted seven candidate algorithms  according  to  their  prediction  performance defined by the area under the receiver-­ operator-­ characteristic curve (AUC) (weights and descriptions of each algorithm are in the online supplemental table 4). Algorithms  in  R  included  gam, 40 biglasso, 41 xgboost, 42 glm and glm.interaction, 43 bayesglm 44 and  ranger. 45 We used the default parameters in R for each candidate algorithm. Another 10-­ fold cross-­ validation was then used to evaluate the performance of the overall ensemble model.

Individuals  living  with  the  same  household  ID  were grouped  in  each  ensemble  model  to  account  for  clustering of observations.

The  model  was  used  to  predict  seroprevalence  and viremia probabilities for all residents in new households, and then for men, women, young people aged 15-24 and adults aged 25-49. The predicted prevalence in each of these groups was compared with the empirical prevalence in the observed sample. The predicted prevalence among residents of new households was multiplied by the size of the group to obtain the predicted number of residents who were HIV positive or viremic. These numbers were combined  with  the  number  HIV  positive  or  viremic  in the observed sample to calculate the total seroprevalence and viremia prevalence for residents in both new and old households.

To account for uncertainty in each individual's probability assignment for being HIV positive or viremic, everyone's  unknown outcome was determined by simulating a  Bernoulli  trial  with  probability  corresponding  to  the predicted  probability  of  the  outcome  from  the  model. To  account  for  uncertainty  due  to  both  sampling  and individual  level  outcome  assignment,  the  analysis  was repeated on 100 bootstrapped samples of residents in new households. We use these prediction intervals among the excluded  sample  to  represent  uncertainty  in  predicted seroprevalence  and  viremia  estimates.  We  additionally estimated 95% CIs of the observed seroprevalence and viremia  values  using  binomial  probabilities  of  seropositivity  and  viremia  among  100  bootstrapped  samples  of residents in old households to represent seroprevalence and viremia in the underlying target population of residents in old households.

## RESULTS

There were 24 729 census-­ eligible adults, of whom 2920 (12%)  were  new  household  residents  and  were  thus excluded from the RCCS survey (figure 1); 21 208 (86%) of censused individuals were old household residents, of whom 17 339  (82%)  were  eligible  to  participate  in  the survey;  among them, 11 942 (69%) were present at the time  of  the  survey.  Residents  who  were  not  eligible  to participate were either minors without parental consent, incapacitated or had already been seen in another household. Of residents in new households, 1358 (47%) were new in-­ migrants compared with 4139 (20%) of those in old households.

Since 2009, the number of residents in new households increased  from  90  to  2920,  with  the  steepest  increase occurring between 2017 and 2020 (online supplemental figure  1).  As  of  2019  (survey  round  19),  2108/12  644 (17%)  households  and  2920/24  729  (12%)  residents were excluded from the RCCS survey.

When comparing residents in new households to residents  in  old  households,  the  two  groups  differed  with regards to all variables except for gender (table 1). On average,  residents  in  new  households  were  more  likely than those in old households to be middle-­ aged, married, the head of household, middle-­ SES, renters versus owners and from small households with less youth dependents.

Figure 1 Study flow including number of participants, Rakai Community Cohort Study (RCCS), Rakai, Uganda 2019-2020.

<!-- image -->

<!-- image -->

Table 1 Characteristics of residents living in old and new households in round 19 of the Rakai Community Cohort, 2018 census (N=24 128)

|                                         | Residents in old   | Residents in old   | Residents in new households (N=2920)   | Residents in new households (N=2920)   |                 |
|-----------------------------------------|--------------------|--------------------|----------------------------------------|----------------------------------------|-----------------|
| Characteristic                          | households n       | (N=21 %            | n                                      | %                                      | χ 2 , p value   |
| Gender                                  |                    |                    |                                        |                                        |                 |
|  Men                                   | 10 134             | 47.8               | 1401                                   | 48.0                                   | 0.039, p=0.84   |
|  Women                                 | 11 074             | 52.2               | 1519                                   | 52.0                                   |                 |
| Age                                     |                    |                    |                                        |                                        |                 |
|  15-19                                 | 5627               | 26.5               | 446                                    | 15.3                                   | 500.839, p<0.01 |
|  20-24                                 | 3692               | 17.4               | 789                                    | 27.0                                   |                 |
|  25-29                                 | 3086               | 14.6               | 701                                    | 24.0                                   |                 |
|  30-39                                 | 5199               | 24.5               | 716                                    | 24.5                                   |                 |
|  40-49                                 | 3604               | 17.0               | 268                                    | 9.2                                    |                 |
| Marital status                          |                    |                    |                                        |                                        |                 |
|  Currently married or cohabitating     | 10 280             | 48.5               | 1691                                   | 57.9                                   | 91.468, p<0.01  |
|  Not currently married or cohabitating | 10 928             | 51.5               | 1229                                   | 42.1                                   |                 |
| Relation to household head              |                    |                    |                                        |                                        |                 |
|  Head                                  | 8602               | 40.6               | 1677                                   | 57.4                                   | 582.715, p<0.01 |
|  Spouse                                | 5071               | 23.9               | 812                                    | 27.8                                   |                 |
|  Child/grandchild                      | 5954               | 28.1               | 251                                    | 8.6                                    |                 |
|  Parent                                | 2                  | 0.0                | 0                                      | 0.0                                    |                 |
|  Sibling                               | 194                | 0.9                | 39                                     | 1.3                                    |                 |
|  Other relative/not related            | 1383               | 6.5                | 141                                    | 4.8                                    |                 |
| Residence status                        |                    |                    |                                        |                                        |                 |
|  Permanent (>6 months/year)            | 20 365             | 96.0               | 2468                                   | 84.5                                   | 668.820, p<0.01 |
|  Transient (<6 months/year)            | 843                | 4.0                | 452                                    | 15.5                                   |                 |
| New in-­ migrant                        |                    |                    |                                        |                                        |                 |
|  Yes                                   | 4139               | 19.5               | 1358                                   | 46.5                                   |                 |
|  No                                    | 17 069             | 80.5               | 1562                                   | 53.5                                   |                 |
| SES quartile                            |                    |                    |                                        |                                        |                 |
|  Lowest                                | 4685               | 22.2               | 536                                    | 18.4                                   | 121.362, p<0.01 |
|  Lower                                 | 5114               | 24.2               | 811                                    | 27.8                                   |                 |
|  Higher                                | 4876               | 23.1               | 874                                    | 30.0                                   |                 |
|  Highest                               | 6458               | 30.6               | 693                                    | 23.8                                   |                 |
| Land ownership                          |                    |                    |                                        |                                        |                 |
|  Rent                                  | 8514               | 40.2               | 1901                                   | 65.2                                   | 741.250, p<0.01 |
|  Own                                   | 11 481             | 54.2               | 803                                    | 27.5                                   |                 |
|  Other                                 | 1176               | 5.6                | 213                                    | 7.3                                    |                 |
| Household size quartiles                |                    |                    |                                        |                                        |                 |
|  Q1 (1-2 members)                      | 6187               | 29.2               | 1658                                   | 56.8                                   | 1,100, p<0.01   |
|  Q2 (3-4 members)                      | 5110               | 24.1               | 720                                    | 24.7                                   |                 |
|  Q3 (5-6 members)                      | 4366               | 20.6               | 317                                    | 10.9                                   |                 |
|  Q4 (7+ members)                       | 5545               | 26.2               | 225                                    | 7.7                                    |                 |
| Gender of household head                |                    |                    |                                        |                                        |                 |
|  Man                                   | 15 415             | 72.8               | 2222                                   | 76.3                                   | 15.610, p<0.01  |
|  Woman                                 | 5753               | 27.2               | 691                                    | 23.7                                   |                 |

Continued

| Characteristic                                              | Residents in old households (N=21 208)                      | Residents in old households (N=21 208)                      | Residents in new households (N=2920)                        | Residents in new households (N=2920)                        | χ 2 , p value                                               |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Characteristic                                              | n                                                           | %                                                           | n                                                           | %                                                           | χ 2 , p value                                               |
| Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) |
|  0 (no dependents) Table 1 Continued                       | 4081                                                        | 19.2                                                        | 1183                                                        | 40.5                                                        | 749.715, p<0.01                                             |
|  0.5-1                                                     | 5274                                                        | 24.9                                                        | 693                                                         | 23.7                                                        |                                                             |
|  1                                                         | 3417                                                        | 16.1                                                        | 386                                                         | 13.2                                                        |                                                             |
|  >1 SES, socioeconomic status.                             | 8436                                                        | 39.8                                                        | 658                                                         | 22.5                                                        |                                                             |

When comparing new in-­ migrants in new households to  new  in-­ migrants  in  old  households,  the  two  groups differed  with  regards  to  all  variables  except  for  marital status and gender of the household head (table 2). New in-­ migrants  in  new  households  were  more  likely  to  be men  (48.1%)  compared  with  those  in  old  households (41.3%).  Compared  with  those  in  old  households,  the new in-­ migrants in new households were also more likely to  be  aged  20-29,  the  household  head,  renters  versus owners and of smaller households (1-2 members) with no dependents.

## Predicted HIV seroprevalence and viremia among residents in new households

## HIV seroprevalence

The  AUC  of  the  seroprevalence  prediction  model  was 0.78 (0.73 to 0.81) (online supplemental table 4). Overall, predicted  seroprevalence  for  new  household  residents was  10.8%  (95%  CI:  9.6%  to  11.8%)  compared  with 11.7% (95% CI: 11.2% to 12.3%) in the observed sample (figure 2; data in online supplemental table 5). Inclusion of new household residents in the total estimate for seroprevalence  did  not  significantly  change  seroprevalence estimates for the total population (11.6% (95% CI: 10.9% to 12.2%)). However, among young people aged 15-24, new household residents had a significantly higher seroprevalence  (4.9%  (95%  CI:  3.6%  to  6.1%))  compared with  old  household  residents  (2.6%  (95%  CI:  2.2%  to 3.1%)).  The  opposite  was  true  for  older  adults  aged 25-49, in which new household residents had a significantly  lower  seroprevalence  (15.0%  (95%  CI:  13.3%  to 16.4%)) compared with old household residents (17.2% (95% CI: 16.4% to 18.1%)). While seroprevalence estimates were significantly different between new and old household residents in both age groups, the inclusion of those in new households in total seroprevalence estimates did not significantly alter current estimates.

## Viremia

The AUC for the viremia prediction model was low relative  to  that  of  the  seroprevalence  prediction  model  at 0.71 (0.65 to 0.75) (online supplemental table 4). Inclusion of new household residents, with a predicted viremia prevalence of 3.7% (95% CI: 3.0% to 4.5%), resulted in a  24%  higher  total  viremia  prevalence  (2.1%  (95%  CI: 1.8%  to  2.4%))  for  both  new  and  old  household  residents compared with the observed sample (1.7% (95% CI: 1.5% to 1.9%)) (figure 3; data in online supplemental table 5). Though viremia among residents of new and old households was significantly different, this difference did not significantly alter current viremia estimates. Similar findings  were  observed  for  all  subgroups  by  age  and gender, with the comparatively highest viremia estimate predicted for young people aged 15-24 (1.2% (95% CI: 0.9% to 1.7%)) in the total population-50% higher than the viremia prevalence of 0.8% (0.6% to 1.1%) among residents in old households.

## DISCUSSION

Longitudinal  population-­ based cohorts have contributed  immensely  to  the  HIV  response  in  Africa,  but rapid population growth poses significant challenges to open cohorts like the RCCS. While there were few new households in 2008 when they were first excluded, the population in new households has expanded with time. In  assessing  the  potential  bias  introduced  by  excluding residents of new households, this study showed that the population in new households substantively differs from the included surveillance sample on various sociodemographic characteristics. These differences did not translate  into  significantly  different  HIV  seroprevalence  or viremia rates overall, suggesting minimal bias at a population level. However, significant differences in viremia and age-­ specific  seroprevalence  estimates  between  new  and old household residents warrant further examination.

Currently,  the  exclusion  of  residents  in  new  households in the RCCS does not impact overall distributions of  sociodemographic  characteristics,  but  the  growing number  of  residents  in  new  households  could  significantly change the underlying population structure of the RCCS in future years. If the population in new households continues to grow, and this growing population maintains a similar demographic profile of being majority married, middle-­ aged and with small household sizes, the survey-­ eligible population may become increasingly unrepresentative of the target population. This 'new' population may Continued

<!-- image -->

Table 2 Characteristics of new in-­ migrants living in old and new households in round 19 of the Rakai Community Cohort, 2018 census (N=5497)

|                                                             | New in-­ migrants in old                                    | New in-­ migrants in old                                    | New in-­ migrants in new households (N=1358)                | New in-­ migrants in new households (N=1358)                |                 |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-----------------|
| Characteristic                                              | households n                                                | (N=4139) %                                                  | n                                                           | %                                                           | χ 2 , p value   |
| Gender                                                      |                                                             |                                                             |                                                             |                                                             |                 |
|  Men                                                       | 1708                                                        | 41.3                                                        | 653                                                         | 48.1                                                        | 19.406, p<0.01  |
|  Women                                                     | 2431                                                        | 58.7                                                        | 705                                                         | 51.0                                                        |                 |
| Age                                                         |                                                             |                                                             |                                                             |                                                             |                 |
|  15-19                                                     | 927                                                         | 22.4                                                        | 187                                                         | 13.8                                                        | 64.630, p<0.01  |
|  20-24                                                     | 1119                                                        | 27.0                                                        | 445                                                         | 32.8                                                        |                 |
|  25-29                                                     | 862                                                         | 20.8                                                        | 353                                                         | 26.0                                                        |                 |
|  30-39                                                     | 886                                                         | 21.4                                                        | 279                                                         | 20.5                                                        |                 |
|  40-49                                                     | 345                                                         | 8.3                                                         | 94                                                          | 6.9                                                         |                 |
| Marital status                                              |                                                             |                                                             |                                                             |                                                             |                 |
|  Currently married or cohabitating                         | 2204                                                        | 53.3                                                        | 723                                                         | 53.2                                                        | <1.0, p=0.99    |
|  Not currently married or cohabitating                     | 1935                                                        | 46.8                                                        | 635                                                         | 46.8                                                        |                 |
| Relation to household head                                  |                                                             |                                                             |                                                             |                                                             |                 |
|  Head                                                      | 1884                                                        | 45.5                                                        | 908                                                         | 66.9                                                        | 233.633, p<0.01 |
|  Spouse                                                    | 1268                                                        | 30.6                                                        | 338                                                         | 24.9                                                        |                 |
|  Child/grandchild                                          | 364                                                         | 8.8                                                         | 44                                                          | 3.2                                                         |                 |
|  Parent                                                    | 0                                                           | 0.0                                                         | 0                                                           | 0.0                                                         |                 |
|  Sibling                                                   | 70                                                          | 1.7                                                         | 18                                                          | 1.3                                                         |                 |
|  Other relative/not related                                | 552                                                         | 13.3                                                        | 50                                                          | 3.7                                                         |                 |
| Residence status                                            |                                                             |                                                             |                                                             |                                                             |                 |
|  Permanent (>6 months/year)                                | 3389                                                        | 81.9                                                        | 938                                                         | 69.1                                                        | 100.110, p<0.01 |
|  Transient (<6 months/year)                                | 750                                                         | 18.1                                                        | 420                                                         | 30.9                                                        |                 |
| SES quartile                                                |                                                             |                                                             |                                                             |                                                             |                 |
|  Lowest                                                    | 984                                                         | 23.9                                                        | 302                                                         | 22.3                                                        | 33.366, p<0.01  |
|  Lower                                                     | 1162                                                        | 28.2                                                        | 453                                                         | 33.4                                                        |                 |
|  Higher                                                    | 1104                                                        | 26.8                                                        | 399                                                         | 29.4                                                        |                 |
| Highest                                                     | 871                                                         | 21.1                                                        | 202                                                         | 14.9                                                        |                 |
|  Land ownership                                            |                                                             |                                                             |                                                             |                                                             |                 |
|  Rent                                                      | 2936                                                        | 71.1                                                        | 1122                                                        | 82.7                                                        | 82.827, p<0.01  |
|  Own                                                       | 770                                                         | 18.7                                                        | 119                                                         | 8.8                                                         |                 |
|  Other                                                     | 421                                                         | 10.2                                                        | 116                                                         | 8.5                                                         |                 |
| Household size quartiles                                    |                                                             |                                                             |                                                             |                                                             |                 |
|  Q1 (1-2 members)                                          | 2449                                                        | 59.2                                                        | 1048                                                        | 77.2                                                        | 215.532, p<0.01 |
|  Q2 (3-4 members)                                          | 856                                                         | 20.7                                                        | 248                                                         | 18.3                                                        |                 |
|  Q3 (5-6 members)                                          | 435                                                         | 10.5                                                        | 52                                                          | 3.8                                                         |                 |
|  Q4 (7+ members)                                           | 399                                                         | 9.6                                                         | 10                                                          | 0.7                                                         |                 |
| Gender of household head                                    |                                                             |                                                             |                                                             |                                                             |                 |
|  Man                                                       | 2962                                                        | 71.8                                                        | 998                                                         | 73.5                                                        | 1.445, p=0.23   |
|  Woman                                                     | 1163                                                        | 28.2                                                        | 360                                                         | 26.5                                                        |                 |
| Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) | Youth dependency ratio (members <18 divided by members 18+) |                 |
|  0 (no dependents)                                         | 1789                                                        | 43.2                                                        | 783                                                         | 57.7                                                        | 99.869, p<0.01  |
|  0.5-1                                                     | 1000                                                        | 24.3                                                        | 271                                                         | 20.0                                                        |                 |

<!-- image -->

Table 2 Continued

| Characteristic   | New in-­ migrants households   | New in-­ migrants households   | in old (N=4139) New in-­ migrants households (N=1358)   | in old (N=4139) New in-­ migrants households (N=1358)   |
|------------------|--------------------------------|--------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Characteristic   | n                              | %                              | n                                                       | %                                                       |
|  1              | 537                            | 13.0                           | 156                                                     | in 11.5                                                 |
|  >1 SES,        | 813                            | 19.6                           | 148                                                     | 10.9                                                    |

represent an important demographic group in Uganda: young middle-­ class married couples or families starting up new households in new geographic areas. Even if overall HIV estimates remain representative of the target population, the decision to expand the sampling frame could be made on the basis of demographic representation.

Considering that all residents in new households were at one point in-­ migrants-the majority of whom in-­ migrated to  the  study  area  after  2016-biases  in  the  age-­ specific seroprevalence estimates may illustrate differences among  migrant  subgroups.  Different  types  of  migrants have different levels of HIV risk. Among 15-24 year-­ olds, there may be a migrant health penalty for those arriving in  new  households  because  their  seroprevalence  was higher than the included sample. Young people in Rakai who migrate have been shown to engage in higher HIV risk behaviours compared with their non-­ migrant counterparts. 46 These risky behaviours often coincide with the transition from school to work, when many mobile young people engage in risky occupations associated with HIV risk,  like  boda-­ boda  drivers,  truck  drivers,  and  bar  and restaurant  workers. 47 Among  25-49 year-­ olds,  the  opposite  seems  to  be  true:  there  may  be  a  healthy  migrant effect for those arriving in new households because their estimated  seroprevalence  was  lower  than  the  included sample.  Since  many  adults  aged  25-49  in  new  households were married men and the head-­ of-­ household, it may be that this group of in-­ migrants travelled for family or greater economic opportunity and not due to circumstances that independently drive HIV risk. 15 16 48

<!-- image -->

Figure 2 Seroprevalence in the RCCS surveillance sample, excluding and including predicted values for new households, Rakai, Uganda 2019-2020 (N=14 679). RCCS, Rakai Community Cohort Study.

<!-- image -->

Figure 3 Viremia in the RCCS surveillance sample, excluding and including predicted values for new households, Rakai, Uganda 2019-2020 (N=14 648). RCCS, Rakai Community Cohort Study.

Unlike seroprevalence, viremia rates are projected to be consistently higher across all subgroups in new households, compared with old households, thereby modestly, though not significantly, increasing the rate of viremia in the total population. This finding is consistent with that of other cohorts in SSA, 49 and provides evidence for the migrant health penalty, which posits that individuals who migrate experience intrinsic risks that heighten their risk for poor HIV outcomes. 17 Mobile populations may face structural barriers to care that lead to treatment interruptions, 18 50 which increases risk of viremia and other poor treatment  outcomes. 51  52 Furthermore,  studies  suggest that  areas  with  higher-­ than-­ average  population  mobility also demonstrate high community-­ level viremia, for example, among both residents and non-­ residents in east African border towns 53 and along transport corridors in Namibia. 54 However, the impact of viremia among in-­ migrants on viremia in the community at large should be studied  using  longitudinal  data  because  high  rates  of viremia among in-­ migrants may cancel out with equally high rates of viremia among out-­ migrants. 49 Thus, it may be  important  to  include  in-­ migrants  in  the  sampling frame  of  ongoing  longitudinal  cohorts:  if  in-­ migrants are  systematically  excluded  from  cohorts  and  they  are less likely to be virally suppressed, local HIV prevention programmes  may  miss  an  important  population  whose linkage to care would help to stem onward HIV transmission. To assess bias in the indicators that monitor progress towards 95-95-95 targets, such as viral load suppression, 55 future  research  could  assess  not  just  population-­ level viremia  among  populations  excluded  from  surveys  but also viremia among excluded people living with HIV, if serostatus among individuals in the excluded population is known.

Furthermore, excluding certain in-­ migrants from surveillance  programmes  could  mean  that  the  wrong inferences  are  made  about  the  health  state  and  risks for  migrant  populations.  For  example,  cohorts  that only  include  in-­ migrants  with  stronger  social  ties  (eg, new  members  of  existing  households)  might  produce evidence for the migrant experience that does not represent transient, young adult, or working-­ class migrants. In the  case  of  the  RCCS,  the  cohort  may  underrepresent migrant men, given that migrant men were more likely to be living in new household structures than old household structures. Since migrant men are more likely to be viremic, 56 it  is  possible  that  viremia  among  migrants  in the RCCS is higher than would be estimated with current data.

Our study had several limitations. First, the prediction model performance was moderate for seroprevalence and relatively  weaker  for  viremia,  which  has  been  observed in  other  HIV  ensemble  modelling  studies. 57 This  may be due to the relative lack of data on new residents: for example, sexual behaviours like age-­ disparate sexual partnerships predict seroprevalence, 58 and health behaviours like alcohol use predict viremia, 59 and these data were not available  for  residents  of  new  households.  Nonetheless, many of the included predictors have been demonstrated to reliably predict HIV outcomes, 56 60 61 and a sub-­ analysis of RCCS survey data confirmed this (online supplemental table 3). Second, this analysis assumes that the risk factors for HIV seroprevalence and viremia are the same for residents  of  new  households  as  for  residents  of  old  households, but this assumption is difficult to prove. Third, the observed sample may be a biased representation of the target population because some eligible participants were away at the time of the survey. While it was not the aim of this paper to estimate seroprevalence and viremia among the full target population (only to describe the currently observed sample), this is  another  potentially  important source of bias that should be evaluated in future studies. Finally, it is possible that we underestimated or overestimated seroprevalence or viremia among residents in new households  because  we  do  not  know  who  would  have been present and survey-­ eligible had the household been included in the survey. In the survey sample, residents in old households are sometimes excluded from the survey because they have died, are incapacitated at the time of the survey, or refuse to respond. If HIV outcomes differ for  eligible  and  ineligible  participants,  then  this  could partially explain results.

## CONCLUSIONS

While we did not find substantial potential biases from excluding  new  household  residents  in  the  RCCS,  our results show this population is growing and so observed differences  may  become  more  problematic  over  time. To  address  potential  future  biases,  longitudinal  surveys may choose to better reflect the target population either by  expanding  the  sampling  frame  or  re-­ weighting  the survey-­ eligible population. 62 63 The latter option may be more cost-­ efficient, but it assumes that the demographic group included in the survey shares the same risk of HIV acquisition and viremia as their excluded counterparts. A substudy with a sample of the excluded in-­ migrants could be conducted to test this assumption. 64

In the context of rapid population growth, open cohorts in SSA may seek to ensure that sampling frames reflect the  growing  target  population.  However,  the  resources required  for  any  changes  may  not  be  met  by  fixed  or decreasing budgets. In the context of HIV funding shortfalls, 65 HIV-­ focused cohorts must make difficult decisions. While expanding the sampling frame to cover more of the target  population  can  improve  representation  of  in-­ migrants,  such  an  effort  may  divert  resources  away  from effective  follow-­ up  of  previously  enrolled  individuals, which can worsen representation of those who are more likely to be lost to follow-­ up, like out-­ migrants. These risks must be carefully considered before opting for a survey redesign. Longitudinal population-­ based cohorts provide critical  evidence  for  the  HIV  response,  and  so  longitudinal sampling efforts must be preserved. Cohorts should routinely  monitor  demographic  changes  in  the  target population and be transparent about any potential biases

## Open access

introduced by these changes or resulting modifications to study design. Lastly, results from studies that prioritise representativeness should be triangulated with those from studies that maintain longitudinal follow-­ up to improve overall understanding of the African HIV epidemic.

## Author affiliations

1 Department of Epidemiology, Columbia University Mailman School of Public Health, New York, New York, USA

2 ICAP, Columbia University, New York, New York, USA

3 Rakai Health Sciences Program, Kalisizo, Uganda

4 Department of Global and Sexual Health, Karolinska Institutet, Stockholm, Sweden

5

Department of Epidemiology, University of North Carolina School of Public Health,

Chapel Hill, North Carolina, USA

6 Carolina Population Center, University of North Carolina, Chapel Hill, North Carolina, USA

7 Department of Epidemiology, Johns Hopkins University Bloomberg School of Public Health, Baltimore, Maryland, USA

8 Population and Family Health, Columbia University Mailman School of Public Health, New York, New York, USA

9 Department of Epidemiology, Columbia University, New York, New York, USA

10 HIV Centre for Clinical and Behavioural Studies, Columbia University Irving Medical Centre, New York, New York, USA

11 Division of Infectious Diseases, Department of Medicine, Johns Hopkins University School of Medicine, Baltimore, Maryland, USA

12 Department of Pathology, Johns Hopkins School of Medicine, Baltimore, Maryland, USA

Contributors All authors conceptualised the paper, contributed to the investigation and methodology, and reviewed and edited the manuscript. AK led the formal analysis, the visualisation and writing of the original draft. JL, JS, MKG and LWC supported the formal analysis and JL, MKG and LWC supported the writing of the original draft. RS, MW, JSS, SH, FN, TL, AN, JS, GK, JK, LWC and MKG contributed equally to data curation and project administration. As guarantor, AK is responsible for the overall content and conduct of the study. AK had access to the data and controlled the decision to publish.

Funding This work was supported by the National Institute of Allergy and Infectious Diseases (R01AI143333 and R01AI155080) and the National Institute of Mental Health (R01MH115799). The findings and conclusions in this article are those of the authors and do not necessarily represent the official position of the funding agencies. Research by Aleya Khalifa reported in this publication was supported by the National Institute of Allergy And Infectious Diseases (T32AI114398). Larry Chang was supported by the National Heart, Lung, and Blood Institute (R01HL152813), Fogarty International Center (D43TW010557) and the Johns Hopkins University Center for AIDS Research (P30AI094189). Susie Hoffman and John Santelli were supported by the U.S. National Institute of Child Health and Human Development (NICHD) (R01HD091003; Santelli, PI). Susie Hoffman was also supported by the National Institute of Mental Health (P30-­ MH43520; Remien, PI).

## Competing interests None declared.

Patient and public involvement Patients and/or the public were not involved in the design, or conduct, or reporting, or dissemination plans of this research.

Patient consent for publication Not applicable.

Ethics approval This study involves human participants and was approved. This study was approved by the Uganda National Council for Science and Technology (approval number HS 540), the Uganda Virus Research Institution Research and Ethics Committee (approval number GC/127/08/12/137), Johns Hopkins Institutional Review Board (approval number IRB-­ 00217467) and the Columbia University Institutional Review Board (approval number IRB-­ AAAR5428). Participants gave informed consent to participate in the study before taking part.

Provenance and peer review Not commissioned; externally peer reviewed.

Data availability statement Data are available upon reasonable request. Data are available upon request to the Rakai Health Sciences Program (RHSP) (email:  datarequests@ rhsp. org). Code will be made available upon request to the corresponding author.

Supplemental material This content has been supplied by the author(s). It has not been vetted by BMJ Publishing Group Limited (BMJ) and may not have been peer-­ reviewed. Any opinions or recommendations discussed are solely those of the author(s) and are not endorsed by BMJ. BMJ disclaims all liability and responsibility arising from any reliance placed on the content. Where the content includes any translated material, BMJ does not warrant the accuracy and reliability of the translations (including but not limited to local regulations, clinical guidelines, terminology, drug names and drug dosages), and is not responsible for any error and/or omissions arising from translation and adaptation or otherwise.

<!-- image -->

Open access This is an open access article distributed in accordance with the Creative Commons Attribution Non Commercial (CC BY-­ NC 4.0) license, which permits others to distribute, remix, adapt, build upon this work non-­ commercially, and license their derivative works on different terms, provided the original work is properly cited, appropriate credit is given, any changes made indicated, and the use is non-­ commercial. See: http://creativecommons.org/licenses/by-nc/4.0/.

## ORCID iDs

Aleya Khalifa http://orcid.org/0000-0001-8234-1295 Robert Ssekubugu http://orcid.org/0000-0003-1245-4774 John S Santelli http://orcid.org/0000-0001-9559-9973

## REFERENCES

- 1	 Reniers G, Wamukoya M, Urassa M, et al . Data resource profile: network for analysing longitudinal population-­ based HIV/AIDS data on Africa (ALPHA network). Int J Epidemiol 2016;45:83-93.
- 2	 United Nations, Department of Economic and Social Affairs, Population Division. World population prospects. 2019. Available: https://population.un.org/wpp/Download/Standard/Population/ [Accessed 11 Apr 2022].
- 3 Kuhn R. Internal migration: developing countries. In: Wright JD, ed. International encyclopedia of the social &amp; behavioral sciences . Second Edition. Elsevier, 2015: 433-42.
- 4	 United Nations Conference on Trade and Development. Economic development in Africa, report 2018: migration for structural transformation . 2018.
- 5	 Schneider MT, Birger M, Haakenstad A, et al . Tracking development assistance for HIV/AIDS: the International response to a global epidemic. AIDS 2016;30:1475-9.
- 6	 Global Burden of Disease Health Financing Collaborator Network. Spending on health and HIV/AIDS: domestic health spending and development assistance in 188 countries, 1995-­ 2015. Lancet 2018;391:1799-829.
- 7 Kates J, Wexler A, Lief E. Donor government funding for HIV in lowand middle-­ income countries in 2019 . Kaiser Family Foundation and Joint United Nations Programme on HIV/AIDS (UNAIDS), 2020: 17.
- 8	 Grabowski MK, Serwadda DM, Gray RH, et al . HIV prevention efforts and incidence of HIV in Uganda. N Engl J Med 2017;377:2154-66.
- 9 Sida, Norad, International Organization for Migration (IOM). Migration in Uganda: a rapid country profile 2013 . 2015.
- 10 Biemer PP . Total survey error: design, implementation, and evaluation. Public Opinion Quarterly 2010;74:817-48.
- 11	 Sié A, Louis VR, Gbangou A, et al . The health and demographic surveillance system (HDSS) in Nouna, Burkina Faso, 1993-­ 2007. Glob Health Action 2010;3.
- 12 Anglewicz P , VanLandingham M, Manda-­ Taylor L, et al . Cohort profile: internal migration in sub-­ Saharan Africa-the migration and health in Malawi (MHM) study. BMJ Open 2017;7:e014799.
- 13	 Cassels S, Jenness SM, Khanna AS. Conceptual framework and research methods for migration and HIV transmission dynamics. AIDS Behav 2014;18:2302-13.
- 14	 Chaabna K, Cheema S, Mamtani R. Migrants, healthy worker effect, and mortality trends in the Gulf Cooperation Council countries. PLoS ONE 2017;12:e0179711.
- 15 Lu Y. Test of the 'healthy migrant hypothesis': a longitudinal analysis of health selectivity of internal migration in Indonesia. Soc Sci Med 2008;67:1331-9.
- 16	 Lu Y, Qin L. Healthy migrant and salmon bias hypotheses: a study of health and internal migration in China. Social Science &amp; Medicine 2014;102:41-8.
- 17 Ginsburg C, Bocquier P , Menashe-­ Oren A, et al . Migrant health penalty: evidence of higher mortality risk among internal migrants in sub-­ Saharan Africa. Glob Health Action 2021;14:1930655.
- 18 Camlin CS, Charlebois ED. Mobility and its effects on HIV acquisition and treatment engagement: recent theoretical and empirical advances. Curr HIV/AIDS Rep 2019;16:314-23.
- 19 Camlin CS, Cassels S, Seeley J. Bringing population mobility into focus to achieve HIV prevention goals. J Int AIDS Soc 2018;21 Suppl 4:e25136.

<!-- image -->

- 20 Santelli JS, Chen I, Makumbi F , et al . Household wealth and HIV incidence over time, rural Uganda, 1994-2018. AIDS 2021;35:1835-43.
- 21 Nardell MF, Adeoti O, Peters C, et al . Men missing from the HIV care continuum in Sub-Saharan Africa: a meta-analysis and metasynthesis. J Int AIDS Soc 2022;25:e25889.
- 22	 Wang W, Xu Y, Yuan S, et al . Prediction of endometrial carcinoma using the combination of electronic health records and an ensemble machine learning method. Front Med 2022;9:851890.
- 23 Chung J, Teo J. Single Classifier vs. ensemble machine learning approaches for mental health prediction. Brain Inform 2023;10:1.
- 24	 Buyruko ğ lu S, Akba ş A. Machine learning based early prediction of type 2 diabetes: a new hybrid feature selection approach using correlation matrix with Heatmap and SDS. Balkan Journal of Electrical and Computer Engineering 2022;10:110-7.
- 25	 Buyruko ğ lu S, Sava ş S. Stacked-­ based ensemble machine learning model for positioning footballer. Arab J Sci Eng 2023;48:1371-83.
- 26	 Buyruko ğ lu S, Yılmaz Y, Topalcengiz Z. Correlation value determined to increase salmonella prediction success of deep neural network for agricultural waters. Environ Monit Assess 2022;194:373.
- 27	 Akbas A, Buyrukoglu S. Stacking ensemble learning-­ based wireless sensor network deployment parameter estimation. Arab J Sci Eng 2022;11.
- 28	 Attai K, Amannejad Y, Vahdat Pour M, et al . A systematic review of applications of machine learning and other soft computing techniques for the diagnosis of tropical diseases. Trop Med Infect Dis 2022;7:398.
- 29	 Chang LW, Grabowski MK, Ssekubugu R, et al . Heterogeneity of the HIV epidemic in agrarian, trading, and fishing communities in Rakai, Uganda: an observational epidemiological study. Lancet HIV 2016;3:e388-96.
- 30	 Galiwango RM, Musoke R, Lubyayi L, et al . Evaluation of current rapid HIV test algorithms in Rakai, Uganda. J Virol Methods 2013;192:25-7.
- 31	 Assaf S, Pullum T. Household and community risk factors and child well-­ being in Low- and middle-­ income countries. The demographic and health surveys program. 2018. Available: https://dhsprogram. com/publications/publication-wp135-working-papers.cfm
- 32	 Liang Y, Wang Z, Peng Y, et al . Development of ensemble learning models for prognosis of hepatocellular carcinoma patients underwent postoperative adjuvant transarterial chemoembolization. Front Oncol 2023;13:1169102.
- 33 Polley E, LeDell E, Kennedy C, et al . Superlearner. Available: https:// cran.r-project.org/web/packages/SuperLearner/index.html [Accessed 13 Jun 2023].
- 34 Baur D, Gehlen T, Scherer J, et al . Decision support by machine learning systems for acute management of severely injured patients: a systematic review. Front Surg 2022;9:924810.
- 35	 Cherifa M, Blet A, Chambaz A, et al . Prediction of an acute hypotensive episode during an ICU hospitalization with a super learner machine-­ learning algorithm. Anesth Analg 2020;130:1157-66.
- 36	 Pirracchio R, Petersen ML, van der Laan M. Improving propensity score estimators' robustness to model misspecification using super learner. Am J Epidemiol 2015;181:108-19.
- 37	 Lee S, Nguyen N, Karamanli A, et al . Super learner machine-­ learning algorithms for compressive strength prediction of high performance concrete. Structural Concrete 2023;24:2208-28.
- 38 Lin H, Zou W, Li T, et al . A super-­ learner model for tumor motion prediction and management in radiation therapy: development and feasibility evaluation. Sci Rep 2019;9:14868.
- 39	 van der Laan MJ, Polley EC, Hubbard AE. Super learner. Stat Appl Genet Mol Biol 2007;6:Article25.
- 40 Yaladanda N, Mopuri R, Vavilala H, et al . The synergistic effect of climatic factors on malaria transmission: a predictive approach for northeastern States of India. Environ Sci Pollut Res Int 2023;30:59194-211.
- 41	 Zhang B, Wang Q, Lin Z, et al . A novel glycolysis-­ related gene signature for predicting the prognosis of multiple myeloma. Front Cell Dev Biol 2023;11:1198949.
- 42 Panagiotopoulos K, Korfiati A, Theofilatos K, et al . Meva-­ X: a hybrid multi-­ objective evolutionary tool using an Xgboost classifier for biomarkers discovery on BIOMEDICAL datasets. Bioinformatics 2023;16:btad384.
- 43 Sharma P, Haaland P , Krishnamurthy A, et al . Evaluating robustness of a generalized linear model when applied to electronic health record data accessed using an open API. Health Informatics J 2023;29:14604582231170892.
- 44	 Hiura S, Abe H, Koyama K, et al . Bayesian generalized linear model for simulating bacterial inactivation/growth considering variability and uncertainty. Front Microbiol 2021;12:674364.
- 45	 Baik SM, Kim KT, Lee H, et al . Machine learning algorithm for early-­ stage prediction of severe morbidity in COVID-­ 19 pneumonia patients based on bio-­ signals. BMC Pulm Med 2023;23:121.
- 46	 Schuyler AC, Edelstein ZR, Mathur S, et al . Mobility among youth in Rakai, Uganda: trends, characteristics, and associations with behavioural risk factors for HIV. Glob Public Health 2017;12:1033-50.
- 47 Kreniske P , Grilo S, Nakyanjo N, et al . Narrating the transition to adulthood for youth in Uganda: leaving school, mobility, risky occupations and HIV. Health Educ Behav 2019;46:550-8.
- 48 Ginsburg C, Bocquier P , Béguy D, et al . Healthy or unhealthy migrants? Identifying internal migration effects on mortality in Africa using health and demographic surveillance systems of the INDEPTH network. Soc Sci Med 2016;164:59-73.
- 49	 Larmarange J, Diallo MH, McGrath N, et al . The impact of population dynamics on the population HIV care Cascade: results from the ANRS 12249 treatment as prevention trial in rural Kwazulu-­ natal (South Africa). J Int AIDS Soc 2018;21 Suppl 4:e25128.
- 50	 Murnane PM, Gandhi M, Bacchetti P , et al . Distinct forms of migration and mobility are differentially associated with HIV treatment adherence. AIDS 2022;36:1021-30.
- 51 Davey C, Dirawo J, Mushati P , et al . Mobility and sex work: why, where, when? A typology of female sex worker mobility in Zimbabwe. Soc Sci Med 2019;220:322-30.
- 52	 Taylor BS, Garduño LS, Reyes EV, et al . HIV care for geographically mobile populations. Mt Sinai J Med 2011;78:342-51.
- 53 Edwards JK, Arimi P , Ssengooba F , et al . The HIV care continuum among resident and Non-Resident populations found in Venues in East Africa Cross-Border areas. J Int AIDS Soc 2019;22:e25226.
- 54	 Low A, Sachathep K, Rutherford G, et al . Migration in Namibia and its association with HIV acquisition and treatment outcomes. PLoS One 2021;16:e0256865.
- 55	 Joint United Nations Programme on HIV/AIDS (UNAIDS). Fast-­ track: ending the AIDS epidemic by 2030. 2014. Available: https://www. unaids.org/sites/default/files/media\_asset/JC2686\_WAD2014report\_ en.pdf
- 56	 Grabowski MK, Patel EU, Nakigozi G, et al . Prevalence and predictors of persistent human immunodeficiency virus viremia and viral rebound after universal test and treat: a population-­ based study. J Infect Dis 2021;223:1150-60.
- 57 Murnane PM, Ayieko J, Vittinghoff E, et al . Machine learning algorithms using routinely collected data do not adequately predict viremia to inform targeted services in postpartum women living with HIV. J Acquir Immune Defic Syndr 2021;88:439-47.
- 58	 Stoner MCD, Nguyen N, Kilburn K, et al . Age-­ disparate partnerships and incident HIV infection in adolescent girls and young women in rural South Africa. AIDS 2019;33:83-91.
- 59	 Myers B, Lombard C, Joska JA, et al . Associations between patterns of alcohol use and viral load suppression amongst women living with HIV in South Africa. AIDS Behav 2021;25:3758-69.
- 60 Nutor JJ, Duah HO, Agbadi P , et al . Spatial analysis of factors associated with HIV infection in Malawi: indicators for effective prevention. BMC Public Health 2020;20:1167.
- 61	 Ibrahim SA, Sabitu K, Abubakar A, et al . Demographic factors associated with HIV infection between low and high prevalence areas in Nigeria, 2015. Pan Afr Med J 2019;32:11.
- 62 Lynn P . Methodology of longitudinal surveys. In: Methods for longitudinal surveys . John Wiley &amp; Sons, Ltd, 2009.
- 63 Lynn P . Advances in longitudinal survey methodology. In: Advances in longitudinal survey methodology . 1st ed. John Wiley &amp; Sons, Ltd, 2021.
- 64 Lynn P . Maintaining cross-­ sectional representativeness in a longitudinal general population survey. 2011.
- 65 The Lancet Hiv. Funding the future of the HIV response. Lancet HIV 2022;9:e595.