"""Download, validate and load daily prices."""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import config  # noqa: E402

FIELDS = ["open", "high", "low", "close", "adj_close", "volume"]
_RENAME = {"Open": "open", "High": "high", "Low": "low", "Close": "close",
           "Adj Close": "adj_close", "Volume": "volume"}


def _download_one(symbol, start, end):
    import yfinance as yf

    df = yf.download(symbol, start=start, end=end, auto_adjust=False,
                     actions=False, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.rename(columns=_RENAME)
    if df.empty:
        return df
    df = df[FIELDS].copy()
    df.index = pd.to_datetime(df.index).tz_localize(None)
    df.index.name = "date"
    df["symbol"] = symbol
    return df.reset_index()


def download_prices(symbols=None, start=None, end=None):
    """Download one symbol at a time. Returns long table: date, symbol, fields.

    BTC-USD (and anything else) is restricted to SPY's trading days.
    """
    symbols = symbols or config.ALL_SYMBOLS
    start = start or config.START
    end = end or config.END
    frames = []
    for s in symbols:
        d = _download_one(s, start, end)
        print(f"{s:8s} {len(d):6d} rows")
        frames.append(d)
    out = pd.concat([f for f in frames if not f.empty], ignore_index=True)
    spy_days = set(out.loc[out.symbol == config.BENCHMARK, "date"])
    if spy_days:
        out = out[out.date.isin(spy_days)]
    cols = ["date", "symbol"] + FIELDS
    return out[cols].sort_values(["symbol", "date"]).reset_index(drop=True)


def validate_prices(df, symbols=None):
    """Raise if the data looks broken. Do NOT switch sources; stop and report."""
    symbols = symbols or config.ALL_SYMBOLS
    problems = []
    present = set(df.symbol.unique())
    for s in symbols:
        if s not in present:
            problems.append(f"{s}: no data returned")
    if problems:
        raise ValueError("Data problems: " + "; ".join(problems))
    spy_last = df.loc[df.symbol == config.BENCHMARK, "date"].max()
    for s, g in df.groupby("symbol"):
        if g.adj_close.isna().mean() > 0.05:
            problems.append(f"{s}: >5% of adj_close missing")
        if (g.adj_close.dropna() <= 0).any():
            problems.append(f"{s}: non-positive adj_close")
        if (g.high < g.low).any():
            problems.append(f"{s}: high < low on {(g.high < g.low).sum()} days")
        if (spy_last - g.date.max()).days > 7:
            problems.append(f"{s}: last date {g.date.max().date()} is stale")
    if (pd.Timestamp.today().normalize() - spy_last).days > 7:
        problems.append(f"SPY last date {spy_last.date()} is stale")
    if problems:
        raise ValueError("Data problems: " + "; ".join(problems))
    return True


def load_prices(symbols=None, fields=None, end=None):
    """Read the saved long-format prices (no downloading).

    `end` (e.g. config.BUILD_END) drops later rows at read time, so they are
    never loaded into memory.
    """
    if not config.PRICES_FILE.exists():
        raise FileNotFoundError(
            f"{config.PRICES_FILE} not found. Run notebooks/00_data.ipynb first.")
    filters = [("date", "<=", pd.Timestamp(end))] if end is not None else None
    df = pd.read_parquet(config.PRICES_FILE, filters=filters)
    if symbols is not None:
        df = df[df.symbol.isin(symbols)]
    if fields is not None:
        df = df[["date", "symbol"] + list(fields)]
    return df.reset_index(drop=True)


def wide(df, field="adj_close"):
    """Pivot long table to date x symbol."""
    return df.pivot(index="date", columns="symbol", values=field).sort_index()
