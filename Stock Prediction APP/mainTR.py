import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Hisse Senedi Tahmin Uygulaması')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Tahmin için veri seti seçin', stocks)

n_years = st.slider('Tahmin yılı:', 1, 4)
period = n_years * 365  # Sabit dönem uzunluğu

@st.cache_data(ttl=600)  # Önbellekte tutma süresini (TTL) saniye cinsinden belirleyin (600 saniye = 10 dakika)
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Veriler yükleniyor...')
data = load_data(selected_stock)
data_load_state.text('Veriler yükleniyor... tamamlandı!')

st.subheader('Ham veriler')
st.write(data.tail())

# Ham verileri çizdir
def plot_raw_data():
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Open'], label="Açılış fiyatı")
    plt.plot(data['Date'], data['Close'], label="Kapanış fiyatı")
    plt.title('Zaman Serisi Verileri ve Kaydırılabilir Aralık')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat')
    plt.legend()
    st.pyplot(plt)

plot_raw_data()

# ARIMA ile tahmin yap
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
df_train['ds'] = pd.to_datetime(df_train['ds'])

# ARIMA modelini uydur
model = ARIMA(df_train['y'], order=(5, 1, 0))
model_fit = model.fit()

# Tahmin
forecast_values = model_fit.forecast(steps=period)

# Tahmin veri çerçevesi oluştur
forecast_dates = pd.date_range(df_train['ds'].iloc[-1], periods=period + 1, freq='D')
forecast_df = pd.DataFrame({
    'ds': forecast_dates[:-1],  # Tahminde son tarihi hariç tut
    'yhat': forecast_values,
})

# Tahmini göster ve çizdir
st.subheader('Tahmin verileri')
st.write(forecast_df.tail())

st.write(f'{n_years} yıl için tahmin grafiği')
plt.figure(figsize=(12, 6))
plt.plot(df_train['ds'], df_train['y'], label="Geçmiş Veriler")
plt.plot(forecast_df['ds'], forecast_df['yhat'], label="Tahmin", color='r')
plt.title('Hisse Senedi Fiyat Tahmini')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
st.pyplot(plt)

st.write("Tahmin bileşenleri")
# Şu an için Prophet kullanmıyoruz, bu nedenle tahminin ayrı bileşenlerini çizdiremiyoruz.
st.write("Alternatif kütüphane ayrı bileşen çizimleri sağlamıyor.")
