"""
Simulation builder for canary-stis.

HIV + four curable bacterial STIs (NG, CT, syphilis, TV) plus BV on a shared
structured sexual network. ``sim_pars()`` returns a nested ``sc.objdict`` grouped
by subsystem; ``build_sim(pars)`` constructs (does not run) the sim.

Diagnostic arm is selected by ``pars.intv_year``: ``None`` runs syndromic
standard-of-care for the whole simulation, a year switches the NG/CT/TV and
syphilis pathways to the POC etiological arm at that year. Demand-side levers
(care-seeking, bundled prevention, FSW outreach) are off at their identity /
zero values and never gated behind a boolean flag.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import sciris as sc
import starsim as ss
import stisim as sti

from .analyzers import (
    CascadeTracker,
    DemographicSnapshotAnalyzer,
    DiagnosisTracker,
    ExposureTracker,
    HIVTransmissionLogger,
    InfectionTracker,
    NetworkPositionTracker,
    SusceptibilityExposureTracker,
)
from .connectors import make_connectors
from .diagnostics import (
    SyphilisANCTimer,
    gate_poc,
    gate_soc,
    make_syph_tx_eligibility,
    seeking_care_any,
    seeking_care_uds,
    seeking_care_vds,
    syph_anc_confirm_eligibility,
    syph_anc_eligibility,
    syph_rash_eligibility,
    syph_ulcer_eligibility,
    tested_this_step,
    treated_this_step,
)
from .interventions import (
    BehavioralScreen,
    CareSeekScaler,
    CondomCounseling,
    FSWOutreach,
    GonorrheaTx,
    MagicCure,
)

_DATA_DIR = Path(__file__).parent / "data"
_SYPH_DX_PATH = _DATA_DIR / "syph_dx.csv"

# stisim's testing modules default stop to the run's last year and only act
# while now < stop, so they would skip the final step. Syndromic and panel
# modules also empty the shared NG/CT/TV treatment queues on every step from
# stop on.
_NO_STOP = np.inf

# NG/CT/TV treatments the syndromic algorithm assigns by presenting syndrome,
# independent of what the patient carries. Each entry is [female, male];
# tx_mix_cerv applies to women with a cervical infection and to all men,
# tx_mix_noncerv to women without one.
SYNDROMIC_TX_MIX_CERV = dict(
    all3=[0.50, 0.10],
    ngct=[0.20, 0.80],
    mtnz=[0.15, 0.00],
    none=[0.15, 0.10],
)
SYNDROMIC_TX_MIX_NONCERV = dict(
    all3=[0.40, 0.10],
    ngct=[0.10, 0.80],
    mtnz=[0.25, 0.00],
    none=[0.25, 0.10],
)


def latent_seed_frame(init_prev, n_risk_groups=3):
    """One row per risk group, sex and sex-work status, all at the same rate.

    A frame rather than the bare scalar sti.Syphilis also accepts: the scalar
    path skips the sexually-active filter the frame path applies, so it would
    seed latent syphilis into children.
    """
    return pd.DataFrame([
        dict(risk_group=rg, sex=sex, sw=sw, init_prev=init_prev)
        for rg in range(n_risk_groups) for sex in ("female", "male") for sw in (0, 1)
    ])


def as_mask(eligibility):
    """Wrap a uids-returning eligibility as the boolean-array callable sti.Prep documents."""
    def fn(sim):
        return sim.people.alive & eligibility(sim)
    return fn


def _deep_update(base, updates):
    for key, val in updates.items():
        if key in base and isinstance(base[key], dict) and isinstance(val, dict):
            _deep_update(base[key], val)
        else:
            base[key] = val
    return base


def sim_pars(**kwargs):
    """
    Build default simulation parameters; caller overrides are deep-merged.

    Each top-level group maps to a constructor or subsystem::

        pars = sim_pars(ct=dict(init_prev=0.08))
        pars = sim_pars(intv_year=2027)                 # run the POC arm
        pars = sim_pars(care_seek_mult=1.5)             # care-seeking lever
        pars = sim_pars(bundled_prevention=dict(coverage=0.5))
        pars = sim_pars(country=dict(name="eswatini"))  # country demographics

    Off-states are sentinels, not flags: ``intv_year=None`` (SOC throughout),
    ``care_seek_mult=1.0``, ``bundled_prevention=None``,
    ``fsw_outreach.rate=0.0``, ``prep.eligibility='none'``, ``magic_cure.year=None``,
    ``country.name=None`` (scalar birth and death rates).
    """
    pars = sc.objdict()

    pars.sim = sc.objdict(
        n_agents=10_000,
        start=1985,  # the year of the country age structures
        stop=2040,  # 13 years past the 2027 intervention year
        dt=1 / 12,
        rand_seed=0,
        label=None,
    )

    # Diagnostic-arm switchover. None keeps syndromic SOC for the whole run; a
    # year switches NG/CT/TV and syphilis to the POC etiological arm then.
    pars.intv_year = None
    pars.rdt_year = 2012.0  # antenatal syphilis screening moves from RPR to dual RDT

    pars.ng = sc.objdict(beta_m2f=0.10, rel_beta_f2m=0.5, init_prev=0.05)
    pars.ct = sc.objdict(beta_m2f=0.11, rel_beta_f2m=0.5, init_prev=0.04)
    pars.syph = sc.objdict(beta_m2f=0.18, rel_beta_f2m=0.5, init_prev=0.005)
    pars.tv = sc.objdict(beta_m2f=0.09, rel_beta_f2m=0.5, init_prev=0.05)
    pars.hiv = sc.objdict(beta_m2f=0.035, rel_beta_f2m=0.5, init_prev=0.05)

    # Non-syphilitic genital ulcers (HSV-2, chancroid) at a fixed background
    # prevalence. Transmits nothing; widens the pool syndromic ulcer management
    # sees, so presumptive treatment reaches syphilis stages with no chancre.
    # Held at zero by default (visible chancres are then the whole ulcer pool).
    pars.gudp = sc.objdict(prevalence=0.0)

    # Standing latent syphilis reservoir at sim start, on top of syph.init_prev,
    # uniform across risk group, sex and sex-work status. Without it the epidemic
    # is prone to stochastic extinction; the endemic level is unchanged. Set
    # init_prev to None to seed no reservoir.
    pars.syph_latent = sc.objdict(init_prev=0.02)

    pars.ng_tx = sc.objdict(treat_eff=0.95)
    pars.ct_tx = sc.objdict(treat_eff=0.95)
    pars.tv_tx = sc.objdict(treat_eff=0.95)  # metronidazole, covers TV and BV
    pars.syph_tx = sc.objdict()  # sti.SyphTx defaults

    pars.syndromic = sc.objdict(
        tx_mix_cerv=SYNDROMIC_TX_MIX_CERV,
        tx_mix_noncerv=SYNDROMIC_TX_MIX_NONCERV,
    )

    # POC etiological panel accuracy, {disease: [female, male]}.
    pars.poc = sc.objdict(
        sens=dict(ng=[0.95, 0.95], ct=[0.95, 0.95], tv=[0.95, 0.95]),
        spec=dict(ng=[0.95, 0.95], ct=[0.95, 0.95], tv=[0.95, 0.95]),
    )

    pars.syph_test = sc.objdict(symp_test_prob=0.15)  # per presentation, not annualised

    # screen_prob is unconditional ANC coverage per pregnancy. It may instead be
    # a sequence paired with screen_years for a coverage ramp (SyphTest snaps to
    # the nearest listed year). anc_low/high bound the gestational visit week.
    pars.syph_anc = sc.objdict(screen_prob=0.47, screen_years=None,
                               anc_low=8, anc_high=32)

    # Demand-side levers, off at identity / sentinel.
    pars.care_seek_mult = 1.0                 # scalar or [female, male]; CareSeekScaler
    pars.bundled_prevention = None            # dict(coverage=, eff=, dur_months=); CondomCounseling
    pars.fsw_outreach = sc.objdict(rate=0.0, start=None, stop=None)

    pars.hiv_test = sc.objdict(test_prob_data=0.3, start=2000)
    pars.art = sc.objdict(coverage=0.6)
    # Voluntary medical male circumcision. HIV carries eff_circ=0.6 already;
    # this delivers it. coverage is site-specific (sti.VMMC accepts a year-indexed
    # schedule of counts, or a scalar); None runs no VMMC.
    pars.vmmc = sc.objdict(coverage=None)
    # Daily oral PrEP cascade, sti.Prep. Eligibility is who is offered PrEP this
    # step: 'none' (off), 'dx' (STI treatment fired this step, pathway D), or
    # 'behavioral' (qualified on the national eligibility screen at an HIV
    # testing or STI clinic visit this step). From start (None follows
    # lever_start), each step's offered group is topped up until coverage of
    # it is on PrEP, chosen by a fixed per-person willingness score. Offered
    # people already on a course count toward it, so fewer than that start.
    pars.prep = sc.objdict(eligibility="none", start=None, coverage=0.30,
                           dur_months=3, prep_eff=0.8, prep_adh=1.0)
    pars.magic_cure = sc.objdict(year=None)

    pars.connectors = sc.objdict(
        hiv_ng=sc.objdict(),
        # stisim's 1 is a placeholder; 1.2 matches gonorrhoea, the same inflammation
        # pathway (issue #12)
        hiv_ct=sc.objdict(rel_sus_hiv_ct=1.2),
        hiv_tv=sc.objdict(),
        hiv_bv=sc.objdict(),
        hiv_syph=sc.objdict(),
        cofactor=sc.objdict(rel_sus_hiv=1.0, rel_sus_aids=1.0),
    )

    pars.network = sc.objdict(
        prop_f0=0.85,
        prop_m0=0.80,
        prop_f2=0.01,
        prop_m2=0.02,
        f1_conc=0.01,
        m1_conc=0.2,
        f2_conc=0.1,
        m2_conc=0.5,
        condom_data={
            (0, 0): dict(year=[1990], val=[0.07]),
            (0, 1): dict(year=[1990], val=[0.15]),
            (1, 0): dict(year=[1990], val=[0.15]),
            (0, 2): dict(year=[1990], val=[0.20]),
            (2, 0): dict(year=[1990], val=[0.20]),
            (1, 1): dict(year=[1990], val=[0.25]),
            (1, 2): dict(year=[1990], val=[0.30]),
            (2, 1): dict(year=[1990], val=[0.30]),
            (2, 2): dict(year=[1990], val=[0.35]),
            ("fsw", "client"): dict(year=[1990], val=[0.55]),
        },
    )

    # Country setup. name=None runs the scalar pregnancy and deaths rates below;
    # a name loads that country's 1985 age structure, age-specific fertility and
    # mortality from datafolder, in stisim's location-file layout.
    pars.country = sc.objdict(name=None, datafolder=_DATA_DIR)

    # 220 births per 1000 women 15-49 reproduces the SSA aggregate; the coupled
    # fertility_rate=10 / death_rate=10 default drains the sexually active
    # denominator and pulls every prevalence down with it.
    pars.pregnancy = sc.objdict(fertility_rate=220)
    pars.deaths = sc.objdict(death_rate=10)

    for group, updates in kwargs.items():
        if group not in pars:
            raise KeyError(f"Unknown parameter group '{group}'; expected one of {list(pars.keys())}")
        # scalar groups (intv_year, rdt_year, care_seek_mult, bundled_prevention)
        # take the override directly rather than being deep-merged
        if not isinstance(pars[group], dict):
            pars[group] = updates
            continue
        if not isinstance(updates, dict):
            raise TypeError(f"Expected dict for group '{group}', got {type(updates).__name__}")
        _deep_update(pars[group], updates)

    return pars


def _syphilis_pipeline(pars, use_poc, intv_year):
    """Build the syphilis test-and-treat chain.

    Three channels feed one treatment: visible chancres (the genital-ulcer
    presentation), a secondary rash, and antenatal screening. The antenatal
    product changes at rdt_year, from non-treponemal RPR to the treponemal dual
    rapid test. Under POC, the ulcer channel switches to an etiological test at
    intv_year and an RPR confirmation gates ANC treatment.

    Ordering in the returned list is load-bearing: syph_anc_confirm reads
    syph_anc_rdt's positives this timestep, and syph_tx reads every test's, so
    each steps after what it reads.
    """
    dx = pd.read_csv(_SYPH_DX_PATH)

    def product(name, label=None):
        return sti.SyphDx(dx[dx.name == name], name=label or f"syph_dx_{name}")

    timer = SyphilisANCTimer(anc_low=pars.syph_anc.anc_low, anc_high=pars.syph_anc.anc_high)

    # dt_scale=False throughout: probabilities are per presentation or per
    # antenatal visit, not annual rates spread over the year's timesteps.
    symp_test = sti.SyphTest(
        name="syph_symp_test", label="syph_symp_test",
        product=product("syndromic_gud"),
        test_prob_data=pars.syph_test.symp_test_prob,
        eligibility=syph_ulcer_eligibility,
        stop=_NO_STOP,
        dt_scale=False,
    )
    rash_test = sti.SyphTest(
        name="syph_rash_test", label="syph_rash_test",
        product=product("syndromic_rash"),
        test_prob_data=pars.syph_test.symp_test_prob,
        eligibility=syph_rash_eligibility,
        stop=_NO_STOP,
        dt_scale=False,
    )

    # years and the era gates are independent: SyphTest picks the coverage value
    # off years but decides whether to run at all off start/stop, reassigned
    # below. Passing both to the constructor is rejected.
    anc_years = pars.syph_anc.screen_years
    anc_rpr = sti.SyphTest(
        name="syph_anc_rpr", label="syph_anc_rpr",
        product=product("rpr"),
        test_prob_data=pars.syph_anc.screen_prob,
        years=anc_years,
        eligibility=syph_anc_eligibility,
        dt_scale=False,
    )
    anc_rpr.start = None
    anc_rpr.stop = pars.rdt_year
    anc_rdt = sti.SyphTest(
        name="syph_anc_rdt", label="syph_anc_rdt",
        product=product("dual"),
        test_prob_data=pars.syph_anc.screen_prob,
        years=anc_years,
        eligibility=syph_anc_eligibility,
        dt_scale=False,
    )
    anc_rdt.start = pars.rdt_year
    anc_rdt.stop = _NO_STOP

    intvs = [timer, symp_test, rash_test, anc_rpr, anc_rdt]
    treat_tests = ["syph_symp_test", "syph_rash_test", "syph_anc_rpr"]
    confirm_name = None

    if use_poc:
        # the POC ulcer test is etiological, taking over from the presumptive one
        symp_test.stop = intv_year
        symp_test_poc = sti.SyphTest(
            name="syph_symp_test_poc", label="syph_symp_test_poc",
            product=product("gud2"),
            test_prob_data=pars.syph_test.symp_test_prob,
            eligibility=syph_ulcer_eligibility,
            stop=_NO_STOP,
            dt_scale=False,
        )
        symp_test_poc.start = intv_year
        treat_tests.append("syph_symp_test_poc")

        anc_confirm = sti.SyphTest(
            name="syph_anc_confirm", label="syph_anc_confirm",
            product=product("rpr", label="syph_dx_rpr_confirm"),
            test_prob_data=1.0,
            eligibility=syph_anc_confirm_eligibility,
            stop=_NO_STOP,
            dt_scale=False,
        )
        anc_confirm.start = intv_year
        confirm_name = "syph_anc_confirm"
        intvs.extend([symp_test_poc, anc_confirm])

    syph_tx = sti.SyphTx(
        name="syph_tx", label="syph_tx",
        eligibility=make_syph_tx_eligibility(
            treat_tests, screen_only_name="syph_anc_rdt", confirm_name=confirm_name,
        ),
        **pars.syph_tx,
    )
    intvs.append(syph_tx)
    return intvs


def build_sim(pars):
    """Build a canary-stis simulation from parameters. Returns an unrun ss.Sim."""
    use_poc = pars.intv_year is not None
    intv_year = pars.intv_year
    lever_start = intv_year if intv_year is not None else pars.sim.start

    ng = sti.Gonorrhea(**pars.ng)
    ct = sti.Chlamydia(**pars.ct)
    latent_prev = pars.syph_latent.init_prev
    tp = sti.Syphilis(
        init_prev_latent_data=None if latent_prev is None else latent_seed_frame(latent_prev),
        **pars.syph,
    )
    tv = sti.Trichomoniasis(**pars.tv)
    bv = sti.SimpleBV()
    # named 'gudp', not 'gud', so stisim's gud_syph auto-connector cannot match it
    gudp = sti.GUDPlaceholder(name="gudp", **pars.gudp)
    hiv = sti.HIV(**pars.hiv)
    diseases = [ng, ct, tp, tv, bv, gudp, hiv]

    ng_tx = GonorrheaTx(name="ng_tx", base_treat_eff=pars.ng_tx.treat_eff)
    ct_tx = sti.STITreatment(diseases="ct", name="ct_tx",
                             treat_eff=ss.bernoulli(p=pars.ct_tx.treat_eff))
    metronidazole = sti.STITreatment(diseases=["tv", "bv"], name="metronidazole",
                                     treat_eff=ss.bernoulli(p=pars.tv_tx.treat_eff))
    treatments = [ng_tx, ct_tx, metronidazole]

    outcome_tx_map = dict(
        all3=[ng_tx, ct_tx, metronidazole],
        ngct=[ng_tx, ct_tx],
        mtnz=[metronidazole],
        none=[],
    )
    syndromic_pars = dict(
        tx_mix_cerv=pars.syndromic.tx_mix_cerv,
        tx_mix_noncerv=pars.syndromic.tx_mix_noncerv,
    )
    syndromic_vds = sti.SyndromicManagement(
        name="syndromic_vds", label="Syndromic management - VDS",
        diseases=["ng", "ct", "tv", "bv"],
        eligibility=gate_soc(seeking_care_vds, use_poc, intv_year),
        stop=_NO_STOP,
        treatments=[ng_tx, ct_tx, metronidazole],
        outcome_tx_map=outcome_tx_map,
        pars=syndromic_pars,
    )
    syndromic_uds = sti.SyndromicManagement(
        name="syndromic_uds", label="Syndromic management - UDS",
        diseases=["ng", "ct", "tv"],
        eligibility=gate_soc(seeking_care_uds, use_poc, intv_year),
        stop=_NO_STOP,
        treatments=[ng_tx, ct_tx, metronidazole],
        outcome_tx_map=outcome_tx_map,
        pars=syndromic_pars,
    )
    panel = sti.SymptomaticTesting(
        name="panel", label="POC panel",
        diseases=["ng", "ct", "tv"],
        eligibility=gate_poc(seeking_care_any, use_poc, intv_year),
        stop=_NO_STOP,
        treatments=[ng_tx, ct_tx, metronidazole],
        disease_treatment_map={"ng": ng_tx, "ct": ct_tx, "tv": metronidazole},
        pars=dict(sens=dict(pars.poc.sens), spec=dict(pars.poc.spec)),
        negative_treatments=[],
    )

    # Detection modules precede treatment modules so a treatment sees eligibility
    # set this step, not next: SymptomaticTesting/SyndromicManagement enqueue onto
    # the shared treatments, which run immediately after. FSW outreach goes
    # first: once past a user-set stop it empties those queues every step, and
    # would erase the syndromic and panel referrals made earlier in the step.
    detection = [syndromic_vds, syndromic_uds, panel]
    if pars.fsw_outreach.rate > 0:
        fsw_stop = pars.fsw_outreach.stop
        fsw = FSWOutreach(
            coverage_per_step=pars.fsw_outreach.rate,
            name="fsw_outreach", label="fsw_outreach",
            start=pars.fsw_outreach.start if pars.fsw_outreach.start is not None else lever_start,
            stop=fsw_stop if fsw_stop is not None else _NO_STOP,
            diseases=["ng", "ct", "tv"],
            treatments=[ng_tx, ct_tx, metronidazole],
            disease_treatment_map={"ng": ng_tx, "ct": ct_tx, "tv": metronidazole},
            negative_treatments=[],
            pars=dict(sens=dict(pars.poc.sens), spec=dict(pars.poc.spec)),
        )
        detection.insert(0, fsw)

    interventions = detection + treatments
    interventions.extend(_syphilis_pipeline(pars, use_poc, intv_year))

    if not isinstance(pars.care_seek_mult, (int, float)) or float(pars.care_seek_mult) != 1.0:
        interventions.append(CareSeekScaler(mult=pars.care_seek_mult, start=lever_start))

    if pars.bundled_prevention is not None:
        bp = dict(pars.bundled_prevention)
        dur_months = bp.pop("dur_months", 6)
        interventions.append(CondomCounseling(
            start=lever_start, dur=ss.months(dur_months), **bp,
        ))

    prep_start = pars.prep.start if pars.prep.start is not None else lever_start
    screen = prep = None
    if pars.prep.eligibility != "none":
        if pars.prep.eligibility == "dx":
            prep_elig = treated_this_step(["ng_tx", "ct_tx", "metronidazole", "syph_tx"])
        elif pars.prep.eligibility == "behavioral":
            screen = BehavioralScreen(
                contacts=tested_this_step(["hiv_test", "syndromic_vds", "syndromic_uds", "panel",
                                           "syph_symp_test", "syph_rash_test",
                                           "syph_symp_test_poc"]),
                start=prep_start,
            )
            # looked up by name: the sim runs a copy of the screen object built here
            def prep_elig(sim):
                return (sim.interventions.behavioral_screen.ti_qualified == sim.ti).uids
        else:
            raise ValueError(f"unknown prep.eligibility '{pars.prep.eligibility}'")
        # sti.Prep extends the first coverage value back to the sim start, so a
        # zero one step before prep_start keeps PrEP off until then
        prep = sti.Prep(
            name="prep",
            eligibility=as_mask(prep_elig),
            coverage={"year": [prep_start - pars.sim.dt, prep_start],
                      "value": [0, pars.prep.coverage]},
            prep_dur=ss.months(pars.prep.dur_months),
            prep_eff=pars.prep.prep_eff,
            prep_adh=pars.prep.prep_adh,
        )

    magic_cure = (MagicCure(year=pars.magic_cure.year, diseases=[ng, ct, tp, tv])
                  if pars.magic_cure.year is not None else None)

    hiv_test = sti.HIVTest(name="hiv_test", **pars.hiv_test)
    art = sti.ART(**pars.art)
    vmmc = sti.VMMC(coverage=pars.vmmc.coverage) if pars.vmmc.coverage is not None else None

    # the screen reads this step's HIV tests, and PrEP reads the screen
    tail = [magic_cure, hiv_test, screen, prep, art, vmmc]
    interventions.extend(i for i in tail if i is not None)

    connectors = make_connectors(hiv, ng=ng, ct=ct, syph=tp, tv=tv, bv=bv, pars=pars.connectors)

    test_diseases = [ng, ct, tp, tv]
    analyzers = [
        DiagnosisTracker(testing=[panel]),
        InfectionTracker(diseases=test_diseases),
        CascadeTracker(
            diseases=test_diseases, screening=None, prep=prep,
            treatment_map={"ng": "ng_tx", "ct": "ct_tx", "syph": "syph_tx", "tv": "metronidazole"},
        ),
        ExposureTracker(),
        SusceptibilityExposureTracker(),
        NetworkPositionTracker(),
        DemographicSnapshotAnalyzer(),
        HIVTransmissionLogger(),
        ss.infection_log(),
    ]

    if pars.country.name is None:
        demographics = dict(demographics=[ss.Pregnancy(**pars.pregnancy), ss.Deaths(**pars.deaths)])
    else:
        # a location string has stisim build Pregnancy, Deaths and the starting
        # People from the country's files, and sets total_pop from the age
        # structure, which UN WPP counts in people; migration stays at stisim's
        # default, off
        demographics = dict(demographics=pars.country.name, datafolder=pars.country.datafolder)

    # sim settings go in as sim_pars: passed flat, sti.Sim would also route dt
    # to the diseases and reject them for arriving as built modules
    sim = sti.Sim(
        sim_pars=dict(
            n_agents=pars.sim.n_agents,
            start=pars.sim.start,
            stop=pars.sim.stop,
            dt=pars.sim.dt,
            rand_seed=pars.sim.rand_seed,
        ),
        label=pars.sim.label,
        diseases=diseases,
        networks=[sti.StructuredSexual(**pars.network), ss.MaternalNet()],
        interventions=interventions,
        analyzers=analyzers,
        connectors=connectors,
        **demographics,
    )
    sim.metadata = sc.objdict(pars=pars)
    return sim
