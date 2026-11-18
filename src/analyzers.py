import numpy as np
import pandas as pd
import sciris as sc
import starsim as ss
import stisim as sti


def _ti_infection(disease):
    """Timestep-of-infection array, across stisim's two naming conventions.

    The SEIS bacterial diseases (NG/CT/TV) expose ``ti_infectious``; syphilis
    and HIV expose ``ti_infected``.
    """
    ti = getattr(disease, "ti_infected", None)
    if ti is None:
        ti = disease.ti_infectious
    return ti


class DiagnosisTracker(ss.Analyzer):
    """
    Track STI diagnoses for incidence analysis.

    Monitors one or more testing interventions' referrals each timestep and
    maintains per-agent diagnosis counts and a persistent diagnosed flag.
    Interventions without a ``ti_referred`` state are skipped.
    """

    def __init__(self, testing=None):
        super().__init__(name='diagnosis_tracker')
        self.testing = sc.tolist(testing)
        self._events = []
        self.define_states(
            ss.BoolArr('diagnosed'),
            ss.FloatArr('ti_diagnosed'),
            ss.FloatArr('n_diagnoses'),
        )

    def init_results(self):
        super().init_results()
        self.define_results(
            ss.Result('new_diagnoses_total', dtype=int, label='New STI diagnoses'),
        )

    def step(self):
        ti = self.ti
        newly_referred = ss.uids()
        for t in self.testing:
            if not hasattr(t, 'ti_referred'):
                continue
            newly_referred = newly_referred | (t.ti_referred == ti).uids

        if len(newly_referred):
            vals = self.n_diagnoses[newly_referred]
            self.n_diagnoses[newly_referred] = np.nan_to_num(vals, nan=0.0) + 1
            self._events.append((np.array(newly_referred), ti))

        new_dx = newly_referred.remove(self.diagnosed.uids)
        if len(new_dx):
            self.diagnosed[new_dx] = True
            self.ti_diagnosed[new_dx] = ti

        # written here rather than in update_results: in starsim 3.6.1 an
        # analyzer's update_results runs before its step, so a ti_diagnosed == ti
        # check there would miss the stamps set this step.
        self.results['new_diagnoses_total'][ti] = len(new_dx)


