"""
Custom interventions for canary-stis.

The NG/CT/TV diagnostic arm (syndromic management vs POC panel) and the syphilis
pipeline are assembled in ``sim.build_sim`` from stock stisim classes; this
module holds the classes with no stisim equivalent: a gonorrhea-treatment
subclass fixing an initial-seeding NaN, the magic cure, a later HIV seed, the
behavioral PrEP eligibility screen, and the demand-side levers (care-seeking
scaler, condom counseling, FSW outreach).
"""

import numpy as np
import starsim as ss
import stisim as sti


class GonorrheaTx(sti.GonorrheaTreatment):
    """GonorrheaTreatment with a fix for rel_treat NaN from initial seeding.

    stisim's Gonorrhea.set_prognoses copies rel_treat from source agents.
    During initial seeding (sources=-1), this reads the last slot of a
    pre-allocated array (NaN padding), so all initially-infected NG agents get
    NaN rel_treat, which then cascades to new infections via the same copy.

    Fixed in step() rather than init_post() because starsim initializes
    interventions before diseases call set_prognoses.
    """

    def step(self):
        if not getattr(self, "_rel_treat_fixed", False):
            nan_mask = np.isnan(self.rel_treat.raw[: self.rel_treat.len_used])
            if nan_mask.any():
                self.rel_treat.raw[np.where(nan_mask)[0]] = 1.0
            self._rel_treat_fixed = True
        return super().step()


class MagicCure(ss.Intervention):
    """Instantly cure all agents of all bacterial STIs at a configurable year.

    The biological-PAF ceiling arm: removes the STI cofactor entirely at one
    instant, bounding the maximum HIV incidence reduction attributable to STI
    clearance.
    """

    def __init__(self, year=2000, diseases=None, name=None):
        super().__init__(name=name or "magic_cure")
        self.cure_year = year
        self._diseases = diseases or []
        self._cured = False

    def _cure_syphilis(self, disease, uids):
        disease.exposed[uids] = False
        disease.infected[uids] = False
        disease.susceptible[uids] = True
        for attr in ("primary", "secondary", "early", "late",
                     "latent", "tertiary", "chancre_visible", "rash_visible"):
            getattr(disease, attr)[uids] = False
        for attr in ("ti_primary", "ti_secondary", "ti_latent", "ti_tertiary"):
            getattr(disease, attr)[uids] = np.nan

    def step(self):
        if self._cured or self.sim.now < self.cure_year:
            return
        self._cured = True
        for disease in self._diseases:
            to_cure = disease.infected.uids | disease.exposed.uids
            if not len(to_cure):
                continue
            if hasattr(disease, "primary"):
                self._cure_syphilis(disease, to_cure)
            else:
                disease.clear_infection(to_cure)
                disease.wipe_dates(to_cure)


class HIVSeed(ss.Intervention):
    """Seed HIV at the first step at or after year, as sti.HIV seeds it at the start.

    sti.HIV's init_post draws its initial cases from init_prev, or from
    init_prev_data scaled by rel_init_prev when given, and backdates their
    infection by dist_ti_init_infected. This repeats that draw at year, so the
    disease must be built with nobody seeded at the start.
    """

    def __init__(self, year, init_prev=None, init_prev_data=None, name="hiv_seed"):
        super().__init__(name=name)
        self.seed_year = year
        self.init_prev = init_prev
        self.init_prev_data = init_prev_data
        self._seeded = False

    def step(self):
        if self._seeded or self.sim.now < self.seed_year:
            return
        self._seeded = True
        hiv = self.sim.diseases.hiv
        p = self.init_prev if self.init_prev_data is None else hiv.make_init_prev(data=self.init_prev_data)
        hiv.pars.init_prev.set(p)
        cases = hiv.pars.init_prev.filter()
        ti = self.ti + hiv.pars.dist_ti_init_infected.rvs(cases).astype(int)
        hiv.set_prognoses(cases, ti=ti)
        diagnosed = hiv.pars.init_diagnosed.filter(cases)
        hiv.diagnosed[diagnosed] = True
        hiv.ti_diagnosed[diagnosed] = self.ti
        hiv.ti_art[diagnosed] = self.ti


