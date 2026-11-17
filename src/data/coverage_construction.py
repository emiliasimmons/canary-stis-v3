"""Build the Zimbabwe ART and VMMC coverage tables and both countries' viral suppression.

Run `uv run python src/data/coverage_construction.py` from the repository root.

Every value is transcribed from a numbered table in a survey report or a named
column in the UNAIDS estimates workbook. Sources sit under `docs/raw/` and are
cataloged in `docs/pages/`:

- ZIMPHIA 2015-16 final report (fieldwork Oct 2015 - Aug 2016), labelled 2016
- ZIMPHIA 2020 final report, Sept 2023 revision (fieldwork Nov 2019 - Mar 2020), labelled 2020
- Zimbabwe DHS 2005-06 and 2010-11, DHS Program API indicator HA_MCRC_M_MCC
- UNAIDS 2026 estimates, HIV-Test-&-Treat_ByArea sheet
- SHIMS3 2021 final report (Eswatini); SHIMS2 2016-17 values as transcribed by
  hivsim_eswatini's `vls_construction.py`, since the SHIMS2 report is not on disk

Sex follows stisim's convention: Gender 0 = female, 1 = male. Age bins are
half-open, matching Eswatini's `art_coverage.csv` and `vmmc_coverage.csv`.
"""

import csv
from pathlib import Path

OUT = Path(__file__).parent
F, M = 0, 1
ART_BINS = ["[15,25)", "[25,35)", "[35,45)", "[45,100)"]
VMMC_BINS = ["[10,15)", "[15,20)", "[20,25)", "[25,30)", "[30,35)", "[35,40)",
             "[40,45)", "[45,50)", "[50,55)", "[55,60)", "[60,65)"]

# ZIMPHIA 2015-16 Table 10.3.B, biomarker-adjusted (self-report or detectable
# ARVs). (diagnosed %, on ART among diagnosed %) for 15-24, 25-34, 35-49, 15-64.
# The product is ART coverage among all PLHIV, the basis Eswatini's table uses.
# 35-49 fills the [35,45) bin, as in Eswatini's table.
Z16_CASCADE = {
    M: [(64.5, 82.6), (56.6, 80.5), (76.4, 87.3), (72.1, 88.0)],
    F: [(58.2, 89.3), (75.8, 82.7), (88.1, 90.1), (80.1, 88.6)],
}
# Table 10.3.B stops at 35-49, so the [45,100) bin comes from Table 8.3.A/B
# (self-reported on ART, 5-year bands): ages 50-64 as (on ART %, n unweighted),
# then (self-reported on ART % at 15-64). 50-64 rather than 45-64 so that 2016
# and 2020's [45,100) bins both describe ages 50+.
Z16_SELF_50_64 = {
    M: [(74.4, 117), (70.1, 96), (84.4, 70)],
    F: [(85.4, 160), (83.7, 133), (68.9, 77)],
}
Z16_SELF_15_64 = {M: 58.9, F: 66.4}

# ZIMPHIA 2020 Table 9.1.A, percentage on ART among all PLHIV (biomarker-
# adjusted), for 15-24, 25-34, 35-49, 50+.
Z20_ART = {M: [68.8, 58.0, 84.4, 90.1], F: [73.4, 79.7, 89.5, 92.5]}

# UNAIDS 2026 estimates, percentage of PLHIV 15+ on ART, 2010 (the first year
# the workbook reports coverage). Supplies the level between 2004 and 2016.
UNAIDS_2010_ART = {M: 24, F: 31}


def zimphia_2016_art(sex):
    cells = [d * t / 1e4 for d, t in Z16_CASCADE[sex]]
    by_age, total = cells[:3], cells[3]
    rows = Z16_SELF_50_64[sex]
    self_50_64 = sum(p * n for p, n in rows) / sum(n for _, n in rows) / 100
    # scale self-report to the biomarker basis with this sex's 15-64 ratio,
    # because detectable ARVs reclassify some self-reported untreated as treated
    older = self_50_64 * total / (Z16_SELF_15_64[sex] / 100)
    return by_age + [older], total


