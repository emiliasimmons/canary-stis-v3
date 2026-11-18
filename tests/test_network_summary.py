"""The network summary each settings draw records in one year."""

import json

import numpy as np
import pytest

from src.sim import build_sim, sim_pars

YEAR = 2003


@pytest.fixture(scope="module")
def sim():
    built = build_sim(sim_pars(sim=dict(n_agents=1000, start=1995, stop=YEAR), network_summary=dict(year=YEAR)))
    built.run(verbose=0)
    return built


@pytest.fixture(scope="module")
def summary(sim):
    return sim.analyzers.network_summary.summary()


def adults(sim, sex):
    ppl = sim.people
    return (ppl.alive & ppl[sex] & (ppl.age >= 15) & (ppl.age < 50)).count()


def test_summary_is_json_ready_and_compact(summary):
    text = json.dumps(summary)
    assert len(text) < 15000
    assert set(summary) == {"year", "lifetime_partners", "new_partners_last_year", "debut_age", "risk_group",
                            "age_gap", "age_pairing"}


@pytest.mark.parametrize("key, n_bins", [("lifetime_partners", 31), ("new_partners_last_year", 11)])
@pytest.mark.parametrize("sex", ["female", "male"])
def test_partner_histograms_count_everyone_15_49(sim, summary, key, n_bins, sex):
    counts = summary[key][sex]
    assert len(counts) == n_bins
    # the snapshot still counts agents dying on its step, the finished sim does not
    assert sum(counts) == pytest.approx(adults(sim, sex), abs=3)


def test_lifetime_partners_cover_the_last_years_new_ones(summary):
    for sex in ("female", "male"):
        lifetime, new = np.array(summary["lifetime_partners"][sex]), np.array(summary["new_partners_last_year"][sex])
        assert lifetime[0] <= new[0]
        assert lifetime[1:].sum() > 0


@pytest.mark.parametrize("sex", ["female", "male"])
def test_risk_group_proportions_sum_to_one(summary, sex):
    props = summary["risk_group"][sex]
    # sex workers and clients are their own category, out of the risk group they belong to
    assert set(props) == {"low", "medium", "high", "sex_work"}
    assert sum(props.values()) == pytest.approx(1)
    assert props["low"] > props["high"]
    assert 0 < props["sex_work"] < 0.2


@pytest.mark.parametrize("sex", ["female", "male"])
def test_debut_age_histogram_counts_everyone_15_49_by_year_of_age(sim, summary, sex):
    counts = np.array(summary["debut_age"][sex])
    # bins are ages 10 (and under), 11, ..., 29, 30 and over
    assert len(counts) == 21
    assert counts.sum() == pytest.approx(adults(sim, sex), abs=3)
    median_bin = np.searchsorted(np.cumsum(counts), counts.sum() / 2)
    assert 15 <= 10 + median_bin <= 25


def test_age_gaps_count_current_partnerships_by_female_age(sim, summary):
    nw = sim.networks.structuredsexual
    current = (nw.edges.edge_type == nw.edge_types["stable"]) | (nw.edges.edge_type == nw.edge_types["casual"])
    f_age = sim.people.age[nw.edges.p2[current]]
    expected = dict(f15_25=((f_age >= 15) & (f_age < 25)).sum(), f25_35=((f_age >= 25) & (f_age < 35)).sum(),
                    f35_50=((f_age >= 35) & (f_age < 50)).sum())
    gaps = summary["age_gap"]
    assert {k: gaps[k]["n"] for k in expected} == expected
    for group in gaps.values():
        q = group["quantiles"]
        assert len(q) == 5 and q == sorted(q)
        # men are older in the network's age preferences
        assert 0 < q[2] < 15


def test_age_pairing_counts_current_partnerships_by_single_year_of_age(sim, summary):
    nw = sim.networks.structuredsexual
    current = (nw.edges.edge_type == nw.edge_types["stable"]) | (nw.edges.edge_type == nw.edge_types["casual"])
    f_age = sim.people.age[nw.edges.p2[current]]
    cells = np.array(summary["age_pairing"])
    # rows are (female age, male age, partnerships), women 15-64, men's ages clipped to 15-79
    assert cells[:, 0].min() >= 15 and cells[:, 0].max() <= 64
    assert cells[:, 1].min() >= 15 and cells[:, 1].max() <= 79
    assert cells[:, 2].sum() == ((f_age >= 15) & (f_age < 65)).sum()
    assert cells[cells[:, 1] > cells[:, 0], 2].sum() > cells[cells[:, 1] < cells[:, 0], 2].sum()


def test_without_a_year_there_is_no_summary():
    built = build_sim(sim_pars(sim=dict(n_agents=200, start=2000, stop=2001)))
    built.init()
    assert "network_summary" not in built.analyzers
