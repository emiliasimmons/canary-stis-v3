"""Settings explorations: a draw's simulation, seeded with HIV by risk group."""

import pytest

from src.settings import setting_pars
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
