import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Investment Portfolio Dashboard / Yatırım Portföy Panosu")
assets = st.text_input("Provide your assets (comma-separated) / Varlıklarınızı girin (virgülle ayrılmış)", "BIMAS.IS, AKBNK.IS, TUPRS.IS, VAKBN.IS, GARAN.IS")
start = st.date_input("Pick a starting date for your analysis / Analiz için bir başlangıç tarihi seçin", value=pd.to_datetime("2022-06-01"))
data = yf.download(assets, start=start)["Adj Close"]

ret_df = data.pct_change()
cumul_ret = (ret_df + 1).cumprod() - 1
pf_cumul_ret = cumul_ret.mean(axis=1)

benchmark = yf.download("XU100.IS", start=start)["Adj Close"]
bench_ret = benchmark.pct_change()
bench_dev = (bench_ret + 1).cumprod() - 1

W = (np.ones(len(ret_df.columns)) / len(ret_df.columns))
pf_std = (W.dot(ret_df.cov()).dot(W))**(1/2)

st.subheader("Portfolio vs Index Development / Portföy ve Endeks Gelişimi")
tog = pd.concat([bench_dev, pf_cumul_ret], axis=1)
tog.columns = ["XU100 Performance", "Portfolio Performance / Portföy Performansı"]

st.line_chart(data=tog)

st.subheader("Portfolio Risk / Portföy Riski:")
pf_std
st.subheader("Benchmark Risk / Kıyaslama Riski:")
bench_risk = bench_ret.std()
bench_risk

st.subheader("Portfolio Composition / Portföy Kompozisyonu:")
fig, ax = plt.subplots(facecolor='#121212')
ax.pie(W, labels=data.columns, autopct='%1.1f%%', textprops={'color': 'white'})
st.pyplot(fig)
