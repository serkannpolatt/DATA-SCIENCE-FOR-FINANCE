import os
import pandas as pd
import yfinance as yf
from datetime import datetime

def download_save_stock_data(ticker, start_date, end_date, output_folder):
    data = yf.download(ticker, start=start_date, end=end_date)["Close"]
    filename = os.path.join(output_folder, f"{ticker}.csv")
    data.to_csv(filename)
    print(f"{ticker} Done")

if __name__ == "__main__":
    ticker_file = 'Tickers.csv'
    output_folder = "./History Data/"
    start_date = '2020-01-01'
    end_date = '2022-07-29'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tickers_df = pd.read_csv(ticker_file)
    
    # Assuming the column name might be different, use the first column
    tickers_list = tickers_df.iloc[:, 0].to_numpy()

    for ticker in tickers_list:
        download_save_stock_data(ticker, start_date, end_date, output_folder)

