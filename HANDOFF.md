# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15.
- Notebook 01 **Part A (build years only, to 2020-12-31) done and executed.** Predictions P1-P4 were committed before the run; results are in FINDINGS.md (P1 and P3 confirmed, P2 and P4 contradicted). Outputs are in `results/01_*`.
- Part B (test years, 2021 onward) has NOT been run. No 2021+ data was loaded in 01 Part A: `load_prices(..., end=config.BUILD_END)` filters at read time.
- Shared helpers: `rotation.data.load_prices()` (now with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so Part B predictions are not blind; mark any that come from it as "already seen."

## Next
next: write Part B predictions in chat, then run 01 Part B (test years).
(Log them in FINDINGS.md before running. Reuse the Part A settings unchanged; the 63-day wobble to compare against is about 0.20 plain / 0.17 market-removed.)
