"""Write {country}_deaths.csv, all-cause mortality with HIV deaths removed.

UN WPP mortality includes AIDS deaths. ss.Deaths kills agents regardless of HIV
status and the HIV module kills them again, so the model reads mortality with
the AIDS excess removed. Ported from the Eswatini HIVsim model's
mortality_construction.py, which it accepted after its experiments 016-018.

Per sex and age, rates strictly between 1985 and 2025 are replaced by a
log-linear interpolation of those two years (constant proportional change), and
only where the observed rate is higher: the excess above the line is taken as
AIDS. The assumptions are that 1985 and 2025 are free of AIDS deaths (2025 is
not quite, so slightly too little is removed) and that other mortality moved
smoothly between them. Rates from 2025 on are projections and stay as they are.

Run with ``uv run python scripts/remove_hiv_mortality.py`` after
``scripts/download_wpp.py``.
"""

from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "src" / "data"
COUNTRIES = ("eswatini", "zimbabwe")
BASE_YEAR, END_YEAR = 1985, 2025
KEYS = ["Sex", "AgeStart"]


def remove_hiv_deaths(all_cause, base_year=BASE_YEAR, end_year=END_YEAR):
    df = all_cause.copy()
    lo = df[df.Time == base_year].set_index(KEYS).Value
    hi = df[df.Time == end_year].set_index(KEYS).Value

    mid = df.Time.between(base_year, end_year, inclusive="neither")
    idx = pd.MultiIndex.from_frame(df.loc[mid, KEYS])
    w = ((df.loc[mid, "Time"] - base_year) / (end_year - base_year)).values
    with np.errstate(divide="ignore", invalid="ignore"):
        line = np.exp((1 - w) * np.log(lo.reindex(idx).values) + w * np.log(hi.reindex(idx).values))
    # a zero anchor rate gives no line to compare against, so the rate stays
    line = np.where(np.isfinite(line), line, df.loc[mid, "Value"].values)
    df.loc[mid, "Value"] = np.minimum(df.loc[mid, "Value"].values, line)
    return df


def main():
    for country in COUNTRIES:
        all_cause = pd.read_csv(DATA / f"{country}_deaths_all_cause.csv")
        out = remove_hiv_deaths(all_cause)
        out.to_csv(DATA / f"{country}_deaths.csv", index=False)

        share = 1 - out.Value / all_cause.Value.where(all_cause.Value > 0)
        peak = all_cause.assign(share=share).loc[share.idxmax()]
        print(f"{country}: {(share > 1e-12).sum()} of {len(out)} rows lowered; largest AIDS share "
              f"{peak.share:.0%} ({peak.Sex}, age {peak.AgeStart}, {peak.Time})")


if __name__ == "__main__":
    main()
