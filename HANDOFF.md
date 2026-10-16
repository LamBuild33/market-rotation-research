# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years used once for it.
- Notebook 02 (volume check) done, Parts A and B. Test years used once for it. Verdict: the dashboard's price-view volume check shows no ability to separate continuing from non-continuing moves; the vs-sector view is an unplanned lead (see Scheduled checks). The dashboard's Volume check column was removed on 2026-10-15 and Up-day share reworded.
- Notebook 03 (Top-5 test) done, Parts A and B. Test years used once for it. Verdict: the top-5 ranking showed no edge over the equal-weight sector average. The dashboard's top-5 wording was updated on 2026-10-16 (logged in FINDINGS.md under 03).
- Notebook 04 (rotation map zones) **done, Parts A and B. Test years have now been used once for 04.** Build years: Z1 confirmed (tiny gap), Z2 contradicted, Z3 confirmed but mechanical. Test years (2021-2026): Y1 confirmed (all four zones' averages within +/-0.5%: Improving +0.22%, Leading -0.32%, Fading -0.26%, Lagging +0.29%, all ranges include zero), Y2 confirmed (real clockwise share 68.7% vs shuffled-days baseline 70.7%), Y3 contradicted (industries Fading minus overall -0.13 points; Part A lead +0.88 did not hold). Verdict in FINDINGS.md: the zones are a description of the recent past, not a signal; the clockwise movement is produced by the zone rules themselves. Pattern repeated in both periods but not a prediction: Leading did worst, Lagging best. Outputs: `results/04_*` (build), `results/04b_*` (test).
- Notebook 04 method (for reference): universe = 11 sector funds (information-only runs also use the 4 industries); checkpoints every 21st trading day counted from 1999-01-04 (same grid as 02 and 03, continuing into the test years), a fund is labeled if it has a price 63 days back; change over n days = close / close n days earlier - 1; sector average for a window = simple mean of that window's change across sector funds with a valid change; excess = fund minus sector average; 3-month map longer = 63-day, shorter = 21-day; 1-month map longer = 21-day, shorter = 5-day; zones Leading (both >= 0), Fading (longer >= 0, shorter < 0), Improving (longer < 0, shorter >= 0), else Lagging; outcome = excess from next day's close to 21 trading days later, sector average = simple mean of sector funds' changes over that span; zone moves compare the 3-month-map zone at consecutive checkpoints.
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Scheduled checks
- 02 vs-sector lead: run F1 no earlier than 2027-10-15. (Prediction and method are in FINDINGS.md under "Future test (fresh data only)". Needs at least 50 "Doesn't confirm" observations, otherwise wait longer. Refresh `data/prices.parquet` first by rerunning notebook 00.)

## Next
next: update the dashboard's zone wording in chat, then 05 Who moves first.
(For 05: write predictions in FINDINGS.md and commit before running; choose settings on build years only; test years are checked once per notebook.)
