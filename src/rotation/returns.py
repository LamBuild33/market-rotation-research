"""Return helpers. Correlations always use daily returns, never prices."""
import pandas as pd


def daily_returns(prices):
    """Daily percent change of a date x symbol price table (use adj_close)."""
    return prices.pct_change(fill_method=None)


def growth_of_1(prices, start):
    """Growth of $1 from the first available date on/after `start`."""
    p = prices.loc[start:]
    return p / p.apply(lambda c: c.dropna().iloc[0])
