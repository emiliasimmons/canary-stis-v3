"""Country setup: demographics and HIV programmes loaded from a country's files, or scalar
rates and programmes when off."""

import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import stisim as sti

from src.sim import build_sim, sim_pars

TINY = dict(n_agents=500, start=2010, stop=2011)

# testland's 1985 age structure is 60% under 15 and 4% aged 75 or over, in
# people summing to 1,000,000, as UN WPP files count them. Its fertility is zero, and its mortality is zero
# for women and 0.3 per year for men.
TESTLAND = dict(name="testland", datafolder=Path(__file__).parent / "data")
TESTLAND_SIM = dict(n_agents=2000, start=1985, stop=1986)
STREAMS = ["hiv_test_fsw", "hiv_test_general", "hiv_test_low_cd4", "hiv_test_anc"]


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


def hiv_tests(sim):
    return {name: intv for name, intv in sim.interventions.items() if isinstance(intv, sti.HIVTest)}


def test_no_country_runs_scalar_hiv_programmes():
    sim = build_sim(sim_pars(sim=TINY))
    sim.run(verbose=0)
    art = sim.interventions.art
    assert art.coverage_format == "p"
    assert np.all(art.coverage == 0.6)
    assert "vmmc" not in sim.interventions
    tests = hiv_tests(sim)
    assert list(tests) == ["hiv_test"]
    assert tests["hiv_test"].test_prob_data == 0.3
    assert tests["hiv_test"].start == 2000


def test_country_art_targets_its_coverage_table():
    # testland's 1985 ART coverage is 0.11-0.14 for women and 0.21-0.24 for men,
    # rising with age band
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND))
    sim.init(verbose=0)
    art = sim.interventions.art
    assert art.coverage_format == "p"
    bands = ["[15,25)", "[25,35)", "[35,45)", "[45,100)"]
    for sex, levels in [(0, [0.11, 0.12, 0.13, 0.14]), (1, [0.21, 0.22, 0.23, 0.24])]:
        for band, level in zip(bands, levels):
            assert art.coverage[(band, sex)][0] == pytest.approx(level)


def test_country_vmmc_circumcises_to_its_coverage_table():
    # testland circumcises 80% of men aged 15-19 and no one else
    sim = build_sim(sim_pars(sim=dict(TESTLAND_SIM, n_agents=5000), country=TESTLAND))
    sim.run(verbose=0)
    men = sim.people.male & sim.people.alive
    age = sim.people.age
    circumcised = sim.diseases.hiv.circumcised
    assert np.mean(circumcised[men & (age >= 15) & (age < 20)]) == pytest.approx(0.8, abs=0.12)
    assert np.mean(circumcised[men & (age >= 30) & (age < 35)]) < 0.05


@pytest.mark.parametrize("name, levels", [
    ("hiv_test_fsw", {1990: 0.0, 2005: 0.375, 2020: 0.75, 2030: 0.8, 2040: 0.85}),
    ("hiv_test_general", {1990: 0.0, 2005: 0.25, 2020: 0.5, 2030: 0.55, 2040: 0.6}),
    ("hiv_test_low_cd4", {1990: 0.0, 2005: 0.425, 2020: 0.85, 2030: 0.9, 2040: 0.95}),
])
def test_country_testing_streams_ramp(name, levels):
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND))
    sim.init(verbose=0)
    stream = hiv_tests(sim)[name]
    for year, level in levels.items():
        assert np.interp(year, stream.years, stream.test_prob_data) == pytest.approx(level)


def test_country_attaches_four_testing_streams():
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND))
    sim.init(verbose=0)
    tests = hiv_tests(sim)
    assert list(tests) == STREAMS
    anc = tests["hiv_test_anc"]
    assert anc.test_prob_data == 0.9
    assert anc.pars.dt_scale is False


def eligible(sim, name):
    found = hiv_tests(sim)[name].eligibility(sim)
    return set(getattr(found, "uids", found).tolist())


