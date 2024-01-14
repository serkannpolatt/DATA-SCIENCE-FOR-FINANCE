import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_tickers(url):
    page = requests.get(url).text
    page_bs = BeautifulSoup(page, "lxml")

    tickers = []
    ticker_elements = page_bs.find("div", class_="column-type7 wmargin").find_all("div", class_="comp-cell _02 vtable")

    for element in ticker_elements:
        ticker = element.get_text(strip=True).replace('\n', '') + ".IS"
        tickers.append(ticker)

    return tickers

def save_tickers_to_csv(tickers, filename):
    df = pd.DataFrame(tickers, columns=['Ticker'])
    df.to_csv(filename, index=False, header=False)

if __name__ == "__main__":
    URL = "https://www.kap.org.tr/en/Pazarlar"
    tickers_list = get_tickers(URL)
    save_tickers_to_csv(tickers_list, "Tickers.csv")
