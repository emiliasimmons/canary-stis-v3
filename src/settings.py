"""
Simulations for the settings explorations: one draw of the explored parameters
on a country setup, with HIV seeded by risk group.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from .sim import _deep_update, sim_pars

# the reference models' risk-group seeding table, identical in sti_notification
# and hivsim_eswatini
HIV_SEED_PATH = Path(__file__).parent / "data" / "init_prev_hiv.csv"

SELECTION_YEAR = 2026
# simulations end once the selection year is complete
STOP = SELECTION_YEAR + 1

# explored parameter name: (sim_pars group, key)
PARAMETERS = dict(
    prop_f0=("network", "prop_f0"),
    prop_m0=("network", "prop_m0"),
    prop_f2=("network", "prop_f2"),
    prop_m2=("network", "prop_m2"),
    f1_conc=("network", "f1_conc"),
    f2_conc=("network", "f2_conc"),
    m1_conc=("network", "m1_conc"),
    hiv_beta_m2f=("hiv", "beta_m2f"),
    rel_init_prev=("hiv", "rel_init_prev"),
    syph_beta_m2f=("syph", "beta_m2f"),
    ng_beta_m2f=("ng", "beta_m2f"),
    ct_beta_m2f=("ct", "beta_m2f"),
    tv_beta_m2f=("tv", "beta_m2f"),
)


def setting_pars(draw, country, **overrides):
    """sim_pars for one draw on a country setup, ending with 2026.

    draw maps names in PARAMETERS to values. HIV is seeded from the risk-group
    table scaled by rel_init_prev, which replaces the scalar hiv.init_prev.
    overrides are further sim_pars groups, applied last.
    """
    unknown = set(draw) - set(PARAMETERS)
    if unknown:
        raise ValueError(f"unknown explored parameters {sorted(unknown)}; expected names in {list(PARAMETERS)}")
    groups = dict(
        country=dict(name=country),
        sim=dict(stop=STOP),
        hiv=dict(init_prev_data=pd.read_csv(HIV_SEED_PATH)),
    )
    for name, value in draw.items():
        group, key = PARAMETERS[name]
        groups.setdefault(group, {})[key] = value
    return sim_pars(**_deep_update(groups, overrides))


def summarize(sim):
    """One simulation's outcomes through the selection year, as JSON-ready values.

    Prevalence and incidence are at ages 15-49. Each year's HIV prevalence is the
    mean of its monthly values. The prevalence-to-incidence ratio is in years.
    STI prevalence is both sexes pooled.
    """
    year = np.floor(sim.t.yearvec).astype(int)
    years = np.arange(year[0], SELECTION_YEAR + 1)
    monthly = np.asarray(sim.results.hiv.prevalence_15_49)
    hiv_prev = np.array([monthly[year == y].mean() for y in years])

    inc = sim.analyzers.hiv_incidence_15_49.annual()
    inc = inc[inc.year <= SELECTION_YEAR].pivot(index="year", columns="sex", values="incidence")
    pooled = inc["all"]
    inc_now = pooled[SELECTION_YEAR]

    sti = sim.analyzers.sti_prevalence_15_49.annual()
    sti = sti[(sti.year == SELECTION_YEAR) & (sti.sex == "all")].set_index("disease").prevalence

    out = dict(
        hiv_prevalence_2026=float(hiv_prev[-1]),
        hiv_incidence_2026=float(inc_now),
        peak_year=int(pooled.idxmax()),
        prevalence_incidence_ratio_2026=float(100 * hiv_prev[-1] / inc_now) if inc_now > 0 else None,
        years=years.tolist(),
        hiv_prevalence=hiv_prev.tolist(),
        **{f"hiv_incidence_{sex}": inc[sex].tolist() for sex in ("all", "female", "male")},
    )
    out.update({f"{d}_prevalence_2026": float(sti[d]) for d in sti.index})
    return out
