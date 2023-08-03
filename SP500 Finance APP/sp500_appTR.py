import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

st.title('S&P 500 Uygulaması')

st.markdown("""
Bu uygulama, **S&P 500** listesini (Wikipedia'dan) ve buna karşılık gelen **hisse senedi kapanış fiyatlarını** (yılın başından itibaren) alır!
* **Python kütüphaneleri:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Veri kaynağı:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('Kullanıcı Giriş Özellikleri')

# S&P 500 verilerini web scraping yapma
@st.cache
def veri_yukle():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df

df = veri_yukle()
sektor = df.groupby('GICS Sector')

# Kenar çubuğu - Sektor seçimi
sirali_sektor_unique = sorted(df['GICS Sector'].unique())
secilen_sektor = st.sidebar.multiselect('Sektor', sirali_sektor_unique, sirali_sektor_unique)

# Verileri filtreleme
df_secilen_sektor = df[(df['GICS Sector'].isin(secilen_sektor))]

st.header('Seçilen Sektördeki Şirketlerin Gösterimi')
st.write('Veri Boyutu: ' + str(df_secilen_sektor.shape[0]) + ' satır ve ' + str(df_secilen_sektor.shape[1]) + ' sütun.')
st.dataframe(df_secilen_sektor)

# S&P500 verilerini indirme
def dosya_indir(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # stringler <-> baytlar dönüşümleri
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">CSV Dosyasını İndir</a>'
    return href

st.markdown(dosya_indir(df_secilen_sektor), unsafe_allow_html=True)

# https://pypi.org/project/yfinance/

data = yf.download(
        tickers=list(df_secilen_sektor[:10].Symbol),
        period="ytd",
        interval="1d",
        group_by='ticker',
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None
    )

# Sorgu Sembolünün Kapanış Fiyatını Çizdir
def fiyat_grafiği(sembol):
  df = pd.DataFrame(data[sembol].Close)
  df['Tarih'] = df.index
  plt.fill_between(df.Tarih, df.Close, color='skyblue', alpha=0.3)
  plt.plot(df.Tarih, df.Close, color='skyblue', alpha=0.8)
  plt.xticks(rotation=90)
  plt.title(sembol, fontweight='bold')
  plt.xlabel('Tarih', fontweight='bold')
  plt.ylabel('Kapanış Fiyatı', fontweight='bold')
  return st.pyplot()

num_sirket = st.sidebar.slider('Şirket Sayısı', 1, 5)

if st.button('Grafikleri Göster'):
    st.header('Hisse Senedi Kapanış Fiyatları')
    for i in list(df_secilen_sektor.Symbol)[:num_sirket]:
        fiyat_grafiği(i)
