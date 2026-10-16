# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years used once for it.
- Notebook 02 (volume check) done, Parts A and B. Test years used once for it. Verdict: the dashboard's price-view volume check shows no ability to separate continuing from non-continuing moves; the vs-sector view is an unplanned lead (see Scheduled checks). The dashboard's Volume check column was removed on 2026-10-15 and Up-day share reworded.
- Notebook 03 (Top-5 test) done, Parts A and B. Test years used once for it. Verdict: the top-5 ranking showed no edge over the equal-weight sector average. The dashboard's top-5 wording was updated on 2026-10-16 (logged in FINDINGS.md under 03).
- Notebook 04 (rotation map zones) done, Parts A and B. Test years used once for it. Verdict: the zones are a description of the recent past, not a signal; the clockwise movement is produced by the zone rules themselves. Dashboard zone wording update is pending (planned in chat).
- Notebook 05 (who moves first) **Part A done** (build years only, 1999-2020): M1, M2, M3 all contradicted. Daily plain view: 415 of 506 ordered pairs (82.0%) outside the 95% noise band, largest |lag-1 correlation| 0.291 (XLC->UUP, short history), 108 pairs above 0.10; weekly: 155 of 552 (28.1%). Cause: a market-wide negative next-day autocorrelation in the stock funds (SPY -0.092; -0.32 in 2020; 81.6% of pairs outside the band in 2020), not specific leaders. Market-removed view (information only): daily 23.3% outside (largest 0.114), weekly 10.7%. Steady leads (plain): daily 115 (78 without XLC/XLRE), weekly 64; mostly negative, EEM and KRE as followers, TLT as the main positive leader; market-removed steady leads: daily 23, weekly 11 (list in FINDINGS.md and `results/05_steady_leads_*`). These are the Part B candidates. Part B (test years) NOT run: no 2021+ data was loaded in Part A (`load_prices(..., end=config.BUILD_END)`).
- Notebook 05 method (for reference): daily returns = pct change of adjusted close, 23 symbols (no BTC-USD); weekly = last trading day of each Monday-Sunday week to the next, 24 symbols; "A leads B" = corr(A return in t, B return in t+1) over periods where both exist, every ordered pair, self-pairs separate; noise band 1.96/sqrt(n); pair-year belongs to the follower's year (min 120 days daily, 26 weeks weekly); steady lead = outside the band over the full period AND same sign in at least 75% of the years the pair exists; market-removed view = residual vs equal-weight sector average, fit per symbol and calendar year (min 120 days daily as in 01, 26 weeks weekly). Part B should use exactly this on the test years.
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Scheduled checks
- 02 vs-sector lead: run F1 no earlier than 2027-10-15. (Prediction and method are in FINDINGS.md under "Future test (fresh data only)". Needs at least 50 "Doesn't confirm" observations, otherwise wait longer. Refresh `data/prices.parquet` first by rerunning notebook 00.)

## Possible future tests
- (Section requested to be kept, but it did not exist in this file, so it is empty. Add items here.)

## Next
next: write 05 Part B predictions in chat, then run 05 Part B (test years).
(Log the predictions in FINDINGS.md and commit before loading any 2021+ data. Test years are checked once; a dry run on build years to catch bugs is fine, and the Part B code should reproduce every Part A number exactly.)
