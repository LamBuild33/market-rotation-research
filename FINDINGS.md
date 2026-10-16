# Findings log (newest first)

Every entry: date run, notebook, data range, the numbers, plain-language takeaway.
Before any new test, add the prediction and what would confirm/contradict it.
Any change to `config.py` must be logged here with the reason.

---

## 2026-10-15 — Notebook 02: volume check (Part A, build years 1999-01-04 to 2020-12-31)

Tests the dashboard's volume rule ("Confirms" / "Doesn't confirm", 55%/45% up-day cutoffs). Main test = plain price view (what the dashboard uses); the vs-average-sector view is a second view.

### Part A predictions (written before running anything)
- **V1.** Over the build years, "Confirms" moves continue (same direction over the next 21 trading days) at least 5 percentage points more often than "Doesn't confirm" moves.
- **V2.** "Confirms" continues more often than "Doesn't confirm" in at least 15 of 22 build years.
- **V3.** "Doesn't confirm" moves continue less than 50% of the time.

Each is confirmed if the stated threshold is met and contradicted if not.

---

## 2026-10-15 — Notebook 01: who moves together (Part A, build years 1999-01-04 to 2020-12-31)

**Note:** The quick-look study (chat, Oct 2022 to Oct 2026) already showed us part of the test years, so Part B predictions are not blind. Mark any Part B prediction that comes from the quick look as "already seen."

### Part A predictions (written before running anything)
- **P1.** Dollar vs gold (UUP vs GLD), plain view: negative in at least 80% of build years where both exist.
- **P2.** Tech group (XLK, SMH, QQQ, SPY): every pair above +0.70 in every build year, plain view.
- **P3.** Stocks vs long bonds (SPY vs TLT), plain view: negative in at least 70% of build years where both exist.
- **P4.** Tech vs staples (XLK vs XLP), market-removed view: negative in at least 80% of build years.

Each is confirmed if the stated threshold is met and contradicted if not.

