## English
## Financial Data Analysis and Trading Strategy Implementation

### Overview
This script performs several tasks related to financial data analysis and trading strategy implementation using the Python programming language. The tasks include:

1. Data Preprocessing
2. Technical Indicator Calculation
3. Signal Generation
4. Visualization
5. Backtesting a Trading Strategy
6. Optimization and Visualization of Strategy Performance

### Data Preprocessing
The script begins by reading a CSV file containing financial candlestick data. It performs the following preprocessing steps:

1. Removes unnecessary substrings from the Gmt time column.
2. Converts the Gmt time column to a datetime format.
3. Filters out rows where the high and low prices are equal.
4. Resets the DataFrame index.

### Technical Indicator Calculation
The script calculates two Exponential Moving Averages (EMAs):

- A fast EMA with a period of 30.
- A slow EMA with a period of 60.

These EMAs are used to identify potential buy and sell signals in the data.


### Signal Generation
A function named TotalSignal is defined to generate buy and sell signals based on the crossover of the fast and slow EMAs:

- A buy signal (2) is generated when the fast EMA crosses above the slow EMA.
- A sell signal (1) is generated when the fast EMA crosses below the slow EMA.

These signals are stored in a new column named TotalSignal.

Additionally, a function named pointposbreak is defined to mark the positions of these signals on the price chart for visualization purposes.

### Visualization
The script uses the plotly library to create an interactive candlestick chart. This chart includes:

- Candlestick representation of the price data.
- Overlaid fast and slow EMAs.
- Markers indicating buy and sell signals.

### Backtesting a Trading Strategy
The script defines a custom trading strategy using the backtesting library. The strategy logic is as follows:

- Enter a long position when the fast EMA crosses above the slow EMA.
- Enter a short position when the fast EMA crosses below the slow EMA.
- Close existing positions when an opposite signal is generated.

### Optimization and Visualization of Strategy Performance
The script optimizes the trading strategy by adjusting the lengths of the fast and slow EMAs. It evaluates the performance of various combinations of EMA lengths to maximize returns.

Finally, the script visualizes the performance of different parameter combinations using a heatmap.

### Conclusion
This script provides a comprehensive workflow for analyzing financial data, generating trading signals, visualizing the results, and backtesting a trading strategy. It is a useful tool for traders and analysts looking to develop and evaluate trading strategies based on technical indicators.

## Türkçe 
## Finansal Veri Analizi ve Ticaret Stratejisinin Uygulanması

### Genel Bakış
Bu komut dosyası, Python programlama dilini kullanarak finansal veri analizi ve ticaret stratejisinin uygulanmasıyla ilgili çeşitli görevleri yerine getirir. Görevler şunları içerir:

1. Veri Ön İşleme
2. Teknik Gösterge Hesaplaması
3. Sinyal Üretimi
4. Görselleştirme
5. Bir Ticaret Stratejisinin Geriye Dönük Testi
6. Strateji Performansının Optimizasyonu ve Görselleştirilmesi

### Veri Ön İşleme
Komut dosyası, finansal mum çubuğu verilerini içeren bir CSV dosyasını okuyarak başlar. Aşağıdaki ön işleme adımlarını gerçekleştirir:

1. Gereksiz alt dizeleri Gmt zaman sütunundan kaldırır.
2. Gmt saat sütununu tarihsaat biçimine dönüştürür.
3. Yüksek ve düşük fiyatların eşit olduğu satırları filtreler.
4. DataFrame dizinini sıfırlar.

### Teknik Gösterge Hesaplaması
Komut dosyası iki Üstel Hareketli Ortalamayı (EMA) hesaplar:

- 30 periyotlu hızlı bir EMA.
- 60 periyotlu yavaş bir EMA.

Bu EMA'lar verilerdeki potansiyel alım ve satım sinyallerini tanımlamak için kullanılır.


### Sinyal Üretimi
Hızlı ve yavaş EMA'ların geçişine dayalı olarak alım ve satım sinyalleri oluşturmak için TotalSignal adlı bir işlev tanımlanmıştır:

- Hızlı EMA, yavaş EMA'nın üzerine geçtiğinde bir satın alma sinyali (2) oluşturulur.
- Hızlı EMA yavaş EMA'nın altına geçtiğinde bir satış sinyali (1) oluşturulur.

Bu sinyaller TotalSignal adlı yeni bir sütunda saklanır.

Ayrıca görselleştirme amacıyla bu sinyallerin fiyat grafiği üzerindeki konumlarını işaretlemek için pointposbreak adında bir fonksiyon tanımlanmıştır.

### Görselleştirme
Komut dosyası, etkileşimli bir mum grafiği oluşturmak için çizim kitaplığını kullanır. Bu grafik şunları içerir:

- Fiyat verilerinin mum çubuğu gösterimi.
- Hızlı ve yavaş EMA'lar yerleştirilmiştir.
- Alış ve satış sinyallerini gösteren işaretler.

### Bir Ticaret Stratejisinin Geriye Dönük Testi
Komut dosyası, geriye dönük test kitaplığını kullanarak özel bir ticaret stratejisi tanımlar. Strateji mantığı şu şekildedir:

- Hızlı EMA yavaş EMA'nın üzerine geçtiğinde uzun bir pozisyon girin.
- Hızlı EMA yavaş EMA'nın altına geçtiğinde kısa pozisyon girin.
- Ters bir sinyal oluştuğunda mevcut pozisyonları kapatın.

### Strateji Performansının Optimizasyonu ve Görselleştirilmesi
Komut dosyası, hızlı ve yavaş EMA'ların uzunluklarını ayarlayarak ticaret stratejisini optimize eder. Getirileri en üst düzeye çıkarmak için çeşitli EMA uzunluk kombinasyonlarının performansını değerlendirir.

Son olarak komut dosyası, bir ısı haritası kullanarak farklı parametre kombinasyonlarının performansını görselleştirir.

### Çözüm
Bu komut dosyası, finansal verileri analiz etmek, ticaret sinyalleri oluşturmak, sonuçları görselleştirmek ve bir ticaret stratejisini geriye doğru test etmek için kapsamlı bir iş akışı sağlar. Teknik göstergelere dayalı ticaret stratejileri geliştirmek ve değerlendirmek isteyen yatırımcılar ve analistler için yararlı bir araçtır.