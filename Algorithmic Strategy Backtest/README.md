## English
## Forex Trading Strategy Optimization

### Overview:

This repository contains Python scripts for developing, optimizing, and testing a forex trading strategy using historical EURUSD candlestick data. The strategy incorporates technical indicators such as Exponential Moving Averages (EMA), Bollinger Bands (BB), Relative Strength Index (RSI), and Average True Range (ATR) to generate buy/sell signals. The optimization process aims to find the optimal parameters for the strategy to maximize returns, followed by testing the strategy's performance on unseen data.

### Scripts:

**1. Data Loading and Preprocessing:**
- Loads historical EURUSD candlestick data from a CSV file.
- Preprocesses the data, including converting timestamps, removing redundant rows, and calculating technical indicators like EMA, MACD, and ATR.

**2. Signal Generation and Visualization:**
- Defines functions to generate buy/sell signals based on EMA and MACD criteria.
- Visualizes the signals on candlestick charts using Plotly.

**3. Strategy Implementation and Optimization:**
- Implements a trading strategy class that utilizes the generated signals for making buy/sell decisions.
- Defines parameters for position sizing, stop-loss, and take-profit levels.
- Optimizes the strategy parameters using the Backtesting library, considering different combinations of parameters to maximize returns.
- Visualizes the optimization results using seaborn heatmap.

**4. Final Strategy Evaluation:**
- Implements the final trading strategy with optimized parameters.
- Conducts backtesting of the strategy on historical data to evaluate its performance.
- Plots the equity curve and other performance metrics.

**5. Performance Evaluation:**
- Conducts backtesting of the optimized strategy on historical data to evaluate its performance.
- Analyzes the cumulative returns and visualizes the optimization results.



**Dependencies:**
- Python 3.x
- Pandas
- pandas_ta
- Plotly
- tqdm
- backtesting
- seaborn
- matplotlib

### Usage:
1. Ensure all dependencies are installed (pip install pandas pandas_ta plotly tqdm backtesting seaborn matplotlib).
2. Place the EURUSD candlestick data CSV file in the same directory as the scripts.
3. Run each script individually in the specified order to perform data preprocessing, signal generation, strategy optimization, and evaluation.

### Note:
- The scripts assume the structure of the CSV file with specific column names ('Gmt time', 'Open', 'High', 'Low', 'Close', etc.).
- Adjustments may be needed based on the actual structure of the data.
- The strategy parameters such as position size, stop-loss coefficient, and take-profit ratio can be adjusted for further customization and optimization.

## Türkçe 
## Forex Ticaret Stratejisi Optimizasyonu

### Genel Bakış:

Bu depo, geçmiş EURUSD şamdan verilerini kullanarak bir forex ticaret stratejisi geliştirmek, optimize etmek ve test etmek için Python komut dosyalarını içerir. Strateji, alım/satım sinyalleri oluşturmak için Üstel Hareketli Ortalamalar (EMA), Bollinger Bantları (BB), Göreceli Güç Endeksi (RSI) ve Ortalama Gerçek Aralık (ATR) gibi teknik göstergeleri içerir. Optimizasyon süreci, getirileri en üst düzeye çıkarmak için strateji için en uygun parametreleri bulmayı ve ardından stratejinin performansını görünmeyen veriler üzerinde test etmeyi amaçlar.

### Kodlar:

**1. Veri Yükleme ve Ön İşleme:**
- Bir CSV dosyasından geçmiş EURUSD mum çubuğu verilerini yükler.
- Zaman damgalarını dönüştürmek, gereksiz satırları kaldırmak ve EMA, MACD ve ATR gibi teknik göstergeleri hesaplamak dahil olmak üzere verileri önceden işler.

**2. Sinyal Üretimi ve Görselleştirme:**
- EMA ve MACD kriterlerine göre alım/satım sinyalleri oluşturmaya yönelik fonksiyonları tanımlar.
- Plotly'yi kullanarak mum grafiklerindeki sinyalleri görselleştirir.

**3. Strateji Uygulama ve Optimizasyon:**
- Alım/satım kararları vermek için oluşturulan sinyalleri kullanan bir ticaret stratejisi sınıfını uygular.
- Pozisyon boyutlandırma, zararı durdurma ve kar alma seviyelerine ilişkin parametreleri tanımlar.
- Getirileri en üst düzeye çıkarmak için farklı parametre kombinasyonlarını dikkate alarak Geriye Dönük Test kitaplığını kullanarak strateji parametrelerini optimize eder.
- Denizdeki ısı haritasını kullanarak optimizasyon sonuçlarını görselleştirir.

**4. Nihai Strateji Değerlendirmesi:**
- Optimize edilmiş parametrelerle nihai ticaret stratejisini uygular.
- Performansını değerlendirmek için stratejinin geçmiş veriler üzerinde geriye dönük testini yapar.
- Özsermaye eğrisini ve diğer performans ölçümlerini çizer.

**5. Performans değerlendirmesi:**
- Performansını değerlendirmek için optimize edilmiş stratejinin geçmiş veriler üzerinde geriye dönük testini gerçekleştirir.
- Kümülatif getirileri analiz eder ve optimizasyon sonuçlarını görselleştirir.

**Bağımlılıklar:**
- Python 3.x
- Pandas
- pandas_ta
- Plotly
- tqdm
- backtesting
- seaborn
- matplotlib

### Kullanım:
1. Tüm bağımlılıkların kurulu olduğundan emin olun (pip install pandas pandas_taplotly tqdm backtesting seaborn matplotlib).
2. EURUSD mum çubuğu verileri CSV dosyasını komut dosyalarıyla aynı dizine yerleştirin.
3. Veri ön işlemeyi, sinyal oluşturmayı, strateji optimizasyonunu ve değerlendirmeyi gerçekleştirmek için her komut dosyasını belirtilen sırayla ayrı ayrı çalıştırın.

### Not:
- Komut dosyaları, CSV dosyasının yapısını belirli sütun adlarıyla ('Gmt zamanı', 'Açık', 'Yüksek', 'Düşük', 'Kapat' vb.) varsayar.
- Verilerin gerçek yapısına göre ayarlamalar yapılması gerekebilir.
- Pozisyon büyüklüğü, zararı durdurma katsayısı ve kar alma oranı gibi strateji parametreleri daha fazla özelleştirme ve optimizasyon için ayarlanabilir.