### Part A results (run 2026-10-15, notebook `01_who_moves_together.ipynb`)
- **Data range:** build years only, 1999-01-04 to 2020-12-31 (5,536 trading days; nothing from 2021 onward was loaded). Daily returns from adjusted close. Market = equal-weight average of the sector funds that exist each day (9 to 11 of them). 276 pairs had 252+ shared days. A year needs 120+ shared days.
- **P1, dollar vs gold (UUP-GLD), plain view: CONFIRMED.** Negative in 14 of 14 years (2007-2020; needed 80%). Yearly range -0.19 (2011) to -0.65 (2018); typical year about -0.4.
- **P2, tech group all pairs above +0.70 every year, plain view: CONTRADICTED.** 4 of 129 pair-years were at or below 0.70, all in SMH vs SPY: 2000 (0.699, a partial year from 2000-06-05, missed by 0.001), 2004 (0.604), 2005 (0.612), 2017 (0.652). The other five pairs never dropped below 0.736 (XLK-SMH 0.737 in 2007, SMH-QQQ 0.736 in 2007, XLK-SPY 0.781, SPY-QQQ 0.790, XLK-QQQ 0.873). Three of the four misses came before 2011-12-20, when "SMH" was a different fund.
- **P3, stocks vs long bonds (SPY-TLT), plain view: CONFIRMED.** Negative in 16 of 18 years (89%; needed 70%). The two exceptions were tiny positives, 2005 (+0.01) and 2006 (+0.05). Strongest years: 2011 (-0.71), 2012 (-0.65), 2010 (-0.55).
- **P4, tech vs staples (XLK-XLP), market-removed view: CONTRADICTED, narrowly.** Negative in 17 of 22 years (77%; needed 80%). Positive years: 2005 (+0.09), 2006 (+0.11), 2008 (+0.09), 2016 (+0.11), 2020 (+0.14). Median year about -0.15, a weak but frequent opposite tilt. In the plain view the same pair is positive in 21 of 22 years (only 2000 is negative) (the market lifts both).
- **Normal wobble:** a 63-day (about 3-month) correlation normally drifts by a standard deviation of **0.20** (median across the 276 pairs, plain view; 0.17 in the market-removed view). So a pair's 3-month correlation moving by about 0.2 is routine, not news.
- **Steadiness (plain view):** 196 pairs are steady together, 23 steady opposite, 57 flip. Market-removed: 69 together, 94 opposite, 113 flip. Most plain-view togetherness is just everything rising and falling with the market; once the market is removed, far fewer pairs stay together.
- **Strongest market-removed pairs:** XLK-QQQ +0.83, XLC-QQQ +0.73, XLK-SMH +0.72, SMH-QQQ +0.67, SPY-QQQ +0.65, XLF-KRE +0.64, XLI-ITA +0.60. Most opposite: XLRE-SPY -0.43, GLD-UUP -0.42 (the only one that is also negative in the plain view), XLI-XLC -0.37. Full lists: `results/01_top10_market_removed.csv`.
- **Caution on the market-removed view:** the market is built from the sector funds, so sector-vs-sector leftovers lean negative by construction (e.g. XLE-XLY -0.33, XLK-XLE -0.29, XLB-SPY -0.33 are mostly that, not a real opposite). Treat sector-vs-sector negatives with care; cross-asset pairs (GLD-UUP) are cleaner.
- **Data notes that affect these results (from 00):** SMH before 2011-12-20 is the old Semiconductor HOLDRS, a different fund (matters for P2). XLK, XLY, XLC, XLF and XLRE changed contents in 2016 and 2018, so results spanning those dates compare slightly different baskets. XLC (3 build years, from 2018-06) and XLRE (5 years, from 2015-10) rank high in the top-10 lists on short history, so their "steady" labels rest on few years. BTC-USD has only about 6 build years (2015-2020) and is near zero with everything.
- **Files:** `results/01_correlations_whole_period.csv`, `01_correlations_by_year.csv`, `01_steadiness.csv`, `01_rolling_wobble.csv`, `01_heatmap_plain.png`, `01_heatmap_market_removed.png`, `01_top10_market_removed.csv`, `01_selected_pairs_by_year.csv`.
- **Takeaway:** Two of the four ideas held (dollar vs gold, stocks vs long bonds were reliably opposite) and two narrowly failed (SMH was not always tightly tied to SPY; tech vs staples was opposite 77%, not 80%, of years once the market is removed). Part B (test years) not run yet.

### Part B predictions (test years 2021-01-01 to last date; written before loading any 2021+ data)
Test years are 2021 through 2026; 2026 counts if it has at least 120 days.
- **B1.** Dollar vs gold (UUP vs GLD), plain view: negative in all 6 test years. [already seen in quick look]
- **B2.** Stocks vs long bonds (SPY vs TLT), plain view: positive in at least 4 of 6 test years (a break from the build years). [already seen in quick look]
- **B3.** Tech group (XLK, SMH, QQQ, SPY), plain view: all 6 pairs above +0.70 in every test year (36 pair-years). [partly seen: quick look showed whole-period numbers only]
- **B4.** Steady pairs stay steady, market-removed view: of the pairs labeled "steady together" or "steady opposite" in Part A, excluding pairs where both funds are among the 11 sector funds, at least 80% have the same sign over the whole test period. [not seen]

Rules: same methods as Part A, no changes after seeing test results; if something looks wrong, report it, don't fix it.

