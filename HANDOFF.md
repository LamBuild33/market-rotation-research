# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15.
- Notebook 01 (who moves together) **done, Parts A and B**. Part A (build years): P1 and P3 confirmed, P2 and P4 contradicted. Part B (test years 2021-01-04 to 2026-10-15, checked once): B1-B4 all confirmed. Details in FINDINGS.md; outputs in `results/01_*` (build) and `results/01b_*` (test).
- Test years have now been used once for notebook 01. Any later notebook that reuses test years should say so in its FINDINGS entry.
- Key numbers to carry forward: normal wobble of a 63-day correlation is about 0.19-0.20 (plain) / 0.17 (market-removed); SPY-TLT turned from negative (build) to mostly positive (test); UUP-GLD steadily negative in both periods.
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Next
next: 02 Volume check.
(Test the 55%/45% up-day cutoffs. Write the prediction and confirm/contradict criteria in FINDINGS.md first; choose cutoffs on build years only.)
