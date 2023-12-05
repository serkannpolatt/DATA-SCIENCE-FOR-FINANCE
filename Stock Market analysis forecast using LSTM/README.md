## Türkçe
## LSTM ile Hisse Senedi Fiyat Tahmini
Bu depo, Uzun Kısa Süreli Bellek (LSTM) sinir ağlarını kullanarak hisse senedi fiyatlarını tahmin etmek için Python kodunu içerir. Analiz, veri görselleştirmeyi, hareketli ortalamaları, günlük getirileri, korelasyon analizini ve geçmiş hisse senedi fiyatlarını kullanan bir tahmin modelini içerir.

### Kurallara Genel Bakış

**1. Veri Alma ve Görselleştirme**
- Kod, gerekli kütüphanelerin içe aktarılmasıyla ve ortamın kurulmasıyla başlar.
- Teknoloji şirketlerinin (Apple, Google, Microsoft, Amazon) geçmiş hisse senedi verileri, Yahoo Finance API kullanılarak alınır.
- Kapanış fiyatları ve işlem hacimleri Matplotlib ve Seaborn kullanılarak görselleştirilir.

**2. Hareketli ortalamalar**
- Her şirket için 10, 20 ve 50 günlük basit hareketli ortalamalar (MA) hesaplanır ve çizilir.

**3. Günlük İadeler**
- Hisse senedi fiyatlarındaki günlük yüzde değişim (günlük getiriler) hesaplanır ve görselleştirilir.

**4. Korelasyon analizi**
- Teknoloji hisselerinin günlük getirileri ile kapanış fiyatları arasındaki ilişkiyi analiz etmek için korelasyon matrisleri çizilmektedir.

**5. LSTM** ile Hisse Senedi Fiyat Tahmini
- Hisse senedi fiyat tahmini LSTM sinir ağı kullanılarak gerçekleştirilir.
- Geçmiş hisse senedi fiyatları MinMaxScaler kullanılarak önceden işlenir ve ölçeklenir.
- LSTM modeli Keras kütüphanesi kullanılarak eğitilir.
- Test veri seti üzerinde tahminler yapılır ve Hatanın Ortalama Karekökü (RMSE) hesaplanır.
- Sonuçlar, eğitim verilerini, gerçek fiyatları ve tahmin edilen fiyatları gösterecek şekilde görselleştirilir.

### Nasıl kullanılır

Gerekli tüm kitaplıkların kurulu olduğundan emin olun.
Sağlanan kodu bir Jupyter not defterinde veya Python ortamında çalıştırın.

> *Not: Bu kod temel bir örnektir ve gerçek dünyadaki bir uygulama için daha fazla özelleştirme ve optimizasyon gerektirebilir.*

Kodu denemekten ve özel ihtiyaçlarınıza göre uyarlamaktan çekinmeyin. Sorularınız veya önerileriniz varsa lütfen konu açın veya projeye katkıda bulunun.

## English
## Stock Price Prediction with LSTM
This repository contains Python code for predicting stock prices using Long Short-Term Memory (LSTM) neural networks. The analysis includes data visualization, moving averages, daily returns, correlation analysis, and a predictive model using historical stock prices.

### Overview of the Code

**1. Data Retrieval and Visualization**
- The code begins by importing necessary libraries and setting up the environment.
- Historical stock data for technology companies (Apple, Google, Microsoft, Amazon) is retrieved using the Yahoo Finance API.
- Closing prices and trading volumes are visualized using Matplotlib and Seaborn.

**2. Moving Averages**
- Simple moving averages (MA) for 10, 20, and 50 days are calculated and plotted for each company.

**3. Daily Returns**
- The daily percentage change in stock prices (daily returns) is calculated and visualized.

**4. Correlation Analysis**
- Correlation matrices are plotted to analyze the relationship between daily returns and closing prices of the technology stocks.

**5. Stock Price Prediction with LSTM**
- Stock price prediction is performed using an LSTM neural network.
- The historical stock prices are preprocessed and scaled using MinMaxScaler.
- The LSTM model is trained using the Keras library.
- Predictions are made on the test dataset, and the Root Mean Squared Error (RMSE) is calculated.
- The results are visualized, showing the training data, actual prices, and predicted prices.

### How to Use

Ensure you have all the required libraries installed.
Run the provided code in a Jupyter notebook or Python environment.

> *Note: This code is a basic example and may need further customization and optimization for a real-world application.*

Feel free to experiment with the code and adapt it to your specific needs. If you have any questions or suggestions, please open an issue or contribute to the project.

