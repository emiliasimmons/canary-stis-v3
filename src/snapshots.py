"""
Arms continued from one simulation stopped at the start of their intervention year.

``snapshot(arms, year)`` builds one simulation carrying every module any of the arms
attaches, each held off past the run's end, and runs it up to ``year``.
``continue_as(snapshot, pars)`` copies it and sets the copy to one arm: modules the arm's
own build lacks are removed, and the settings ``build_sim`` gives the arm's modules are
copied over. The arms must agree on every sim_pars group outside ``SWITCHES``, and every
switch an arm turns on must start at or after ``year``, so that before it all arms run
the same simulation. Modules are present from the start because some draw per-person
states at birth (PrEP willingness), which a module added in ``year`` would draw
differently.
"""

import numpy as np
import pandas as pd
import sciris as sc

from .sim import SOC_LEVER_START, build_sim

# sim_pars groups the arms may set differently
SWITCHES = ("intv_year", "pn", "prep", "sti_screening", "magic_cure", "anc")

# settings build_sim derives from the switches, read by the modules on every step
STEP_ATTRS = dict(
    syndromic_vds=["eligibility"],
    syndromic_uds=["eligibility"],
    panel=["eligibility"],
    syph_symp_test=["stop"],
    syph_symp_test_poc=["start"],
    syph_anc_confirm=["start"],
    syph_pn_test=["start"],
    syph_anc_rpr=["start"],
    syph_anc_rdt=["start"],
    hiv_test_anc=["start"],
    syph_tx=["eligibility"],
    pn=["eligibility"],
    sti_screening=["contacts", "include_men"],
    magic_cure=["cure_year"],
    prep=["eligibility", "coverage", "coverage_format", "age_bins", "sex_keys"],
)
# probabilities of initialised distributions, set in place so their random streams stay
DIST_PROBS = dict(pn=["p_notify_current", "p_attends_current"], sti_screening=["acceptance"])
PLAIN_PARS = dict(prep=["prep_eff", "prep_dur", "prep_adh"])


def _equal(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_equal(a[k], b[k]) for k in a)
    frames = (pd.DataFrame, pd.Series)
    if isinstance(a, frames) or isinstance(b, frames):
        return type(a) is type(b) and a.equals(b)
    if isinstance(a, (list, tuple, np.ndarray)) and isinstance(b, (list, tuple, np.ndarray)):
        return len(a) == len(b) and all(_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, float) and isinstance(b, float) and np.isnan(a) and np.isnan(b):
        return True
    return a is b or a == b


def _unsupported(pars):
    """Levers whose start follows intv_year, which snapshots leave out."""
    mult = pars.care_seek_mult
    return [name for name, on in (
        ("care_seek_mult", not isinstance(mult, (int, float)) or float(mult) != 1.0),
        ("bundled_prevention", pars.bundled_prevention is not None),
        ("fsw_outreach", pars.fsw_outreach.rate > 0),
        ("behavioral PrEP", pars.prep.eligibility == "behavioral"),
    ) if on]


def _switch_years(pars, anc_differs):
    """The year each switch an arm turns on first acts in."""
    intv = pars.intv_year
    years = dict(intv_year=intv, magic_cure=pars.magic_cure.year)
    if pars.pn is not None:
        years["pn"] = intv
    if pars.sti_screening is not None:
        years["sti_screening"] = intv
    if pars.prep.eligibility != "none":
        lever_start = intv if intv is not None else SOC_LEVER_START
        years["prep"] = pars.prep.start if pars.prep.start is not None else lever_start
    if anc_differs:
        years["anc"] = pars.sim.start if pars.anc.start is None else pars.anc.start
    return {k: y for k, y in years.items() if y is not None and np.isfinite(y)}


def _check(arms, year):
    for pars in arms:
        unsupported = _unsupported(pars)
        if unsupported:
            raise ValueError(f"snapshots do not support {', '.join(unsupported)}: "
                             "its start follows intv_year, which the arms set")
    first = arms[0]
    for group in first:
        if group not in SWITCHES and not all(_equal(pars[group], first[group]) for pars in arms):
            raise ValueError(f"arms continued from one snapshot must share sim_pars group '{group}'")
    anc_differs = not all(_equal(pars.anc, first.anc) for pars in arms)
    for pars in arms:
        for switch, start in _switch_years(pars, anc_differs).items():
            if start < year:
                raise ValueError(f"{switch} acts from {start} in an arm, before the snapshot year {year}")


