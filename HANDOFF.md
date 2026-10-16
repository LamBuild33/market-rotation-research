# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years used once for it.
- Notebook 02 (volume check) done, Parts A and B. Test years used once for it. Verdict: the dashboard's price-view volume check shows no ability to separate continuing from non-continuing moves; the vs-sector view is an unplanned lead (see Scheduled checks). The dashboard's Volume check column was removed on 2026-10-15 and Up-day share reworded.
- Notebook 03 (Top-5 test) done, Parts A and B. Test years used once for it. Verdict: the top-5 ranking showed no edge over the equal-weight sector average. The dashboard's top-5 wording was updated on 2026-10-16 (logged in FINDINGS.md under 03).
- Notebook 04 (rotation map zones) done, Parts A and B. Test years used once for it. Verdict: the zones are a description of the recent past, not a signal; the clockwise movement is produced by the zone rules themselves. The dashboard's map wording was updated on 2026-10-16 (logged in FINDINGS.md under 04).
- Notebook 05 (who moves first) **done, Parts A and B. Test years have now been used once for 05.** Build years (1999-2020): M1-M3 all contradicted (82.0% of daily pairs and 28.1% of weekly pairs outside the 95% noise band), caused by a market-wide negative next-day autocorrelation (SPY -0.092; -0.32 in 2020), not specific leaders. Test years (2021-2026): N1 confirmed (SPY daily autocorrelation -0.031, inside the noise band of +/-0.051), N2 contradicted (13 of 23 market-removed daily steady leads kept their sign = 57%, one short of the 14 needed, about coin-flip), N3 contradicted (3 of 11 weekly = 27%). In the test years only about 8-9% of pairs are outside the band in every view (near the 5% chance level); the largest daily |lag-1 correlation| is 0.10. Verdict in FINDINGS.md: no lead-lag relationship held up and is large enough to matter after the 0.10% cost; the dashboard should not describe any market as moving first. Outputs: `results/05_*` (build), `results/05b_*` (test).
- Notebook 05 method (for reference): daily returns = pct change of adjusted close, 23 symbols (no BTC-USD); weekly = last trading day of each Monday-Sunday week to the next, 24 symbols; "A leads B" = corr(A return in t, B return in t+1) over periods where both exist, every ordered pair, self-pairs separate; noise band 1.96/sqrt(n); pair-year belongs to the follower's year (min 120 days daily, 26 weeks weekly); steady lead = outside the band over the full period AND same sign in at least 75% of the years the pair exists; market-removed view = residual vs equal-weight sector average, fit per symbol and calendar year (min 120 days daily as in 01, 26 weeks weekly).
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Scheduled checks
- 02 vs-sector lead: run F1 no earlier than 2027-10-15. (Prediction and method are in FINDINGS.md under "Future test (fresh data only)". Needs at least 50 "Doesn't confirm" observations, otherwise wait longer. Refresh `data/prices.parquet` first by rerunning notebook 00.)

## Possible future tests
- Leaders vs laggards: recent leaders did slightly worse and laggards slightly better in 03, 04 Part A and 04 Part B. Never predicted; needs its own predicted test on fresh data.

## Next
next: 06 Market moods.
(For 06: write predictions in FINDINGS.md and commit before running; choose settings on build years only; test years are checked once per notebook.)
