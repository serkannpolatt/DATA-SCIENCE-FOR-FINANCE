import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Sadece sayı girin.")

def get_valid_ticker_input(prompt):
    while True:
        try:
            ticker = input(prompt).upper()
            # Add additional validation for the ticker if needed
            return ticker
        except:
            print("Geçerli hisse kodu giriniz.")

def main():
    big_data = pd.read_csv("MergedData.csv")

    selected_tickers = []
    num_of_tickers = get_integer_input("Kaç tane hissenin kolerasyonuna bakacaksınız?\n")

    for i in range(num_of_tickers):
        ticker = get_valid_ticker_input(f"{i + 1} numaralı hissenin kodunu giriniz.\n")
        selected_tickers.append(ticker)

    # Check if selected tickers exist in columns
    missing_tickers = [ticker for ticker in selected_tickers if ticker not in big_data.columns]

    if missing_tickers:
        print(f"Belirtilen hisse kodları bulunamadı: {', '.join(missing_tickers)}")
    else:
        selected_data = big_data[selected_tickers].dropna().corr()
        print(selected_data)

        heatmap = sns.heatmap(selected_data, linewidths=0.5, cmap="RdBu")
        plt.show()

if __name__ == "__main__":
    main()
