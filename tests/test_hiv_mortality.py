"""HIV deaths removed from all-cause mortality by interpolating between AIDS-free years."""

import pandas as pd
import pytest

from scripts.remove_hiv_mortality import remove_hiv_deaths


def rates(rows):
    return pd.DataFrame(rows, columns=["Time", "Sex", "AgeStart", "Value"])


def test_aids_hump_replaced_by_geometric_interpolation():
    all_cause = rates([
        (1985, "Female", 30, 0.01),
        (2005, "Female", 30, 0.05),
        (2025, "Female", 30, 0.0025),
        (2030, "Female", 30, 0.002),
        (1985, "Male", 0, 0.02),
        (2005, "Male", 0, 0.004),
        (2025, "Male", 0, 0.01),
        (2030, "Male", 0, 0.008),
    ])
    out = remove_hiv_deaths(all_cause).set_index(["Time", "Sex", "AgeStart"]).Value
    # halfway between 0.01 and 0.0025 on a log scale is their geometric mean, 0.005
    assert out[2005, "Female", 30] == pytest.approx(0.005)
    # below its interpolated 0.01414, so nothing there is attributed to AIDS
    assert out[2005, "Male", 0] == pytest.approx(0.004)
    for year in (1985, 2025, 2030):
        for sex, age in (("Female", 30), ("Male", 0)):
            assert out[year, sex, age] == all_cause.set_index(["Time", "Sex", "AgeStart"]).Value[year, sex, age]
