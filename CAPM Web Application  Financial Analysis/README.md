
## English
## Capital Asset Pricing Model (CAPM) 
This code is a web application that implements the Capital Asset Pricing Model (CAPM). It allows users to select stocks and a time period, and then calculates and displays various financial metrics based on the selected data.

### Purpose
The purpose of this application is to provide insights into the risk and return of different stocks using the CAPM. It helps users understand the relationship between a stock's beta value and its expected return. The application also visualizes the stock prices and returns to facilitate analysis and comparison.

### Features
**Stock Selection:** Users can choose up to four stocks from a predefined list.

**Time Period:** Users can specify the number of years of historical data to consider for analysis.

**Data Retrieval:** The application retrieves historical stock price data from the Yahoo Finance API.

**Data Visualization:** The application displays the stock prices and returns in interactive line charts using the Plotly library.

**CAPM Calculations:** The application calculates the beta value and expected return for each selected stock using the CAPM formula.

**Dataframe Display:** The application presents the stock price and return data in tabular format using Pandas dataframes.

**Error Handling:** The application handles errors gracefully and provides appropriate error messages for invalid inputs.

### How to Use
1. Install the required dependencies by running pip install streamlit pandas yfinance pandas_datareader datetime plotly.
2. Run the script using streamlit run <filename>.py (replace <filename> with the actual filename).
3. Access the application in your web browser at http://localhost:8501.
4. Choose up to four stocks from the provided list.
5. Specify the number of years of historical data to consider.
6. Explore the interactive charts and view the calculated metrics.

### Dependencies
**streamlit:** Used to create the web application interface.

**pandas:** Used for data manipulation and analysis.

**yfinance:** Used to retrieve historical stock price data from Yahoo Finance.

**pandas_datareader:** Used to fetch data from various online sources.

**datetime:** Used for date and time calculations.

**plotly:** Used for interactive charting and data visualization.

### Author
This application was developed by Serkan Polat.

## Türkçe
## Sermaye Varlıkları Fiyatlandırma Modeli (CAPM)
Bu kod, Sermaye Varlıkları Fiyatlandırma Modeli (CAPM) uygulayan bir web uygulamasıdır. Kullanıcılara hisse senetleri ve bir zaman aralığı seçme imkanı sunar ve ardından seçilen verilere dayanarak çeşitli finansal metrikleri hesaplar ve görüntüler.

### Amaç
Bu uygulamanın amacı, CAPM kullanarak farklı hisse senetlerinin risk ve getirisine ilişkin içgörüler sağlamaktır. Kullanıcılara bir hisse senedinin beta değeri ile beklenen getirisi arasındaki ilişkiyi anlamalarına yardımcı olur. Uygulama ayrıca hisse senedi fiyatlarını ve getirilerini görselleştirerek analiz ve karşılaştırma yapmayı kolaylaştırır.

### Özellikler
**Hisse Senedi Seçimi:** Kullanıcılar önceden tanımlanmış bir listeden en fazla dört hisse senedi seçebilir.

**Zaman Aralığı:** Kullanıcılar analiz için göz önünde bulundurmak üzere geçmiş verilerin yıl sayısını belirleyebilir.

**Veri Alımı:** Uygulama, Yahoo Finance API'den geçmiş hisse senedi fiyat verilerini alır.

**Veri Görselleştirme:** Uygulama, Plotly kütüphanesini kullanarak hisse senedi fiyatlarını ve getirilerini etkileşimli çizgi grafikleriyle gösterir.

**CAPM Hesaplamaları:** Uygulama, CAPM formülünü kullanarak her bir seçilen hisse senedi için beta değerini ve beklenen getirisini hesaplar.

**Veri Tablosu Görüntüleme:** Uygulama, Pandas veri çerçevelerini kullanarak hisse senedi fiyatı ve getiri verilerini tablo formatında sunar.

**Hata Yönetimi:** Uygulama, hataları düzgün bir şekilde ele alır ve geçersiz girişler için uygun hata mesajları sağlar.

### Nasıl Kullanılır

1. Gerekli bağımlılıkları yüklemek için pip install streamlit pandas yfinance pandas_datareader datetime plotly komutunu çalıştırın.
2. Script'i streamlit run <dosya_adı>.py komutuyla çalıştırın (<dosya_adı>'nı gerçek dosya adıyla değiştirin).
3. Uygulamayı web tarayıcınızda http://localhost:8501 adresinden erişin.
4. Sağlanan listeden en fazla dört hisse senedi seçin.
5. Analiz için göz önünde bulundurmak istediğiniz yıl sayısını belirtin.
6. Etkileşimli grafikleri keşfedin ve hesaplanmış metrikleri görüntüleyin.

### Bağımlılıklar

**streamlit:** Web uygulama arayüzü oluşturmak için kullanılır.

**pandas:** Veri manipülasyonu ve analizi için kullanılır.

**yfinance:** Yahoo Finance'den geçmiş hisse senedi fiyat verilerini almak için kullanılır.

**pandas_datareader:** Çeşitli çevrimiçi kaynaklardan veri almak için kullanılır.

**datetime:** Tarih ve saat hesaplamaları için kullanılır.

**plotly:** Etkileşimli grafik oluşturma ve veri görselleştirme için kullanılır.

### Yazar
Bu uygulama Serkan Polat tarafından geliştirilmiştir.