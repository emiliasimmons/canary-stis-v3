"""STI-triggered PrEP through sti.Prep, and the 2040 end year."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

TREATMENTS = ["ng_tx", "ct_tx", "metronidazole", "syph_tx"]


@pytest.fixture(scope="module")
def triggered():
    # high STI prevalence and a stop six months past the intervention year keep
    # the last step's treated pool above 50
    sim = build_sim(sim_pars(
        sim=dict(n_agents=10_000, start=2010, stop=2011.5),
        intv_year=2011,
        prep=dict(eligibility="dx"),
        ng=dict(init_prev=0.15), ct=dict(init_prev=0.15), tv=dict(init_prev=0.15),
    ))
    sim.run(verbose=0)
    return sim


def test_prep_off_puts_nobody_on_prep():
    sim = build_sim(sim_pars(sim=dict(n_agents=500, start=2010, stop=2011)))
    sim.run(verbose=0)
    assert "prep" not in sim.interventions
    assert not sim.diseases.hiv.on_prep.any()
    assert sim.diseases.hiv.prep_naive[sim.people.auids].all()


def test_nobody_starts_prep_before_the_intervention_year(triggered):
    new = triggered.interventions.prep.results.new_prep
    before = triggered.t.yearvec < 2011
    assert new[before].sum() == 0
    assert new[~before].sum() > 0


def test_30_percent_of_people_treated_in_a_step_are_on_prep_after_it(triggered):
    # sti.Prep tops the offered group up to 30% on PrEP, and offered people
    # already on a course fill part of that, so fewer than 30% start
    hiv = triggered.diseases.hiv
    last = triggered.t.npts - 1
    treated = np.zeros(len(hiv.on_prep.raw), dtype=bool)
    for name in TREATMENTS:
        treated[(triggered.interventions[name].ti_treated == last).uids] = True
    offered = (hiv.susceptible | (hiv.ti_infected == last)) & treated
    n = offered.count()
    assert n >= 50
    on_prep = (offered & hiv.on_prep).count()
    assert 0.3 * n - 1 < on_prep <= 0.3 * n
    assert 0 < (hiv.ti_prep_start == last).count() <= on_prep


def test_a_course_ends_after_3_months_and_is_not_renewed(triggered):
    hiv = triggered.diseases.hiv
    on = hiv.on_prep
    assert on.any()
    assert np.all(hiv.ti_prep_stop[on] - hiv.ti_prep_start[on] == 3)
    # monthly steps: everyone on PrEP started in this step or one of the two before
    res = triggered.interventions.prep.results
    new, n_on = np.asarray(res.new_prep), np.asarray(res.n_on_prep)
    started_within_3 = np.convolve(new, np.ones(3, dtype=int))[:len(new)]
    assert np.all(n_on <= started_within_3)
    assert hiv.prep_discontinued.any()
    # a start happens only in a step the person is treated, so it can never
    # postdate their latest treatment
    last_treated = np.fmax.reduce([triggered.interventions[name].ti_treated.raw
                                   for name in TREATMENTS])
    assert np.all(last_treated[on.uids] >= hiv.ti_prep_start[on])


def test_prep_cuts_hiv_susceptibility_by_75_percent(triggered):
    hiv = triggered.diseases.hiv
    assert np.all(hiv.prep_eff[hiv.on_prep] == pytest.approx(0.75))


def test_run_ends_in_2040_whatever_the_start():
    sim = build_sim(sim_pars(sim=dict(n_agents=200, start=2039)))
    sim.run(verbose=0)
    assert sim.t.yearvec[-1] == pytest.approx(2040)
