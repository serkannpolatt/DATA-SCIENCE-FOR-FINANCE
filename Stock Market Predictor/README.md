## English
## Stock Market Predictor
This project aims to predict stock prices using a Long Short-Term Memory (LSTM) neural network model. It utilizes historical stock data obtained from Yahoo Finance (yfinance library) and implements a sequential LSTM model using the Keras library.

### Usage

1. Clone the repository or download the script.

2. Run the script:

		streamlit run your_script_name.py

3. Open the provided Streamlit web application in your browser.

4. Enter the stock symbol and observe the predicted stock prices.

### Code Overview

**1. Data Collection and Preprocessing**

- The script uses the yfinance library to download historical stock data for a specified stock symbol.
- It calculates and plots the 100-day and 200-day moving averages.

**2. Model Training**

- The LSTM neural network model is built using the Keras library.
- The model is trained on a portion of the historical data (80%) to predict future stock prices.

**3. Model Evaluation and Prediction**

- The trained model is used to predict stock prices on a test dataset.
- The predictions are compared with the original prices, and the results are visualized using Matplotlib.

**4. Streamlit Web Application**

- The web application allows users to input a stock symbol and view historical stock data, moving averages, and the predicted vs. actual prices.

**5. Model Saving and Loading**

- The trained model is saved in a Keras-compatible file (Stock Predictions Model.keras).
- The Streamlit application loads the pre-trained model for making predictions.


## Türkçe
## Hisse Senedi Piyasası Tahmincisi
Bu proje, Uzun Kısa Süreli Bellek (LSTM) sinir ağı modelini kullanarak hisse senedi fiyatlarını tahmin etmeyi amaçlamaktadır. Yahoo Finance'den (yfinance kütüphanesi) elde edilen geçmiş hisse senedi verilerini kullanır ve Keras kütüphanesini kullanarak sıralı bir LSTM modeli uygular.

### Kullanım

1. Depoyu klonlayın veya betiği indirin.

2. Komut dosyasını çalıştırın:

		streamlit run your_script_name.py

3. Sağlanan Streamlit web uygulamasını tarayıcınızda açın.

4. Hisse senedi sembolünü girin ve tahmin edilen hisse senedi fiyatlarını gözlemleyin.

### Kodlara Genel Bakış

**1. Veri Toplama ve Ön İşleme**

- Komut dosyası, belirli bir hisse senedi sembolüne ilişkin geçmiş hisse senedi verilerini indirmek için yfinance kitaplığını kullanır.
- 100 günlük ve 200 günlük hareketli ortalamaları hesaplar ve çizer.

**2. Model Eğitimi**

- LSTM sinir ağı modeli Keras kütüphanesi kullanılarak oluşturulmuştur.
- Model, gelecekteki hisse senedi fiyatlarını tahmin etmek için geçmiş verilerin bir kısmı (%80) üzerinde eğitilmiştir.

**3. Model Değerlendirme ve Tahmin**

- Eğitilen model, bir test veri kümesinde hisse senedi fiyatlarını tahmin etmek için kullanılır.
- Tahminler orijinal fiyatlarla karşılaştırılır ve sonuçlar Matplotlib kullanılarak görselleştirilir.

**4. Kolaylaştırılmış Web Uygulaması**

- Web uygulaması, kullanıcıların bir hisse senedi sembolü girmesine ve geçmiş hisse senedi verilerini, hareketli ortalamaları ve tahmin edilen ve gerçek fiyatları görüntülemesine olanak tanır.

**5. Model Kaydetme ve Yükleme**

- Eğitilen model Keras uyumlu bir dosyaya (Stock Predictions Model.keras) kaydedilir.
- Streamlit uygulaması, tahmin yapmak için önceden eğitilmiş modeli yükler.
