"""STI screening at HIV testing: the POC panel for people at a background HIV testing visit."""

import numpy as np
import pytest

from src.sim import HIV_TEST_NAMES, build_sim, sim_pars

INTV = 2010.5


def run(screening, **overrides):
    sim = build_sim(sim_pars(**{"sim": dict(n_agents=5000, start=2010, stop=2011.5),
                                "intv_year": INTV, "hiv_test": dict(test_prob_data=0.9),
                                "ng": dict(init_prev=0.15), "sti_screening": screening,
                                **overrides}))
    sim.run(verbose=0)
    return sim


@pytest.fixture(scope="module")
def women():
    return run(dict())


def hiv_tested(sim, ti, women_only=False):
    """People at an HIV testing visit in step ti."""
    uids = set()
    for name in HIV_TEST_NAMES:
        if name in sim.interventions:
            uids |= set((sim.interventions[name].ti_tested == ti).uids.tolist())
    if women_only:
        uids = {u for u in uids if sim.people.female[u]}
    return uids


def screened_at(sim, ti):
    return set((sim.interventions.sti_screening.ti_tested == ti).uids.tolist())


def test_no_screening_by_default():
    sim = build_sim(sim_pars(sim=dict(n_agents=500, start=2010, stop=2011), intv_year=2010))
    sim.init(verbose=0)
    assert "sti_screening" not in sim.interventions


def test_screening_needs_the_poc_arm():
    with pytest.raises(ValueError, match="intv_year"):
        build_sim(sim_pars(sim=dict(n_agents=500, start=2010, stop=2011), sti_screening=dict()))


# the no-country HIV test keeps stisim's default stop and skips the final step,
# and later visits overwrite earlier stamps, so tests read the second-last step
def check_step(sim):
    return sim.t.npts - 2


def test_every_woman_at_an_hiv_testing_visit_is_screened_from_the_intervention_year(women):
    sim = women
    screening = sim.interventions.sti_screening
    stamped = np.asarray(screening.ti_tested.raw)
    first = int(np.flatnonzero(sim.t.yearvec >= INTV)[0])
    assert np.nanmin(stamped) >= first
    ti = check_step(sim)
    women = hiv_tested(sim, ti, women_only=True)
    assert len(women) > 0
    assert screened_at(sim, ti) == women


def test_include_men_screens_men_too():
    sim = run(dict(include_men=True))
    ti = check_step(sim)
    screened = screened_at(sim, ti)
    assert any(sim.people.male[u] for u in screened)
    assert screened == hiv_tested(sim, ti)


def test_acceptance_sets_the_proportion_screened():
    sim = run(dict(acceptance=0.5))
    ti = check_step(sim)
    offered = hiv_tested(sim, ti, women_only=True)
    screened = screened_at(sim, ti)
    assert screened <= offered and len(offered) > 200
    assert 0.4 < len(screened) / len(offered) < 0.6


def test_screened_positives_are_treated_the_month_after(women):
    sim = women
    screening = sim.interventions.sti_screening
    ti = check_step(sim)
    referred = (screening.ti_referred == ti).uids
    assert len(referred) > 0
    treated_next = np.zeros(len(referred), dtype=bool)
    for name in ["ng_tx", "ct_tx", "metronidazole"]:
        treated_next |= np.asarray(sim.interventions[name].ti_treated[referred] == ti + 1)
    assert treated_next.mean() > 0.9
    log = sim.interventions.treatment_log.to_df()
    assert "sti_screening" in set(log.channel.str.split("+").explode())
