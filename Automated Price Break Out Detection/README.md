## English
## Trading Strategy Implementation 

### Overview
This repository contains Python code for implementing a trading strategy using candlestick data of EUR/USD forex pair. The strategy involves detecting pivot points, calculating Exponential Moving Averages (EMAs), identifying structure breakouts, and generating trading signals based on these factors.

### Installation
Ensure you have Python installed on your machine. You can install the required Python packages using pip. Run the following command in your terminal:

	pip install -r requirements.txt


### Usage
**- Data Preparation:**

- Make sure you have the candlestick data of EUR/USD forex pair in CSV format.
- Update the file path in the code to match your dataset's location.

**- Executing the Strategy:**

- Run the provided Python script in your preferred Python environment.
- Adjust parameters such as window sizes, candle ranges, and other parameters as per your requirements.

**- Visualization:**

- The script generates candlestick charts using Plotly library for visualizing pivot points and detected structures.
- Candlestick charts provide a graphical representation of the trading signals and structural patterns identified by the strategy.

**- Backtesting:**

- The backtesting module is utilized to assess the performance of the trading strategy.
- Adjust parameters such as trade sizes, risk management rules, and other parameters to evaluate different trading scenarios.

### Components
**- EMA Calculation:**
- Exponential Moving Averages (EMAs) with a length of 150 are computed to identify trend directions.

**- Pivot Point Detection:**
- Pivot points are identified as high or low points within a specified window.

**- Structure Breakout Detection:**
- The strategy detects structural breakouts by analyzing recent price movements and pivot points.


**- Trading Signal Generation:**

- Based on the detected pivot points and structural patterns, buy or sell signals are generated to initiate trades.

**- Backtesting:**
- The performance of the trading strategy is evaluated using historical data through backtesting.

### Disclaimer
This trading strategy implementation is for educational purposes only and should not be considered financial advice. Trading involves risks, and past performance does not guarantee future results. Use this code at your own discretion.


## Türkçe 
## Ticaret Stratejisinin Uygulanması

### Genel Bakış
Bu depo, EUR/USD forex çiftinin mum çubuğu verilerini kullanarak bir ticaret stratejisi uygulamak için Python kodunu içerir. Strateji, pivot noktalarının tespit edilmesini, Üstel Hareketli Ortalamaların (EMA'ların) hesaplanmasını, yapı kırılmalarının belirlenmesini ve bu faktörlere dayalı olarak ticaret sinyallerinin oluşturulmasını içerir.

### Kurulum
Makinenizde Python'un kurulu olduğundan emin olun. Gerekli Python paketlerini pip kullanarak kurabilirsiniz. Terminalinizde aşağıdaki komutu çalıştırın:

pip kurulumu -r gereksinimleri.txt


### Kullanım
**- Veri Hazırlama:**

- EUR/USD forex çiftinin mum çubuğu verilerinin CSV formatında olduğundan emin olun.
- Veri kümenizin konumuyla eşleşecek şekilde koddaki dosya yolunu güncelleyin.

**- Stratejinin Yürütülmesi:**

- Sağlanan Python betiğini tercih ettiğiniz Python ortamında çalıştırın.
- Pencere boyutları, mum aralıkları ve diğer parametreler gibi parametreleri gereksinimlerinize göre ayarlayın.

**- Görselleştirme:**

- Komut dosyası, pivot noktalarını ve tespit edilen yapıları görselleştirmek için Plotly kütüphanesini kullanarak mum grafikleri oluşturur.
- Mum grafikleri, strateji tarafından tanımlanan ticaret sinyallerinin ve yapısal modellerin grafiksel bir temsilini sağlar.

**- Geriye dönük test:**

- Geriye dönük test modülü, ticaret stratejisinin performansını değerlendirmek için kullanılır.
- Farklı ticaret senaryolarını değerlendirmek için işlem boyutları, risk yönetimi kuralları ve diğer parametreler gibi parametreleri ayarlayın.

### Bileşenler
**- EMA Hesaplaması:**
- Trend yönlerini belirlemek için 150 uzunluğunda Üstel Hareketli Ortalamalar (EMA'lar) hesaplanır.

**- Pivot Noktası Algılama:**
- Pivot noktaları, belirli bir pencere içinde yüksek veya alçak noktalar olarak tanımlanır.

**- Yapı Koparma Tespiti:**
- Strateji, son fiyat hareketlerini ve pivot noktalarını analiz ederek yapısal kırılmaları tespit eder.


**- Ticaret Sinyali Üretimi:**

- Tespit edilen pivot noktalarına ve yapısal kalıplara dayanarak alım satımı başlatmak için alım veya satım sinyalleri üretilir.

**- Geriye dönük test:**
- Ticaret stratejisinin performansı, geriye dönük test yoluyla geçmiş veriler kullanılarak değerlendirilir.

### Sorumluluk reddi beyanı
Bu ticaret stratejisi uygulaması yalnızca eğitim amaçlıdır ve finansal tavsiye olarak değerlendirilmemelidir. Ticaret riskler içerir ve geçmiş performans gelecekteki sonuçları garanti etmez. Bu kodu kendi takdirinize bağlı olarak kullanın.