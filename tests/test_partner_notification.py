"""Partner notification: current stable and casual partners of every treated person, from intv_year."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

INTV = 2010.5
EVERYONE = dict(notify_rates=dict(stable=1.0, casual=1.0),
                attendance_rates=dict(stable=1.0, casual=1.0))
HIGH_STI = dict(ng=dict(init_prev=0.15), ct=dict(init_prev=0.15), tv=dict(init_prev=0.15),
                syph=dict(init_prev=0.05), syph_latent=dict(init_prev=0.1))


def run(**overrides):
    sim = build_sim(sim_pars(**{"sim": dict(n_agents=5000, start=2010, stop=2011.5),
                                "intv_year": INTV, **overrides}))
    sim.run(verbose=0)
    return sim


@pytest.fixture(scope="module")
def notified():
    return run(pn=EVERYONE, **HIGH_STI)


def attendees(sim, ti):
    return (sim.interventions.pn.ti_notified == ti).uids


def union(*arrays):
    return np.unique(np.concatenate(arrays))


def last_busy_step(sim):
    return int(np.flatnonzero(np.asarray(sim.interventions.pn.results.new_attending))[-1])


def test_no_partner_notification_by_default():
    sim = build_sim(sim_pars(sim=dict(n_agents=500, start=2010, stop=2011), intv_year=2010))
    sim.init(verbose=0)
    assert "pn" not in sim.interventions


def test_partner_notification_needs_the_poc_arm():
    with pytest.raises(ValueError, match="intv_year"):
        build_sim(sim_pars(sim=dict(n_agents=500, start=2010, stop=2011), pn=EVERYONE))


def test_nobody_is_notified_before_the_intervention_year(notified):
    new = np.asarray(notified.interventions.pn.results.new_notified)
    before = notified.t.yearvec < INTV
    assert new[before].sum() == 0
    assert new[~before].sum() > 0


def test_attendees_get_the_panel_a_syphilis_test_and_an_hiv_test_at_one_visit(notified):
    ti = last_busy_step(notified)
    uids = attendees(notified, ti)
    intvs = notified.interventions
    assert len(uids) >= 20
    assert np.all(intvs.panel.ti_tested[uids] == ti)
    assert np.all(intvs.syph_pn_test.ti_tested[uids] == ti)
    hiv = notified.diseases.hiv
    undiagnosed_before = uids[~(hiv.diagnosed[uids] & (hiv.ti_diagnosed[uids] < ti))]
    assert len(undiagnosed_before) > 0
    assert np.all(intvs.hiv_test_pn.ti_tested[undiagnosed_before] == ti)


def test_syphilis_positive_attendees_are_treated_that_month(notified):
    intvs = notified.interventions
    pos = (intvs.syph_pn_test.ti_positive >= 0).uids
    assert len(pos) > 0
    assert np.all(intvs.syph_tx.ti_treated[pos] >= intvs.syph_pn_test.ti_positive[pos])
    same_month = intvs.syph_tx.ti_treated[pos] == intvs.syph_pn_test.ti_positive[pos]
    assert same_month.mean() > 0.9


def test_only_current_stable_and_casual_partners_of_indexes_are_notified(notified):
    sim = notified
    ti = sim.t.npts - 1
    intvs = sim.interventions
    index = union(*[(intvs[n].ti_treated == ti).uids for n in ["ng_tx", "ct_tx", "metronidazole"]],
                     (intvs.syph_tx.ti_treated == ti - 1).uids)
    net = sim.networks.structuredsexual
    e = net.edges
    kept = np.isin(e.edge_type, [net.edge_types["stable"], net.edge_types["casual"]])
    p1_index, p2_index = np.isin(e.p1, index), np.isin(e.p2, index)
    one = kept & (p1_index ^ p2_index)
    partners = set(np.where(p1_index, e.p2, e.p1)[one].tolist())
    got = set(attendees(sim, ti).tolist())
    assert len(got) > 0
    # deaths at the end of the step can remove an edge PN walked
    assert len(got - partners) <= 0.02 * len(got)


def test_syphilis_treatments_notify_partners_the_month_after():
    no_discharge = dict(ng=dict(init_prev=0.0), ct=dict(init_prev=0.0), tv=dict(init_prev=0.0),
                        syph=dict(init_prev=0.1), syph_latent=dict(init_prev=0.2),
                        syph_test=dict(symp_test_prob=1.0))
    # a perfect panel, so women presenting with BV are never treated as TV
    perfect = dict(ng=[1.0, 1.0], ct=[1.0, 1.0], tv=[1.0, 1.0])
    sim = run(pn=EVERYONE, poc=dict(sens=perfect, spec=perfect), **no_discharge)
    notified = np.asarray(sim.interventions.pn.results.new_notified)
    treated = np.asarray(sim.interventions.syph_tx.results.new_treated)
    first = int(np.flatnonzero(sim.t.yearvec >= INTV)[0])
    # the month before is SOC, whose syphilis treatments notify nobody
    assert treated[first - 1] > 0 and notified[first] == 0
    notified_steps = np.flatnonzero(notified)
    assert len(notified_steps) > 0
    assert np.all(treated[notified_steps - 1] > 0)


def test_attendees_positive_for_ng_ct_or_tv_are_treated_the_month_after(notified):
    sim = notified
    ti = sim.t.npts - 2
    intvs = sim.interventions
    uids = attendees(sim, ti)
    referred = uids[intvs.panel.ti_referred[uids] == ti]
    assert len(referred) >= 10
    treated_next = np.zeros(len(referred), dtype=bool)
    for name in ["ng_tx", "ct_tx", "metronidazole"]:
        treated_next |= np.asarray(intvs[name].ti_treated[referred] == ti + 1)
    assert treated_next.mean() > 0.9
