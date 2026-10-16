# market-rotation-research

A research repo that tests the ideas behind my sector-rotation dashboard and studies how money moves between markets. Notebooks are built one at a time.

## Data
24 symbols of daily prices from Yahoo Finance (via yfinance), 1999 to today (each fund starts on its own date):

- Benchmark: SPY
- 11 sectors: XLK XLE XLV XLU XLF XLI XLB XLP XLY XLC XLRE
- 4 industries: SMH XBI KRE ITA
- Other markets: QQQ IWM GLD TLT USO UUP EEM
- Bitcoin: BTC-USD (kept only on stock-market trading days)

## Ground rules (locked in `config.py`)
- Build years: start through 2020-12-31. Test years: 2021-01-01 onward. Ideas and cutoffs are chosen on build years only, then checked once on test years.
- Trading cost: 0.10% per trade in any "would I have made money" test.
- Sector average = equal-weight average of whichever of the 11 sectors exist on that date (XLRE starts 2015, XLC 2018).

## Setup
```
conda env create -f environment.yml
conda activate rotation
python -m ipykernel install --user --name rotation
```
Then run `notebooks/00_data.ipynb` to download prices into `data/` (git-ignored).

## Notebook plan
00 Data · 01 Who moves together · 02 Volume check (test the 55%/45% up-day cutoffs) · 03 Top-5 test · 04 Rotation map zones · 05 Who moves first · 06 Market moods · 07 Big-day reactions · 08 Rotation thermometer · Later: real fund-flow data, monthly report.