### Part B results (run 2026-10-15, same notebook, test years checked once)
- **Data range:** 2021-01-04 to 2026-10-15, 1,453 trading days. Years used: 2021 to 2026 (2026 has 198 days, above the 120 minimum). Methods identical to Part A; an automatic check confirmed the test code reproduces Part A's market-removed numbers exactly on build years. Before the real run, the Part B code was dry-run on 2015-2020 only (no 2021+ data loaded) to catch bugs. The test years were then run once, with no method changes. BTC-USD ends 2026-10-14 (one day behind), as in 00.
- **B1, dollar vs gold (UUP-GLD), plain view: CONFIRMED.** Negative in 6 of 6 years: 2021 -0.51, 2022 -0.52, 2023 -0.56, 2024 -0.40, 2025 -0.42, 2026 -0.50. Build-year range was -0.19 to -0.65, so this is a very steady relationship. [already seen in quick look]
- **B2, stocks vs long bonds (SPY-TLT), plain view: CONFIRMED.** Positive in 5 of 6 years (needed 4): 2021 -0.14, 2022 +0.08, 2023 +0.13, 2024 +0.06, 2025 +0.10, 2026 +0.34. This is a real break from the build years, where it was negative in 16 of 18 years. The positives are modest except 2026. [already seen in quick look]
- **B3, tech group all 6 pairs above +0.70 every year, plain view: CONFIRMED.** 36 of 36 pair-years above 0.70. Lowest was SMH-SPY at 0.739 (2021); next lowest SMH-SPY 0.746 (2023) and 0.752 (2026). Every other pair stayed at or above 0.84. SMH-SPY is the pair that failed this test in the build years (0.60-0.70 in 2000, 2004, 2005, 2017), so it is now tighter than it used to be. [partly seen: quick look showed whole-period numbers only]
- **B4, steady pairs stay steady, market-removed view: CONFIRMED.** 127 pairs qualified (labelled steady together or steady opposite in Part A, not sector-vs-sector); 111 of 127 (87%) kept the same sign over the test period (needed 80%). Steady-together pairs: 55 of 62 kept their sign; steady-opposite: 56 of 65. All 127 had enough test data. [not seen]
  - 16 pairs flipped. 12 of the 16 flipped to a test correlation within 0.06 of zero (e.g. ITA-GLD +0.05, QQQ-TLT +0.00, XLE-UUP +0.05), so those are better read as "relationship faded to nothing" than "reversed". The other four are XLE-EEM (-0.08) and three SPY-vs-sector pairs: XLV-SPY (-0.18), KRE-SPY (-0.09), XLF-SPY (-0.07).
- **Normal wobble, 63-day rolling correlation (median across 276 pairs):** test years **0.189** vs build years 0.204 (plain view); 0.168 vs 0.173 (market-removed). About the same, slightly calmer. A move of about 0.2 in a 3-month correlation is still routine.
- **Sign held overall (build-year median vs test period, all 276 pairs):** 88% of pairs kept the same sign in the plain view, 81% in the market-removed view. The typical plain-view pair is about 0.09 less correlated in the test years than its build-year median (median change -0.086); market-removed change is about zero (-0.011).
- **Biggest changes from build to test (market-removed view, sector-vs-sector excluded; build median yearly -> test period):**
  - SMH-SPY +0.34 -> +0.75: chips and the S&P 500 (relative to the equal-weight sector average) moved together far more.
  - XLP-SPY -0.04 -> -0.44: staples went from unrelated to clearly opposite the S&P 500's big-company tilt.
  - XLF-SPY +0.31 -> -0.07 and KRE-SPY +0.26 -> -0.09: financials and regional banks stopped moving with the S&P 500 tilt.
  - QQQ-EEM +0.10 -> +0.45: Nasdaq-100 and emerging markets became much more linked once the market is removed.
  - XLV-SPY +0.17 -> -0.18: health care flipped from slightly together to slightly opposite.
  - XLK-SPY +0.57 -> +0.91 and SPY-QQQ +0.59 -> +0.92: tech and Nasdaq-100 became almost the same trade as the S&P 500's tilt.
  - SMH-EEM +0.20 -> +0.53 and XLY-SPY +0.19 -> +0.51: chips and emerging markets, and consumer discretionary and the S&P 500, moved much more together.
  - Pattern: 7 of the 10 involve SPY. In the market-removed view SPY's leftover is "S&P 500 vs the equal-weight sector average" (a big-company tilt). In the test years that tilt moved with tech, chips and Nasdaq funds and against staples, health care and banks. That is consistent with a few very large tech-heavy companies driving the S&P 500, but this study did not test that explanation.
