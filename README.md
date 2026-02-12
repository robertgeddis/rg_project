🪙 Is Bitcoin Really 'Digital Gold'? 📊

This project conducts a data-driven investigation into the 'Digital Gold' hypothesis. 
By analyzing 10 years of market data, I test whether Bitcoin behaves as a safe-haven asset, an inflation hedge, or simply a high-beta technology stock.



🧠 Research Hypotheses

1. Safe Haven Test: When the S&P 500 crashes, do Bitcoin and Gold move inversely to the market, or does Bitcoin crash alongside equities?
2. Inflation Hedge: During the 2022–2024 inflationary spike, which asset better protected purchasing power?
3. Correlation Shift: Has the institutionalization of Bitcoin (via ETFs) coupled its price action more tightly with Gold?



🛠️ Data & Methodology

Data Sources
I utilize the yfinance library to extract 10 years of daily historical data for: 
  - Bitcoin (BTC-USD)
  - Gold (GC=F)
  - S&P 500 (^GSPC)

Data Pipeline
- Cleaning: Resolved the 'Weekend Gap' issue — since Bitcoin trades 24/7 while Gold and the S&P 500 do not, I aligned timestamps to standard trading days.
- Normalization: Because of the massive price disparity (e.g., $100k BTC vs $2k Gold), I utilized Log Returns and Indexed Returns (Base 100) to ensure a fair 'apples-to-apples' comparison.



📈 Analysis Workflow

1. Exploratory Data Analysis
A 'big picture' view of all three assets over the last decade to identify general trends and growth cycles.

2. Crisis Deep-Dives
I 'zoom in' on critical economic pivots:
- 2020 COVID Crash: Testing immediate liquidity responses.
- 2022–2024 Inflationary Period: Evaluating purchasing power protection.
- 2024 ETF Era: Analyzing the impact of institutional entry.

3. Correlation & Volatility
- Rolling Correlation: A time-series heatmap visualizing how the relationship between BTC and Gold evolves.
- Volatility Analysis: Calculating the standard deviation of returns to compare the 'risk' profile of each asset.



🚀 Getting Started

Prerequisites
Bash
pip install yfinance pandas matplotlib seaborn numpy

Usage
Clone the repository:

Bash
git clone https://github.com/robertgeddis/rg_project.git

Run the analysis:

Bash
python main_analysis.py



⚖️ Final Verdict
TBC. 



📬 Contact & Contributions
Feel free to open an issue or submit a pull request if you have ideas for additional metrics (e.g. M2 Money Supply correlation).

Author: Robert Geddis
