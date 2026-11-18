"""
Care-seeking eligibility, arm gating, and the syphilis ANC visit timer.

Two diagnostic arms share one set of treatment modules. Which arm is live is
decided by wrapping each arm's eligibility callable rather than by setting
``start``/``stop``: ``SyndromicManagement.step`` wipes its linked treatments'
eligibility once past ``stop``, which would silently disarm the other arm's
referrals on the same timestep.
"""

import numpy as np
import starsim as ss

# NG/CT/TV drive both discharge syndromes; BV drives the female one only, and
# is the bulk of the real vaginal-discharge queue.
_DISCHARGE_DISEASES = ("ng", "ct", "tv")


def _seeking(dis, ti):
    """UIDs symptomatic for *dis* whose care-seeking visit falls on *ti*."""
    return (dis.symptomatic & (dis.ti_seeks_care == ti)).uids


def _discharge_modules(sim, include_bv):
    """Disease modules feeding a discharge syndrome."""
    names = _DISCHARGE_DISEASES + (("bv",) if include_bv else ())
    for dis in sim.diseases():
        if dis.name in names:
            yield dis


def seeking_care_vds(sim):
    """
    Women presenting with vaginal discharge: NG, CT, TV, or BV care-seekers.

    UIDs are unioned rather than the BoolArrs ored, to avoid the
    shape-(0,)|shape-(N,) raise on step 0 when a module has no care-seekers.
    """
    uids = ss.uids()
    female = sim.people.female
    for dis in _discharge_modules(sim, include_bv=True):
        seekers = _seeking(dis, sim.ti)
        uids = uids | seekers[female[seekers]]
    return uids


def seeking_care_uds(sim):
    """Men presenting with urethral discharge: NG, CT, or TV care-seekers."""
    uids = ss.uids()
    male = sim.people.male
    for dis in _discharge_modules(sim, include_bv=False):
        seekers = _seeking(dis, sim.ti)
        uids = uids | seekers[male[seekers]]
    return uids


def seeking_care_any(sim):
    """Every discharge care-seeker, either sex. The POC panel does not split by sex."""
    return seeking_care_vds(sim) | seeking_care_uds(sim)


def gate_soc(raw_fn, use_poc, intv_year):
    """Wrap *raw_fn* so it goes quiet from *intv_year* on, and only if POC is enabled."""
    def eligibility(sim):
        if use_poc and sim.t.now("year") >= intv_year:
            return ss.uids()
        return raw_fn(sim)
    return eligibility


def gate_poc(raw_fn, use_poc, intv_year):
    """Wrap *raw_fn* so it stays quiet until *intv_year*, and for the whole run if POC is off."""
    def eligibility(sim):
        if not use_poc or sim.t.now("year") < intv_year:
            return ss.uids()
        return raw_fn(sim)
    return eligibility


def treated_this_step(treatment_names):
    """Eligibility: agents whose treatment fired this step, across *treatment_names*.

    Arm-agnostic diagnosis signal: under SOC a positive is an empiric syndromic
    treatment, under POC an etiological-panel-driven one, and both land as a
    ``ti_treated == ti`` stamp on the shared treatment modules.
    """
    def eligibility(sim):
        uids = ss.uids()
        for name in treatment_names:
            tx = sim.interventions.get(name)
            if tx is None or not hasattr(tx, "ti_treated"):
                continue
            uids = uids | (tx.ti_treated == sim.ti).uids
        return uids
    return eligibility


def notification_indexes(sim):
    """People whose NG/CT/TV treatment fired this step, or syphilis treatment last step.

    Partner notification runs before syph_tx in each step, so a syphilis
    treatment makes its index the step after.
    """
    ti = sim.ti
    uids = treated_this_step(["ng_tx", "ct_tx", "metronidazole"])(sim)
    return uids | (sim.interventions.syph_tx.ti_treated == ti - 1).uids


def tested_this_step(test_names):
    """Agents any of *test_names* tested this step; absent tests are skipped."""
    def contacts(sim):
        uids = ss.uids()
        for name in test_names:
            test = sim.interventions.get(name)
            if test is not None:
                uids = uids | (test.ti_tested == sim.ti).uids
        return uids
    return contacts


