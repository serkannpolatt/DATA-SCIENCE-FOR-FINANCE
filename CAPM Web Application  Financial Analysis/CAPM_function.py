import plotly.express as px
import numpy as np

def interactive_plot(df):
    """
    Veri çerçevesini çizgi grafiği şeklinde görselleştiren bir işlevdir.
    
    Visualizes the data frame as a line plot.
    
    Parametreler / Parameters:
        df: Veri çerçevesi / Data frame (pandas.DataFrame)
    
    Döndürülen değer / Returns:
        fig: Plotly figür nesnesi / Plotly figure object
    """
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df["Date"], y=df[i], name=i)
    fig.update_layout(width=450, margin=dict(l=20, r=20, t=50, b=20), legend=dict(orientation="h", yanchor="bottom",
                                                                                 y=1.02, xanchor="right", x=1,))
    return fig


def normalize(df_2):
    """
    Veri çerçevesindeki sütunları normalize eden bir işlevdir.
    Normalizasyon, her sütunun ilk değere bölünerek yapılır.
    
    Normalizes the columns in the data frame.
    Normalization is performed by dividing each column by its first value.
    
    Parametreler / Parameters:
        df_2: Veri çerçevesi / Data frame (pandas.DataFrame)
    
    Döndürülen değer / Returns:
        df: Normalize edilmiş veri çerçevesi / Normalized data frame (pandas.DataFrame)
    """
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i] / df[i][0]
    return df


def daily_return(df):
    """
    Veri çerçevesindeki günlük getirileri hesaplayan bir işlevdir.
    Günlük getiri, bir önceki güne göre değişimin yüzdesi olarak hesaplanır.
    
    Calculates the daily returns of the data frame.
    Daily return is calculated as the percentage change from the previous day.
    
    Parametreler / Parameters:
        df: Veri çerçevesi / Data frame (pandas.DataFrame)
    
    Döndürülen değer / Returns:
        df_daily_return: Günlük getirileri içeren veri çerçevesi / Data frame containing daily returns (pandas.DataFrame)
    """
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1, len(df)):
            df_daily_return[i][j] = ((df[i][j] - df[i][j-1]) / df[i][j-1]) * 100
        df_daily_return[i][0] = 0
    return df_daily_return


def calculate_beta(stocks_daily_return, stock):
    """
    Bir hisse senedinin beta katsayısını hesaplayan bir işlevdir.
    Beta katsayısı, hisse senedinin piyasa getirisiyle olan ilişkisini ölçer.
    
    Calculates the beta coefficient of a stock.
    The beta coefficient measures the relationship between a stock's return and the market return.
    
    Parametreler / Parameters:
        stocks_daily_return: Günlük getirileri içeren veri çerçevesi / Data frame containing daily returns (pandas.DataFrame)
        stock: Hesaplanacak hisse senedinin sütun adı / Column name of the stock to calculate beta (str)
    
    Döndürülen değerler / Returns:
        b: Beta katsayısı / Beta coefficient (float)
        a: Alfa katsayısı / Alpha coefficient (float)
    """
    rm = stocks_daily_return["sp500"].mean() * 252
    b, a = np.polyfit(stocks_daily_return["sp500"], stocks_daily_return[stock], 1)
    return b, a
