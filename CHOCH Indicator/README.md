## English
## Candlestick Analysis with Pivot Points and Pattern Detection

### Purpose of the Code

This code performs candlestick analysis on EUR/USD forex data. Here's a brief overview of each section:

1. **Loading and Preprocessing Data:**
   - Reads candlestick data from a CSV file, filters out rows with zero volume, and calculates the RSI and EMA indicators.

2. **Identifying Pivot Points:**
   - Defines a function to identify pivot points based on local minima and maxima in the candlestick data.
   - Calculates the position of pivot points.

3. **Visualizing Candlestick Chart with Pivot Points:**
   - Uses Plotly to create a candlestick chart with pivot points marked as purple markers.

4. **Detecting Patterns:**
   - Defines a function to detect specific candlestick patterns based on predefined conditions.
   - The patterns detected include sequences of higher highs and higher lows or lower highs and lower lows.

### Usage
To utilize this code:
- Make sure to have the required libraries installed (pandas, pandas_ta, numpy, plotly, scipy).
- Provide the path to your candlestick data CSV file.
- Adjust parameters such as window sizes and pattern conditions according to your analysis requirements.
- Run the code and check the DataFrame for detected patterns.

This code can be beneficial for traders and analysts in identifying pivot points and detecting specific candlestick patterns, aiding in their technical analysis of financial markets.

Please feel free to reach out if you need further assistance or have any questions!

## Türkçe
## Pivot Noktaları ve Desen Tespiti ile Mum Analizi

### Kuralların Amacı

Bu kod, EUR/USD forex verileri üzerinde mum çubuğu analizi gerçekleştirir. Her bölüme kısa bir genel bakış:

1. **Verileri Yükleme ve Ön İşleme:**
   - Bir CSV dosyasından mum çubuğu verilerini okur, sıfır hacimli satırları filtreler ve RSI ve EMA göstergelerini hesaplar.

2. **Pivot Noktalarını Belirleme:**
   - Mum çubuğu verilerindeki yerel minimum ve maksimumlara dayalı olarak pivot noktalarını belirleyen bir fonksiyon tanımlar.
   - Pivot noktalarının konumunu hesaplar.

3. **Mum Grafiğinin Pivot Noktalarıyla Görselleştirilmesi:**
   - Mor işaretleyicilerle işaretlenmiş pivot noktalarına sahip bir mum çubuğu grafiği oluşturmak için Plotly'yi kullanır.

4. **Desenleri Algılama:**
   - Önceden tanımlanmış koşullara dayalı olarak belirli mum çubuğu modellerini tespit etmek için bir işlev tanımlar.
   - Tespit edilen modeller, daha yüksek en yüksek ve daha yüksek en düşük veya daha düşük en yüksek ve en düşük düşük dizilerini içerir.

### Kullanım
Bu kodu kullanmak için:
- Gerekli kütüphanelerin kurulu olduğundan emin olun (pandas, pandas_ta, numpy,plotly,scipy).
- Şamdan verileri CSV dosyanızın yolunu belirtin.
- Analiz gereksinimlerinize göre pencere boyutları ve desen koşulları gibi parametreleri ayarlayın.
- Kodu çalıştırın ve algılanan modeller için DataFrame'i kontrol edin.

Bu kod, tüccarlar ve analistler için pivot noktalarını belirlemede ve belirli mum çubuğu modellerini tespit etmede faydalı olabilir ve finansal piyasaların teknik analizlerine yardımcı olabilir.

Daha fazla yardıma ihtiyacınız varsa veya sorularınız varsa lütfen bizimle iletişime geçmekten çekinmeyin!