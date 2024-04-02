## English
## Analysis of Transaction Data

### Overview:
This repository contains Python scripts for analyzing transaction data stored in a CSV file named "transactions.csv". The scripts utilize the Pandas library for data manipulation and Matplotlib for data visualization. The main objective is to perform exploratory data analysis and statistical tests to gain insights into the transaction data.

### Scripts:
**1. Data Loading and Plotting Balance Over Time:**
- This script loads the transaction data into a Pandas DataFrame from the CSV file.
- It preprocesses the 'TRANSACTION DATE' column to extract the date part and convert it to datetime format.
- Plots the balance over time using Matplotlib.

**2. Plotting Positive and Negative PL Over Transaction Time:**
- Extracts transaction times and preprocesses them to numeric format.
- Filters the DataFrame for positive and negative PL (Profit/Loss).
- Plots histograms of transaction times for positive and negative PL, overlaid with original time labels.
- Performs statistical tests (T-test and Mann-Whitney U test) to compare transaction times between positive and negative PL.

**3. Comparing Positive and Negative PL Counts Over Transaction Time:**
- Further explores the distribution of positive and negative PL over transaction time.
- Plots bar charts of counts of positive and negative PL over transaction time.
- Overlays a line plot showing the difference between positive and negative PL counts.

### Dependencies:

- Python 3.x
- Pandas
- Matplotlib
- NumPy
- SciPy (for statistical tests)

### Usage:

1. Ensure all dependencies are installed (pip install pandas matplotlib numpy scipy).
2. Place the transaction data CSV file named "transactions.csv" in the same directory as the scripts.
3. Run each script individually to perform different analyses on the transaction data.

### Note:

- The scripts assume the structure of the CSV file with specific column names ('TRANSACTION DATE', 'PL', etc.).
- Adjustments may be needed based on the actual structure of the data.
- Feel free to modify and extend the scripts according to specific analytical requirements.

## Türkçe 
## İşlem Verilerinin Analizi

### Genel Bakış:
Bu depo, "transactions.csv" adlı bir CSV dosyasında saklanan işlem verilerini analiz etmeye yönelik Python komut dosyalarını içerir. Komut dosyaları, veri işleme için Pandas kütüphanesini ve veri görselleştirme için Matplotlib'i kullanır. Temel amaç, işlem verilerine ilişkin içgörü elde etmek için keşif amaçlı veri analizi ve istatistiksel testler gerçekleştirmektir.

### Kodlar:
**1. Zaman İçinde Veri Yükleme ve Grafiklendirme Dengesi:**
- Bu komut dosyası, işlem verilerini CSV dosyasından Pandas DataFrame'e yükler.
- 'İŞLEM TARİHİ' sütununu ön işleme tabi tutarak tarih kısmını çıkarır ve tarih saat formatına dönüştürür.
- Matplotlib'i kullanarak zaman içindeki dengeyi çizer.

**2. İşlem Süresi Boyunca Pozitif ve Negatif PL'nin Grafiği:**
- İşlem sürelerini çıkarır ve bunları sayısal formatta önceden işler.
- DataFrame'i pozitif ve negatif PL (Kar/Zarar) için filtreler.
- Orijinal zaman etiketleriyle kaplanmış, pozitif ve negatif PL için işlem zamanlarının histogramlarını çizer.
- Pozitif ve negatif PL arasındaki işlem sürelerini karşılaştırmak için istatistiksel testler (T testi ve Mann-Whitney U testi) gerçekleştirir.

**3. İşlem Süresi Boyunca Pozitif ve Negatif PL Sayımlarının Karşılaştırılması:**
- İşlem süresi boyunca pozitif ve negatif PL dağılımını daha ayrıntılı olarak araştırır.
- İşlem süresi boyunca pozitif ve negatif PL sayımlarının çubuk grafiklerini çizer.
- Pozitif ve negatif PL sayıları arasındaki farkı gösteren bir çizgi grafiğini kaplar.

### Bağımlılıklar:

- Python 3.x
- Pandas
- Matplotlib
- NumPy
- SciPy (for statistical tests)

### Kullanım:

1. Tüm bağımlılıkların kurulu olduğundan emin olun (pip install pandas matplotlib numpy scipy).
2. "transactions.csv" adlı işlem verileri CSV dosyasını komut dosyalarıyla aynı dizine yerleştirin.
3. İşlem verileri üzerinde farklı analizler gerçekleştirmek için her betiği ayrı ayrı çalıştırın.

### Not:

- Komut dosyaları, belirli sütun adlarıyla ('İŞLEM TARİHİ', 'PL' vb.) CSV dosyasının yapısını varsayar.
- Verilerin gerçek yapısına göre ayarlamalar yapılması gerekebilir.
- Senaryoları belirli analitik gereksinimlere göre değiştirmekten ve genişletmekten çekinmeyin.
