## English
## RSI Trading Strategy using Python

### Introduction

This project implements a Relative Strength Index (RSI) trading strategy using Python. The RSI is a popular technical indicator that helps traders identify potential overbought or oversold conditions in a stock's price. The strategy involves calculating the RSI values for a list of stocks from the S&P 500 index and making buy and sell decisions based on these RSI values.

### Getting Started
To get started with this project, follow these steps:

1. **Install Required Packages:** Make sure you have the required packages installed. You can install them using the following command:

		pip install pandas yfinance matplotlib

2. **Clone the Repository:** Clone this repository to your local machine using the following command:

		git clone https://github.com/yourusername/rsi-trading-strategy.git
		cd rsi-trading-strategy

3. **Run the Script:** Open the Python script rsi_trading.py using your preferred code editor. Run the script to execute the RSI trading strategy and visualize the results:

		python rsi_trading.py


### Code Explanation

This project involves the following main steps:

1. **Data Collection:** The project starts by collecting a list of stock tickers from the S&P 500 index. The tickers are then preprocessed to replace dots with hyphens.

2. **RSI Calculation:** The RSIcalc function is responsible for calculating the RSI values for a given stock. It uses historical price data obtained from the Yahoo Finance API. The RSI values are calculated based on price changes and moving averages.

3. **Trading Signal Generation:** The getSignals function generates trading signals based on the calculated RSI values. It identifies buying opportunities when the RSI is below a certain threshold and selling opportunities when the RSI exceeds another threshold.

4. **Visualization:** The project includes code to visualize the buy signals on price charts using Matplotlib.

5. **Performance Evaluation:** The project calculates and displays the overall performance of the trading strategy. It calculates the win rate by comparing the number of winning trades to the total number of trades.

### Conclusion

This project provides a hands-on example of implementing a basic RSI trading strategy using Python. The RSI indicator is widely used in technical analysis, and this project demonstrates how it can be applied to real-world stock data. By following the steps outlined in this README, you can explore the code, run the strategy, and gain insights into potential trading opportunities.

## Türkçe
## Python kullanarak RSI Ticaret Stratejisi

### Giriiş

Bu proje, Python kullanarak bir Göreceli Güç Endeksi (RSI) ticaret stratejisi uygular. RSI, tacirlerin bir hisse senedi fiyatındaki potansiyel aşırı alım veya aşırı satım koşullarını belirlemesine yardımcı olan popüler bir teknik göstergedir. Strateji, S&P 500 endeksinden bir hisse senedi listesi için RSI değerlerinin hesaplanmasını ve bu RSI değerlerine göre alım satım kararlarının verilmesini içerir.

### Başlarken
Bu projeye başlamak için şu adımları izleyin:

1. **Gerekli Paketleri Kurun:** Gerekli paketlerin kurulu olduğundan emin olun. Aşağıdaki komutu kullanarak bunları kurabilirsiniz:

pip kurulumu pandalar yfinance matplotlib

2. **Havuzu Kopyalayın:** Aşağıdaki komutu kullanarak bu depoyu yerel makinenize kopyalayın:

git klonu https://github.com/yourusername/rsi-trading-strategy.git
cd rsi ticaret stratejisi

3. **Komut Dosyasını Çalıştırın:** Tercih ettiğiniz kod düzenleyiciyi kullanarak rsi_trading.py Python betiğini açın. RSI ticaret stratejisini yürütmek ve sonuçları görselleştirmek için betiği çalıştırın:

		python rsi_trading.py


### Kod Açıklama

Bu proje aşağıdaki ana adımları içermektedir:

1. **Veri Toplama:** Proje, S&P 500 endeksinden bir hisse senedi listesi toplayarak başlar. Daha sonra şeritler, noktaları kısa çizgilerle değiştirmek için önceden işlenir.

2. **RSI Hesaplaması:** RSIcalc işlevi, belirli bir hisse senedi için RSI değerlerini hesaplamaktan sorumludur. Yahoo Finance API'sinden elde edilen geçmiş fiyat verilerini kullanır. RSI değerleri, fiyat değişimleri ve hareketli ortalamalara göre hesaplanır.

3. **Ticaret Sinyali Oluşturma:** getSignals işlevi, hesaplanan RSI değerlerine dayalı olarak ticaret sinyalleri üretir. RSI belirli bir eşiğin altında olduğunda satın alma fırsatlarını ve RSI başka bir eşiği aştığında satış fırsatlarını tanımlar.

4. **Görselleştirme:** Proje, satın alma sinyallerini Matplotlib kullanarak fiyat çizelgelerinde görselleştirmek için kod içerir.

5. **Performans Değerlendirmesi:** Proje, ticaret stratejisinin genel performansını hesaplar ve görüntüler. Kazanan işlem sayısını toplam işlem sayısıyla karşılaştırarak kazanma oranını hesaplar.

### Çözüm

Bu proje, Python kullanarak temel bir RSI ticaret stratejisi uygulamanın uygulamalı bir örneğini sunar. RSI göstergesi, teknik analizde yaygın olarak kullanılmaktadır ve bu proje, gerçek dünya hisse senedi verilerine nasıl uygulanabileceğini göstermektedir. Bu BENİOKU'da özetlenen adımları izleyerek kodu keşfedebilir, stratejiyi çalıştırabilir ve potansiyel ticaret fırsatları hakkında bilgi edinebilirsiniz.