class TreatmentLog(ss.Intervention):
    """
    One row per STI treatment: when, who, which drug, which channels flagged the
    person that step, and whether they carried each of ``diseases`` at the time
    and had symptoms of it they could notice.

    Built as an intervention so it can read infection status before the step's
    treatments clear it. ``step`` runs first among the interventions and
    snapshots status. ``update_results`` runs once every intervention has
    stepped and reads who was treated. Status is as of presentation, so a
    person given ng_tx and syph_tx on one step shows NG on both rows.

    Drugs are every STITreatment in the sim. A drug's channels are the testing
    modules that enqueue onto it (syndromic, panel, outreach) and, for a drug
    treating syphilis, every syphilis test. ``channel`` joins with "+" every one
    of the drug's channels that flagged the person that step, so a person
    reached by two channels on one step carries both on each drug's row, and an
    antenatal treatment after the confirmatory RPR starts reads
    "syph_anc_rdt+syph_anc_confirm".
    """

    def __init__(self, diseases=("ng", "ct", "tv", "syph"), name="treatment_log"):
        super().__init__(name=name)
        self.status_diseases = list(diseases)
        self._infected = {}
        self._symptomatic = {}
        self._drugs = []
        self._channels = {}
        self._rows = []

    def init_post(self):
        super().init_post()
        intvs = list(self.sim.interventions())
        if intvs[0] is not self:
            raise ValueError("TreatmentLog must be the first intervention, or it reads status after treatment")
        self._drugs = [i for i in intvs if isinstance(i, sti.STITreatment)]
        syph_tests = [i for i in intvs if isinstance(i, sti.SyphTest)]
        for tx in self._drugs:
            channels = [i for i in intvs if any(t is tx for t in getattr(i, "treatments", ()))]
            if "syph" in tx.diseases:
                channels += syph_tests
            self._channels[tx.name] = channels

    def step(self):
        self._infected = {d: self.sim.diseases[d].infected.uids for d in self.status_diseases}
        self._symptomatic = {d: self._symptoms(self.sim.diseases[d]).uids for d in self.status_diseases}

    @staticmethod
    def _symptoms(disease):
        # syphilis's symptomatic covers the primary and secondary stages even
        # when the chancre or rash is not where the person would notice it
        return getattr(disease, "visibly_symptomatic", disease.symptomatic)

    def _flagged(self, channel):
        # syphilis tests call a result; NG/CT/TV channels refer to treatment
        stamp = channel.ti_positive if isinstance(channel, sti.SyphTest) else channel.ti_referred
        return (stamp == self.ti).uids

    def update_results(self):
        super().update_results()
        channels = {ch.name: ch for chs in self._channels.values() for ch in chs}
        flagged = {name: self._flagged(ch) for name, ch in channels.items()}
        for tx in self._drugs:
            treated = (tx.ti_treated == self.ti).uids
            if not len(treated):
                continue
            channel = np.full(len(treated), "", dtype=object)
            for ch in self._channels[tx.name]:
                hit = np.isin(treated, flagged[ch.name])
                channel[hit] = np.where(channel[hit] == "", ch.name, channel[hit] + "+" + ch.name)
            row = dict(year=np.full(len(treated), self.sim.t.now("year")), uid=np.array(treated),
                       drug=np.full(len(treated), tx.name, dtype=object), channel=channel)
            for d, infected in self._infected.items():
                row[d] = np.isin(treated, infected)
                row[f"{d}_symptomatic"] = np.isin(treated, self._symptomatic[d])
            self._rows.append(row)

    def to_df(self):
        """All treatments so far, one row each."""
        cols = ["year", "uid", "drug", "channel", *self.status_diseases,
                *(f"{d}_symptomatic" for d in self.status_diseases)]
        if not self._rows:
            return pd.DataFrame(columns=cols)
        return pd.DataFrame({c: np.concatenate([r[c] for r in self._rows]) for c in cols})


class HIVIncidence1549(ss.Analyzer):
    """
    HIV incidence at ages 15-49 per 100 person-years, both sexes pooled and by sex.

    stisim reports incidence in age bands but not the number at risk in each,
    so its bands cannot be pooled into one 15-49 rate. Each step adds the new
    infections at 15-49 and one step of person-time for every 15-49-year-old
    who was HIV-negative at its start.
    """

    SEXES = ("all", "female", "male")

    def __init__(self, name="hiv_incidence_15_49"):
        super().__init__(name=name)
        self._new = {}
        self._py = {}

    def init_results(self):
        super().init_results()
        npts = self.t.npts
        self._new = {s: np.zeros(npts, dtype=int) for s in self.SEXES}
        self._py = {s: np.zeros(npts) for s in self.SEXES}

    def step(self):
        ppl, hiv, ti = self.sim.people, self.sim.diseases.hiv, self.ti
        age = ppl.age
        adult = ppl.alive & (age >= 15) & (age < 50)
        new = hiv.ti_infected == ti
        at_risk = adult & (~hiv.infected | new)
        for sex, mask in zip(self.SEXES, (adult, adult & ppl.female, adult & ppl.male)):
            self._new[sex][ti] = (new & mask).count()
            self._py[sex][ti] = (at_risk & mask).count() * self.t.dt_year

    def annual(self):
        """One row per calendar year and sex: new infections, person-years, incidence per 100."""
        year = np.floor(self.t.yearvec).astype(int)
        rows = []
        for sex in self.SEXES:
            for y in np.unique(year):
                n, py = self._new[sex][year == y].sum(), self._py[sex][year == y].sum()
                rows.append(dict(year=y, sex=sex, new_infections=n, person_years=py,
                                 incidence=100 * n / py if py else np.nan))
        return pd.DataFrame(rows)


