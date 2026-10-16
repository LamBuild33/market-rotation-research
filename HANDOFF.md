# Handoff

## Current state
- Repo set up; conda env `rotation` (Python 3.11) built from `environment.yml`; kernel "Python (rotation)" registered.
- Notebook 00 (data) done and executed. `data/prices.parquet` (git-ignored) holds 24 symbols, 1999-01-04 to 2026-10-15. Summary in `results/00_data_summary.csv`.
- Shared helpers: `rotation.data.load_prices()` / `wide()`, `rotation.returns.daily_returns()` / `growth_of_1()`.
- Windows note: run the env via `conda run -n rotation ...` (or activate it). Calling the env's python.exe directly without activating crashes on matplotlib's DLLs.
- Config unchanged since setup (build years to 2020-12-31, test years from 2021-01-01, cost 0.10%).

## Next
next: 01 who moves together
(Write the prediction and confirm/contradict criteria in FINDINGS.md first. Use daily returns, build years only.)
