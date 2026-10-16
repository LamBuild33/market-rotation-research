# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years used once for it.
- Notebook 02 (volume check) **done, Parts A and B. Test years have now been used once for 02.** Build years (1999-2020): V1-V3 all contradicted (Confirms 50.98% vs Doesn't confirm 52.09% continued; baseline 51.43%). Test years (2021-2026): W1 confirmed (price-view gap -3.47), W2 contradicted (vs-sector gap +13.76), W3 contradicted (baseline 48.53%). Verdict in FINDINGS.md: the dashboard's price-view volume check shows no ability to separate continuing from non-continuing moves in either period. The vs-average-sector view is an unplanned lead, not support for the rule. Outputs: `results/02_*` (build), `results/02b_*` (test).
- The dashboard's Volume check column was removed on 2026-10-15 and Up-day share was reworded (logged in FINDINGS.md).
- Notebook 02 method (for reference): 21-trading-day windows, up-day share from adjusted close, checkpoints every 21st trading day counted from 1999-01-04 (grid continues across build and test), labels at 55/45, at least 18 nonzero-volume days of 21, 23 symbols (no BTC).
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Scheduled checks
- 02 vs-sector lead: run F1 no earlier than 2027-10-15. (Prediction and method are in FINDINGS.md under "Future test (fresh data only)". Needs at least 50 "Doesn't confirm" observations, otherwise wait longer. Refresh `data/prices.parquet` first by rerunning notebook 00.)

## Next
next: 03 Top-5 test.
(For 03: write predictions in FINDINGS.md and commit before running; choose settings on build years only; test years are checked once per notebook.)