class CondomCounseling(ss.Intervention):
    """Condoms/counselling for the diagnosed (bundled-prevention lever).

    When an agent is treated for an STI, with probability ``coverage`` they enter
    a protection window of ``dur``: during it their re-acquisition
    susceptibility (``rel_sus``) for the protected diseases is multiplied by
    ``(1 - eff)``. Acquisition only; onward transmission is untouched.

    The multiplier is applied multiplicatively each step, matching how disease
    risk factors and coinfection connectors compose on ``rel_sus``. Each
    disease's ``step_state`` resets ``rel_sus[:] = 1`` and connectors re-apply
    their cofactors before interventions run, so multiplying the
    currently-protected set here both composes with those cofactors and
    self-expires when an agent leaves the protected set.
    """

    def __init__(self, coverage=0.5, eff=0.5, dur=ss.months(6),
                 diseases=("ng", "ct", "tv", "syph"),
                 trigger_tx=("ng_tx", "ct_tx", "metronidazole", "syph_tx"),
                 start=2027, name="condom_counseling", *args, **kwargs):
        super().__init__(name=name)
        self.define_pars(
            coverage=ss.bernoulli(p=coverage),
            eff=eff,
            dur=dur,
        )
        self.update_pars(*args, **kwargs)
        self.diseases = list(diseases)
        self.trigger_tx = list(trigger_tx)
        self.start = start
        self._window_steps = None
        self.define_states(
            ss.FloatArr("ti_protect_end", default=np.nan),
        )
        return

    def init_pre(self, sim):
        super().init_pre(sim)
        dt_year = sim.t.dt_year if sim.t.dt_year else 1 / 12
        dur_years = self.pars.dur.years if hasattr(self.pars.dur, "years") else float(self.pars.dur)
        self._window_steps = max(1, int(round(dur_years / dt_year)))
        return

    def _newly_treated(self):
        ti = self.ti
        uids = ss.uids()
        for name in self.trigger_tx:
            tx = self.sim.interventions.get(name)
            if tx is None or not hasattr(tx, "ti_treated"):
                continue
            uids = uids | (tx.ti_treated == ti).uids
        return uids

    def step(self):
        sim = self.sim
        if sim.now < self.start:
            return
        ti = self.ti

        treated = self._newly_treated()
        if len(treated):
            enroll = self.pars.coverage.filter(treated)
            if len(enroll):
                self.ti_protect_end[enroll] = ti + self._window_steps

        protected = (self.ti_protect_end > ti).uids
        if not len(protected):
            return
        factor = 1.0 - float(self.pars.eff)
        for d in self.diseases:
            dis = sim.diseases.get(d)
            if dis is None:
                continue
            dis.rel_sus[protected] *= factor
        return

    def init_results(self):
        super().init_results()
        self.define_results(
            ss.Result("n_protected", dtype=int, label="Currently protected", auto_plot=False),
            ss.Result("new_enrolled", dtype=int, label="Newly enrolled", auto_plot=False),
        )
        return

    def update_results(self):
        super().update_results()
        ti = self.ti
        self.results["n_protected"][ti] = int((self.ti_protect_end > ti).sum())
        self.results["new_enrolled"][ti] = int((self.ti_protect_end == ti + self._window_steps).sum())
        return


