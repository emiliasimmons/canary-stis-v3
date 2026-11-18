"""Settings explorations: a draw's simulation, seeded with HIV by risk group."""

import json

import numpy as np
import pytest

from src.settings import SELECTION_YEAR, setting_pars, summarize
from src.sim import build_sim

INIT = dict(n_agents=20_000, stop=1986)


def seeded(draw, **overrides):
    sim = build_sim(setting_pars(draw, "eswatini", sim=INIT, **overrides))
    sim.init()
    return sim


def test_scalar_init_prev_is_ignored_when_seeding_by_risk_group():
    sim = seeded(dict(rel_init_prev=1.0), hiv=dict(init_prev=0.9))
    ppl = sim.people
    adults = ppl.alive & (ppl.age >= 15) & (ppl.age < 50)
    assert 0 < (sim.diseases.hiv.infected & adults).count() < 0.05 * adults.count()


def test_seeding_by_risk_group_infects_no_children():
    sim = seeded(dict(rel_init_prev=1.5))
    children = sim.people.alive & (sim.people.age < 10)
    assert children.count() > 0
    assert (sim.diseases.hiv.infected & children).count() == 0


def test_rel_init_prev_scales_the_seed():
    low = seeded(dict(rel_init_prev=0.5)).diseases.hiv.infected.count()
    high = seeded(dict(rel_init_prev=2.0)).diseases.hiv.infected.count()
    assert high / low == pytest.approx(4, rel=0.3)


def run(draw, **sim):
    built = build_sim(setting_pars(draw, "eswatini", sim=dict(n_agents=1000, stop=1990, **sim)))
    built.run(verbose=0)
    return built


def test_without_seed_year_hiv_is_seeded_at_the_start_as_before():
    # pinned from the model before seed_year existed
    n_infected = run(dict(rel_init_prev=10.0)).results.hiv.n_infected
    assert n_infected[0] > 0
    assert int(n_infected.sum()) == 2279600


@pytest.fixture(scope="module")
def summarized():
    sim = build_sim(setting_pars(dict(rel_init_prev=10.0, seed_year=1996.4), "eswatini", sim=dict(n_agents=500)))
    sim.run(verbose=0)
    return summarize(sim)


def test_summary_is_json_ready_with_the_network_in_the_selection_year(summarized):
    json.dumps(summarized)
    assert summarized["network"]["year"] == SELECTION_YEAR
    assert sum(summarized["network"]["lifetime_partners"]["female"]) > 0


def test_summary_has_no_hiv_before_seed_year(summarized):
    prevalence = dict(zip(summarized["years"], summarized["hiv_prevalence"]))
    assert prevalence[1995] == 0
    assert prevalence[1997] > 0


def test_before_seed_year_there_is_no_hiv():
    sim = run(dict(rel_init_prev=10.0, seed_year=1988.4))
    n_infected = sim.results.hiv.n_infected
    seed_ti = np.argmax(sim.t.yearvec >= 1988.4)
    assert (n_infected[:seed_ti] == 0).all()
    assert n_infected[seed_ti] > 0
