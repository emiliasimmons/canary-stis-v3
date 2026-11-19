# Exp 47: Seed noise in 45's prevented fractions, over 10 seeds per member

**Question.** How much of the spread in each arm's prevented fraction across
[45](../45_barker_cofactors_anc_arms/SUMMARY.md)'s 30 members comes from seed noise, and
where do the arms' medians sit once each member's prevented fraction is averaged over 10
seeds? 45 ran each member on one seed. Across its members, the range of the prevented
fraction of SOC's HIV infections at 15-49 over 2027-2040 crosses zero for the point-of-care
panel (-1.7 to 8.9%). So does the range of the pathway contribution, in percentage points
of the same prevented fraction, for notification at 54% notified and 50% attending (-2.0
to 7.9), for PrEP on STI treatment at 30% uptake and 3-month courses (-2.6 to 5.5) and for
ANC testing with the panel at ANC (-4.2 to 5.7). With seed noise separated
out, the spread that remains is what the members' parameters produce. This experiment
answers issue 47.

**Plan.** The members are 45's 30, with their draws in `members.json`, copied from the
`ensemble.json` that 45's `run.py` writes. They take 45's baseline (Barker 2022 acquisition
cofactors, ANC testing off) and 45's twelve arms, SOC included. Each member runs on 10 new
seeds, `crc32("47-<member>-<k>")` for k = 1-10, none of them 45's. On each member and
seed, all twelve arms continue from one simulation stopped at the start of 2027
(`src/snapshots.py`), which reproduces running each arm from 1985 exactly. That makes
300 sets of twelve arms, 3,600 simulations, about 30-40 minutes on zebra at 80 workers.
Each arm's prevented fraction on a seed is against SOC on the same seed. A member's
prevented fraction over its seeds is 1 minus the arm's HIV infections at 15-49 over
2027-2040 summed over the 10 seeds, divided by SOC's summed the same way. Pathway
contributions are differences between arms, as in 45. Per arm and per contribution, the
standard deviation across seeds within a member is compared with the standard deviation
across members of the 10-seed values. Members stay the ones 45 selected on seed 1's 2026
HIV prevalence at 15-49. The spread of that prevalence across each member's seeds is
reported, since other seeds can fall outside the 22-28% band of 2026 HIV prevalence at
15-49 that 45 selected on.

**Success criteria.** All 3,600 simulations finish, and 45's two wiring checks pass on the
10-seed values: the ANC + HIV testing arm at or above the ANC arm, and Magic PrEP at
3-month courses above the contribution of PrEP on STI treatment at 30% uptake. If the
standard deviation across seeds is comparable to 45's standard deviation across members,
most of 45's spread is seed noise, and the setting's range in 45's tables is wider than
its members' parameters produce. If it is small against that, 45's spread comes from the
members' parameters and its tables stand.