def syph_ulcer_eligibility(sim):
    """Anyone presenting with a genital ulcer, whatever is causing it.

    Syndromic management treats the presentation, so the pool is a syphilitic
    chancre at a visible site *or* a non-syphilitic ulcer (the gudp module).
    The second arm is the only route by which the ulcer channel reaches latent
    syphilis, and the source of presumptive over-treatment.

    The chancre side reads ``ulcerative``: stisim draws ``chancre_visible`` at
    infection and clears it only on treatment or death, so on its own it also
    covers the incubation, secondary and latent stages.
    """
    syph = sim.diseases.syph
    gudp = sim.diseases.get("gudp")
    if gudp is None:
        return syph.ulcerative.uids
    return (syph.ulcerative | gudp.symptomatic).uids


def syph_rash_eligibility(sim):
    """Syphilis presenting as a noticeable secondary rash."""
    return sim.diseases.syph.rash_visible.uids


def syph_anc_eligibility(sim):
    """Pregnant women whose single scheduled ANC visit falls this timestep."""
    timer = sim.interventions.get("syph_anc_timer")
    if timer is None:
        return ss.uids()
    return timer.today_uids


def syph_anc_confirm_eligibility(sim):
    """Women whose ANC dual RDT came back positive this timestep."""
    rdt = sim.interventions.get("syph_anc_rdt")
    if rdt is None:
        return ss.uids()
    return (rdt.ti_positive == rdt.ti).uids


def make_syph_tx_eligibility(test_names, screen_only_name=None, confirm_name=None):
    """
    Build the syphilis treatment selector: anyone a treatment-triggering test
    called positive this timestep.

    The ANC channel has two shapes. Without a confirmatory step the dual RDT
    positives are the trigger. With one (POC arm, post-switch), the RDT becomes
    screen-only and the confirmation replaces it: the treponemal RDT reads
    positive on 95% of previously infected but cleared women against 5% for the
    non-treponemal RPR, so treating on the RDT alone re-treats every cured woman
    who returns for antenatal care.
    """
    def eligibility(sim):
        names = list(test_names)
        confirm = sim.interventions.get(confirm_name) if confirm_name else None
        if confirm is not None and sim.t.now("year") >= confirm.start:
            names.append(confirm_name)
        elif screen_only_name is not None:
            names.append(screen_only_name)
        uids = ss.uids()
        for name in names:
            test = sim.interventions.get(name)
            if test is not None:
                uids = uids | (test.ti_positive == test.ti).uids
        return uids
    return eligibility


class SyphilisANCTimer(ss.Intervention):
    """
    One antenatal visit per pregnancy, at a gestational week drawn per woman.

    Antenatal attendance is not concentrated in the first trimester, so the
    visit week is drawn uniformly across the window rather than fixed. Syphilis
    screening interventions read ``today_uids``.

    Args:
        anc_low  (int): earliest visit, weeks post-conception.
        anc_high (int): latest visit, weeks post-conception.
    """

    def __init__(self, pars=None, anc_low=8, anc_high=32, name="syph_anc_timer", **kwargs):
        super().__init__(name=name)
        self.define_pars(
            visit_week=ss.uniform(low=anc_low, high=anc_high),
        )
        self.update_pars(pars, **kwargs)
        self.define_states(
            ss.FloatArr("ti_anc_visit", default=np.nan, label="ti of scheduled ANC visit"),
        )
        return

    @property
    def pregnancy(self):
        return self.sim.demographics.get("pregnancy")

    def _schedule(self, uids):
        if len(uids) == 0:
            return
        weeks = self.pars.visit_week.rvs(uids)  # keyed on uids, so common-random-number safe
        weeks_per_step = self.t.dt_year * 52.0
        steps_to_visit = np.round(weeks / weeks_per_step).astype(int)
        self.ti_anc_visit[uids] = self.pregnancy.ti_pregnant[uids] + steps_to_visit
        return

    def init_post(self):
        super().init_post()
        # women already pregnant at sim start would otherwise never be screened
        if self.pregnancy is not None:
            self._schedule(self.pregnancy.pregnant.uids)
        return

    def step(self):
        preg = self.pregnancy
        if preg is None:
            return
        pregnant = preg.pregnant.uids
        self._schedule(pregnant[preg.ti_pregnant[pregnant] == self.ti])
        return

    @property
    def today_uids(self):
        preg = self.pregnancy
        if preg is None:
            return ss.uids()
        candidates = self.ti_anc_visit.notnan.uids
        if len(candidates) == 0:
            return ss.uids()
        due = candidates[self.ti_anc_visit[candidates] == self.ti]
        if len(due) == 0:
            return ss.uids()
        return due[preg.pregnant[due] & self.sim.people.alive[due]]
