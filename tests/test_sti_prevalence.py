"""Curable-STI prevalence at ages 15-49 by year, the settings' STI burden check."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

SIM = dict(n_agents=3000, start=2010, stop=2013)
YEARS = [2010, 2011, 2012]
BANDS = ["15_20", "20_25", "25_30", "30_35", "35_50"]
DISEASES = ["ng", "ct", "tv", "syph"]


def run(**overrides):
    sim = build_sim(sim_pars(sim=SIM, **overrides))
    sim.run(verbose=0)
    return sim


@pytest.fixture(scope="module")
def epidemic():
    return run()


@pytest.mark.parametrize("disease", DISEASES)
@pytest.mark.parametrize("sex, key", [("all", ""), ("female", "_f"), ("male", "_m")])
def test_infected_person_years_match_stisims_age_bands(epidemic, disease, sex, key):
    annual = epidemic.analyzers.sti_prevalence_15_49.annual().set_index(["year", "sex", "disease"])
    res = epidemic.results[disease]
    year = np.floor(epidemic.t.yearvec)
    for y in YEARS:
        bands = sum(res[f"n_infected{key}_{band}"][year == y].sum() for band in BANDS)
        assert bands > 0
        py = annual.loc[(y, sex, disease), "person_years_infected"]
        # stisim's bands still count agents dying this step, the analyzer only the living
        assert py == pytest.approx(bands * epidemic.t.dt_year, rel=0.01)


def test_without_gonorrhoea_its_prevalence_is_zero():
    sim = run(ng=dict(init_prev=0.0))
    annual = sim.analyzers.sti_prevalence_15_49.annual()
    assert (annual[annual.disease == "ng"].prevalence == 0).all()
    assert (annual[annual.disease == "ct"].prevalence > 0).all()
