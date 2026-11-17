"""sim_pars overrides, merging and off-states."""

import pytest

from src.sim import build_sim, sim_pars

TINY = dict(n_agents=500, start=2010, stop=2011)
LEVERS = ["care_seek_scaler", "fsw_outreach", "condom_counseling", "prep", "magic_cure"]


def run(**overrides):
    sim = build_sim(sim_pars(**{"sim": TINY, **overrides}))
    sim.run(verbose=0)
    return sim


def test_disease_override_reaches_module():
    sim = run(ng=dict(init_prev=0.0))
    assert sim.results.ng.n_infected.sum() == 0
    assert sim.results.ct.n_infected.sum() > 0


def test_intervention_override_reaches_module():
    sim = run(syph=dict(init_prev=0.2), syph_test=dict(symp_test_prob=0.0))
    assert sim.interventions.syph_symp_test.results.new_tests.sum() == 0
    assert sim.interventions.syph_anc_rpr.results.new_tests.sum() > 0


def test_sim_override_reaches_sim():
    sim = run(sim=dict(TINY, n_agents=321, rand_seed=7))
    assert sim.pars.rand_seed == 7
    assert sim.pars.n_agents == 321


def test_lever_override_adds_module():
    sim = run(care_seek_mult=2.0, fsw_outreach=dict(rate=0.1),
              bundled_prevention=dict(coverage=0.5, eff=0.5),
              prep=dict(eligibility="dx"), magic_cure=dict(year=2010.5))
    for name in LEVERS:
        assert name in sim.interventions, name


def test_defaults_add_no_lever_modules():
    sim = run()
    for name in LEVERS:
        assert name not in sim.interventions, name
    assert "syph_symp_test_poc" not in sim.interventions
    assert sim.interventions.panel.results.new_tests.sum() == 0


def test_levers_default_to_off_states():
    pars = sim_pars()
    assert pars.intv_year is None
    assert pars.care_seek_mult == 1.0
    assert pars.bundled_prevention is None
    assert pars.fsw_outreach.rate == 0.0
    assert pars.prep.eligibility == "none"
    assert pars.magic_cure.year is None


def test_nested_override_is_deep_merged():
    default = sim_pars()
    pars = sim_pars(poc=dict(sens=dict(ng=[0.5, 0.6])), sim=dict(stop=2015))
    assert pars.poc.sens["ng"] == [0.5, 0.6]
    assert pars.poc.sens["ct"] == default.poc.sens["ct"]
    assert pars.poc.spec == default.poc.spec
    assert pars.sim.stop == 2015
    assert pars.sim.n_agents == default.sim.n_agents


def test_scalar_group_takes_override_directly():
    pars = sim_pars(intv_year=2027, bundled_prevention=dict(coverage=0.5))
    assert pars.intv_year == 2027
    assert pars.bundled_prevention == dict(coverage=0.5)


def test_unknown_group_raises():
    with pytest.raises(KeyError):
        sim_pars(not_a_group=dict(x=1))


def test_non_dict_for_dict_group_raises():
    with pytest.raises(TypeError):
        sim_pars(ng=0.1)
