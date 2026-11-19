"""Exp 44 stage 1: each member's prevented fraction for each arm as a ratio to its Magic cure
prevented fraction, and how much of each quantity's spread the setting accounts for.

    uv run python experiments/pathways/44_ensemble_prevented_fractions/ratio_to_magic_cure.py

Reads the per-setting prevented fractions run.py writes to outputs/.
"""

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
import yaml

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

EXP = Path(__file__).parent
OUT = EXP / "outputs"
CONFIG = yaml.safe_load((EXP / "config.yaml").read_text())
CELLS = CONFIG["cells"]
ARMS = ["poc", "poc_pn", "poc_sti_prep", "poc_sti_prep_pn", "poc_screening", "magic_prep"]
LABELS = {a: CONFIG["labels"][a] for a in ARMS}
LABELS["poc_sti_prep"] = "Panel + PrEP on STI treatment"
LABELS["poc_sti_prep_pn"] = "Panel + PrEP + notification"
LABELS["magic_prep"] = "Magic PrEP"

pf = pd.concat({c: pd.read_csv(EXP / "outputs" / f"prevented_fractions_{c}.csv", index_col=0)
                for c in CELLS}, names=["cell", "member"])
ratio = pf[ARMS].div(pf["magic_cure"], axis=0)


def setting_share(table):
    """Proportion of each column's variance across all 120 members explained by setting (eta squared)."""
    grand = table.mean()
    between = table.groupby(level="cell").apply(lambda g: len(g) * (g.mean() - grand) ** 2).sum()
    total = ((table - grand) ** 2).sum()
    return between / total


summary = pd.DataFrame({
    **{f"ratio median, {c}": ratio.xs(c).median() for c in CELLS},
    "setting share of variance, prevented fraction": setting_share(pf[ARMS]),
    "setting share of variance, ratio to Magic cure": setting_share(ratio),
}).rename(index=LABELS)
summary.round(3).to_csv(OUT / "ratio_to_magic_cure_summary.csv")
ratio.round(4).to_csv(OUT / "ratio_to_magic_cure_per_member.csv")
print(summary.round(2).T.to_string())

colors = dict(zip(CELLS, ["#1f77b4", "#aec7e8", "#d62728", "#ff9896"]))
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True, layout="constrained")
rng = np.random.default_rng(0)
for ax, table, scale, xlabel in (
        (axes[0], pf[ARMS], 100, "HIV infections at 15-49 prevented, 2027-2040 (% of SOC's)"),
        (axes[1], ratio, 1, "Prevented fraction / the same member's Magic cure prevented fraction")):
    for j, cell in enumerate(CELLS):
        values = [scale * table.xs(cell)[a].to_numpy() for a in ARMS]
        pos = np.arange(len(ARMS)) + (j - 1.5) * 0.2
        ax.boxplot(values, positions=pos, orientation="horizontal", widths=0.17, showfliers=False,
                   patch_artist=True, boxprops=dict(facecolor=colors[cell], alpha=0.8),
                   medianprops=dict(color="k"))
        for p, v in zip(pos, values):
            ax.scatter(v, p + rng.uniform(-0.05, 0.05, len(v)), s=4, color="0.3", alpha=0.5, zorder=3)
    ax.axvline(0, color="k", lw=0.8)
    ax.set_xlabel(xlabel)
axes[0].set_yticks(range(len(ARMS)), [LABELS[a] for a in ARMS])
axes[0].invert_yaxis()
axes[0].set_title("Prevented fraction against SOC")
axes[1].set_title("Ratio to Magic cure, per member")
axes[1].legend([plt.Rectangle((0, 0), 1, 1, color=colors[c]) for c in CELLS], CELLS.values(),
               loc="upper right", fontsize=8)
fig.suptitle("Fig 9: prevented fraction and its ratio to Magic cure, 30 members per setting")
fig.savefig(EXP / "figures" / "fig9_ratio_to_magic_cure.png", dpi=150)
