"""HIV incidence at ages 15-49 per 100 person-years, the settings' phase measure."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

SIM = dict(n_agents=3000, start=2010, stop=2013)
YEARS = [2010, 2011, 2012]
BANDS = ["15_20", "20_25", "25_30", "30_35", "35_50"]


def run(**overrides):
    sim = build_sim(sim_pars(sim=SIM, **overrides))
    sim.run(verbose=0)
    return sim


@pytest.fixture(scope="module")
def epidemic():
    return run(hiv=dict(init_prev=0.2, beta_m2f=0.1))


@pytest.mark.parametrize("sex, key", [("all", ""), ("female", "_f"), ("male", "_m")])
def test_new_infections_at_15_49_match_stisims_age_bands(epidemic, sex, key):
    annual = epidemic.analyzers.hiv_incidence_15_49.annual().set_index(["year", "sex"])
    res = epidemic.results.hiv
    year = np.floor(epidemic.t.yearvec)
    for y in YEARS:
        bands = sum(res[f"new_infections{key}_{band}"][year == y].sum() for band in BANDS)
        assert bands > 0
        assert annual.loc[(y, sex), "new_infections"] == bands


def test_without_hiv_person_years_are_the_15_49_population():
    sim = run(hiv=dict(init_prev=0.0))
    annual = sim.analyzers.hiv_incidence_15_49.annual().set_index(["year", "sex"])
    age = sim.people.age[sim.people.alive]
    population = ((age >= 15) & (age < 50)).sum()
    assert annual.loc[(2012, "all"), "person_years"] == pytest.approx(population, rel=0.05)
    assert (annual.incidence == 0).all()

