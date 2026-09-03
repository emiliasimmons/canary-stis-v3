"""
HIV-STI coinfection connectors.

Two upstream traps are worked around here.

The connectors must be passed to sti.Sim explicitly: its auto-wiring guards on
``len(sc.tolist(self.pars['connectors'])) > 0`` with an empty ``ss.ndict``
default that sc.tolist wraps rather than flattens, so the guard always fires and
no connector is ever added.

And stisim's connectors take their targets as constructor arguments and hold
those references for the run, which does not survive sim construction: the sim
copies the modules it is given, so the objects the connector holds are orphans of
the ones actually simulated. The subclasses below rebind their targets by name
once the sim exists.
"""

import starsim as ss
import stisim as sti

# hiv_bv keys on BV.cst4, which SimpleBV does not define, so it is not in
# stisim's __all__. Import defensively: without it, the BV->HIV coupling is
# simply omitted rather than breaking construction.
try:
    from stisim.connectors.hiv_sti import hiv_simplebv
except ImportError:
    hiv_simplebv = None

__all__ = ["HIVSTICofactor", "make_connectors"]


class ResolveModules:
    """
    Rebind a connector's module references to the sim's own instances.

    Mixed in ahead of the connector class so this init_pre runs first. Reads the
    name off whatever instance was passed to the constructor and looks that name
    up in sim.diseases, so a connector can be built before the sim exists and
    still point at the live modules afterwards.
    """

    module_attrs = ()

    def init_pre(self, sim):
        super().init_pre(sim)
        for attr in self.module_attrs:
            mod = getattr(self, attr, None)
            if mod is not None:
                setattr(self, attr, sim.diseases[mod.name])
        return


class HIVNg(ResolveModules, sti.hiv_ng):
    module_attrs = ("hiv", "ng")


class HIVCt(ResolveModules, sti.hiv_ct):
    module_attrs = ("hiv", "ct")


class HIVTv(ResolveModules, sti.hiv_tv):
    module_attrs = ("hiv", "tv")


class HIVSyph(ResolveModules, sti.hiv_syph):
    module_attrs = ("hiv", "syphilis")


if hiv_simplebv is not None:
    class HIVBv(ResolveModules, hiv_simplebv):
        module_attrs = ("hiv", "bv")
else:
    HIVBv = None


class HIVSTICofactor(ResolveModules, ss.Connector):
    """
    Raise STI susceptibility in agents with HIV, keyed on CD4.

    stisim carries the STI-to-HIV direction for gonorrhea, chlamydia and
    trichomoniasis (hiv_ng, hiv_ct, hiv_tv all write only hiv.rel_sus and
    hiv.rel_trans); hiv_syph is the sole connector that also runs the reverse
    direction. This supplies the reverse direction for the SEIS diseases, using
    the same two CD4 thresholds hiv_syph uses: one multiplier below 500 and a
    further one below 200.

    Both multipliers default to 1, so attaching this changes nothing until a
    value is set: the sexual network already generates part of the observed
    HIV-STI association through shared risk-group membership, so setting a
    multiplier to an observed prevalence ratio would count that contribution
    twice. This is the lever for whatever residual association the network does
    not reproduce.
    """

    module_attrs = ("hiv",)

    def __init__(self, hiv_module, sti_modules, pars=None, **kwargs):
        super().__init__()
        self.hiv = hiv_module
        self.stis = list(sti_modules)
        self.define_pars(
            rel_sus_hiv=1.0,
            rel_sus_aids=1.0,
        )
        self.update_pars(pars, **kwargs)
        return

    def init_pre(self, sim):
        super().init_pre(sim)
        self.stis = [sim.diseases[m.name] for m in self.stis]
        return

    def step(self):
        # cd4 is NaN for agents HIV has never touched, and NaN comparisons are
        # False, so both masks select only people with a CD4 trajectory
        hiv_pos = self.hiv.cd4 < 500
        aids = self.hiv.cd4 < 200
        for dis in self.stis:
            dis.rel_sus[hiv_pos] *= self.pars.rel_sus_hiv
            dis.rel_sus[aids] *= self.pars.rel_sus_aids
        return


def make_connectors(hiv, ng=None, ct=None, syph=None, tv=None, bv=None, pars=None):
    """
    Build the HIV-STI connector list for whichever diseases are present.

    Returns an empty list when ``hiv`` is None. ``pars`` is a nested dict of
    per-connector overrides keyed ``hiv_ng``, ``hiv_ct``, ``hiv_tv``,
    ``hiv_bv``, ``hiv_syph``, ``cofactor`` (see sim_pars().connectors).
    """
    if hiv is None:
        return []

    pars = pars or {}
    connectors = []

    if ng is not None:
        connectors.append(HIVNg(hiv, ng, **dict(pars.get("hiv_ng", {}))))
    if ct is not None:
        connectors.append(HIVCt(hiv, ct, **dict(pars.get("hiv_ct", {}))))
    if tv is not None:
        connectors.append(HIVTv(hiv, tv, **dict(pars.get("hiv_tv", {}))))
    if bv is not None and HIVBv is not None:
        connectors.append(HIVBv(hiv, bv, **dict(pars.get("hiv_bv", {}))))
    if syph is not None:
        connectors.append(HIVSyph(hiv, syph, **dict(pars.get("hiv_syph", {}))))

    targets = [m for m in (ng, ct, tv) if m is not None]
    if targets:
        connectors.append(HIVSTICofactor(hiv, targets, **dict(pars.get("cofactor", {}))))

    return connectors