def _snapshot_pars(arms):
    """The arms' first pars with every switch any arm turns on attached and held off."""
    pars = sc.dcp(arms[0])
    never = pars.sim.stop + 1
    pars.intv_year = never if any(a.intv_year is not None for a in arms) else None
    pars.pn = next((a.pn for a in arms if a.pn is not None), None)
    pars.sti_screening = next((a.sti_screening for a in arms if a.sti_screening is not None), None)
    prep = next((a.prep for a in arms if a.prep.eligibility != "none"), None)
    if prep is not None:
        pars.prep = sc.objdict(sc.dcp(prep), start=never)
    pars.magic_cure.year = never if any(a.magic_cure.year is not None for a in arms) else None
    if not all(_equal(a.anc, pars.anc) for a in arms):
        pars.anc.start = never
    return pars


def snapshot(arms, year):
    """One simulation for all arms (sim_pars), run to the start of year."""
    arms = list(arms)
    _check(arms, year)
    sim = build_sim(_snapshot_pars(arms))
    sim.init(verbose=0)
    ti = np.flatnonzero(np.isclose(sim.t.yearvec, year))
    if len(ti) != 1 or ti[0] == 0:
        raise ValueError(f"the snapshot year {year} must start a step after the first")
    sim.run(until=sim.t.tvec[ti[0] - 1], verbose=0)
    sim.metadata.arms = sc.dcp(arms)
    sim.metadata.random_state = np.random.get_state()
    return sim


def _restore_random_state(sim):
    # stisim's partner matching draws from NumPy's global random state, which
    # building or running any other sim moves on
    np.random.set_state(sim.metadata.random_state)


def _prune(sim, arm):
    """Remove the interventions, products and results the arm's own build lacks."""
    for name in [name for name in sim.interventions if name not in arm.interventions]:
        del sim.interventions[name]
        sim.pars.interventions.pop(name, None)
    for name in [name for name in sim.results if name not in arm.results]:
        del sim.results[name]
    if [m.name for m in sim.modules] != [m.name for m in arm.modules]:
        raise RuntimeError("the continued simulation's modules differ from the arm's own build")


def _replan(sim):
    """Rebuild the loop over the remaining modules, restoring the random state first."""
    loop = sim.loop
    ti = loop.plan[loop.index].ti
    if loop.index > 0 and loop.plan[loop.index - 1].ti == ti:
        raise RuntimeError("the snapshot stopped partway through a step")
    loop.init()
    loop.insert(_restore_random_state, match_fn=lambda plan: (plan.ti == ti) & (plan.func_order == 0),
                before=True)
    loop.index = next(i for i, entry in enumerate(loop.plan) if entry.ti == ti)


def _configure(sim, arm):
    """Copy the settings the arm's own build gives its modules."""
    for name, attrs in STEP_ATTRS.items():
        if name in arm.interventions:
            for attr in attrs:
                setattr(sim.interventions[name], attr, getattr(arm.interventions[name], attr))
    for name, keys in DIST_PROBS.items():
        if name in arm.interventions:
            for key in keys:
                sim.interventions[name].pars[key].set(p=arm.interventions[name].pars[key].pars.p)
    for name, keys in PLAIN_PARS.items():
        if name in arm.interventions:
            for key in keys:
                sim.interventions[name].pars[key] = arm.interventions[name].pars[key]
    sim.analyzers.cascade_tracker._prep = sim.interventions.get("prep")
    sim.metadata = sc.objdict(pars=arm.metadata.pars, random_state=sim.metadata.random_state)
    # catches a start or stop build_sim sets from a switch that STEP_ATTRS misses
    for name, intv in sim.interventions.items():
        for attr in ("start", "stop", "cure_year"):
            if not _equal(getattr(intv, attr, None), getattr(arm.interventions[name], attr, None)):
                raise RuntimeError(f"{name}.{attr} differs from the arm's own build; add it to STEP_ATTRS")


def continue_as(snapshot, pars):
    """A copy of the snapshot set to the arm pars, one of those it was built for, ready to run."""
    if "arms" not in snapshot.metadata:
        raise ValueError("continue_as takes a simulation made by snapshot()")
    if not any(_equal(pars, arm) for arm in snapshot.metadata.arms):
        raise ValueError("pars are not among the arms the snapshot was built for")
    arm = build_sim(pars)
    arm.init(verbose=0)
    sim = snapshot.copy()
    _prune(sim, arm)
    _configure(sim, arm)
    _replan(sim)
    return sim


def run_arms(arms, year):
    """Run each arm (name: sim_pars) from one snapshot at year, yielding (name, sim) as each finishes."""
    snap = snapshot(arms.values(), year)
    for name, pars in arms.items():
        yield name, continue_as(snap, pars).run(verbose=0)