def zimbabwe_art():
    table = {}
    for sex in (F, M):
        z16, z16_total = zimphia_2016_art(sex)
        # 2010 has only a national 15+ level, so it takes 2016's age pattern
        table[(2004, sex)] = [0.0] * 4
        table[(2010, sex)] = [min(1.0, UNAIDS_2010_ART[sex] / 100 * c / z16_total) for c in z16]
        table[(2016, sex)] = z16
        table[(2020, sex)] = [p / 100 for p in Z20_ART[sex]]
    return [dict(Year=y, Gender=s, AgeBin=b, p_art=round(v, 4))
            for (y, s), vals in sorted(table.items()) for b, v in zip(ART_BINS, vals)]


# Proportion of men circumcised by any provider, 5-year bands 15-19 to 60-64.
# Medical and non-medical circumcision both protect, and the 2005 and 2010 DHS
# report only "circumcised", so the total is the comparable quantity across
# surveys. ZIMPHIA 2015-16 Table 15.5.A total 15-49 (12.4 + 1.9 = 14.3%) matches
# ZDHS 2015's 14.3%, so the two instruments agree where they overlap.
VMMC_SURVEYS = {
    # ZDHS 2005-06, HA_MCRC_M_MCC; men's survey stops at 54
    2005: [7.9, 10.6, 12.5, 12.8, 8.8, 11.3, 10.3, 14.4],
    # ZDHS 2010-11, HA_MCRC_M_MCC
    2010: [5.3, 8.1, 10.6, 10.2, 12.3, 10.1, 13.6, 10.8],
    # ZIMPHIA 2015-16 Table 15.5.A, medical + non-medical
    2016: [22.9 + 0.7, 15.8 + 1.8, 10.1 + 1.7, 6.0 + 1.8, 6.1 + 2.0, 6.3 + 2.9,
           5.8 + 5.1, 9.2 + 5.1, 4.9 + 4.5, 2.6 + 7.5],
    # ZIMPHIA 2020 Table 12.5, medical + non-medical
    2020: [37.4 + 1.2, 30.8 + 1.4, 15.4 + 2.7, 11.8 + 4.8, 12.7 + 5.3, 10.7 + 4.4,
           7.3 + 7.4, 8.1 + 5.0, 7.5 + 7.9, 4.2 + 6.9],
}


def zimbabwe_vmmc():
    table = {}
    for year, vals in VMMC_SURVEYS.items():
        vals = [v / 100 for v in vals]
        # no survey covers 55-64 before 2016: carry the 50-54 value
        vals += [vals[-1]] * (10 - len(vals))
        # no survey interviews boys 10-14: carry the 15-19 value
        table[year] = [vals[0]] + vals
    # the national VMMC programme began in 2009, so 2005 is taken as the
    # pre-programme level back to 1990
    table[1990] = table[2005]
    return [dict(Year=y, Gender=M, AgeBin=b, p_vmmc=round(v, 4), lb="", ub="")
            for y, vals in sorted(table.items()) for b, v in zip(VMMC_BINS, vals)]


# Viral suppression (<1,000 copies/mL) among people on ART, adults, by sex.
# The surveys report it by age too; the table has one [15,100) bin so both
# countries share Eswatini's shape.
VLS = {
    "zimbabwe": {
        2016: {M: 82.5, F: 87.0},  # ZIMPHIA 2015-16 Table 10.3.B, ages 15-64
        2020: {M: 89.0, F: 91.0},  # ZIMPHIA 2020 Table 9.1.B, ages 15+
    },
    "eswatini": {
        2016: {M: 90.5, F: 91.8},  # SHIMS2 Table 10.3.B, 15+, via vls_construction.py
        2021: {M: 96.7, F: 95.9},  # SHIMS3 Table 9.1.B, 15+
    },
}


def vls(country):
    return [dict(Year=y, Gender=s, AgeBin="[15,100)", p_vls=round(by_sex[s] / 100, 4))
            for y, by_sex in sorted(VLS[country].items()) for s in (F, M)]


def write(name, rows):
    with open(OUT / name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {name}: {len(rows)} rows")


if __name__ == "__main__":
    art = zimbabwe_art()
    assert all(0 <= r["p_art"] <= 1 for r in art)
    write("zimbabwe_art_coverage.csv", art)
    write("zimbabwe_vmmc_coverage.csv", zimbabwe_vmmc())
    write("zimbabwe_vls.csv", vls("zimbabwe"))
    write("eswatini_vls.csv", vls("eswatini"))
