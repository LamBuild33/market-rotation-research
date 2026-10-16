# Working rules

- Plain-language summaries; spell out jargon.
- One notebook per task. Stop and report when it's done.
- Before running any new test: write the prediction, plus what result would confirm or contradict it, in FINDINGS.md.
- Choose settings on build years only; check test years once. Break results down by year before writing them up.
- Correlations use daily returns, never prices.
- Every FINDINGS.md entry gets: date run, notebook, data range, the numbers, and a plain-language takeaway.

# Repo notes

- Use conda env `rotation` (see environment.yml). Never install into base.
- Read prices with `rotation.data.load_prices()`; don't re-download in later notebooks.
- Settings (symbols, dates, build/test split, costs) live in `config.py`. Any change must be noted in FINDINGS.md with the reason.
- If yfinance fails or returns obviously broken data, stop and tell the user. Don't switch data sources.
