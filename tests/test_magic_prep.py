"""Magic PrEP: everyone HIV-negative who acquires a curable STI starts PrEP, diagnosed or not."""

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

STIS = ["ng", "ct", "tv", "syph"]
START = 2011


@pytest.fixture(scope="module")
def magic():
    # SOC arm, so most new STI infections are never treated
    sim = build_sim(sim_pars(
        sim=dict(n_agents=5_000, start=2010, stop=2011.5),
        prep=dict(eligibility="infected", start=START, coverage=1.0),
        ng=dict(init_prev=0.15), ct=dict(init_prev=0.15), tv=dict(init_prev=0.15),
    ))
    sim.run(verbose=0)
    return sim


def sti_infected_at(sim, ti):
    hit = np.zeros(len(sim.people.alive.raw), dtype=bool)
    for name in STIS:
        hit[(sim.diseases[name].ti_infected == ti).uids] = True
    return hit


def test_nobody_starts_magic_prep_before_its_start(magic):
    new = np.asarray(magic.interventions.prep.results.new_prep)
    before = magic.t.yearvec < START
    assert new[before].sum() == 0
    assert new[~before].sum() > 0


def test_everyone_hiv_negative_infected_with_an_sti_last_step_is_on_prep(magic):
    # interventions run before transmission, so a step's new STI infections
    # reach PrEP in the following step
    hiv = magic.diseases.hiv
    last = magic.t.npts - 1
    infected = sti_infected_at(magic, last - 1)
    negative = (hiv.susceptible | (hiv.ti_infected == last)).raw
    offered = infected & negative & magic.people.alive.raw
    assert offered.sum() >= 50
    assert hiv.on_prep.raw[offered].all()


def test_magic_prep_starts_only_after_an_sti_infection(magic):
    hiv = magic.diseases.hiv
    last = magic.t.npts - 1
    started = (hiv.ti_prep_start == last).raw
    assert started.sum() > 0
    assert sti_infected_at(magic, last - 1)[started].all()
