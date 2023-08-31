## English
## Predicting if the stock market is going Up or Down
This project demonstrates the use of logistic regression for predicting the direction of the stock market based on historical price and volume data. It utilizes the statsmodels and sklearn libraries in Python to build and evaluate the predictive model.

### Requirements

Before running the code, make sure you have the following Python libraries installed:

- **pandas:** Data manipulation library
- **yfinance:** Yahoo Finance API to download stock data
- **statsmodels:** Statistical modeling library
- **numpy:** Numerical computations library
- **sklearn:** Machine learning library

You can install these libraries using the following command:

	pip install pandas yfinance statsmodels numpy scikit-learn

### Usage

1. Clone or download this repository to your local machine.

2. Open the Python script (stock_market_prediction.py) in your preferred Python environment.

3. Modify the script as needed, including the stock symbol and date range for data download.

4. Run the script using the following command:

		python stock_market_prediction.py

### Description

The code follows these main steps:

1. Download historical stock market data for a specified date range using the Yahoo Finance API.

2. Calculate the daily percentage change of the adjusted closing prices and prepare lagged features.

3. Create a binary target variable representing the market direction (1 for up, 0 for down).

4. Perform logistic regression using the statsmodels library to predict the market direction based on lagged features and volume.

5. Evaluate the model's performance using a confusion matrix and classification report from the sklearn library.

### Results

After running the script, you will see the following outputs:

- Model summary containing logistic regression statistics.
- Confusion matrix showing the performance of the model on the test data.
- Classification report with precision, recall, F1-score, and support metrics.


## Türkçe
## Borsanın Yukarı mı yoksa Aşağı mı gideceğini tahmin etme
Bu proje, tarihsel fiyat ve hacim verilerine dayalı olarak borsanın yönünü tahmin etmek için lojistik regresyonun kullanımını göstermektedir. Tahmine dayalı modeli oluşturmak ve değerlendirmek için Python'daki istatistik modellerini ve sklearn kitaplıklarını kullanır.

### Gereksinimler

Kodu çalıştırmadan önce, aşağıdaki Python kitaplıklarının kurulu olduğundan emin olun:

- **pandalar:** Veri işleme kitaplığı
- **yfinance:** Hisse senedi verilerini indirmek için Yahoo Finance API
- **statsmodels:** İstatistiksel modelleme kitaplığı
- **numpy:** Sayısal hesaplama kitaplığı
- **sklearn:** Makine öğrenimi kitaplığı

Bu kütüphaneleri aşağıdaki komutu kullanarak kurabilirsiniz:

pip kurulumu pandalar yfinans istatistik modelleri numpy scikit-learn

### Kullanım

1. Bu havuzu yerel makinenize kopyalayın veya indirin.

2. Python betiğini (stock_market_prediction.py) tercih ettiğiniz Python ortamında açın.

3. Veri indirme için hisse senedi simgesi ve tarih aralığı dahil olmak üzere komut dizisini gerektiği gibi değiştirin.

4. Komut dosyasını aşağıdaki komutu kullanarak çalıştırın:

piton stock_market_prediction.py

### Tanım

Kod şu ana adımları takip eder:

1. Yahoo Finance API'sini kullanarak belirli bir tarih aralığı için geçmiş borsa verilerini indirin.

2. Düzeltilmiş kapanış fiyatlarının günlük yüzde değişimini hesaplayın ve gecikmeli özellikler hazırlayın.

3. Pazar yönünü temsil eden ikili bir hedef değişken oluşturun (yukarı için 1, aşağı için 0).

4. Gecikmeli özelliklere ve hacme dayalı olarak pazar yönünü tahmin etmek için istatistik modelleri kitaplığını kullanarak lojistik regresyon gerçekleştirin.

5. Sklearn kitaplığından bir karışıklık matrisi ve sınıflandırma raporu kullanarak modelin performansını değerlendirin.

### Sonuçlar

Komut dosyasını çalıştırdıktan sonra aşağıdaki çıktıları göreceksiniz:

- Lojistik regresyon istatistiklerini içeren model özeti.
- Modelin test verileri üzerindeki performansını gösteren karışıklık matrisi.
- Kesinlik, geri çağırma, F1 puanı ve destek metrikleri ile sınıflandırma raporu.