- **Heads-up (reported, not fixed):** pairs involving SPY in the market-removed view are special because SPY is not a sector, so the equal-weight sector average does not contain it; the big changes above partly reflect how much SPY differs from that average in the test years, not only changes in the funds themselves. Part A's tables used the same definition, so the comparison is like for like.
- **Files:** `results/01b_correlations_whole_test.csv`, `01b_correlations_by_year.csv`, `01b_rolling_wobble.csv`, `01b_selected_pairs_by_year.csv`, `01b_build_vs_test.csv`, `01b_top10_changes_market_removed.csv`, `01b_steady_pairs_check.csv`, `01b_heatmap_plain.png`, `01b_heatmap_market_removed.png`.
- **Takeaway:** All four Part B predictions held. Dollar vs gold stayed opposite every year. Stocks and long bonds stopped being opposite (positive in 5 of 6 years after being negative in most build years). Tech funds stayed tightly together, even SMH-SPY. And most pairs that were reliably together or opposite in 1999-2020 kept their direction in 2021-2026, with the main exceptions being pairs that faded to near zero and a few SPY-vs-sector pairs. Only the stocks-vs-bonds relationship changed in a way that matters for practical use.

---

## 2026-10-15 — Notebook 00: data download and checks
- **Data range:** 1999-01-04 to 2026-10-15 (BTC-USD to 2026-10-14; it is one day behind because SPY's latest day had no bitcoin row yet). 24 symbols, 6,989 SPY trading days.
- **Start dates differ:** SPY/XL* sectors 1999-01-04 (except XLRE 2015-10-08, XLC 2018-06-19), QQQ 1999-03-10, SMH 2000-06-05, IWM 2000-05-26, TLT 2002-07-30, EEM 2003-04-14, GLD 2004-11-18, XBI 2006-02-06, ITA 2006-05-05, USO 2006-04-10, KRE 2006-06-22, UUP 2007-03-01, BTC-USD 2014-09-17.
- **Missing days inside any symbol's history:** 0 for all 24.
- **Moves bigger than 15% in a day (adjusted close):** 30 for BTC-USD (range -37.2% to +25.2%; its Monday moves include the weekend), and 36 across the other funds: XLF 6, XLE 4, KRE 5, USO 5, SMH 3, EEM 3, XLK 1, XLRE 1, QQQ 1. All line up with known events (Oct 2008 crash, Mar 2020 COVID crash, Apr 2020 oil collapse, 3 Jan 2001 Fed rate cut, 9 Apr 2025 rally), so none look like data errors. Full list: `results/00_big_moves.csv`.
- **Dividend effect:** on the last day raw and adjusted close are equal (0.0 gap for all), because Yahoo adjusts history backwards from today. The real effect shows over time: e.g. SPY price-only return since 1999 is +527% vs +914% with dividends; TLT -1.9% vs +125.8%. GLD, USO and BTC-USD pay no dividends, so no gap.
- **Files:** `results/00_data_summary.csv`, `results/00_big_moves.csv`, `results/00_growth_since_2015.png`.
- **Last-row check:** SPY close on 2026-10-15 is 771.789978 in our saved data vs 771.79 on Twelve Data, so that row is a final close, not a mid-day pull. No change to notebook 00 was needed.
- **Takeaway:** The data is complete and believable. Use adjusted close for any return or correlation, since raw prices badly understate bond and dividend-heavy funds. Tests involving XLRE, XLC or BTC-USD have far less history, so results for them rest on a shorter period.

### Data notes
- **SMH before 2011-12-20** is the old Semiconductor HOLDRS, a different fund that used the same ticker.
- **Sector funds changed contents:** real estate left XLF for XLRE (Sept 2016); Alphabet and Meta moved from XLK, and Netflix and Disney from XLY, into the new XLC (Sept 2018). Results spanning those dates compare slightly different baskets.
- **USO** holds oil futures and loses value when it rolls contracts, so its long-run return understates oil's. Fine for daily correlations; don't read its multi-month returns as oil's performance.
- **BTC-USD's daily close** is at 00:00 UTC, about 4 hours after US stocks close. Matters for lead/lag tests (notebook 05).
- **Spot-checked against Twelve Data on 2026-10-15:** price-only returns for SPY, USO and TLT match; BTC within about 0.2%.
