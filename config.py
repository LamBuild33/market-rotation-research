"""Locked research settings.

Fixed BEFORE looking at any results. Any later change must be logged in
FINDINGS.md with the reason.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"
PRICES_FILE = DATA_DIR / "prices.parquet"

# ---- Symbols (24) ----
BENCHMARK = "SPY"
SECTORS = ["XLK", "XLE", "XLV", "XLU", "XLF", "XLI", "XLB", "XLP", "XLY", "XLC", "XLRE"]
INDUSTRIES = ["SMH", "XBI", "KRE", "ITA"]
OTHER = ["QQQ", "IWM", "GLD", "TLT", "USO", "UUP", "EEM"]
CRYPTO = ["BTC-USD"]  # kept only on stock-market trading days (SPY's calendar)

ALL_SYMBOLS = [BENCHMARK] + SECTORS + INDUSTRIES + OTHER + CRYPTO

GROUP = {BENCHMARK: "benchmark"}
GROUP.update({s: "sector" for s in SECTORS})
GROUP.update({s: "industry" for s in INDUSTRIES})
GROUP.update({s: "other market" for s in OTHER})
GROUP.update({s: "bitcoin" for s in CRYPTO})

# ---- Dates ----
START = "1999-01-01"
END = None  # None = today
BUILD_END = "2020-12-31"   # build years: start .. BUILD_END (choose ideas/cutoffs here)
TEST_START = "2021-01-01"  # test years: check ONCE

# ---- Costs ----
COST_PER_TRADE = 0.0010  # 0.10% per trade in any "would I have made money" test

# ---- Definitions ----
# Sector average = equal-weight average of whichever of the 11 sectors exist on
# that date (XLRE starts 2015, XLC 2018).

# ---- Data checks ----
BIG_MOVE = 0.15  # flag daily adjusted-close moves bigger than 15%
