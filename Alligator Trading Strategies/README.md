## English
## Forex Trading Strategy Optimization

### Purpose of the Code

This code aims to optimize a forex trading strategy based on simple moving averages (SMA) and candlestick patterns using the backtesting library. Here's a summary of each section:

1. **Loading and Preprocessing Data:**
   - Reads candlestick data from a CSV file and preprocesses it by converting timestamps, filtering out rows with zero volume, and setting the timestamp column as the index.

2. **Calculating SMAs and Generating Signals:**
   - Calculates three SMAs with different lengths and defines conditions to generate trading signals based on SMA crossovers and candlestick patterns.

3. **Assigning Total Signals:**
   - Combines individual SMA signals to generate total signals based on specific conditions.

4. **Visualizing Candlestick Chart with SMAs and Signals:**
   - Utilizes Plotly to visualize the candlestick chart along with the SMAs and entry signals.

5. **Strategy Optimization:**
   - Defines a trading strategy class that uses the total signals to execute buy or sell orders with specified stop-loss and take-profit levels.
   - Optimizes the strategy parameters (`TPSLRatio` and `perc`) using the `optimize` method from the backtesting library and generates statistics and a heatmap to analyze the results.

### Usage
To use this code:
- Provide the path to your candlestick data CSV file.
- Adjust parameters such as SMA lengths, signal conditions, and strategy parameters (`TPSLRatio` and `perc`) according to your trading strategy.
- Run the code to preprocess the data, generate signals, visualize the chart, and optimize the strategy.

This code is helpful for traders and analysts to refine their trading strategies and find optimal parameter combinations that maximize returns while minimizing risks.

Feel free to reach out if you need further assistance or have any questions!

## Türkçe
## Forex Ticaret Stratejisi Optimizasyonu

### Kuralların Amacı

Bu kod, geriye dönük test kitaplığını kullanarak basit hareketli ortalamalara (SMA) ve mum çubuğu modellerine dayalı bir forex ticaret stratejisini optimize etmeyi amaçlamaktadır. İşte her bölümün özeti:

1. **Verileri Yükleme ve Ön İşleme:**
   - Bir CSV dosyasından mum çubuğu verilerini okur ve zaman damgalarını dönüştürerek, sıfır hacimli satırları filtreleyerek ve zaman damgası sütununu dizin olarak ayarlayarak bunları önceden işler.

2. **SMA'ların Hesaplanması ve Sinyallerin Oluşturulması:**
   - Farklı uzunluklara sahip üç SMA'yı hesaplar ve SMA geçişlerine ve mum çubuğu modellerine dayalı alım satım sinyalleri oluşturmak için koşulları tanımlar.

3. **Toplam Sinyallerin Atanması:**
   - Belirli koşullara göre toplam sinyaller oluşturmak için ayrı SMA sinyallerini birleştirir.

4. **Mum Grafiğinin SMA'lar ve Sinyallerle Görselleştirilmesi:**
   - Şamdan grafiğini SMA'lar ve giriş sinyalleriyle birlikte görselleştirmek için Plotly'yi kullanır.

5. **Strateji Optimizasyonu:**
   - Belirli zararı durdurma ve kar alma seviyeleriyle alım veya satım emirlerini gerçekleştirmek için toplam sinyalleri kullanan bir ticaret stratejisi sınıfını tanımlar.
   - Geriye dönük test kütüphanesindeki 'optimize' yöntemini kullanarak strateji parametrelerini ('TPSLRatio' ve 'perc') optimize eder ve sonuçları analiz etmek için istatistikler ve bir ısı haritası oluşturur.

### Kullanım
Bu kodu kullanmak için:
- Şamdan verileri CSV dosyanızın yolunu belirtin.
- SMA uzunlukları, sinyal koşulları ve strateji parametreleri ("TPSLRatio" ve "perc") gibi parametreleri ticaret stratejinize göre ayarlayın.
- Verileri önceden işlemek, sinyaller oluşturmak, grafiği görselleştirmek ve stratejiyi optimize etmek için kodu çalıştırın.

Bu kod, yatırımcıların ve analistlerin ticaret stratejilerini geliştirmelerine ve riskleri en aza indirirken getirileri en üst düzeye çıkaran en uygun parametre kombinasyonlarını bulmalarına yardımcı olur.

Daha fazla yardıma ihtiyacınız olursa veya sorularınız olursa bizimle iletişime geçmekten çekinmeyin!