class BehavioralScreen(ss.Intervention):
    """Uganda's national PrEP eligibility tool, asked of HIV-negative people 15 and over at a contact.

    A person qualifies on any one item in the past 12 months: more than one
    partner (the model carries no disclosure, so every partner is of unknown
    status), a condomless act in a non-stable partnership, a sex-work
    partnership as sex worker or client, or a visible syphilis chancre. Every
    item is something a person could report, so the screen never reads the
    network's risk group.

    The network keeps only current edges, so the screen keeps its own record
    from the sim start: per person, the last step with a non-stable
    partnership, with a sex-work partnership, and with a visible chancre, and
    the last active step of their two most recently ended partnerships.
    Condoms cover a fraction of a partnership's acts, so any non-stable
    partnership with condom use below 1 has condomless acts.

    ``contacts`` is a callable returning the uids at a contact this step. People
    who qualify at a contact have ``ti_qualified`` set to this step.
    """

    def __init__(self, contacts, start, name="behavioral_screen"):
        super().__init__(name=name)
        self.contacts = contacts
        self.start = start
        self._window_steps = None
        self.define_states(
            ss.FloatArr("ti_nonstable"),
            ss.FloatArr("ti_sw"),
            ss.FloatArr("ti_ulcer"),
            ss.FloatArr("ti_ended"),
            ss.FloatArr("ti_ended_prev"),
            ss.FloatArr("ti_screened"),
            ss.FloatArr("ti_qualified"),
        )
        return

    def init_pre(self, sim):
        super().init_pre(sim)
        self._window_steps = int(round(1 / sim.t.dt_year))
        # the record learns of ended partnerships from the network's expiry buffer
        sim.networks.structuredsexual.record_expired = True
        return

    def init_results(self):
        super().init_results()
        self.define_results(
            ss.Result("n_screened", dtype=int, label="Screened", auto_plot=False),
            ss.Result("n_qualified", dtype=int, label="Qualified", auto_plot=False),
            ss.Result("n_screened_15_49", dtype=int, label="Screened, 15-49", auto_plot=False),
            ss.Result("n_qualified_15_49", dtype=int, label="Qualified, 15-49", auto_plot=False),
        )
        return

    def _record(self, net):
        ti = self.ti
        ended = net.expired_this_loop
        if len(ended.get("p1", [])):
            # every expired edge was last active in the previous step: end_pairs
            # ran earlier this step, and deaths were appended after last step's
            # analyzers
            uids, n = np.unique(np.concatenate([ended["p1"], ended["p2"]]), return_counts=True)
            uids = ss.uids(uids)
            self.ti_ended_prev[uids] = np.where(n > 1, ti - 1, self.ti_ended[uids])
            self.ti_ended[uids] = ti - 1

        e = net.edges
        nonstable = (e.edge_type != net.edge_types["stable"]) & (e.condoms < 1)
        sw = e.edge_type == net.edge_types["sw"]
        self.ti_nonstable[ss.uids(np.concatenate([e.p1[nonstable], e.p2[nonstable]]))] = ti
        self.ti_sw[ss.uids(np.concatenate([e.p1[sw], e.p2[sw]]))] = ti
        self.ti_ulcer[self.sim.diseases.syph.ulcerative.uids] = ti
        return

    def _qualifies(self, net, uids):
        since = self.ti - self._window_steps + 1
        e = net.edges
        n_current = np.bincount(np.concatenate([e.p1, e.p2]), minlength=len(self.ti_sw.raw))
        n_partners = (n_current[uids]
                      + (self.ti_ended[uids] >= since)
                      + (self.ti_ended_prev[uids] >= since))
        return ((n_partners > 1)
                | (self.ti_nonstable[uids] >= since)
                | (self.ti_sw[uids] >= since)
                | (self.ti_ulcer[uids] >= since))

    def step(self):
        net = self.sim.networks.structuredsexual
        self._record(net)
        if self.sim.now < self.start:
            return
        hiv = self.sim.diseases.hiv
        age = self.sim.people.age
        uids = self.contacts(self.sim)
        # HIV testing has no lower age limit, and PrEP is not offered to children
        uids = uids[~hiv.infected[uids] & (age[uids] >= 15)]
        qualified = uids[self._qualifies(net, uids)]
        self.ti_screened[uids] = self.ti
        self.ti_qualified[qualified] = self.ti
        self.results["n_screened"][self.ti] = len(uids)
        self.results["n_qualified"][self.ti] = len(qualified)
        # the RCCS age range, for comparison with its 29% qualifying
        self.results["n_screened_15_49"][self.ti] = (age[uids] < 50).sum()
        self.results["n_qualified_15_49"][self.ti] = (age[qualified] < 50).sum()
        return


class NotificationVisit(sti.PartnerNotification):
    """Partner notification whose attendees get the POC panel, a syphilis test and an HIV test.

    Upstream ``notify_attendees`` schedules one test, and separate notification
    instances would draw attendees independently, so a partner could get the
    panel without the HIV test. The visit runs all three on the same attendees
    in the index's treatment month. The modules are looked up by name because
    the sim runs copies of the objects built in ``build_sim``.
    """

    VISIT = ("panel", "syph_pn_test", "hiv_test_pn")

    def notify_attendees(self, uids):
        hiv = self.sim.diseases.hiv
        for name in self.VISIT:
            test_uids = uids[~hiv.diagnosed[uids]] if name == "hiv_test_pn" else uids
            if len(test_uids):
                test = self.sim.interventions[name]
                test.step(uids=test_uids)
                # upstream stamps ti_tested only on testers it picks itself, and
                # new_tests counts from it
                test.ti_tested[test_uids] = self.ti


