"""Country setup: demographics loaded from a country's files, or scalar rates when off."""

from pathlib import Path

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

TINY = dict(n_agents=500, start=2010, stop=2011)

# testland's 1985 age structure is 60% under 15 and 4% aged 75 or over, in
# people summing to 1,000,000, as UN WPP files count them. Its fertility is zero, and its mortality is zero
# for women and 0.3 per year for men.
TESTLAND = dict(name="testland", datafolder=Path(__file__).parent / "data")
TESTLAND_SIM = dict(n_agents=2000, start=1985, stop=1986)


def run_testland():
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND))
    sim.run(verbose=0)
    return sim


def test_simulations_start_in_1985():
    assert sim_pars().sim.start == 1985


def test_no_country_uses_scalar_rates():
    pars = sim_pars(sim=TINY, pregnancy=dict(fertility_rate=123), deaths=dict(death_rate=7))
    assert pars.country.name is None
    sim = build_sim(pars)
    sim.run(verbose=0)
    assert sim.demographics.pregnancy.pars.fertility_rate.value == 123
    assert sim.demographics.deaths.pars.death_rate.value == 7
    assert set(sim.demographics.keys()) == {"pregnancy", "deaths"}


def test_country_sets_starting_age_structure():
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND))
    sim.init(verbose=0)
    age = sim.people.age
    assert np.mean(age < 15) == pytest.approx(0.60, abs=0.04)
    assert np.mean(age >= 75) == pytest.approx(0.04, abs=0.02)


def test_country_takes_fertility_and_mortality_from_files():
    sim = run_testland()
    res = sim.results
    assert res.pregnancy.births.sum() == 0
    women = res.n_female.values
    men = res.n_alive.values - women
    # one year at a death rate of 0.3 leaves exp(-0.3) = 74% of men
    assert men[-1] / men[0] == pytest.approx(0.74, abs=0.05)
    assert women[-1] / women[0] > 0.95
    assert set(sim.demographics.keys()) == {"pregnancy", "deaths"}


def test_country_population_counts_are_people():
    # the first record comes after one month of male deaths
    sim = run_testland()
    assert sim.results.n_alive[0] == pytest.approx(1_000_000, rel=0.03)
