import streamlit as st 
import pandas as pd 
import yfinance as yf
import pandas_datareader.data as web
import datetime 
import CAPM_function

st.set_page_config(page_title="CAPM",
                   page_icon="chart_with_upwards_trend",
                   layout="wide")



st.title("Capital Assest Pricing Model / Sermaye Varlıkları Fiyatlandırma Modeli")


col1,col2=st.columns([1,1])

with col1:
    stock_list=st.multiselect("Choose 4 stocks / 4 hisse senedi seçin",("TSLA","AAPL","NFLX","MSFT","MGM","AMZN","NVDA","GOOGL"),["TSLA","AAPL","AMZN","GOOGL"])
with col2:
    year=st.number_input("Number of years / Yılların sayısı",1,10)


try:

    end=datetime.date.today()
    start=datetime.date(datetime.date.today().year-year,datetime.date.today().month,datetime.date.today().day)
    SP500=web.DataReader(["sp500"],"fred",start,end)
    #print(SP500.tail())

    stocks_df=pd.DataFrame()

    for stock in stock_list:
        data=yf.download(stock,period=f"{year}y")
        stocks_df[f"{stock}"]=data["Close"]

    stocks_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)
    SP500.columns=["Date","sp500"]
    stocks_df["Date"]=stocks_df["Date"].astype("datetime64[ns]")
    stocks_df["Date"]=stocks_df["Date"].apply(lambda x:str(x)[:10])
    stocks_df["Date"]=pd.to_datetime(stocks_df["Date"])
    stocks_df=pd.merge(stocks_df,SP500,on="Date",how="inner")

    col1,col2=st.columns([1,1])
    with col1:
        st.markdown("### Dataframe Head / İlk 5 Veri")
        st.dataframe(stocks_df.head(),use_container_width=True)
    with col2:
        st.markdown("### Dataframe Tail / Son 5 Veri")
        st.dataframe(stocks_df.tail(),use_container_width=True)


    col1,col2=st.columns([1,1])
    with col1:
        st.markdown("### Price of all the Stocks / Tüm Hisselerin Fiyatı")
        st.plotly_chart(CAPM_function.interactive_plot(stocks_df))
    with col2:
        st.markdown("### Price of all the stocks (after normalizing) / Tüm hisse senetlerinin fiyatı (normalize edildikten sonra)")
        st.plotly_chart(CAPM_function.interactive_plot(CAPM_function.normalize(stocks_df)))

    stocks_daily_return=CAPM_function.daily_return(stocks_df)
    print(stocks_daily_return.head())


    beta={}
    alpha={}

    for i in stocks_daily_return.columns:
        if i !="Date" and i !="SP500":
            b,a=CAPM_function.calculate_beta(stocks_daily_return,i)

            beta[i]=b
            alpha[i]=a
    print(beta,alpha)

    beta_df=pd.DataFrame(columns=["Stock","Beta Value"])
    beta_df["Stock"]=beta.keys()
    beta_df["Beta Value"]=[str(round(i,2)) for i in beta.values()]

    with col1:
        st.markdown("### Calculated Beta Value / Hesaplanan Beta Değeri")
        st.dataframe(beta_df,use_container_width=True)

    rf=0
    rm=stocks_daily_return["sp500"].mean()*252

    return_df=pd.DataFrame()
    return_value=[]

    for stock,value in beta.items():
        return_value.append(str(round(rf+(value*(rm-rf)),2)))
    return_df["Stock"]=stock_list
    return_df["Return Value"]=return_value

    with col2:
        st.markdown("### Calculated Return using CAPM / CAPM kullanılarak Hesaplanan Getiri")
        st.dataframe(return_df,use_container_width=True)

except:
    st.write("Please select valid inputs / Lütfen geçerli girişler seçin")