def test_country_testing_streams_select_the_undiagnosed():
    # about 1 in 1000 testland agents is an active sex worker, and the test needs three
    sim = build_sim(sim_pars(sim=dict(TESTLAND_SIM, n_agents=10_000), country=TESTLAND))
    sim.init(verbose=0)
    hiv = sim.diseases.hiv
    fsw = sim.networks.structuredsexual.fsw
    agents = dict(
        fsw_new=dict(fsw=True),
        fsw_diagnosed=dict(fsw=True, diagnosed=True),
        fsw_on_art=dict(fsw=True, on_art=True),
        other_new=dict(),
        other_on_art=dict(on_art=True),
        low_cd4_on_art=dict(cd4=150, on_art=True),
        low_cd4_diagnosed=dict(cd4=150, diagnosed=True),
    )
    # sex work status derives from age and the network's draws, so agents are
    # picked by their status
    pool = {True: fsw.uids.tolist(), False: (~fsw & sim.people.alive).uids.tolist()}
    uid = {name: pool[state.get("fsw", False)].pop() for name, state in agents.items()}
    for name, state in agents.items():
        u = uid[name]
        hiv.diagnosed[u] = state.get("diagnosed", False)
        hiv.on_art[u] = state.get("on_art", False)
        hiv.cd4[u] = state.get("cd4", 800)

    expected = dict(
        hiv_test_fsw={"fsw_new"},
        hiv_test_general={"other_new"},
        hiv_test_low_cd4={"low_cd4_on_art"},
    )
    for stream, members in expected.items():
        assert {a for a in agents if uid[a] in eligible(sim, stream)} == members, stream


def test_country_antenatal_stream_selects_undiagnosed_pregnant_women():
    # testland has no births, so this uses Zimbabwe's fertility
    sim = build_sim(sim_pars(sim=dict(n_agents=2000, start=1985, stop=1985.5), country=dict(name="zimbabwe")))
    sim.run(verbose=0)
    pregnancy = sim.demographics.pregnancy
    first = eligible(sim, "hiv_test_anc")
    assert first
    assert first <= set(pregnancy.pregnant.uids.tolist())
    one = next(iter(first))
    sim.diseases.hiv.diagnosed[one] = True
    assert eligible(sim, "hiv_test_anc") == first - {one}


def test_behavioral_prep_screens_at_every_country_testing_stream():
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND, prep=dict(eligibility="behavioral")))
    sim.init(verbose=0)
    agents = sim.people.auids[:len(STREAMS)]
    for name, uid in zip(STREAMS, agents):
        sim.interventions[name].ti_tested[uid] = sim.ti
    contacts = sim.interventions.behavioral_screen.contacts(sim)
    assert set(contacts.tolist()) == set(agents.tolist())


@pytest.mark.parametrize("programme", ["art", "vmmc"])
def test_country_rejects_coverage_tables_in_counts(programme, tmp_path):
    for path in TESTLAND["datafolder"].glob("testland_*.csv"):
        shutil.copy(path, tmp_path)
    table = tmp_path / f"testland_{programme}_coverage.csv"
    rows = pd.read_csv(table)
    rows[f"n_{programme}"] = 5000
    rows.drop(columns=f"p_{programme}").to_csv(table, index=False)
    with pytest.raises(ValueError, match=f"p_{programme}"):
        build_sim(sim_pars(sim=TESTLAND_SIM, country=dict(TESTLAND, datafolder=tmp_path)))


@pytest.mark.parametrize("programme", ["art", "vmmc"])
def test_country_coverage_override_in_proportions_replaces_its_table(programme):
    sim = build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND, **{programme: dict(coverage=0.37)}))
    sim.init(verbose=0)
    module = sim.interventions[programme]
    assert module.coverage_format == "p"
    assert np.all(module.coverage == 0.37)


@pytest.mark.parametrize("override", [
    dict(art=dict(coverage=50_000)),
    dict(art=dict(coverage=dict(year=[2000, 2020], value=[10_000, 80_000]))),
    dict(vmmc=dict(coverage=dict(year=[2000, 2020], value=[0, 50_000]))),
])
def test_country_rejects_coverage_overrides_in_counts(override):
    with pytest.raises(ValueError, match="proportion"):
        build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND, **override))


def test_country_rejects_hiv_test_override():
    with pytest.raises(ValueError, match="country"):
        build_sim(sim_pars(sim=TESTLAND_SIM, country=TESTLAND, hiv_test=dict(test_prob_data=0.5)))


@pytest.mark.parametrize("name", ["eswatini", "zimbabwe"])
def test_real_country_tables_pass_the_proportion_check(name):
    build_sim(sim_pars(country=dict(name=name)))


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
