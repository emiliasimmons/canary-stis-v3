"""The Magic cure clears the four curable STIs in the simulation it runs in."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

CURED = ["ng", "ct", "syph", "tv"]
CURE_YEAR = 2010.5


@pytest.fixture(scope="module")
def cured():
    sim = build_sim(sim_pars(
        sim=dict(n_agents=2_000, start=2010, stop=2011),
        magic_cure=dict(year=CURE_YEAR),
        ng=dict(init_prev=0.15), ct=dict(init_prev=0.15), tv=dict(init_prev=0.15), syph=dict(init_prev=0.05),
    ))
    sim.run(verbose=0)
    return sim


@pytest.mark.parametrize("disease", CURED)
def test_prevalence_falls_at_least_90_percent_in_the_cure_step(cured, disease):
    # transmission runs after the interventions in a step, so a few people are
    # infected again within the cure step itself
    ti = int(np.searchsorted(cured.t.yearvec, CURE_YEAR))
    prev = np.asarray(cured.results[disease].prevalence)
    assert prev[ti - 1] > 0.01
    assert prev[ti] < 0.1 * prev[ti - 1]
