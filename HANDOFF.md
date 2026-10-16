# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years used once for it.
- Notebook 02 (volume check) done, Parts A and B. Test years used once for it. Verdict: the dashboard's price-view volume check shows no ability to separate continuing from non-continuing moves; the vs-sector view is an unplanned lead (see Scheduled checks). The dashboard's Volume check column was removed on 2026-10-15 and Up-day share reworded.
- Notebook 03 (Top-5 test) **Part A done** (build years only, 1999-2020): T1, T2, T3 all contradicted. Top 5 (after 0.10% costs) trailed the equal-weight sector average by 2.52% a year (95% range -4.53% to -0.55%), beat it in 8 of 22 years and 42.7% of 262 holding periods; growth of $1: top 5 $3.31, bottom 5 $5.47, sector average $5.59. Costs about 1.13% a year, about 2.35 of 5 funds swapped per month. Information only: 3-month ranking -2.17% a year, no-delay trading -3.19% a year. Details in FINDINGS.md; outputs in `results/03_*`. Part B (test years) NOT run: no 2021+ data was loaded in Part A (`load_prices(..., end=config.BUILD_END)`).
- Notebook 03 method (for reference): universe = 11 sector funds that exist and have a price 21 trading days back; checkpoints every 21st trading day counted from 1999-01-04 (same grid as 02); rank at checkpoint close by 21-day change, trade at next day's close, equal weight, weights drift; cost = 0.001 x sum of absolute weight changes (first purchase counts) taken at the trade close and counted in the period it pays for; sector average = equal-weight, rebalanced daily, no cost; complete holding periods only for period statistics. Part B must use exactly this (the last test period will be partial; drop it from period stats and say so).
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Scheduled checks
- 02 vs-sector lead: run F1 no earlier than 2027-10-15. (Prediction and method are in FINDINGS.md under "Future test (fresh data only)". Needs at least 50 "Doesn't confirm" observations, otherwise wait longer. Refresh `data/prices.parquet` first by rerunning notebook 00.)

## Next
next: write 03 Part B predictions in chat, then run 03 Part B (test years).
(Log the predictions in FINDINGS.md and commit before loading any 2021+ data. Test years are checked once; a dry run on build years to catch bugs is fine, as in 01 and 02.)
