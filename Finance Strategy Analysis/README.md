# English
# Stock Breakout Strategy Analyzer

This application performs a **stock breakout strategy analysis** using **Streamlit**, **Yahoo Finance (YFinance)**, and **Plotly**. It allows users to input stock tickers, date ranges, and custom thresholds to analyze breakout trading opportunities based on volume and price movements. The app provides a user-friendly interface for summary statistics, detailed trade results, and interactive visualizations.

---

## Features

- **Fetch Historical Stock Data**: Retrieves data using Yahoo Finance.
- **Breakout Analysis**: Identifies trading opportunities based on:
  - Volume breakout thresholds (e.g., volume higher than a percentage of its 20-day moving average).
  - Daily price change thresholds.
- **Holding Period Simulation**: Calculates returns for a specified holding period after breakouts.
- **Interactive Charts**: Visualizes stock price movements, volume trends, and return distributions using Plotly.
- **Downloadable Results**: Exports breakout analysis results as a CSV file.
- **Multi-Ticker Analysis**: Supports analysis of multiple stock tickers in a single run.
  
---

## How It Works

1. **Input Parameters**:  
   In the sidebar, you can specify:
   - Stock tickers (e.g., TSLA, AAPL).
   - Date range for the analysis.
   - Volume breakout threshold (e.g., 200% of the 20-day moving average).
   - Daily price change threshold (e.g., 2% increase).
   - Holding period to calculate returns after breakouts (e.g., 10 days).

2. **Data Fetching**:  
   The app fetches historical stock data for the selected tickers and date range.

3. **Breakout Conditions**:  
   The app calculates:
   - Volume ratios (current volume vs. 20-day moving average).
   - Daily returns (percentage change in stock price).
   - Identifies breakout days based on user-defined thresholds.

4. **Trade Analysis**:  
   For each breakout day, it computes:
   - Entry/exit dates and prices.
   - Percentage return after the holding period.
   - Volume ratios on breakout days.

5. **Results Display**:  
   The app provides:
   - **Summary Statistics**: Total trades, win rate, average return, max/min returns, and return standard deviation.
   - **Detailed Results**: Entry/exit points, returns, and volume ratios in a tabular format.
   - **Interactive Charts**:
     - Candlestick chart of stock price.
     - Bar chart of volume trends.
     - Histogram of return distributions.

6. **Download Results**:  
   Users can download the detailed results as a CSV file.

---

## Technologies Used

- **Streamlit**: For building the web interface.
- **YFinance**: To fetch historical stock data.
- **Plotly**: For creating interactive visualizations.
- **Pandas**: For data manipulation and analysis.
- **Datetime**: To handle date-related operations.

# Türkçe
# Hisse Senedi Breakout Strateji Analizörü

Bu uygulama, **Streamlit**, **Yahoo Finance (YFinance)** ve **Plotly** kullanarak **hisse senedi breakout strateji analizi** gerçekleştirir. Kullanıcıların hisse senedi sembolleri, tarih aralıkları ve özel eşik değerlerini girerek, hacim ve fiyat hareketlerine dayalı breakout ticaret fırsatlarını analiz etmelerini sağlar. Uygulama, kullanıcı dostu bir arayüzde özet istatistikler, detaylı ticaret sonuçları ve etkileşimli görselleştirmeler sunar.

---

## Özellikler

- **Tarihi Hisse Senedi Verisi Çekme**: Yahoo Finance API'si kullanarak veri çeker.
- **Breakout Analizi**:
  - Hacim breakout eşiği (ör. 20 günlük hareketli ortalamanın %200'ü üzerinde hacim).
  - Günlük fiyat değişim eşiği (ör. %2 artış).
- **Pozisyon Süresi Simülasyonu**: Breakout sonrası belirli bir pozisyon süresi için getirileri hesaplar.
- **Etkileşimli Grafikler**: 
  - Hisse fiyat hareketleri.
  - Hacim trendleri.
  - Getiri dağılımları.
- **Sonuçları İndirme**: Breakout analizi sonuçlarını CSV dosyası olarak dışa aktarır.
- **Çoklu Sembol Analizi**: Birden fazla hisse senedi sembolü için aynı anda analiz yapabilir.

---

## Nasıl Çalışır?

1. **Parametre Girişi**:  
   Yan panelde aşağıdaki parametreler girilebilir:
   - Hisse senedi sembolleri (ör. TSLA, AAPL).
   - Analiz için tarih aralığı.
   - Hacim breakout eşiği (ör. %200).
   - Günlük fiyat değişim eşiği (ör. %2).
   - Pozisyon süresi (ör. 10 gün).

2. **Veri Çekimi**:  
   Uygulama, belirtilen hisse senetleri ve tarih aralığı için tarihi hisse senedi verilerini çeker.

3. **Breakout Koşulları**:  
   Uygulama aşağıdaki hesaplamaları yapar:
   - Hacim oranları (mevcut hacim / 20 günlük hareketli ortalama).
   - Günlük getiri (% değişim).
   - Kullanıcı tanımlı eşiklere göre breakout günlerini belirler.

4. **Ticaret Analizi**:  
   Her breakout günü için aşağıdaki hesaplamalar yapılır:
   - Giriş/çıkış tarihleri ve fiyatları.
   - Pozisyon süresi sonunda yüzdelik getiri.
   - Breakout günündeki hacim oranları.

5. **Sonuçları Görüntüleme**:  
   Uygulama şu çıktıları sağlar:
   - **Özet İstatistikler**: Toplam işlem sayısı, kazanma oranı, ortalama getiri, maksimum/minimum getiriler, standart sapma.
   - **Detaylı Sonuçlar**: Giriş/çıkış noktaları, getiriler ve hacim oranları tablosu.
   - **Etkileşimli Grafikler**:
     - Hisse fiyatları için mum grafiği.
     - Hacim trendleri için çubuk grafik.
     - Getiri dağılımları için histogram.

6. **Sonuçları İndirme**:  
   Analiz sonuçları CSV dosyası olarak indirilebilir.

---

## Kullanılan Teknolojiler

- **Streamlit**: Web arayüzü oluşturmak için.
- **YFinance**: Hisse senedi verilerini almak için.
- **Plotly**: Etkileşimli görselleştirmeler için.
- **Pandas**: Veri manipülasyonu ve analizi için.
- **Datetime**: Tarih işlemleri için.