class STIPrevalence1549(ss.Analyzer):
    """
    Curable-STI prevalence at ages 15-49, both sexes pooled and by sex.

    stisim's adult prevalence spans 15-64 for gonorrhoea, chlamydia and
    trichomoniasis and counts only the sexually active for syphilis. Each step
    adds one step of person-time for every 15-49-year-old and for every one
    infected. Syphilis is counted at any stage ('syph') and as RPR-positive
    ('syph_rpr'), the measure surveys report as active syphilis.
    """

    SEXES = ("all", "female", "male")
    DISEASES = ("ng", "ct", "tv", "syph", "syph_rpr")

    def __init__(self, name="sti_prevalence_15_49"):
        super().__init__(name=name)
        self._infected = {}
        self._py = {}

    def init_results(self):
        super().init_results()
        npts = self.t.npts
        self._infected = {(s, d): np.zeros(npts) for s in self.SEXES for d in self.DISEASES}
        self._py = {s: np.zeros(npts) for s in self.SEXES}

    def step(self):
        ppl, dis, ti = self.sim.people, self.sim.diseases, self.ti
        adult = ppl.alive & (ppl.age >= 15) & (ppl.age < 50)
        states = dict(ng=dis.ng.infected, ct=dis.ct.infected, tv=dis.tv.infected,
                      syph=dis.syph.infected, syph_rpr=dis.syph.nontrep)
        dt = self.t.dt_year
        for sex, mask in zip(self.SEXES, (adult, adult & ppl.female, adult & ppl.male)):
            self._py[sex][ti] = mask.count() * dt
            for disease, state in states.items():
                self._infected[(sex, disease)][ti] = (state & mask).count() * dt

    def annual(self):
        """One row per calendar year, sex and disease: person-years infected and at 15-49, prevalence."""
        year = np.floor(self.t.yearvec).astype(int)
        rows = []
        for (sex, disease), infected in self._infected.items():
            for y in np.unique(year):
                inf, py = infected[year == y].sum(), self._py[sex][year == y].sum()
                rows.append(dict(year=y, sex=sex, disease=disease, person_years_infected=inf,
                                 person_years=py, prevalence=inf / py if py else np.nan))
        return pd.DataFrame(rows)


