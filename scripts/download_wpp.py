"""Download UN WPP demographics for the country setups into src/data.

Fetches the indicators stisim's location demographics read (1985 population by
single year of age, age-specific fertility, mortality by sex and age, net
migration) for 1985-2040, the Median variant, in stisim's file layout.

Mortality is all-cause and lands in {country}_deaths_all_cause.csv. The model
reads {country}_deaths.csv, which must have HIV deaths removed first so the
model's own HIV deaths are not counted twice.

The UN Data Portal token is read from the macOS Keychain:

    security add-generic-password -s un-dataportal-token -a "$USER" -w

Run with ``uv run python scripts/download_wpp.py``.
"""

import getpass
import subprocess
from pathlib import Path

import pandas as pd
import requests

API = "https://population.un.org/dataportalapi/api/v1"
OUT = Path(__file__).resolve().parent.parent / "src" / "data"
START, STOP = 1985, 2040

# UN M49 codes, which the portal uses as location ids
COUNTRIES = dict(eswatini=748, zimbabwe=716)

# indicator id, filename suffix, which Sex rows stisim reads
INDICATORS = dict(
    age=(47, "age_1985", "Both sexes"),
    asfr=(68, "asfr", "Both sexes"),
    deaths=(80, "deaths_all_cause", ["Female", "Male"]),
    migration=(65, "migration", "Both sexes"),
)
COLUMNS = {"timeLabel": "Time", "sex": "Sex", "ageStart": "AgeStart", "value": "Value"}


def token():
    return subprocess.run(
        ["security", "find-generic-password", "-s", "un-dataportal-token",
         "-a", getpass.getuser(), "-w"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def fetch(session, path):
    rows = []
    url = f"{API}/{path}"
    params = dict(pageSize=1000)
    while url:
        resp = session.get(url, params=params, timeout=60)
        resp.raise_for_status()
        page = resp.json()
        rows.extend(page["data"])
        url, params = page.get("nextPage"), None
    return pd.DataFrame(rows)


def download(session, country, loc_id, indicator):
    ind_id, suffix, sexes = INDICATORS[indicator]
    end = START if indicator == "age" else STOP
    df = fetch(session, f"data/indicators/{ind_id}/locations/{loc_id}/start/{START}/end/{end}")
    if not df.location.str.lower().eq(country).all():
        raise ValueError(f"location {loc_id} returned {df.location.unique()}, expected {country}")
    df = df[(df.variant == "Median") & df.sex.isin(pd.Series(sexes).tolist())]
    df = df.rename(columns=COLUMNS)[list(COLUMNS.values())]
    df = df.sort_values(["Time", "Sex", "AgeStart"])
    path = OUT / f"{country}_{suffix}.csv"
    df.to_csv(path, index=False)
    print(f"{path.name}: {len(df)} rows, {df.Time.min()}-{df.Time.max()}")


def main():
    with requests.Session() as session:
        session.headers["Authorization"] = f"Bearer {token()}"
        for country, loc_id in COUNTRIES.items():
            for indicator in INDICATORS:
                download(session, country, loc_id, indicator)


if __name__ == "__main__":
    main()
