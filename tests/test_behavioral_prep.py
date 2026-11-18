"""Behavioral PrEP: Uganda's national eligibility screen at HIV testing and STI clinic visits.

The item tests read each screened person's history from network and disease
state the screen does not use (lifetime partner counts, current edges,
the network's partnership log, syphilis infection counts), every step.
Lifetime counts start at the sim start, as the screen's record does.
"""

from collections import defaultdict

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

START = 2010.25
STI_CLINIC = ["syndromic_vds", "syndromic_uds", "panel",
              "syph_symp_test", "syph_rash_test", "syph_symp_test_poc"]


def _screen_by_step(sim, classify):
    """Run sim, grouping each step's screened people with classify(sim, ti, screened).

    Returns {group: dict(n=, qualified=, risk_groups=)} summed over steps.
    """
    sim.init(verbose=0)
    groups = defaultdict(lambda: dict(n=0, qualified=0, risk_groups=set()))
    for ti in np.flatnonzero(sim.t.yearvec >= START):
        sim.run(until=sim.t.yearvec[ti], verbose=0)
        screen = sim.interventions.behavioral_screen
        qualified = screen.ti_qualified == ti
        rg = sim.networks.structuredsexual.risk_group
        for name, group in classify(sim, ti, screen.ti_screened == ti).items():
            g = groups[name]
            g["n"] += group.count()
            g["qualified"] += (group & qualified).count()
            g["risk_groups"] |= set(np.unique(rg[group]).tolist())
    return dict(groups)


def _lifetime(net):
    return {k: getattr(net, f"lifetime_{k}_partners") for k in ("stable", "casual", "onetime", "sw")}


def _by_item(sim, ti, screened):
    net, syph = sim.networks.structuredsexual, sim.diseases.syph
    life = _lifetime(net)
    no_nonstable = (life["casual"] == 0) & (life["onetime"] == 0) & (life["sw"] == 0)
    one_partnership = sum(life.values()) == 1
    never_syph = syph.n_infections == 0
    on_sw = syph.n_infections < 0
    sw = net.edges.edge_type == net.edge_types["sw"]
    on_sw.raw[np.concatenate([net.edges.p1[sw], net.edges.p2[sw]])] = True
    return dict(
        partners=screened & no_nonstable & never_syph & (net.stable_partners >= 2),
        nonstable=screened & one_partnership & never_syph
        & ((net.casual_partners + net.onetime_partners) == 1),
        sw=screened & one_partnership & never_syph & on_sw,
        ulcer=screened & no_nonstable & (life["stable"] <= 1)
        & syph.ulcerative & (syph.ti_infected < ti),
        none=screened & no_nonstable & (life["stable"] <= 1) & never_syph,
    )


def _by_window(sim, ti, screened):
    """Screened people by how many of their partnerships were active in the past 12 months.

    The network logs the start and length of stable and casual partnerships
    lasting more than one step, so only people with exactly two partnerships,
    both logged, are grouped. People with a dead partner are left out, since
    their partnership may have ended before its logged length.
    """
    net = sim.networks.structuredsexual
    life = _lifetime(net)
    two = screened & (life["stable"] + life["casual"] == 2) & (life["onetime"] == 0) & (life["sw"] == 0)
    last_active = defaultdict(list)
    for (a, b), partnerships in net.relationship_durs.items():
        for p in partnerships:
            t = min(p["start"] + p["dur"] - 1, ti)
            last_active[a].append((t, b))
            last_active[b].append((t, a))
    alive = sim.people.alive.raw
    groups = dict(two_in_window_one_ended=screened & False, one_in_window_one_before=screened & False)
    for u in two.uids:
        ps = last_active[int(u)]
        if len(ps) != 2 or not all(alive[p] for _, p in ps):
            continue
        ended = [t for t, _ in ps if t < ti]
        n_in = sum(t > ti - 12 for t, _ in ps)
        if n_in == 2 and ended:
            groups["two_in_window_one_ended"].raw[u] = True
        elif n_in == 1:
            groups["one_in_window_one_before"].raw[u] = True
    return groups


@pytest.fixture(scope="module")
def behavioral():
    """Screening from three months in, with each screened person's items read every step.

    Sex-work acts all use condoms, so a sex-work partnership qualifies only
    through the sex-work item. Clients form a new one-step sex-work partnership
    most months, so people whose only partnership is a sex-work one are rare.
    Raised client and sex-worker shares and short histories make a few.
    """
    condom_data = sim_pars().network.condom_data
    condom_data[("fsw", "client")] = dict(year=[1990], val=[1.0])
    sim = build_sim(sim_pars(
        sim=dict(n_agents=10_000, start=2010, stop=2011.25),
        prep=dict(eligibility="behavioral", start=START),
        syph=dict(init_prev=0.1),
        hiv_test=dict(test_prob_data=0.95),
        network=dict(condom_data=condom_data, client_shares=0.6, fsw_shares=0.15),
    ))
    sim.groups = _screen_by_step(sim, _by_item)
    return sim


