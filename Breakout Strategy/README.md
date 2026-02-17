# Multi-Timeframe NY Session Breakout Strategy

A Python-based algorithmic trading strategy that combines **multi-timeframe analysis** with **New York session breakouts** for forex and commodities trading.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Research-yellow.svg)

## 📋 Overview

This project implements a systematic breakout trading strategy that:

1. **Analyzes daily candlestick patterns** to determine directional bias (bullish/bearish)
2. **Transfers signals to hourly timeframe** for precise entry timing
3. **Executes breakout trades** based on session high/low levels
4. **Manages risk** through automated position closing at session end

## 🎯 Strategy Logic

### Daily Signal Generation
- **Bullish Signal (2)**: Previous day's close > open (green candle)
- **Bearish Signal (1)**: Previous day's close < open (red candle)

### Intraday Execution
- **For Bullish Bias**: Set buy stop at the highest high of the first N candles
- **For Bearish Bias**: Set sell stop at the lowest low of the first N candles
- **Exit**: Close all positions after specified delay period

### Key Parameters
| Parameter | Default | Description |
|-----------|---------|-------------|
| `test_candles` | 8 | Number of candles to determine session range |
| `exit_delay` | 4 | Days to hold position before exit |
| `cash` | 5000 | Initial capital |
| `margin` | 1/5 | Margin requirement (20%) |

## 📁 Project Structure

```
MutliTimeframe_NY_Session_Break_Out/
│
├── main.ipynb                 # Main strategy notebook
├── README.md                  # Project documentation
│
├── data_daily/                # Daily candlestick data
│   ├── USDJPY_Candlestick_1_D_BID_*.csv
│   └── XAUUSD_Candlestick_1_D_BID_*.csv
│
└── data_hourly/               # 2-hour candlestick data
    ├── USDJPY_Candlestick_2_Hour_BID_*.csv
    └── XAUUSD_Candlestick_2_Hour_BID_*.csv
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook / VS Code with Jupyter extension

### Dependencies

```bash
pip install pandas numpy pandas-ta plotly matplotlib tqdm backtesting
```

### Required Libraries
| Library | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computations |
| `pandas-ta` | Technical analysis indicators |
| `plotly` | Interactive charting |
| `matplotlib` | Static visualizations |
| `tqdm` | Progress bars |
| `backtesting` | Strategy backtesting framework |




### Equity Curve
The notebook generates equity curves comparing strategy performance across different instruments (USDJPY, XAUUSD).

## 📈 Instruments Supported

| Instrument | Timeframe | Data Range |
|------------|-----------|------------|
| USD/JPY | Daily, 2-Hour | Jun 2015 - Jun 2024 |
| XAU/USD | Daily, 2-Hour | Jun 2015 - Jun 2024 |

## ⚙️ Customization

### Modify Strategy Parameters

```python
# In the notebook, adjust these values:
hourly_df = apply_strategy_dataframes(hourly_df, 
                                       test_candles=8,  # Adjust breakout period
                                       exit_delay=4)    # Adjust holding period
```

### Backtest Settings

```python
bt = Backtest(df, Strat_01, 
              cash=5000,      # Initial capital
              margin=1/5,     # Margin requirement
              commission=0.0) # Commission per trade
```

## 📝 Data Format

The strategy expects CSV files with the following columns:
- `Gmt time`: Timestamp in format `DD.MM.YYYY HH:MM:SS`
- `Open`: Opening price
- `High`: Highest price
- `Low`: Lowest price
- `Close`: Closing price
- `Volume`: Trading volume

## ⚠️ Disclaimer

**This project is for educational and research purposes only.** 

- Past performance does not guarantee future results
- Trading forex and commodities involves substantial risk of loss
- Always perform your own due diligence before trading
- This is not financial advice

