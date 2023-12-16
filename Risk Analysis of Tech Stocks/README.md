## English
## Stock Analysis and Monte Carlo Simulation
This script performs a comprehensive analysis of selected stocks (AAPL, GOOG, MSFT, AMZN, NFLX). The analysis includes:

1. Downloading historical stock data using Yahoo Finance API (yfinance).
2. Calculating moving averages for different time periods (10, 25, 50 days) and visualizing them.
3. Calculating daily returns and visualizing them.
4. Exploratory data analysis using seaborn's pairplot and correlation heatmap.
5. Monte Carlo simulation for predicting future stock prices.

### Prerequisites
- Python 3.x
- Required Python libraries: pandas, numpy, matplotlib, seaborn, yfinance

### Installation
	pip install -r requirements.txt
	
### Usage

1. Open the script in a Python environment (Jupyter Notebook, Spyder, etc.).
2. Run each cell sequentially.
3. The script will download historical stock data, perform various analyses, and visualize the results.

### Description
- **Data Retrieval:** The script fetches historical stock data for the specified stocks (AAPL, GOOG, MSFT, AMZN, NFLX) using Yahoo Finance.
- **Moving Averages:** Moving averages for 10, 25, and 50 days are calculated and plotted.
- **Daily Returns:** The script calculates and visualizes the daily returns for the selected stocks.
- **Exploratory Data Analysis (EDA):** The script uses seaborn to create a pairplot and a correlation heatmap for a deeper understanding of the relationships between stock returns.
- **Monte Carlo Simulation:** A Monte Carlo simulation is performed to predict future stock prices for Google (GOOG).

### Results
The script generates visualizations and statistics to help analyze stock performance, understand relationships between stocks, and estimate potential future prices using Monte Carlo simulation.

### Disclaimer
This script is for educational and informational purposes only. Stock market investments involve risks, and past performance is not indicative of future results. Always perform your own research and consider seeking advice from a qualified financial professional before making investment decisions.  

## Türkçe
## Stok Analizi ve Monte Carlo Simülasyonu
Bu komut dosyası, seçilen hisse senetlerinin (AAPL, GOOG, MSFT, AMZN, NFLX) kapsamlı bir analizini gerçekleştirir. Analiz şunları içerir:

1. Yahoo Finance API (yfinance) kullanarak geçmiş hisse senedi verilerini indirme.
2. Farklı zaman dilimleri (10, 25, 50 gün) için hareketli ortalamaların hesaplanması ve görselleştirilmesi.
3. Günlük getirilerin hesaplanması ve görselleştirilmesi.
4. Seaborn'un çift grafiğini ve korelasyon ısı haritasını kullanan keşifsel veri analizi.
5. Gelecekteki hisse senedi fiyatlarını tahmin etmek için Monte Carlo simülasyonu.

### Önkoşullar
- Python 3.x
- Gerekli Python kütüphaneleri: pandas, numpy, matplotlib, seaborn, yfinance

### Kurulum
	pip install -r requirements.txt

### Kullanım

1. Betiği bir Python ortamında açın (Jupyter Notebook, Spyder, vb.).
2. Her hücreyi sırayla çalıştırın.
3. Komut dosyası geçmiş stok verilerini indirecek, çeşitli analizler yapacak ve sonuçları görselleştirecektir.

### Tanım
- **Veri Alma:** Komut dosyası, Yahoo Finance'i kullanarak belirtilen hisse senetleri (AAPL, GOOG, MSFT, AMZN, NFLX) için geçmiş hisse senedi verilerini getirir.
- **Hareketli Ortalamalar:** 10, 25 ve 50 günlük hareketli ortalamalar hesaplanır ve çizilir.
- **Günlük Getiriler:** Komut dosyası, seçilen hisse senetlerinin günlük getirilerini hesaplar ve görselleştirir.
- **Keşifsel Veri Analizi (EDA):** Komut dosyası, hisse senedi getirileri arasındaki ilişkilerin daha derinlemesine anlaşılması amacıyla bir çift grafiği ve korelasyon ısı haritası oluşturmak için seaborn'u kullanır.
- **Monte Carlo Simülasyonu:** Google'ın (GOOG) gelecekteki hisse senedi fiyatlarını tahmin etmek için bir Monte Carlo simülasyonu gerçekleştirilir.

### Sonuçlar
Komut dosyası, Monte Carlo simülasyonunu kullanarak hisse senedi performansını analiz etmeye, hisse senetleri arasındaki ilişkileri anlamaya ve gelecekteki potansiyel fiyatları tahmin etmeye yardımcı olacak görselleştirmeler ve istatistikler üretir.

### Sorumluluk reddi beyanı
Bu script yalnızca eğitim ve bilgilendirme amaçlıdır. Hisse senedi piyasası yatırımları risk içerir ve geçmiş performans gelecekteki sonuçların göstergesi değildir. Yatırım kararları vermeden önce her zaman kendi araştırmanızı yapın ve nitelikli bir finans uzmanından tavsiye almayı düşünün.
