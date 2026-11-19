"""ANC testing: the ANC HIV test and ANC syphilis screening start in anc.start."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

# testland has no births, so these use Zimbabwe's fertility
ANC_TESTS = ["hiv_test_anc", "syph_anc_rpr"]


def run(**overrides):
    sim = build_sim(sim_pars(sim=dict(n_agents=3000, start=1985, stop=1987),
                             country=dict(name="zimbabwe"), **overrides))
    sim.run(verbose=0)
    return sim


def anc_tests_per_step(sim, name):
    return np.asarray(sim.interventions[name].results.new_tests)


@pytest.fixture(scope="module")
def default():
    return run()


@pytest.mark.parametrize("name", ANC_TESTS)
def test_anc_testing_runs_from_the_start_by_default(default, name):
    first_year = anc_tests_per_step(default, name)[:12]
    assert first_year.sum() > 0


@pytest.mark.parametrize("name", ANC_TESTS)
def test_anc_testing_starts_in_its_start_year(name):
    sim = run(anc=dict(start=1986))
    tests = anc_tests_per_step(sim, name)
    start = int(np.flatnonzero(sim.t.yearvec >= 1986)[0])
    assert tests[:start].sum() == 0
    assert tests[start:].sum() > 0


@pytest.mark.parametrize("name", ANC_TESTS)
def test_anc_testing_never_runs_from_infinity(name):
    sim = run(anc=dict(start=np.inf))
    assert anc_tests_per_step(sim, name).sum() == 0


def test_anc_syphilis_rdt_starts_in_the_later_of_rdt_year_and_anc_start():
    sim = run(rdt_year=1985.5, anc=dict(start=1986))
    tests = anc_tests_per_step(sim, "syph_anc_rdt")
    start = int(np.flatnonzero(sim.t.yearvec >= 1986)[0])
    assert tests[:start].sum() == 0
    assert tests[start:].sum() > 0
