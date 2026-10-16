# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years used once for it.
- Notebook 02 (volume check) done, Parts A and B. Test years used once for it. Verdict: the dashboard's price-view volume check shows no ability to separate continuing from non-continuing moves; the vs-sector view is an unplanned lead (see Scheduled checks). The dashboard's Volume check column was removed on 2026-10-15 and Up-day share reworded.
- Notebook 03 (Top-5 test) done, Parts A and B. Test years used once for it. Verdict: the top-5 ranking showed no edge over the equal-weight sector average. The dashboard's top-5 wording was updated on 2026-10-16 (logged in FINDINGS.md under 03).
- Notebook 04 (rotation map zones) **Part A done** (build years only, 1999-2020): Z1 confirmed (Improving +0.044% vs Leading -0.193% a month, but tiny and indistinguishable from zero), Z2 contradicted (Fading +0.108%, median -0.219%), Z3 confirmed (831 clockwise vs 353 counter-clockwise one-step moves) but a shuffled-days check shows this is built into the zone rules (70.9% clockwise on shuffled data vs 71.0% real). No zone average beats +0.2% a month. Details in FINDINGS.md; outputs in `results/04_*`. Part B (test years) NOT run: no 2021+ data was loaded in Part A (`load_prices(..., end=config.BUILD_END)`; the 2020-12-14 checkpoint has no full outcome and is dropped).
- Notebook 04 method (for reference): universe = 11 sector funds (information-only runs also use the 4 industries); checkpoints every 21st trading day counted from 1999-01-04 (same grid as 02 and 03), a fund is labeled if it has a price 63 days back; change over n days = close / close n days earlier - 1; sector average for a window = simple mean of that window's change across sector funds with a valid change; excess = fund minus sector average; 3-month map longer = 63-day, shorter = 21-day; 1-month map longer = 21-day, shorter = 5-day; zones Leading (both >= 0), Fading (longer >= 0, shorter < 0), Improving (longer < 0, shorter >= 0), else Lagging; outcome = excess from next day's close to 21 trading days later, sector average = simple mean of sector funds' changes over that span; zone moves compare the 3-month-map zone at consecutive checkpoints. Part B must use exactly this.
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Scheduled checks
- 02 vs-sector lead: run F1 no earlier than 2027-10-15. (Prediction and method are in FINDINGS.md under "Future test (fresh data only)". Needs at least 50 "Doesn't confirm" observations, otherwise wait longer. Refresh `data/prices.parquet` first by rerunning notebook 00.)

## Next
next: write 04 Part B predictions in chat, then run 04 Part B (test years).
(Log the predictions in FINDINGS.md and commit before loading any 2021+ data. Test years are checked once; a dry run on build years to catch bugs is fine, as in 01-03, and the Part B code should reproduce every Part A number exactly.)
