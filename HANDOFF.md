# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11); kernel "Python (rotation)" registered.
- Notebook 00 (data) done. `data/prices.parquet` (git-ignored): 24 symbols, 1999-01-04 to 2026-10-15, including daily volume (same download as prices).
- Notebook 01 (who moves together) done, Parts A and B. Test years have been used once for it.
- Notebook 02 (volume check) **Part A done** (build years only, 1999-2020): V1, V2, V3 all contradicted. Confirms 50.98% vs Doesn't confirm 52.09% continued, baseline 51.43%; Confirms beat Doesn't confirm in 11 of 22 years; no cutoff (50/50 to 65/35) gives a 5-point gap. Details in FINDINGS.md; outputs in `results/02_*`. Part B (test years) NOT run: no 2021+ data was loaded in Part A (`load_prices(..., end=config.BUILD_END)`, and every outcome window ends by 2020-12-14).
- Notebook 02 rules implemented: 21-trading-day windows, up-day share from adjusted close, checkpoints every 21 trading days starting at the 22nd trading day (1999-02-03), labels at 55/45, at least 18 nonzero-volume days out of 21. Part B must use these exactly (do not retune cutoffs).
- Shared helpers: `rotation.data.load_prices()` (with `end=`) / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly crashes on matplotlib's DLLs.
- Config unchanged since setup.
- The quick-look study (chat, Oct 2022 to Oct 2026) already showed part of the test years, so predictions touching those years are not blind; mark any that come from it as "already seen."

## Next
next: write 02 Part B predictions in chat, then run 02 Part B (test years).
(Log them in FINDINGS.md and commit before loading any 2021+ data. Test years are checked once; same methods and cutoffs as Part A. Note the first test checkpoints need prices from late 2020 for the 21-day look-back.)