class NetworkSummary(ss.Analyzer):
    """
    Sexual network summary at ages 15-49 in one year, as JSON-ready aggregates.

    Taken at the step nearest the start of year. Partner histograms are agent
    counts in bins 0, 1, ... with the last bin open-ended. Lifetime partners
    include sex-work partners, which stisim counts apart from the rest. New
    partners in the last year are the rise in that count since the step nearest
    the start of the year before. Debut quantiles are among those past their
    debut age. Age gaps are male age minus female age in current stable and
    casual partnerships, grouped by the female partner's age.
    """

    LIFETIME_BINS = 20
    NEW_BINS = 10
    DEBUT_QUANTILES = (10, 25, 50, 75, 90)
    GAP_QUANTILES = (5, 25, 50, 75, 95)
    FEMALE_AGE_GROUPS = dict(f15_20=(15, 20), f20_25=(20, 25), f25_50=(25, 50))

    def __init__(self, year, name="network_summary"):
        super().__init__(name=name)
        self.year = year
        self._ti_before = self._ti_snapshot = None
        self._partners_before = None
        self._summary = None

    def init_results(self):
        super().init_results()
        yearvec = self.t.yearvec
        nearest = lambda y: int(np.argmin(np.abs(yearvec - y)))
        # a sim that ends before the year never takes the snapshot
        if yearvec[0] <= self.year - 1 and self.year <= yearvec[-1]:
            self._ti_before, self._ti_snapshot = nearest(self.year - 1), nearest(self.year)

    def _lifetime_partners(self):
        nw = self.sim.networks.structuredsexual
        return np.asarray(nw.lifetime_partners.raw) + np.asarray(nw.lifetime_sw_partners.raw)

    def step(self):
        if self.ti == self._ti_before:
            self._partners_before = self._lifetime_partners()
        if self.ti == self._ti_snapshot:
            self._summary = self._snapshot()

    def _snapshot(self):
        ppl, nw = self.sim.people, self.sim.networks.structuredsexual
        adult = ppl.alive & (ppl.age >= 15) & (ppl.age < 50)
        lifetime = self._lifetime_partners()
        before = np.zeros_like(lifetime)
        before[:len(self._partners_before)] = self._partners_before
        new = lifetime - before

        def histogram(values, top):
            return np.bincount(np.minimum(values, top).astype(int), minlength=top + 1).tolist()

        out = dict(year=self.year, lifetime_partners={}, new_partners_last_year={}, debut_age_quantiles={},
                   risk_group={})
        for sex in ("female", "male"):
            uids = (adult & ppl[sex]).uids
            out["lifetime_partners"][sex] = histogram(lifetime[uids], self.LIFETIME_BINS)
            out["new_partners_last_year"][sex] = histogram(new[uids], self.NEW_BINS)
            debut = np.asarray(nw.debut[uids])
            debut = debut[np.asarray(ppl.age[uids]) >= debut]
            out["debut_age_quantiles"][sex] = (np.percentile(debut, self.DEBUT_QUANTILES).tolist()
                                               if len(debut) else None)
            rg = np.asarray(nw.risk_group[uids])
            out["risk_group"][sex] = [float(np.mean(rg == g)) if len(rg) else None
                                      for g in range(nw.pars.n_risk_groups)]

        e = nw.edges
        current = (e.edge_type == nw.edge_types["stable"]) | (e.edge_type == nw.edge_types["casual"])
        f_age = np.asarray(ppl.age[e.p2[current]])
        gap = np.asarray(ppl.age[e.p1[current]]) - f_age
        out["age_gap"] = {}
        for key, (lo, hi) in self.FEMALE_AGE_GROUPS.items():
            g = gap[(f_age >= lo) & (f_age < hi)]
            out["age_gap"][key] = dict(n=int(len(g)),
                                       quantiles=np.percentile(g, self.GAP_QUANTILES).tolist() if len(g) else None)
        return out

    def summary(self):
        """The snapshot's aggregates, or None if the sim did not reach the year."""
        return self._summary


class InfectionTracker(ss.Analyzer):
    """
    Track per-agent STI infections for incidence analysis.

    Monitors ti_infected on each tracked disease every timestep and maintains
    a cumulative per-agent infection count.
    """

    def __init__(self, diseases=None):
        super().__init__(name='infection_tracker')
        self.tracked_diseases = diseases or []
        self._events = []
        self.define_states(
            ss.FloatArr('n_infections'),
        )

    def init_results(self):
        super().init_results()
        self.define_results(
            ss.Result('new_infections_total', dtype=int, label='New STI infections'),
        )

    def step(self):
        ti = self.ti
        for disease in self.tracked_diseases:
            disease_new = (_ti_infection(disease) == ti).uids
            if len(disease_new):
                vals = self.n_infections[disease_new]
                self.n_infections[disease_new] = np.nan_to_num(vals, nan=0.0) + 1
                self._events.append((np.array(disease_new), ti))

    def update_results(self):
        super().update_results()
        ti = self.ti
        total = sum(len((_ti_infection(d) == ti).uids) for d in self.tracked_diseases)
        self.results['new_infections_total'][ti] = total


