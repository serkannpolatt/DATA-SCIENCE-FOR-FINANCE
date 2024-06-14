## English
## Trading Strategy Analysis with Bollinger Bands and RSI
### Overview
This project involves developing and analyzing a trading strategy using historical candlestick data for BMW. The strategy incorporates technical indicators such as Bollinger Bands, Relative Strength Index (RSI), and Average True Range (ATR) to generate buy and sell signals. Additionally, it visualizes these indicators and signals on a candlestick chart and optimizes the strategy's parameters to maximize returns.

### Features
#### Data Processing
**1. Loading Data:** The script reads historical candlestick data from a CSV file.
**2. Data Cleaning:** It removes rows where the high and low prices are equal and converts the 'Gmt time' column to a datetime format.

#### Technical Indicators
**1. Bollinger Bands**: The script calculates Bollinger Bands with a 30-day period and a standard deviation of 2.
**2. RSI:** It computes the RSI with a 14-day period.
**3. ATR:** The Average True Range is calculated with a 14-day period.
**4. Bollinger Bands Width:** This is computed as the difference between the upper and lower Bollinger Bands divided by the middle band.

#### Signal Generation
- **Buy Signal:** Generated when the previous candle closes below the lower Bollinger Band, the RSI is below 30, the current close is above the previous high, and the Bollinger Band width is above a specified threshold.
- **Sell Signal:** Generated when the previous candle closes above the upper Bollinger Band, the RSI is above 70, the current close is below the previous low, and the Bollinger Band width is above a specified threshold.

### Visualization
- **Candlestick Chart:** The script plots the candlestick chart along with Bollinger Bands and RSI.
- **Entry Points:** Markers are added to indicate buy and sell signals.

### Backtesting and Optimization
**1. Backtesting:** The strategy is backtested using historical data.
**2. Parameter Optimization:** The script optimizes the stop-loss and take-profit coefficients to maximize returns.

### Usage
**1. Import Libraries:** Ensure that the required libraries (pandas, pandas_ta, numpy, plotly, backtesting, seaborn, matplotlib) are installed.
**2. Load Data:** Place the historical candlestick data CSV file in the same directory as the script.
**3. Run the Script:** Execute the script to process the data, calculate indicators, generate signals, visualize the results, and perform backtesting and optimization.

### Conclusion
This project provides a comprehensive approach to developing, visualizing, and optimizing a trading strategy based on technical analysis. By using Bollinger Bands, RSI, and ATR, it aims to identify profitable entry and exit points in the market. The visualization and backtesting features help in evaluating the strategy's performance and refining its parameters for better results.

## Türkçe 
## Bollinger Bantları ve RSI ile Ticaret Stratejisi Analizi
### Genel Bakış
Bu proje, BMW için geçmiş mum çubuğu verilerini kullanarak bir ticaret stratejisinin geliştirilmesini ve analiz edilmesini içermektedir. Strateji, alım ve satım sinyalleri oluşturmak için Bollinger Bantları, Göreceli Güç Endeksi (RSI) ve Ortalama Gerçek Aralık (ATR) gibi teknik göstergeleri içerir. Ek olarak, bu göstergeleri ve sinyalleri bir mum grafiği üzerinde görselleştirir ve getirileri en üst düzeye çıkarmak için stratejinin parametrelerini optimize eder.

### Özellikler
#### Veri işleme
**1. Veri Yükleme:** Komut dosyası, geçmiş mum çubuğu verilerini bir CSV dosyasından okur.
**2. Veri Temizleme:** Yüksek ve düşük fiyatların eşit olduğu satırları kaldırır ve 'Gmt time' sütununu tarihsaat biçimine dönüştürür.

#### Teknik Göstergeler
**1. Bollinger Bantları**: Program, Bollinger Bantlarını 30 günlük bir süre ve 2 standart sapma ile hesaplar.
**2. RSI:** RSI'yi 14 günlük periyotlarla hesaplar.
**3. ATR:** Ortalama Gerçek Aralık 14 günlük bir dönemle hesaplanır.
**4. Bollinger Bant Genişliği:** Üst ve alt Bollinger Bantları arasındaki farkın orta banda bölünmesiyle hesaplanır.

#### Sinyal Üretimi
- **Alış Sinyali:** Bir önceki mum alt Bollinger Bandının altında kapandığında, RSI 30'un altında olduğunda, mevcut kapanış önceki en yüksek seviyenin üzerinde olduğunda ve Bollinger Bandı genişliği belirlenen eşiğin üzerinde olduğunda oluşturulur.
- **Satış Sinyali:** Önceki mum üst Bollinger Bandının üzerinde kapandığında, RSI 70'in üzerinde olduğunda, mevcut kapanış önceki en düşük seviyenin altında olduğunda ve Bollinger Bandı genişliği belirlenen eşiğin üzerinde olduğunda oluşturulur.

### Görselleştirme
- **Mum Grafiği:** Komut, mum grafiğini Bollinger Bantları ve RSI ile birlikte çizer.
- **Giriş Noktaları:** Alış ve satış sinyallerini belirtmek için işaretler eklenir.

### Geriye Dönük Test ve Optimizasyon
**1. Geriye dönük test:** Strateji, geçmiş veriler kullanılarak geriye doğru test edilir.
**2. Parametre Optimizasyonu:** Komut, getirileri en üst düzeye çıkarmak için zararı durdurma ve kar alma katsayılarını optimize eder.

### Kullanım
**1. Kütüphaneleri İçe Aktar:** Gerekli kütüphanelerin (pandas, pandas_ta, numpy, komplo, backtesting, seaborn, matplotlib) kurulu olduğundan emin olun.
**2. Verileri Yükle:** Geçmiş mum çubuğu verileri CSV dosyasını komut dosyasıyla aynı dizine yerleştirin.
**3. Komut Dosyasını Çalıştırın:** Verileri işlemek, göstergeleri hesaplamak, sinyaller oluşturmak, sonuçları görselleştirmek ve geriye dönük test ve optimizasyon gerçekleştirmek için komut dosyasını yürütün.

### Çözüm
Bu proje, teknik analize dayalı bir ticaret stratejisinin geliştirilmesine, görselleştirilmesine ve optimize edilmesine yönelik kapsamlı bir yaklaşım sağlar. Bollinger Bantları, RSI ve ATR'yi kullanarak piyasaya karlı giriş ve çıkış noktalarını belirlemeyi amaçlamaktadır. Görselleştirme ve geriye dönük test özellikleri, stratejinin performansının değerlendirilmesine ve daha iyi sonuçlar için parametrelerinin iyileştirilmesine yardımcı olur.