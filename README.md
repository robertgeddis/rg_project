# Is Bitcoin Really 'Digital Gold'? 🪙

An analytical investigation into the correlation between Bitcoin and Gold.

---

## 🔬 Hypothesis

* **Safe Haven:** When the stock market crashes, do Bitcoin and Gold both go up? Or does Bitcoin crash like a high-risk 'Tech Stock'?
* **Inflation Hedge:** During the period of record global inflation (2022-2024), which asset protected purchasing power better?
* **Correlation Shift:** Has the relationship between Bitcoin and Gold remained constant, or have they become more coupled as institutional investors buy both?

---

## 📊 Data Details

* **Source:** 10 years of daily market data from the `yfinance` library and 10 years monthly macro data from the pandas_datareader library. 
* **Cleaning:** * Handled the 'Weekend Gap' for non-Bitcoin market price data by creating both forward filled and synced versions to ensure consistent comparison.
* **Normalization:** Applied Base-100 indexing for market price data to allow for an accurate comparison between a $100k asset (BTC) and a $2k asset (Gold).

---

## 📈 Analysis Workflow

1. **Exploratory Analysis:** Plotting the 'Big Picture' to see long-term trends across all market prices and macro indexes.
2. **Crisis Deep-Dive:** Zooming in on specific volatility windows (2020 COVID, 2022-2024 Inflation).
3. **Visualizing Relationships:** Using Heatmaps and Rolling Correlation to track shifting sentiments.

---

## 🏁 Conclusion

TBC