class CascadeTracker(ss.Analyzer):
    """
    Track the care cascade for STI diseases per timestep.

    Records counts at each cascade step (infected, symptomatic, diagnosed via
    syndromic vs screening, treated, cured) for each bacterial STI. HIV is
    tracked separately. ``screening`` and ``prep`` are optional; when None their
    columns stay zero.
    """

    def __init__(self, diseases=None, screening=None, prep=None, treatment_map=None):
        super().__init__(name='cascade_tracker')
        self._diseases = diseases or []
        self._screening = screening
        self._prep = prep
        self._treatment_names = treatment_map or {}
        self._tx_map = {}
        self._data = sc.objdict()

    def init_pre(self, sim):
        super().init_pre(sim)
        # sti.Sim runs copies of the modules build_sim passed in, so read the sim's own
        self._diseases = [sim.diseases[d.name] for d in self._diseases]
        if self._prep is not None:
            self._prep = sim.interventions[self._prep.name]
        self._tx_map = {
            dname: sim.interventions[tname]
            for dname, tname in self._treatment_names.items()
            if tname in sim.interventions
        }
        npts = self.t.npts
        disease_names = [d.name for d in self._diseases] + ['hiv']
        cascade_keys = (
            'infected', 'symptomatic',
            'new_infections', 'new_symptomatic',
            'new_care_seekers',
            'dx_total', 'dx_screening',
            'false_neg_total', 'screening_false_neg',
            'treated', 'cured',
        )
        for dname in disease_names:
            self._data[dname] = sc.objdict({key: np.zeros(npts, dtype=int) for key in cascade_keys})
        self._data['prep'] = sc.objdict({key: np.zeros(npts, dtype=int) for key in ('n_on_prep', 'new_on_prep')})

    def _screening_result(self, key, ti):
        if self._screening is not None and key in self._screening.results:
            return int(self._screening.results[key][ti])
        return 0

    def _count_syphilis_symptomatic(self, disease, ti):
        new_symp = 0
        if hasattr(disease, 'ti_primary') and hasattr(disease, 'primary'):
            newly_primary = disease.primary & (disease.ti_primary > ti - 1) & (disease.ti_primary <= ti)
            new_symp += len((newly_primary & disease.chancre_visible).uids)
        if hasattr(disease, 'ti_secondary') and hasattr(disease, 'secondary'):
            newly_secondary = disease.secondary & (disease.ti_secondary > ti - 1) & (disease.ti_secondary <= ti)
            new_symp += len((newly_secondary & disease.rash_visible).uids)
        return new_symp

    def _result(self, results, key, ti):
        return int(results[key][ti]) if key in results else 0

    def step(self):
        sim = self.sim
        ti = sim.ti

        for disease in self._diseases:
            dname = disease.name
            d = self._data[dname]

            d['infected'][ti] = len(disease.infected.uids)
            if hasattr(disease, 'symptomatic'):
                d['symptomatic'][ti] = len(disease.symptomatic.uids)

            d['new_infections'][ti] = self._result(disease.results, 'new_infections', ti)

            if 'new_symptomatic' in disease.results:
                d['new_symptomatic'][ti] = int(disease.results['new_symptomatic'][ti])
            elif hasattr(disease, 'chancre_visible'):
                d['new_symptomatic'][ti] = self._count_syphilis_symptomatic(disease, ti)

            d['new_care_seekers'][ti] = self._result(disease.results, 'new_care_seekers', ti)
            d['dx_total'][ti] = self._result(disease.results, 'new_true_pos', ti)
            d['dx_screening'][ti] = self._screening_result(f'screened_true_pos_{dname}', ti)
            d['false_neg_total'][ti] = self._result(disease.results, 'new_false_neg', ti)
            d['screening_false_neg'][ti] = self._screening_result(f'screened_false_neg_{dname}', ti)

            tx = self._tx_map.get(dname)
            if tx is not None:
                d['treated'][ti] = len((tx.ti_treated == ti).uids)
                outcomes = getattr(tx, 'outcomes', None)
                if outcomes and dname in outcomes:
                    d['cured'][ti] = len(outcomes[dname].get('successful', ss.uids()))

        hiv = sim.diseases.hiv
        hd = self._data['hiv']
        hd['infected'][ti] = len(hiv.infected.uids)
        hd['new_infections'][ti] = self._result(hiv.results, 'new_infections', ti)
        if hasattr(hiv, 'symptomatic'):
            hd['symptomatic'][ti] = len(hiv.symptomatic.uids)
        if hasattr(hiv, 'ti_diagnosed'):
            hd['dx_total'][ti] = len((hiv.ti_diagnosed == ti).uids)
        if hasattr(hiv, 'on_art'):
            hd['treated'][ti] = len(hiv.on_art.uids)

        if self._prep is not None:
            self._data['prep']['n_on_prep'][ti] = self._prep.results.n_on_prep[ti]
            self._data['prep']['new_on_prep'][ti] = self._prep.results.new_prep[ti]


