## English
## Forex Trading Strategy Backtesting

### Purpose of the Code

This code implements a simple forex trading strategy and backtests it on EUR/USD hourly candlestick data. Here's a summary of each section:

1. **Loading and Preprocessing Data:**
   - Reads candlestick data from a CSV file, filters out rows with zero volume, and calculates the RSI and EMA indicators.

2. **Generating Trading Signals:**
   - Defines a function to generate trading signals based on certain conditions, such as the relationship between price, EMA, and recent swing highs/lows.
   - Determines entry points, stop-loss (SL), and take-profit (TP) levels.

3. **Visualizing Candlestick Chart with Trading Signals:**
   - Uses Plotly to create a candlestick chart with trading signals marked as purple markers.

4. **Backtesting Strategy:**
   - Utilizes the `backtesting` library to backtest the trading strategy.
   - Implements a simple trading strategy based on the generated signals.

### Usage
To utilize this code:
- Make sure to have the required libraries installed (pandas, pandas_ta, plotly, numpy, backtesting).
- Provide the path to your candlestick data CSV file.
- Adjust parameters such as window sizes, thresholds, and trading strategy rules according to your analysis requirements.
- Run the code to generate trading signals, visualize them on the chart, and backtest the strategy.

This code can be useful for traders and analysts to backtest their trading strategies on historical forex data, enabling them to evaluate strategy performance and make improvements.

Please feel free to reach out if you need further assistance or have any questions!

## Türkçe 
## Forex Ticaret Stratejisinin Geriye Dönük Testi

### Kuralların Amacı

Bu kod, basit bir forex ticaret stratejisi uygular ve bunu EUR/USD saatlik mum çubuğu verileri üzerinde geriye doğru test eder. İşte her bölümün özeti:

1. **Verileri Yükleme ve Ön İşleme:**
   - Bir CSV dosyasından mum çubuğu verilerini okur, sıfır hacimli satırları filtreler ve RSI ve EMA göstergelerini hesaplar.

2. **Ticaret Sinyalleri Oluşturmak:**
   - Fiyat, EMA ve son dönemdeki yükselişler/düşükler arasındaki ilişki gibi belirli koşullara dayalı olarak alım satım sinyalleri üreten bir işlevi tanımlar.
   - Giriş noktalarını, zararı durdurma (SL) ve kar alma (TP) seviyelerini belirler.

3. **Mum Grafiğinin Ticaret Sinyalleriyle Görselleştirilmesi:**
   - Mor işaretleyicilerle işaretlenmiş ticaret sinyalleri içeren bir şamdan grafiği oluşturmak için Plotly'yi kullanır.

4. **Geri Test Stratejisi:**
   - Ticaret stratejisini geriye dönük test etmek için 'geriye dönük test' kütüphanesini kullanır.
   - Oluşturulan sinyallere dayalı basit bir ticaret stratejisi uygular.

### Kullanım
Bu kodu kullanmak için:
- Gerekli kütüphanelerin kurulu olduğundan emin olun (pandas, pandas_ta,plotly, numpy, backtesting).
- Şamdan verileri CSV dosyanızın yolunu belirtin.
- Analiz gereksinimlerinize göre pencere boyutları, eşikler ve ticaret stratejisi kuralları gibi parametreleri ayarlayın.
- Ticaret sinyalleri oluşturmak, bunları grafikte görselleştirmek ve stratejiyi geriye doğru test etmek için kodu çalıştırın.

Bu kod, tüccarların ve analistlerin ticaret stratejilerini geçmiş forex verileri üzerinde geriye doğru test etmeleri için yararlı olabilir, strateji performansını değerlendirmelerine ve iyileştirmeler yapmalarına olanak tanır.

Daha fazla yardıma ihtiyacınız varsa veya sorularınız varsa lütfen bizimle iletişime geçmekten çekinmeyin!