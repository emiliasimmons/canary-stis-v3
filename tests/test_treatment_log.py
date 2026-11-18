"""Treatment log: every STI treatment with the treated person's true infection status."""

import pytest

from src.sim import build_sim, sim_pars

STIS = ["ng", "ct", "tv", "syph"]
SMALL = dict(sim=dict(n_agents=2000, start=2010, dur=2))
# no NG, CT, TV or syphilis is ever seeded, so BV alone sends women to syndromic care
NO_STI = dict(
    ng=dict(init_prev=0.0), ct=dict(init_prev=0.0), tv=dict(init_prev=0.0),
    syph=dict(init_prev=0.0), syph_latent=dict(init_prev=None),
)


def treatment_log(**overrides):
    sim = build_sim(sim_pars(**{**SMALL, **overrides}))
    sim.run(verbose=0)
    return sim.interventions.treatment_log.to_df()


def test_syndromic_treatment_without_sti_records_all_statuses_false():
    log = treatment_log(**NO_STI)
    syndromic = log[log.channel.str.contains("syndromic")]
    assert len(syndromic) > 0
    assert not syndromic[STIS].any().any()


SYMPTOMS = [f"{d}_symptomatic" for d in STIS]


def test_syndromic_treatment_without_sti_records_no_symptoms():
    log = treatment_log(**NO_STI)
    assert not log[SYMPTOMS].any().any()


def test_panel_treats_symptomatic_and_asymptomatic_infections():
    perfect = dict(ng=[1.0, 1.0], ct=[1.0, 1.0], tv=[1.0, 1.0])
    log = treatment_log(intv_year=2010, poc=dict(sens=perfect, spec=perfect))
    panel = log[log.channel == "panel"]
    for d in ["ng", "ct", "tv"]:
        infected = panel[panel[d]]
        assert infected[f"{d}_symptomatic"].any() and not infected[f"{d}_symptomatic"].all(), d
        assert not (panel[f"{d}_symptomatic"] & ~panel[d]).any(), d


def test_perfect_panel_treats_exactly_the_recorded_infections():
    perfect = dict(ng=[1.0, 1.0], ct=[1.0, 1.0], tv=[1.0, 1.0])
    log = treatment_log(intv_year=2010, poc=dict(sens=perfect, spec=perfect))
    panel = log[log.channel == "panel"]
    drugs = panel.groupby(["year", "uid"]).drug.agg(set)
    status = panel.groupby(["year", "uid"])[["ng", "ct", "tv"]].first()
    assert len(status) > 0
    for disease, drug in [("ng", "ng_tx"), ("ct", "ct_tx"), ("tv", "metronidazole")]:
        given = drugs.apply(lambda d: drug in d)
        assert given.any() and (status[disease] == given).all(), disease


# syphilis common and every presentation tested; the antenatal test moves from
# RPR to the dual RDT a year in, so both antenatal products treat. No
# non-syphilitic ulcers, so every ulcer presentation is a syphilitic chancre.
SYPH = dict(
    rdt_year=2011,
    gudp=dict(prevalence=0.0),
    syph=dict(init_prev=0.05),
    syph_latent=dict(init_prev=0.2),
    syph_test=dict(symp_test_prob=1.0),
)


@pytest.mark.parametrize("intv_year, channels", [
    (None, {"syph_symp_test", "syph_rash_test", "syph_anc_rpr", "syph_anc_rdt"}),
    (2010, {"syph_symp_test_poc", "syph_rash_test", "syph_anc_rpr", "syph_anc_confirm"}),
], ids=["soc", "poc"])
def test_every_syphilis_channel_logs_its_treatments(intv_year, channels):
    log = treatment_log(intv_year=intv_year, **SYPH)
    syph = log[log.drug == "syph_tx"]
    assert channels <= set(syph.channel.str.split("+").explode())
    visible = syph[syph.channel.str.contains("syph_symp_test|syph_rash_test")]
    assert len(visible) > 0 and visible.syph.all()
    # the ulcer and rash tests reach only visible symptoms; antenatal screening
    # also finds latent syphilis
    assert visible.syph_symptomatic.all()
    antenatal_only = syph[~syph.channel.str.contains("syph_symp_test|syph_rash_test")]
    assert (antenatal_only.syph & ~antenatal_only.syph_symptomatic).any()
