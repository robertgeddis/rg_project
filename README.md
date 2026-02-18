# Is Bitcoin Really 'Digital Gold'? 🪙

An analytical investigation into the correlation between Bitcoin and Gold.

---

## 🔬 Hypothesis

* **Safe Haven:** Does Bitcoin act like a fail safe such as Gold or a tech stock?
* **Inflation Hedge:** How did Bitcoin and Gold behave during the record inflation of 2022-2024?
* **Institutional Coupling:** Has institutional investment in Bitcoin made it more like Gold or like a tech stock?

---

## 📊 Data Details

* **Source:** 10 years of daily market data from the `yfinance` library and 10 years monthly macro data from the pandas_datareader library. 
* **Cleaning:** * Handled the 'Weekend Gap' for non-Bitcoin market price data by creating both forward filled and synced versions to ensure consistent comparison.
* **Normalization:** Applied Base-100 indexing for market price data to allow for an accurate comparison between a $100k asset (BTC) and a $2k asset (Gold).

---

## 📈 Analysis Workflow

1. **Exploratory Analysis:** Plotting the 'Big Picture' to see long-term trends across all market based price metrics.
2. **Correlations and Trends:** Exploring the relationship between Bitcoin, Gold and macro-economic indexes.
3. **Causality and Forecasting:** Testing relationsips between Bitcoin and macro-economic indexes to test the gold vs stock thesis.

---

## 🏁 Conclusion

TBC