class ExposureTracker(ss.Analyzer):
    """
    Track per-agent unprotected sexual exposures to infected partners.

    Walks the sexual network edges each timestep and counts partnerships where
    one partner is infected with a bacterial STI or HIV.
    """

    def __init__(self):
        super().__init__(name='exposure_tracker')
        self.define_states(
            ss.FloatArr('sti_exposures'),
            ss.FloatArr('hiv_exposures'),
        )

    def init_results(self):
        super().init_results()
        self.define_results(
            ss.Result('new_sti_exposures', dtype=int, label='New STI exposures'),
            ss.Result('new_hiv_exposures', dtype=int, label='New HIV exposures'),
        )

    def step(self):
        sim = self.sim
        ti = sim.ti

        sexual_net = sim.networks.get('structuredsexual')
        if sexual_net is None:
            return

        p1 = sexual_net.edges.p1
        p2 = sexual_net.edges.p2

        if len(p1) == 0:
            return

        n_raw = len(self.sti_exposures.raw)
        sti_step = np.zeros(n_raw, dtype=float)
        hiv_step = np.zeros(n_raw, dtype=float)

        for dname in ('ng', 'ct', 'syph', 'tv'):
            if dname not in sim.diseases:
                continue
            disease = sim.diseases[dname]
            inf_p1 = disease.infected[p1]
            inf_p2 = disease.infected[p2]
            np.add.at(sti_step, p2[inf_p1], 1)
            np.add.at(sti_step, p1[inf_p2], 1)

        if 'hiv' in sim.diseases:
            hiv = sim.diseases.hiv
            inf_p1 = hiv.infected[p1]
            inf_p2 = hiv.infected[p2]
            np.add.at(hiv_step, p2[inf_p1], 1)
            np.add.at(hiv_step, p1[inf_p2], 1)

        auids = sim.people.auids
        self.sti_exposures.raw[auids] = (
            np.nan_to_num(self.sti_exposures.raw[auids], nan=0.0) + sti_step[auids]
        )
        self.hiv_exposures.raw[auids] = (
            np.nan_to_num(self.hiv_exposures.raw[auids], nan=0.0) + hiv_step[auids]
        )

        self.results['new_sti_exposures'][ti] = int(sti_step[auids].sum())
        self.results['new_hiv_exposures'][ti] = int(hiv_step[auids].sum())


