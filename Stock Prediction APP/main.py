import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365  # Fix the period length

@st.cache_data(ttl=600)  # Set the time-to-live (TTL) for the cache in seconds (600 seconds = 10 minutes)
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Open'], label="stock_open")
    plt.plot(data['Date'], data['Close'], label="stock_close")
    plt.title('Time Series data with Rangeslider')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(plt)

plot_raw_data()

# Predict forecast with ARIMA.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
df_train['ds'] = pd.to_datetime(df_train['ds'])

# Fit ARIMA model
model = ARIMA(df_train['y'], order=(5, 1, 0))
model_fit = model.fit()

# Forecast
forecast_values = model_fit.forecast(steps=period)

# Create forecast dataframe
forecast_dates = pd.date_range(df_train['ds'].iloc[-1], periods=period + 1, freq='D')
forecast_df = pd.DataFrame({
    'ds': forecast_dates[:-1],  # Exclude the last date in the forecast
    'yhat': forecast_values,
})

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast_df.tail())

st.write(f'Forecast plot for {n_years} years')
plt.figure(figsize=(12, 6))
plt.plot(df_train['ds'], df_train['y'], label="Historical Data")
plt.plot(forecast_df['ds'], forecast_df['yhat'], label="Forecast", color='r')
plt.title('Stock Price Forecast')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
st.pyplot(plt)

st.write("Forecast components")
# Since we are not using Prophet now, we don't have individual components to plot.
st.write("Alternative library does not provide individual component plots.")