class CareSeekScaler(ss.Intervention):
    """Scale symptomatic care-seeking from ``start`` on (care-seeking lever).

    Deferring to ``start`` mirrors how the POC arm activates at intv_year, so
    pre-switch trajectories match across cells with different care settings.

    On the first step at or after ``start``:
      * NG / CT / TV ``pars.p_symp_care`` is multiplied (sex-stratified, clipped
        to 1.0).
      * Each named syph testing intervention's ``pars.rel_test`` is multiplied by
        the scalar form of the multiplier.

    ``p_symp_care`` is read at infection time, not care-seeking time, so agents
    already infected when this fires keep their stamped ``ti_seeks_care``; only
    new infections after ``start`` use the scaled probability.
    """

    def __init__(self, mult=1.0, start=2027,
                 diseases=("ng", "ct", "tv"),
                 syph_test_interventions=("syph_symp_test", "syph_symp_test_poc", "syph_rash_test"),
                 name="care_seek_scaler", *args, **kwargs):
        super().__init__(name=name)
        self.update_pars(*args, **kwargs)
        if hasattr(mult, "__len__"):
            self.mult_f = float(mult[0])
            self.mult_m = float(mult[1])
        else:
            self.mult_f = self.mult_m = float(mult)
        self.start = start
        self.diseases = list(diseases)
        self.syph_test_interventions = list(syph_test_interventions)
        self._fired = False
        return

    def step(self):
        if self._fired or self.sim.now < self.start:
            return
        for d_name in self.diseases:
            disease = self.sim.diseases.get(d_name)
            if disease is None:
                continue
            curr = disease.pars.p_symp_care
            disease.pars.p_symp_care = [min(1.0, float(curr[0]) * self.mult_f),
                                        min(1.0, float(curr[1]) * self.mult_m)]
        mult_scalar = (self.mult_f + self.mult_m) / 2.0
        if mult_scalar != 1.0:
            for intv_name in self.syph_test_interventions:
                intv = self.sim.interventions.get(intv_name)
                if intv is None or not hasattr(intv, "pars"):
                    continue
                if hasattr(intv.pars, "rel_test"):
                    intv.pars.rel_test = intv.pars.rel_test * mult_scalar
        self._fired = True
        return


class STIScreeningAtHIVTesting(sti.SymptomaticTesting):
    """The POC panel offered to women without discharge symptoms at an HIV testing visit.

    ``contacts`` returns the uids at an HIV testing visit this step. Women are
    offered the panel, men too with ``include_men``, and each offer is
    accepted with probability ``acceptance``. People with NG, CT or TV
    symptoms are left to the care-seeking door, which would otherwise test
    and queue them for treatment a second time. Positives join the shared
    treatment queues, which have already run this step, so treatment follows
    the month after.
    """

    DISCHARGE = ("ng", "ct", "tv")

    def __init__(self, contacts, include_men=False, acceptance=1.0, **kwargs):
        super().__init__(eligibility=self._offered, **kwargs)
        self.define_pars(acceptance=ss.bernoulli(p=acceptance))
        self.contacts = contacts
        self.include_men = include_men

    def _offered(self, sim):
        uids = self.contacts(sim)
        if not self.include_men:
            uids = uids[sim.people.female[uids]]
        for name in self.DISCHARGE:
            uids = uids[~sim.diseases[name].symptomatic[uids]]
        return self.pars.acceptance.filter(uids)


class FSWOutreach(sti.SymptomaticTesting):
    """Periodic NG/CT/TV testing of currently-active FSW (outreach lever).

    Models proactive sex-worker outreach that tests FSW for STIs on a fixed
    cadence regardless of symptoms. Reuses SymptomaticTesting internals: per-step
    bernoulli over ``structuredsexual.fsw.uids``, per-pathogen sens/spec,
    positives enqueued onto the shared treatments. This reaches the asymptomatic
    FSW reservoir the symptomatic-door arms cannot.

    Args:
        coverage_per_step (float): per-step probability an active FSW gets
            screened. 0.10 is roughly 70% annual reach at monthly dt.
    """

    def __init__(self, coverage_per_step=0.10, **kwargs):
        super().__init__(eligibility=self._fsw_eligibility, **kwargs)
        self.define_pars(
            coverage=ss.bernoulli(p=coverage_per_step),
        )

    def _fsw_eligibility(self, sim):
        fsw = sim.networks.structuredsexual.fsw.uids
        if len(fsw) == 0:
            return ss.uids()
        return self.pars.coverage.filter(fsw)
