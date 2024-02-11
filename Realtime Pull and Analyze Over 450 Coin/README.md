## English
## Real-Time Coin Price Data Collection and Analysis

### Introduction

This repository contains Python code for collecting real-time coin price data from the Binance exchange WebSocket stream, storing the data in a CSV file, and analyzing the returns of various cryptocurrencies over a specified period.

### Purpose

The purpose of this code is to demonstrate how to:

- Collect real-time coin price data from Binance using WebSocket streams.
- Manipulate and store the data in a CSV file for further analysis.
- Calculate the returns of different cryptocurrencies over a given timeframe.
- Identify the top-performing cryptocurrencies based on their returns.

### Components

1. **Real-Time Data Collection:** Utilize the Binance WebSocket stream to receive real-time coin price updates.

2. **Data Manipulation and Storage:** Extract relevant information from the WebSocket messages, such as coin prices and timestamps. Store the data in a CSV file for further analysis.

3. **Return Calculation:** Calculate the returns of different cryptocurrencies by comparing their initial and final prices over a specified timeframe.

4. **Performance Analysis:** Analyze the returns of various cryptocurrencies and identify the top performers based on their returns.

### Usage

To use the code:

1. **Install Python along with the required libraries:** websocket-client, pandas, and python-binance.

2. Import the necessary modules and initialize the Binance client.

3. Define functions to manipulate WebSocket messages, store data in a CSV file, and calculate returns.

4. Connect to the Binance WebSocket stream and start receiving real-time data.

5. Perform analysis on the collected data, such as calculating returns and identifying top performers.

### Example

In the provided code snippet, real-time coin price data is collected from the Binance exchange using WebSocket streams. The data is manipulated to extract relevant information and stored in a CSV file named "coinprices.csv". After collecting sufficient data, the returns of various cryptocurrencies are calculated over the specified period. Finally, the top-performing cryptocurrencies based on their returns are identified and displayed.

### Note

- This code is intended for educational purposes and should be used responsibly.
- Ensure compliance with Binance API usage guidelines when accessing real-time data from the exchange.

### References

- Binance API Documentation: https://binance-docs.github.io/apidocs/
- WebSocket-client Documentation: https://pypi.org/project/websocket-client/
- pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/index.html

## Türkçe
## Gerçek Zamanlı Coin Fiyat Verisi Toplama ve Analizi

### Giriş

Bu depo, Binance borsası WebSocket akışından gerçek zamanlı kripto para fiyatı verilerini toplamak, verileri bir CSV dosyasında depolamak ve belirli bir süre boyunca çeşitli kripto para birimlerinin getirilerini analiz etmek için Python kodunu içerir.

### Amaç

Bu kodun amacı aşağıdakilerin nasıl yapılacağını göstermektir:

- WebSocket akışlarını kullanarak Binance'ten gerçek zamanlı kripto para fiyatı verilerini toplayın.
- Daha fazla analiz için verileri bir CSV dosyasında işleyin ve saklayın.
- Belirli bir zaman diliminde farklı kripto para birimlerinin getirilerini hesaplayın.
- Getirilerine göre en iyi performans gösteren kripto para birimlerini belirleyin.

### Bileşenler

1. **Gerçek Zamanlı Veri Toplama:** Gerçek zamanlı coin fiyat güncellemelerini almak için Binance WebSocket akışını kullanın.

2. **Veri İşleme ve Depolama:** WebSocket mesajlarından madeni para fiyatları ve zaman damgaları gibi ilgili bilgileri çıkarın. Daha fazla analiz için verileri bir CSV dosyasında saklayın.

3. **Getiri Hesaplaması:** Belirli bir zaman diliminde başlangıç ​​ve nihai fiyatlarını karşılaştırarak farklı kripto para birimlerinin getirilerini hesaplayın.

4. **Performans Analizi:** Çeşitli kripto para birimlerinin getirilerini analiz edin ve getirilerine göre en iyi performansı gösterenleri belirleyin.

### Kullanım

Kodu kullanmak için:

1. **Python'u gerekli kitaplıklarla birlikte yükleyin:** websocket-client, pandas ve python-binance.

2. Gerekli modülleri içe aktarın ve Binance istemcisini başlatın.

3. WebSocket mesajlarını işlemek, verileri bir CSV dosyasında depolamak ve getirileri hesaplamak için işlevler tanımlayın.

4. Binance WebSocket akışına bağlanın ve gerçek zamanlı veri almaya başlayın.

5. Toplanan veriler üzerinde, getirilerin hesaplanması ve en iyi performans gösterenlerin belirlenmesi gibi analizler gerçekleştirin.

### Örnek

Sağlanan kod parçacığında, WebSocket akışları kullanılarak Binance borsasından gerçek zamanlı kripto para fiyatı verileri toplanıyor. Veriler, ilgili bilgileri çıkarmak için işlenir ve "coinprices.csv" adlı bir CSV dosyasında saklanır. Yeterli veri toplandıktan sonra belirlenen süre boyunca çeşitli kripto para birimlerinin getirileri hesaplanır. Son olarak, getirilerine göre en iyi performans gösteren kripto para birimleri belirleniyor ve gösteriliyor.

### Not

- Bu kod eğitim amaçlıdır ve sorumlu bir şekilde kullanılmalıdır.
- Borsadan gerçek zamanlı verilere erişirken Binance API kullanım kurallarına uygunluğu sağlayın.

### Referanslar

- Binance API Belgeleri: https://binance-docs.github.io/apidocs/
- WebSocket istemcisi Belgeleri: https://pypi.org/project/websocket-client/
- pandalar Dokümantasyonu: https://pandas.pydata.org/pandas-docs/stable/index.html
