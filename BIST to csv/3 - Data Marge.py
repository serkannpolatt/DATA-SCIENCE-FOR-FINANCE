import glob
import os
import pandas as pd

csv_list = glob.glob(os.path.join("History Data", "*.csv"))
merged = pd.DataFrame()

for i in csv_list:
    ticker_name = os.path.splitext(os.path.basename(i))[0]
    print(ticker_name)

    ticker = pd.read_csv(i)
    ticker = ticker.rename(columns={"Close": ticker_name})
    ticker.set_index("Date", inplace=True)  # Added inplace=True to set the index in the same DataFrame
    merged = merged.join(ticker, how="outer")

merged.to_csv("MergedData.csv")
