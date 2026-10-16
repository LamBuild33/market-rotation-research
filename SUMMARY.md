# Market rotation research: summary

Built October 2026. Tests whether the ideas behind my sector rotation dashboard
hold up on real history.

## How the testing worked
- Data: 24 funds (S&P 500, 11 sectors, 4 industries, Nasdaq-100, small caps, gold,
  long-term bonds, oil, the dollar, emerging markets, Bitcoin), daily prices from
  1999, adjusted for dividends. Spot-checked against Twelve Data.
- Every idea was tested on 1999-2020 first ("build years"), then checked ONCE on
  2021-2026 ("test years") that it had never seen.
- Guesses were written down and committed BEFORE each test, so results couldn't be
  explained away afterward.
- Trading cost: 0.10% per trade. Results broken down year by year.

## What held up
- **Some markets reliably move opposite.** The dollar and gold moved opposite every
  year for 20 years (from -0.19 to -0.65, typically about -0.4). Relationships found
  with the market's own moves removed mostly kept their direction on new data (87%).
- **Market mood predicts bumpiness, not direction.** After the S&P 500 was in a
  downtrend (below its 200-day average), the next month's swings were about twice
  as big as after an uptrend (about 25% vs 13% a year). It did not predict whether
  the market went up or down.
- **Big down days come in bunches, and the same sectors cushion them.** After a big
  down day, another often followed within a week. On those days, consumer staples,
  utilities and health care fell less than the S&P 500 in both periods.

## What didn't hold up
- **Volume check:** whether volume "confirmed" a move didn't predict whether it
  continued. Removed from the dashboard.
- **Top-5 sectors:** holding last month's top 5 sectors trailed holding all sectors
  equally by about 2.5% a year (1999-2020) and 3.1% a year (2021-2026) after costs.
  Before costs it still trailed, by about 1.4% and 1.7% a year, and won about 48.5%
  of periods.
- **Rotation map zones:** no zone (Leading, Fading, Improving, Lagging) predicted the
  next month. The clockwise drift through the zones comes from how the map is
  drawn: it appeared just as strongly with the days shuffled at random.
- **Who moves first:** no fund reliably led another by enough to use. An apparent
  "bounce back the next day" came mostly from panic years (2007-2008 and 2020) and
  faded.
- **Rotation thermometer:** how spread out the sectors were weakly predicted next
  month's spread in 1999-2020, but in 2021-2026 the link weakened from 0.46 to 0.18,
  too small to tell apart from zero.

## What changed over time
- **Stocks and bonds:** moved opposite in 16 of 18 build years, but together in 5
  of 6 test years. Bonds stopped cushioning stock sell-offs after 2020, and so did
  gold.
- **Who falls most on bad days:** financials and energy in 1999-2020; chips, tech
  and consumer discretionary in 2021-2026.

## Lessons
- A description of the recent past isn't a prediction. Most dashboard labels turned
  out to be descriptions.
- Some patterns come from how they are measured (the clockwise drift).
- Some patterns come from a few wild years and fade when markets calm down.
- A recurring hint, never formally tested: recent leaders did slightly worse and
  recent laggards slightly better afterward.

## Dashboard changes (2026-10-15 to 2026-10-16)
- Removed: Volume check column.
- Reworded: Up-day share, Top 5 (description, not a buy list; tags gray), rotation
  map intro and zone definitions.
- Added: Market mood card (description and next-month bumpiness only), with one
  line on which sectors cushion big down days.
- Not added: rotation thermometer.

## Still to do
- Scheduled check: the 02 vs-sector volume lead (F1), no earlier than 2027-10-15.
  Rerun notebook 00 first.
- Possible future test: leaders vs laggards, with its own predictions on fresh data.
