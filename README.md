Is Bitcoin Really 'Digital Gold'? 🪙
An analytical investigation into the correlation between Bitcoin, Gold, and the S&P 500 over a 10-year period.

🔬 Hypothesis
Safe Haven: When the stock market crashes, do Bitcoin and Gold both go up? Or does Bitcoin crash like a high-risk 'Tech Stock'?

Inflation Hedge: During the period of record global inflation (2022-2024), which asset protected purchasing power better?

Correlation Shift: Has the relationship between Bitcoin and Gold remained constant, or have they become more coupled as institutional investors buy both?

📊 Data Details
Source: Using the yfinance library to pull 10 years of daily price data for Gold, Bitcoin, and the S&P 500.

Cleaning: * Handled the "Weekend Gap" for Gold and S&P 500 (since Bitcoin trades 24/7 while traditional markets do not).

Aligned timestamps to ensure consistent day-to-day comparison.

Normalization: Applied Log Scale and Indexed Returns to allow for an accurate comparison between a $100k asset (BTC) and a $2k asset (Gold).

📈 Analysis Workflow
Exploratory Analysis: Plotting the "Big Picture" to see long-term trends across all three assets.

Crisis Deep-Dive: Zooming in on specific volatility windows:

2020: The COVID-19 Market Crash.

2022–2024: Period of record-high inflation.

2024: The launch of Bitcoin ETFs.

Visualizing Relationships:

Heatmaps: Showing how the relationship between assets changes over time.

Rolling Correlation: Calculating coefficients and volatility to track shifting sentiments.

🏁 Conclusion
The Verdict: Based on the data, is Bitcoin truly "Digital Gold" or something else entirely?

(Check the notebooks in this repository for the data-driven results!)
