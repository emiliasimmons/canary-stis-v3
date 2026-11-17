"""Care-pathway timing: which modules test and treat on which steps."""

import numpy as np
import pytest
import starsim as ss

from src.sim import build_sim, sim_pars

# antenatal RDT era from the first step, syphilis common and every presentation
# tested, so each channel has care-seekers on every step
SMALL = dict(
    sim=dict(n_agents=2000, start=2010, stop=2012),
    rdt_year=2010,
    syph=dict(init_prev=0.05),
    syph_latent=dict(init_prev=0.2),
    syph_test=dict(symp_test_prob=1.0),
)


def run(**overrides):
    sim = build_sim(sim_pars(**{**SMALL, **overrides}))
    sim.run(verbose=0)
    return sim


@pytest.mark.parametrize("overrides, channels", [
    (dict(), ["syndromic_vds", "syndromic_uds",
              "syph_symp_test", "syph_rash_test", "syph_anc_rdt"]),
    (dict(intv_year=2010), ["panel", "syph_symp_test_poc", "syph_rash_test",
                            "syph_anc_rdt", "syph_anc_confirm"]),
    (dict(fsw_outreach=dict(rate=1.0)), ["fsw_outreach"]),
], ids=["soc", "poc", "fsw"])
def test_default_stops_test_and_treat_on_last_step(overrides, channels):
    sim = run(**overrides)
    intvs = sim.interventions
    for name in channels:
        assert intvs[name].results.new_tests[-1] > 0, name
    for name in ["ng_tx", "ct_tx", "metronidazole", "syph_tx"]:
        assert intvs[name].results.new_treated[-1] > 0, name


def test_intv_year_switches_syndromic_to_panel():
    sim = run(intv_year=2011)
    before = sim.t.yearvec < 2011
    for name in ["syndromic_vds", "syndromic_uds"]:
        tests = sim.interventions[name].results.new_tests
        assert tests[before][-1] > 0 and tests[~before].sum() == 0, name
    tests = sim.interventions.panel.results.new_tests
    assert tests[before].sum() == 0 and tests[~before][0] > 0


@pytest.mark.parametrize("intv_year", [None, 2010], ids=["syndromic", "panel"])
def test_referrals_treated_after_fsw_outreach_stops(intv_year):
    sim = run(intv_year=intv_year, fsw_outreach=dict(rate=1.0, stop=2011))
    after = sim.t.yearvec >= 2011
    assert sim.interventions.fsw_outreach.results.new_tests[after].sum() == 0
    for name in ["ng_tx", "ct_tx", "metronidazole"]:
        assert sim.interventions[name].results.new_treated[after].sum() > 0, name


# an ulcer test that reaches every presentation treats each chancre before
# its primary stage ends, so the stage tests need chancres that go untested
PAST_PRIMARY = {**SMALL, "syph_test": dict(symp_test_prob=0.15)}


def _steps_with_past_primary(sim):
    """Step sim, yielding (ti, people past primary syphilis when step ti began).

    Stages only advance at the start of a step and infection only enters the
    primary stage, so state at the end of the previous step is a lower bound on
    who is past primary when the step's tests run.
    """
    sim.init(verbose=0)
    syph = sim.diseases.syph
    for ti in range(len(sim.t.yearvec)):
        past = (syph.secondary | syph.latent | syph.tertiary).uids
        sim.run(until=sim.t.yearvec[ti], verbose=0)
        yield ti, past


def _stamped(sim, names, attr, ti):
    uids = ss.uids()
    for name in names:
        test = sim.interventions.get(name)
        if test is not None:
            uids = uids | (getattr(test, attr) == ti).uids
    return uids


@pytest.mark.parametrize("intv_year", [None, 2010], ids=["soc", "poc"])
def test_ulcer_test_skips_syphilis_past_primary(intv_year):
    sim = build_sim(sim_pars(**PAST_PRIMARY, intv_year=intv_year))
    n_tested = n_past = 0
    for ti, past in _steps_with_past_primary(sim):
        tested = _stamped(sim, ["syph_symp_test", "syph_symp_test_poc"], "ti_tested", ti)
        assert len(np.intersect1d(past, tested)) == 0, ti
        n_tested += len(tested)
        n_past += len(past)
    assert n_tested > 0 and n_past > 0


def test_ulcer_test_reaches_non_syphilitic_ulcers():
    sim = run(syph=dict(init_prev=0, beta_m2f=0), syph_latent=dict(init_prev=None),
              gudp=dict(prevalence=0.1))
    assert sim.diseases.syph.ever_exposed.count() == 0
    assert sim.interventions.syph_symp_test.results.new_tests.sum() > 0


@pytest.mark.parametrize("intv_year", [None, 2010], ids=["soc", "poc"])
def test_syphilis_past_primary_treated_only_via_rash_or_antenatal(intv_year):
    sim = build_sim(sim_pars(**PAST_PRIMARY, intv_year=intv_year))
    channels = ["syph_rash_test", "syph_anc_rpr", "syph_anc_rdt", "syph_anc_confirm"]
    n_treated = 0
    for ti, past in _steps_with_past_primary(sim):
        treated = np.intersect1d(past, (sim.interventions.syph_tx.ti_treated == ti).uids)
        via = _stamped(sim, channels, "ti_positive", ti)
        assert np.isin(treated, via).all(), ti
        n_treated += len(treated)
    assert n_treated > 0
