"""
This application performs a stock breakout strategy analysis using Streamlit, 
YFinance, and Plotly. It allows users to input stock tickers, dates, and thresholds 
to analyze breakout trading opportunities and provides both summary statistics 
and visualizations.
"""

import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Set up the Streamlit app with a title and wide layout
st.set_page_config(page_title="Stock Breakout Analysis", layout="wide")

# Display the main title of the app
st.title('Stock Breakout Strategy Analyzer')

# A custom Streamlit fragment to add a reusable download button without refreshing the app
@st.fragment
def download_button_no_refresh(label, data, file_name, mime):
    st.download_button(label=label, data=data, file_name=file_name, mime=mime)

# Function to fetch stock data using Yahoo Finance
def get_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data for the given ticker and date range.
    Adjusts the start date by 30 days to ensure data availability for rolling averages.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        DataFrame: Historical stock data or None if an error occurs.
    """
    adjusted_start = (pd.to_datetime(start_date) - timedelta(days=30)).strftime('%Y-%m-%d')
    
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(start=adjusted_start, end=end_date)
        return df
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {str(e)}")
        return None

# Function to analyze breakout conditions based on user thresholds
def analyze_breakouts(df, volume_threshold, price_threshold, holding_period):
    """
    Identifies breakout days based on volume and price thresholds, calculates returns, 
    and stores results in a DataFrame.

    Args:
        df (DataFrame): Historical stock data.
        volume_threshold (float): Minimum volume ratio threshold (percentage).
        price_threshold (float): Minimum daily return threshold (percentage).
        holding_period (int): Number of days to hold after a breakout.

    Returns:
        DataFrame: Results with entry/exit dates, prices, returns, and volume ratios.
    """
    # Calculate moving averages, daily returns, and volume ratio
    df['Volume_MA20'] = df['Volume'].rolling(window=20).mean()  # 20-day moving average of volume
    df['Daily_Return'] = df['Close'].pct_change()  # Daily percentage change in closing price
    df['Volume_Ratio'] = df['Volume'] / df['Volume_MA20']  # Ratio of current volume to its moving average
    
    # Breakout condition based on thresholds
    breakout_condition = (df['Volume_Ratio'] > volume_threshold/100) & \
                         (df['Daily_Return'] > price_threshold/100)
    
    breakout_results = []
    breakout_days = df[breakout_condition].index

    # Calculate returns for each breakout day
    for breakout_day in breakout_days:
        try:
            entry_price = df.loc[breakout_day, 'Close']
            entry_date = breakout_day
            exit_date_idx = min(df.index.get_loc(breakout_day) + holding_period, len(df) - 1)
            exit_date = df.index[exit_date_idx]
            exit_price = df.iloc[exit_date_idx]['Close']
            trade_return = (exit_price - entry_price) / entry_price * 100  # Percentage return
            
            breakout_results.append({
                'Entry_Date': entry_date.strftime('%Y-%m-%d'),
                'Entry_Price': round(entry_price, 2),
                'Exit_Date': exit_date.strftime('%Y-%m-%d'),
                'Exit_Price': round(exit_price, 2),
                'Return_Pct': round(trade_return, 2),
                'Volume_Ratio': round(df.loc[breakout_day, 'Volume_Ratio'], 2)
            })
        except Exception as e:
            st.warning(f"Could not calculate returns for breakout on {breakout_day}: {str(e)}")
            continue
            
    return pd.DataFrame(breakout_results)

# Function to compute summary statistics for breakout trades
def create_summary_stats(results_df):
    """
    Computes summary statistics such as total trades, win rate, and return metrics.

    Args:
        results_df (DataFrame): Results from the breakout analysis.

    Returns:
        Series: Summary statistics for the analyzed trades.
    """
    if len(results_df) == 0:
        return pd.Series({
            'Total_Trades': 0,
            'Win_Rate': 0,
            'Average_Return': 0,
            'Max_Return': 0,
            'Min_Return': 0,
            'Std_Dev': 0
        })
    
    summary = {
        'Total_Trades': len(results_df),
        'Win_Rate': (results_df['Return_Pct'] > 0).mean() * 100,  # Percentage of profitable trades
        'Average_Return': results_df['Return_Pct'].mean(),
        'Max_Return': results_df['Return_Pct'].max(),
        'Min_Return': results_df['Return_Pct'].min(),
        'Std_Dev': results_df['Return_Pct'].std()
    }
    return pd.Series(summary).round(2)

# Sidebar input elements for user parameters
st.sidebar.header('Enter Parameters')

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    ticker_input = st.text_input('Stock Ticker(s)', value='', placeholder='e.g., AMZN, TSLA')

tickers = [t.strip().upper() for t in ticker_input.split(',') if t.strip()]

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    start_date = st.date_input('Start Date', value=datetime.now() - timedelta(days=365))

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    end_date = st.date_input('End Date', value=datetime.now())

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    volume_threshold = st.number_input('Volume Breakout Threshold (%)', value=200, min_value=50)

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    price_threshold = st.number_input('Daily Change Threshold (%)', value=2.0, min_value=0.1)

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    holding_period = st.number_input('Holding Period (Days)', value=10, min_value=1)

# Validate inputs
if start_date >= end_date:
    st.sidebar.error("Start date must be earlier than the end date.")
if end_date > datetime.now().date():
    st.sidebar.error("End date cannot be in the future.")
if not tickers:
    st.sidebar.error('Please enter at least one stock ticker to proceed.')

# Generate report upon button click
if st.sidebar.button('Generate Report', key='generate_report_button'):
    if tickers:
        tabs = st.tabs(tickers)
        for idx, ticker in enumerate(tickers):
            with tabs[idx]:
                df = get_stock_data(ticker, start_date, end_date)
                if df is None or df.empty:
                    st.error(f"No data found for ticker: {ticker}. Please check the symbol.")
                else:
                    results_df = analyze_breakouts(df, volume_threshold, price_threshold, holding_period)
                    if not results_df.empty:
                        st.header(f'Analysis for {ticker}')
                        
                        st.subheader('Summary Statistics')
                        summary_stats = create_summary_stats(results_df)
                        cols = st.columns(3)
                        for i, (label, value) in enumerate(summary_stats.items()):
                            cols[i % 3].metric(label=label, value=value)
                        
                        st.subheader('Detailed Trade Results')
                        st.dataframe(results_df)

                        st.subheader('Stock Data Visualization')
                        
                        # Plot stock price as a candlestick chart
                        fig_price = go.Figure(data=[go.Candlestick(
                            x=df.index,
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close']
                        )])
                        fig_price.update_layout(title=f'{ticker} Stock Price Over Time', xaxis_title='Date', yaxis_title='Price (USD)')
                        st.plotly_chart(fig_price)

                        # Plot volume over time as a bar chart
                        fig_vol = go.Figure(data=[go.Bar(
                            x=df.index,
                            y=df['Volume']
                        )])
                        fig_vol.update_layout(title=f'{ticker} Volume Over Time', xaxis_title='Date', yaxis_title='Volume')
                        st.plotly_chart(fig_vol)

                        # Plot the distribution of returns as a histogram
                        fig_returns = go.Figure(data=[go.Histogram(
                            x=results_df['Return_Pct'],
                            nbinsx=20
                        )])
                        fig_returns.update_layout(xaxis_title='Return (%)', yaxis_title='Frequency')
                        st.plotly_chart(fig_returns)

                        # Provide a download link for the results
                        csv_data = results_df.to_csv(index=False).encode('utf-8')
                        download_button_no_refresh(
                                label="Download Results CSV",
                                data=csv_data,
                                file_name=f"{ticker}_breakout_analysis.csv",
                                mime="text/csv"
                        )
                    else:
                        st.warning(f'No breakout conditions found for {ticker} with the given parameters.')
    else:
        st.error('Please enter at least one stock ticker to proceed.')
