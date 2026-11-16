"""Care-pathway timing: which modules test and treat on which steps."""

import pytest

from src.sim import build_sim, sim_pars

# antenatal RDT era from the first step, syphilis common and every presentation
# tested, so each channel has care-seekers on every step
SMALL = dict(
    sim=dict(n_agents=2000, start=2010, dur=2),
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
