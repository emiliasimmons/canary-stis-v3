"""Snapshots: an arm continued from a copy of a simulation stopped at the start of the
intervention year gives the same results as the arm run from the start."""

import copy
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from src import snapshots
from src.settings import setting_pars
from src.sim import _deep_update, build_sim
from src.snapshots import continue_as, run_arms, snapshot

EXP_45 = yaml.safe_load(
    (Path(__file__).parents[1] / "experiments/pathways/45_barker_cofactors_anc_arms/config.yaml").read_text())
YEAR = 2027
# member eswatini_mature-0006 of exp 43's ensembles
DRAW = dict(
    prop_f0=0.6186, prop_m0=0.4616, prop_f2=0.0597, prop_m2=0.1230, f1_conc=0.0670,
    f2_conc=0.2172, m1_conc=0.1976, hiv_beta_m2f=0.0135, rel_init_prev=0.544,
    seed_year=1996.66, syph_beta_m2f=0.0849, ng_beta_m2f=0.1274, ct_beta_m2f=0.0462,
    tv_beta_m2f=0.0460,
)
SMALL = dict(n_agents=2000, rand_seed=7, stop=2030)


def arm_pars(arm, **sim):
    overrides = _deep_update(copy.deepcopy(EXP_45["baseline"]), copy.deepcopy(EXP_45["arms"][arm]))
    return setting_pars(DRAW, "eswatini", sim={**SMALL, **sim}, network_summary=dict(year=None),
                        **overrides)


ARMS = {arm: arm_pars(arm) for arm in EXP_45["arms"]}


@pytest.fixture(scope="module")
def continued():
    t0 = time.perf_counter()
    sims = dict(run_arms(ARMS, YEAR))
    print(f"\n{len(sims)} arms from one snapshot in {time.perf_counter() - t0:.1f} s")
    return sims


def results(sim):
    return {key: np.asarray(res) for key, res in sim.results.flatten().items()}


def assert_same_run(got, expected):
    got_results, expected_results = results(got), results(expected)
    assert list(got_results) == list(expected_results)
    unequal = [key for key in expected_results
               if not np.array_equal(got_results[key], expected_results[key], equal_nan=True)]
    assert not unequal
    pd.testing.assert_frame_equal(got.interventions.treatment_log.to_df(),
                                  expected.interventions.treatment_log.to_df())
    pd.testing.assert_frame_equal(got.analyzers.infection_log.logs.hiv.to_df(),
                                  expected.analyzers.infection_log.logs.hiv.to_df())


@pytest.mark.parametrize("arm", list(ARMS))
def test_continued_arm_matches_the_arm_run_from_1985(continued, arm):
    t0 = time.perf_counter()
    expected = build_sim(ARMS[arm]).run(verbose=0)
    print(f"\n{arm} from 1985 in {time.perf_counter() - t0:.1f} s")
    assert_same_run(continued[arm], expected)


def test_run_arms_yields_each_arm_complete(continued):
    assert list(continued) == list(ARMS)
    assert all(sim.complete for sim in continued.values())


@pytest.fixture(scope="module")
def soc_poc():
    return snapshot([ARMS["soc"], ARMS["poc"]], YEAR)


def test_continue_as_leaves_the_snapshot_unrun_past_its_year(soc_poc):
    continue_as(soc_poc, ARMS["poc"]).run(verbose=0)
    assert soc_poc.t.now("year") == pytest.approx(YEAR)


def test_a_switch_setting_left_uncopied_is_caught(soc_poc, monkeypatch):
    monkeypatch.delitem(snapshots.STEP_ATTRS, "syph_symp_test_poc")
    with pytest.raises(RuntimeError, match="syph_symp_test_poc.start"):
        continue_as(soc_poc, ARMS["poc"])


def test_arms_differing_outside_the_switches_are_rejected():
    other = arm_pars("poc", rand_seed=8)
    with pytest.raises(ValueError, match="group 'sim'"):
        snapshot([ARMS["soc"], other], YEAR)


def test_an_arm_switching_on_before_the_snapshot_year_is_rejected():
    early = arm_pars("soc")
    early.intv_year = 2020
    with pytest.raises(ValueError, match="2020"):
        snapshot([ARMS["soc"], early], YEAR)


def test_arms_differing_in_care_seeking_are_rejected():
    scaled = arm_pars("poc")
    scaled.care_seek_mult = 1.5
    with pytest.raises(ValueError, match="care_seek_mult"):
        snapshot([ARMS["poc"], scaled], YEAR)


def test_an_arm_outside_the_snapshot_is_rejected(soc_poc):
    with pytest.raises(ValueError, match="arms the snapshot was built for"):
        continue_as(soc_poc, ARMS["poc_pn"])