class SusceptibilityExposureTracker(ss.Analyzer):
    """
    Track HIV exposures stratified by whether the exposed agent has an active
    bacterial STI at the time of exposure.
    """

    def __init__(self):
        super().__init__(name='susceptibility_exposure')
        self.define_states(
            ss.FloatArr('exposures_while_sti'),
            ss.FloatArr('exposures_while_clean'),
            ss.FloatArr('sti_person_time'),
        )

    def init_results(self):
        super().init_results()
        self.define_results(
            ss.Result('new_exposures_while_sti', dtype=int, label='HIV exposures during STI'),
            ss.Result('new_exposures_while_clean', dtype=int, label='HIV exposures while STI-free'),
            ss.Result('new_sti_person_time', dtype=int, label='Person-steps with active STI'),
        )

    def step(self):
        sim = self.sim
        ti = sim.ti

        sexual_net = sim.networks.get('structuredsexual')
        if sexual_net is None:
            return

        p1 = sexual_net.edges.p1
        p2 = sexual_net.edges.p2
        if len(p1) == 0:
            return

        n_raw = len(self.exposures_while_sti.raw)
        auids = sim.people.auids

        has_sti = np.zeros(n_raw, dtype=bool)
        for dname in ('ng', 'ct', 'syph', 'tv'):
            if dname in sim.diseases:
                has_sti[sim.diseases[dname].infected.uids] = True

        sti_pt = has_sti[auids].astype(float)
        self.sti_person_time.raw[auids] = (
            np.nan_to_num(self.sti_person_time.raw[auids], nan=0.0) + sti_pt
        )

        if 'hiv' not in sim.diseases:
            return

        hiv = sim.diseases.hiv
        inf_p1 = hiv.infected[p1]
        inf_p2 = hiv.infected[p2]

        hiv_exp = np.zeros(n_raw, dtype=float)
        np.add.at(hiv_exp, p2[inf_p1], 1)
        np.add.at(hiv_exp, p1[inf_p2], 1)

        hiv_susceptible = ~np.array(hiv.infected.raw)
        hiv_exp *= hiv_susceptible.astype(float)

        exp_sti = hiv_exp * has_sti.astype(float)
        exp_clean = hiv_exp * (~has_sti).astype(float)

        self.exposures_while_sti.raw[auids] = (
            np.nan_to_num(self.exposures_while_sti.raw[auids], nan=0.0) + exp_sti[auids]
        )
        self.exposures_while_clean.raw[auids] = (
            np.nan_to_num(self.exposures_while_clean.raw[auids], nan=0.0) + exp_clean[auids]
        )

        self.results['new_exposures_while_sti'][ti] = int(exp_sti[auids].sum())
        self.results['new_exposures_while_clean'][ti] = int(exp_clean[auids].sum())
        self.results['new_sti_person_time'][ti] = int(sti_pt.sum())


class NetworkPositionTracker(ss.Analyzer):
    """
    Record network position metrics at periodic snapshots: per-agent risk group,
    FSW/client status, and partner counts.
    """

    def __init__(self, snapshot_interval=1.0):
        super().__init__(name='network_position')
        self.snapshot_interval = snapshot_interval
        self._snapshots = []
        self._next_snapshot = None

    def init_pre(self, sim):
        super().init_pre(sim)
        self._next_snapshot = float(sim.t.yearvec[0])

    def step(self):
        sim = self.sim
        year = float(sim.t.yearvec[sim.ti])

        if year < self._next_snapshot:
            return
        self._next_snapshot += self.snapshot_interval

        nw = sim.networks.get('structuredsexual')
        if nw is None:
            return

        ppl = sim.people
        auids = ppl.auids

        snapshot = dict(
            year=float(year),
            ti=sim.ti,
            uids=np.array(auids),
            risk_group=np.nan_to_num(np.array(nw.risk_group[auids]), nan=-1).astype(int),
            is_fsw=np.array(nw.fsw[auids]),
            is_client=np.array(nw.client[auids]),
            n_partners=np.nan_to_num(np.array(nw.partners[auids]), nan=0).astype(int),
            n_stable=np.nan_to_num(np.array(nw.stable_partners[auids]), nan=0).astype(int),
            n_casual=np.nan_to_num(np.array(nw.casual_partners[auids]), nan=0).astype(int),
            n_sw=np.nan_to_num(np.array(nw.sw_partners[auids]), nan=0).astype(int),
        )
        self._snapshots.append(snapshot)


