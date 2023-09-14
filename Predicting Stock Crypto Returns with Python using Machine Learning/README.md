## English
## Stock Price Direction Prediction using Logistic Regression

This repository contains a demonstration of predicting stock price direction (upward or downward) using a Logistic Regression model. The project includes data preprocessing, feature engineering, model training, and evaluation.

## Introduction

In this project, we aim to predict the direction of stock price movements using historical price data and logistic regression. We will create a trading strategy based on the predictions and evaluate its performance.

## Project Overview

- **Data Collection**: We use the `yfinance` library to download historical stock price data for Apple Inc. (AAPL) from January 1, 2020.

- **Feature Engineering**: We calculate logarithmic returns and assign direction labels to each return value. Lagged features are created to capture historical price movements.

- **Model Training**: We train a Logistic Regression model using the lagged features and direction labels.

- **Model Evaluation**: The model's performance is evaluated on a test set. We plot the cumulative returns of the trading strategy and provide a classification report.

### Setup

Make sure you have the required libraries installed. You can install them using the following:

	pip install pandas numpy yfinance scikit-learn

### Instructions

1. Clone the repository:
 		git clone https://github.com/your-username/stock-price-prediction.git

2. Navigate to the project directory:
		cd stock-price-prediction

3. Open the Python script stock_price_prediction.py to see the implementation details.

### Conclusion
This project demonstrates the process of using logistic regression for stock price direction prediction and evaluating the model's performance. The trading strategy's cumulative returns are plotted, and a classification report provides insights into the model's accuracy, precision, and recall.

## Türkçe
## Lojistik Regresyon Kullanarak Hisse Senedi Fiyat Yönü Tahmini

Bu havuz, bir Lojistik Regresyon modeli kullanarak hisse senedi fiyat yönünü (yukarı veya aşağı) tahmin etmenin bir gösterimini içerir. Proje, veri ön işleme, özellik mühendisliği, model eğitimi ve değerlendirmeyi içerir.

## Giriş

Bu projede geçmiş fiyat verilerini ve lojistik regresyonu kullanarak hisse senedi fiyat hareketlerinin yönünü tahmin etmeyi amaçlıyoruz. Tahminlere dayalı bir ticaret stratejisi oluşturacağız ve performansını değerlendireceğiz.

## Projeye Genel Bakış

- **Veri Toplama**: 1 Ocak 2020 tarihinden itibaren Apple Inc. (AAPL) için geçmiş hisse senedi fiyatı verilerini indirmek için "yfinance" kitaplığını kullanıyoruz.

- **Özellik Mühendisliği**: Logaritmik getirileri hesaplar ve her bir dönüş değerine yön etiketleri atarız. Gecikmeli özellikler, geçmiş fiyat hareketlerini yakalamak için oluşturulur.

- **Model Eğitimi**: Gecikmeli özellikler ve yön etiketlerini kullanarak bir Lojistik Regresyon modeli eğitiyoruz.

- **Model Değerlendirmesi**: Modelin performansı bir test setinde değerlendirilir. Ticaret stratejisinin kümülatif getirilerini çizer ve bir sınıflandırma raporu sunarız.

### Kurmak

Gerekli kitaplıkların kurulu olduğundan emin olun. Bunları aşağıdakileri kullanarak kurabilirsiniz:

pip kurulumu pandalar numpy yfinance scikit-learn

### Talimatlar

1. Depoyu klonlayın:
 git klonu https://github.com/your-username/stock-price-prediction.git

2. Proje dizinine gidin:
cd hisse senedi fiyatı tahmini

3. Uygulama ayrıntılarını görmek için stock_price_prediction.py Python komut dosyasını açın.

### Çözüm
Bu proje, stok fiyat yönü tahmini için lojistik regresyon kullanma sürecini ve modelin performansını değerlendirmeyi göstermektedir. Alım satım stratejisinin kümülatif getirileri çizilir ve bir sınıflandırma raporu, modelin doğruluğu, kesinliği ve geri çağırması hakkında içgörü sağlar.