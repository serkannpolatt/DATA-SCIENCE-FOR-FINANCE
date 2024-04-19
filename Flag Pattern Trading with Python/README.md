## English
## Candlestick Analysis with Pivot Points and Flag Detection

### Purpose of the Code

This set of code snippets aims to analyze candlestick data for the EUR/USD forex pair. Here's a breakdown of what each section accomplishes:

1. **Loading and Preprocessing Data:**
   - Reads candlestick data from a CSV file containing columns for time, open, high, low, close, and volume.
   - Renames columns and removes rows with zero volume.
   - Checks for NA values and displays the first 10 rows of the DataFrame.

2. **Identifying Pivot Points:**
   - Defines a function `pivotid` to identify pivot points based on given conditions.
   - Adds a new column 'pivot' to the DataFrame indicating pivot points.
   - Defines a function `pointpos` to calculate the position of pivot points.

3. **Visualizing Candlestick Chart with Pivot Points:**
   - Uses Plotly to create a candlestick chart with pivot points marked as purple markers.

4. **Detecting Flags:**
   - Utilizes linear regression to detect flag patterns in the candlestick data.
   - Defines a function `detect_flag` to identify flag patterns based on slope and correlation conditions.
   - Optionally, plots candlestick charts with detected flags.

### Usage
To use this code:
- Ensure you have the required libraries installed (pandas, numpy, plotly, scipy).
- Provide the path to your candlestick data CSV file.
- Adjust parameters such as window sizes and conditions according to your analysis needs.
- Call the `detect_flag` function with appropriate parameters to detect flag patterns.

This code can be useful for traders and analysts in identifying pivot points and detecting flag patterns, which are commonly used in technical analysis of financial markets.

Please let me know if you need further assistance or clarification!


## Türkçe
## Pivot Noktaları ve Bayrak Tespiti ile Mum Analizi

### Kuralların Amacı

Bu kod parçacıkları seti, EUR/USD forex çifti için mum çubuğu verilerini analiz etmeyi amaçlamaktadır. Her bölümün neyi başardığının bir dökümü aşağıda verilmiştir:

1. **Verileri Yükleme ve Ön İşleme:**
   - Zaman, açılış, yüksek, düşük, kapanış ve hacim sütunlarını içeren bir CSV dosyasından mum çubuğu verilerini okur.
   - Sütunları yeniden adlandırır ve sıfır hacimli satırları kaldırır.
   - NA değerlerini kontrol eder ve DataFrame'in ilk 10 satırını görüntüler.

2. **Pivot Noktalarını Belirleme:**
   - Verilen koşullara göre pivot noktalarını belirlemek için bir 'pivotid' fonksiyonu tanımlar.
   - DataFrame'e pivot noktalarını gösteren yeni bir 'pivot' sütunu ekler.
   - Pivot noktalarının konumunu hesaplamak için bir 'pointpos' fonksiyonunu tanımlar.

3. **Mum Grafiğinin Pivot Noktalarıyla Görselleştirilmesi:**
   - Mor işaretleyicilerle işaretlenmiş pivot noktalarına sahip bir mum çubuğu grafiği oluşturmak için Plotly'yi kullanır.

4. **Bayrakların Tespiti:**
   - Şamdan verilerindeki bayrak desenlerini tespit etmek için doğrusal regresyondan yararlanır.
   - Eğim ve korelasyon koşullarına dayalı olarak bayrak desenlerini tanımlamak için bir "algılama_bayrağı" işlevi tanımlar.
   - İsteğe bağlı olarak, algılanan bayraklarla birlikte mum grafikleri çizer.

### Kullanım
Bu kodu kullanmak için:
- Gerekli kütüphanelerin kurulu olduğundan emin olun (pandas, numpy,plotly,scipy).
- Şamdan verileri CSV dosyanızın yolunu belirtin.
- Pencere boyutları ve koşulları gibi parametreleri analiz ihtiyaçlarınıza göre ayarlayın.
- Bayrak desenlerini tespit etmek için uygun parametrelerle 'detect_flag' işlevini çağırın.

Bu kod, finansal piyasaların teknik analizinde yaygın olarak kullanılan pivot noktalarının belirlenmesinde ve bayrak modellerinin tespit edilmesinde yatırımcılar ve analistler için yararlı olabilir.

Daha fazla yardıma veya açıklamaya ihtiyacınız olursa lütfen bana bildirin!