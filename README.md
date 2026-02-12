# Is Bitcoin Really 'Digital Gold'? 🪙

An analytical investigation into the correlation between Bitcoin, Gold, and the S&P 500.

---

## 🔬 Hypothesis

* **Safe Haven:** When the stock market crashes, do Bitcoin and Gold both go up? Or does Bitcoin crash like a high-risk 'Tech Stock'?
* **Inflation Hedge:** During the period of record global inflation (2022-2024), which asset protected purchasing power better?
* **Correlation Shift:** Has the relationship between Bitcoin and Gold remained constant, or have they become more coupled as institutional investors buy both?

---

## 📊 Data Details

* **Source:** 10 years of daily price data for Gold, Bitcoin and the S&P 500 from the `yfinance` library.
* **Cleaning:** * Handled the 'Weekend Gap' for Gold and S&P 500 by aligning timestamps to ensure consistent day-to-day comparison.
* **Normalization:** Applied **Log Scale** and **Indexed Returns** to allow for an accurate comparison between a $100k asset (BTC) and a $2k asset (Gold).

---

## 📈 Analysis Workflow

1. **Exploratory Analysis:** Plotting the 'Big Picture' to see long-term trends across all three assets.
2. **Crisis Deep-Dive:** Zooming in on specific volatility windows (2020 COVID, 2022-2024 Inflation).
3. **Visualizing Relationships:** Using Heatmaps and Rolling Correlation to track shifting sentiments.

---

## 🏁 Conclusion

Check the notebooks in this repository for the final data-driven verdict!