class DemographicSnapshotAnalyzer(ss.Analyzer):
    """
    Record demographic-stratified disease and intervention states: per-timestep
    HIV incidence by sex, ART/PLHIV counts by age bin and sex, and full per-agent
    snapshots at configurable years.
    """

    def __init__(self, snapshot_years=None, age_bins=None):
        super().__init__(name='demographic_snapshot')
        self.snapshot_years = snapshot_years or [2007, 2011, 2016, 2021]
        self.age_bins = age_bins or [15, 25, 35, 45, 55, 65]
        self._snapshots = []
        self._ts = sc.objdict()
        self._taken_snapshots = set()

    def init_pre(self, sim):
        super().init_pre(sim)
        npts = self.t.npts
        n_bins = len(self.age_bins) - 1
        self._ts.hiv_incidence_f = np.zeros(npts, dtype=int)
        self._ts.hiv_incidence_m = np.zeros(npts, dtype=int)
        self._ts.n_plhiv_f = np.zeros((npts, n_bins), dtype=int)
        self._ts.n_plhiv_m = np.zeros((npts, n_bins), dtype=int)
        self._ts.n_art_f = np.zeros((npts, n_bins), dtype=int)
        self._ts.n_art_m = np.zeros((npts, n_bins), dtype=int)

    def step(self):
        sim = self.sim
        ti = self.ti
        ppl = sim.people
        hiv = sim.diseases.hiv
        auids = ppl.auids

        age = np.array(ppl.age[auids])
        female = np.array(ppl.female[auids])
        male = ~female
        hiv_inf = np.array(hiv.infected[auids])

        new_hiv = np.array(hiv.ti_infected[auids]) == ti
        self._ts.hiv_incidence_f[ti] = int(np.sum(new_hiv & female))
        self._ts.hiv_incidence_m[ti] = int(np.sum(new_hiv & male))

        on_art = np.array(hiv.on_art[auids]) if hasattr(hiv, 'on_art') else np.zeros(len(auids), dtype=bool)
        bins = self.age_bins
        for b in range(len(bins) - 1):
            in_bin = (age >= bins[b]) & (age < bins[b + 1])
            self._ts.n_plhiv_f[ti, b] = int(np.sum(hiv_inf & female & in_bin))
            self._ts.n_plhiv_m[ti, b] = int(np.sum(hiv_inf & male & in_bin))
            self._ts.n_art_f[ti, b] = int(np.sum(on_art & female & in_bin))
            self._ts.n_art_m[ti, b] = int(np.sum(on_art & male & in_bin))

        year = sim.t.yearvec[ti]
        for sy in self.snapshot_years:
            if abs(year - sy) < sim.t.dt_year / 2 and sy not in self._taken_snapshots:
                self._taken_snapshots.add(sy)
                snapshot = dict(
                    year=float(year),
                    ti=ti,
                    uids=np.array(auids),
                    age=age.copy(),
                    female=female.copy(),
                    hiv_infected=hiv_inf.copy(),
                )
                if hasattr(hiv, 'on_art'):
                    snapshot['on_art'] = on_art.copy()
                self._snapshots.append(snapshot)


class HIVTransmissionLogger(ss.Analyzer):
    """
    Backfill HIV infection_log entries that stisim's HIV.set_prognoses skips.

    Each step, detects newly HIV-infected agents via ti_infected and infers the
    transmitting partner from the active sexual network.
    """

    def __init__(self):
        super().__init__(name='hiv_tx_logger')

    def step(self):
        sim = self.sim
        hiv = sim.diseases['hiv']

        if not getattr(hiv, 'infection_log', None):
            return

        new_uids = (hiv.ti_infected == self.ti).uids
        if len(new_uids) == 0:
            return

        net = sim.networks.get('structuredsexual')
        if net is None:
            return

        p1 = np.asarray(net.edges.p1)
        p2 = np.asarray(net.edges.p2)

        for uid in new_uids:
            partners = np.concatenate([p2[p1 == uid], p1[p2 == uid]])
            if len(partners) == 0:
                hiv.infection_log.append(np.nan, int(uid), self.now)
                continue
            candidates = partners[hiv.infected[partners] & (hiv.ti_infected[partners] < self.ti)]
            if len(candidates) == 0:
                hiv.infection_log.append(np.nan, int(uid), self.now)
                continue
            hiv.infection_log.append(int(candidates[0]), int(uid), self.now)
