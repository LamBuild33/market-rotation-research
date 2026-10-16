# Findings log (newest first)

Every entry: date run, notebook, data range, the numbers, plain-language takeaway.
Before any new test, add the prediction and what would confirm/contradict it.
Any change to `config.py` must be logged here with the reason.

---

## 2026-10-15 — Notebook 00: data download and checks
- **Data range:** 1999-01-04 to 2026-10-15 (BTC-USD to 2026-10-14; it is one day behind because SPY's latest day had no bitcoin row yet). 24 symbols, 6,989 SPY trading days.
- **Start dates differ:** SPY/XL* sectors 1999-01-04 (except XLRE 2015-10-08, XLC 2018-06-19), QQQ 1999-03-10, SMH 2000-06-05, IWM 2000-05-26, TLT 2002-07-30, EEM 2003-04-14, GLD 2004-11-18, XBI 2006-02-06, ITA 2006-05-05, USO 2006-04-10, KRE 2006-06-22, UUP 2007-03-01, BTC-USD 2014-09-17.
- **Missing days inside any symbol's history:** 0 for all 24.
- **Moves bigger than 15% in a day (adjusted close):** 30 for BTC-USD (range -37.2% to +25.2%; its Monday moves include the weekend), and 36 across the other funds: XLF 6, XLE 4, KRE 5, USO 5, SMH 3, EEM 3, XLK 1, XLRE 1, QQQ 1. All line up with known events (Oct 2008 crash, Mar 2020 COVID crash, Apr 2020 oil collapse, 3 Jan 2001 Fed rate cut, 9 Apr 2025 rally), so none look like data errors. Full list: `results/00_big_moves.csv`.
- **Dividend effect:** on the last day raw and adjusted close are equal (0.0 gap for all), because Yahoo adjusts history backwards from today. The real effect shows over time: e.g. SPY price-only return since 1999 is +527% vs +914% with dividends; TLT -1.9% vs +125.8%. GLD, USO and BTC-USD pay no dividends, so no gap.
- **Files:** `results/00_data_summary.csv`, `results/00_big_moves.csv`, `results/00_growth_since_2015.png`.
- **Takeaway:** The data is complete and believable. Use adjusted close for any return or correlation, since raw prices badly understate bond and dividend-heavy funds. Tests involving XLRE, XLC or BTC-USD have far less history, so results for them rest on a shorter period.