@pytest.fixture(scope="module")
def window():
    """Condoms on every act and no syphilis, so partner count is the only item that can fire."""
    condom_data = {k: dict(year=[1990], val=[1.0]) for k in sim_pars().network.condom_data}
    sim = build_sim(sim_pars(
        sim=dict(n_agents=10_000, start=2010, stop=2012),
        prep=dict(eligibility="behavioral", start=START),
        syph=dict(init_prev=0), syph_latent=dict(init_prev=None),
        hiv_test=dict(test_prob_data=0.95),
        network=dict(condom_data=condom_data),
    ))
    return _screen_by_step(sim, _by_window)


def test_behavioral_prep_off_runs_no_screen():
    sim = build_sim(sim_pars(sim=dict(n_agents=500, start=2010, stop=2011),
                             prep=dict(eligibility="dx")))
    sim.run(verbose=0)
    assert "behavioral_screen" not in sim.interventions


def test_results_count_screened_and_qualified_from_the_start_year(behavioral):
    res = behavioral.interventions.behavioral_screen.results
    screened, qualified = np.asarray(res.n_screened), np.asarray(res.n_qualified)
    before = behavioral.t.yearvec < START
    assert screened[before].sum() == 0
    assert screened[~before].min() > 0
    assert np.all(qualified <= screened)
    assert 0 < qualified.sum() < screened.sum()


def test_only_hiv_negative_people_15_and_over_at_a_testing_or_sti_clinic_visit_are_screened(behavioral):
    sim = behavioral
    last = sim.t.npts - 1
    at_visit = sim.interventions.hiv_test.ti_tested == last
    for name in STI_CLINIC:
        if name in sim.interventions:
            at_visit = at_visit | (sim.interventions[name].ti_tested == last)
    hiv = sim.diseases.hiv
    # infections from this step's transmission come after the screen
    negative_at_screen = ~(hiv.infected & (hiv.ti_infected < last))
    age = sim.people.age
    assert (at_visit & negative_at_screen & (age < 15)).count() > 0
    screened = sim.interventions.behavioral_screen.ti_screened == last
    assert screened.count() >= 50
    assert (screened == (at_visit & negative_at_screen & (age >= 15))).all()


def test_results_count_screened_and_qualified_at_15_49(behavioral):
    sim = behavioral
    last = sim.t.npts - 1
    screen = sim.interventions.behavioral_screen
    age = sim.people.age
    adult = (age >= 15) & (age < 50)
    assert (screen.ti_screened == last).count() > (adult & (screen.ti_screened == last)).count() > 0
    assert screen.results.n_screened_15_49[last] == (adult & (screen.ti_screened == last)).count()
    assert screen.results.n_qualified_15_49[last] == (adult & (screen.ti_qualified == last)).count()


def test_prep_starts_only_in_a_step_the_person_qualified(behavioral):
    # ti_qualified keeps the latest qualification, which can postdate the start
    hiv = behavioral.diseases.hiv
    qualified = behavioral.interventions.behavioral_screen.ti_qualified
    started = hiv.ti_prep_start >= 0
    last = behavioral.t.npts - 1
    assert started.any()
    assert np.all(qualified[started] >= hiv.ti_prep_start[started])
    assert np.all(qualified[hiv.ti_prep_start == last] == last)


@pytest.mark.parametrize("item", ["partners", "nonstable", "sw", "ulcer"])
def test_each_item_alone_qualifies(behavioral, item):
    group = behavioral.groups[item]
    assert group["n"] > 0
    assert group["qualified"] == group["n"]


def test_nobody_without_an_item_qualifies_in_any_risk_group(behavioral):
    group = behavioral.groups["none"]
    assert group["risk_groups"] == {0, 1, 2}
    assert group["qualified"] == 0


def test_a_partnership_ended_in_the_past_12_months_counts_toward_partners(window):
    group = window["two_in_window_one_ended"]
    assert group["n"] >= 50
    assert group["qualified"] == group["n"]


def test_a_partnership_last_active_over_12_months_ago_does_not_count(window):
    group = window["one_in_window_one_before"]
    assert group["n"] >= 20
    assert group["qualified"] == 0
