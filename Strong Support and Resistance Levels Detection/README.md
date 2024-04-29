## English
## Candlestick Data Analysis with Pivot Points

### Purpose of the Code

This set of code snippets serves the purpose of analyzing candlestick data for the EUR/USD forex pair. Here's a breakdown of what each section accomplishes:

1. **Loading and Preprocessing Data:**
   - Reads candlestick data from a CSV file containing Open, High, Low, Close, and Volume columns for the EUR/USD forex pair.
   - Removes rows with zero volume and resets the index.

2. **Identifying Pivot Points:**
   - Defines a function `pivotid` to identify pivot points in the candlestick data based on the given conditions.
   - Adds a new column 'pivot' to the DataFrame indicating pivot points.

3. **Visualizing Candlestick Chart with Pivot Points:**
   - Uses Plotly to create a candlestick chart with pivot points marked.
   - Sets different colors for increasing and decreasing candlesticks.
   - Adjusts the layout and styling of the chart.

4. **Creating Histogram of High and Low Values:**
   - Utilizes Matplotlib to generate a histogram of high and low values corresponding to pivot points.
   - Defines bin width and calculates the number of bins based on the data.
   - Displays separate histograms for high and low values with different colors.

### Usage
To use this code:
- Ensure you have the required libraries installed (pandas, plotly, matplotlib).
- Provide the path to your candlestick data CSV file.
- Adjust parameters such as window sizes and colors according to your analysis needs.

This code can be helpful for traders and analysts in visually identifying pivot points and understanding the distribution of high and low values within the data.

Please let me know if you need further assistance or clarification!


## Türkçe
## Pivot Noktalarıyla Mum Çubuğu Veri Analizi

### Kuralların Amacı

Bu kod parçacıkları seti, EUR/USD forex çifti için mum çubuğu verilerinin analiz edilmesi amacına hizmet eder. Her bölümün neyi başardığının bir dökümü aşağıda verilmiştir:

1. **Verileri Yükleme ve Ön İşleme:**
   - EUR/USD forex çifti için Açık, Yüksek, Düşük, Kapanış ve Hacim sütunlarını içeren bir CSV dosyasından mum çubuğu verilerini okur.
   - Sıfır hacimli satırları kaldırır ve dizini sıfırlar.

2. **Pivot Noktalarını Belirleme:**
   - Verilen koşullara göre mum çubuğu verilerindeki pivot noktalarını tanımlamak için bir 'pivotid' fonksiyonu tanımlar.
   - DataFrame'e pivot noktalarını gösteren yeni bir 'pivot' sütunu ekler.

3. **Mum Grafiğinin Pivot Noktalarıyla Görselleştirilmesi:**
   - İşaretlenmiş pivot noktalarına sahip bir mum grafiği oluşturmak için Plotly'yi kullanır.
   - Artan ve azalan şamdanlar için farklı renkler ayarlar.
   - Grafiğin düzenini ve stilini ayarlar.

4. **Yüksek ve Düşük Değerlerin Histogramını Oluşturma:**
   - Pivot noktalarına karşılık gelen yüksek ve düşük değerlerin histogramını oluşturmak için Matplotlib'i kullanır.
   - Kutu genişliğini tanımlar ve verilere göre kutu sayısını hesaplar.
   - Yüksek ve düşük değerler için farklı renklerle ayrı histogramlar görüntüler.

### Kullanım
Bu kodu kullanmak için:
- Gerekli kütüphanelerin kurulu olduğundan emin olun (pandalar, komplo, matplotlib).
- Şamdan verileri CSV dosyanızın yolunu belirtin.
- Pencere boyutları ve renkleri gibi parametreleri analiz ihtiyaçlarınıza göre ayarlayın.

Bu kod, tüccarlar ve analistler için pivot noktalarını görsel olarak belirlemede ve verilerdeki yüksek ve düşük değerlerin dağılımını anlamada yardımcı olabilir.

Daha fazla yardıma veya açıklamaya ihtiyacınız olursa lütfen bana bildirin!