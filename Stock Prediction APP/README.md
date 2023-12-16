## English
## Stock Forecast App

This is a simple Streamlit web application that allows you to forecast stock prices using the ARIMA (AutoRegressive Integrated Moving Average) model. The app fetches historical stock price data using the Yahoo Finance API and then uses the ARIMA model to make future price predictions.

### How to Use

1. Select a stock from the dropdown list for which you want to make predictions (GOOG, AAPL, MSFT, or GME).
2. Use the slider to choose the number of years you want to forecast into the future (1 to 4 years).
3. The app will display the raw data and a plot of the historical stock prices along with the forecasted prices.

### Getting Started

To run this app locally, you will need to have Python and Streamlit installed. You can install the required dependencies using the following command:

		pip install streamlit pandas numpy yfinance statsmodels matplotlib

Next, you can run the app using the following command:

		streamlit run main.py

Make sure to replace main.py with the filename of the script containing the code above.

### Code Overview

The app is written in Python and uses the Streamlit library for creating the web application. Here is a brief overview of the main components of the code:

1. **Importing Libraries:** The necessary libraries, including Streamlit, pandas, numpy, yfinance, statsmodels, and matplotlib, are imported at the beginning of the script.

2. **User Input:** The user can select a stock and the number of years for the forecast using a dropdown and a slider, respectively.

3. **Data Loading:** The data for the selected stock is fetched from Yahoo Finance using the yfinance library. The fetched data is then displayed in the app as raw data.

4. **Plotting**: The historical stock prices are plotted using matplotlib and displayed in the app.

5. **ARIMA Model:** The historical stock prices are prepared for the ARIMA model, and the model is fitted to the data using the statsmodels library.

6. **Forecasting:** The ARIMA model is used to make future price predictions for the selected number of years.

7. **Forecast Plot:** The forecasted prices are plotted along with the historical data using matplotlib, and the plot is displayed in the app.

8. **Forecast Components:** The app displays a message indicating that individual forecast components are not available in the current implementation.

### Caching

The app uses Streamlit's caching feature (@st.cache_data) to store the fetched data for a certain amount of time (TTL) to avoid unnecessary API calls when the user revisits the same stock's forecast within the TTL period.

> *Please note that this app provides a basic stock price forecast using the ARIMA model. For more advanced and accurate predictions, you may consider using other forecasting methods and incorporating additional features.*


## İngilizce
## Stok Tahmini Uygulaması

Bu, ARIMA (Otomatik Regresif Entegre Hareketli Ortalama) modelini kullanarak hisse senedi fiyatlarını tahmin etmenizi sağlayan basit bir Streamlit web uygulamasıdır. Uygulama, Yahoo Finance API'sini kullanarak geçmiş hisse senedi fiyat verilerini alır ve ardından gelecekteki fiyat tahminlerini yapmak için ARIMA modelini kullanır.

### Nasıl kullanılır

1. Açılır listeden tahmin yapmak istediğiniz hisse senedini seçin (GOOG, AAPL, MSFT veya GME).
2. Geleceğe yönelik tahminde bulunmak istediğiniz yıl sayısını (1 ila 4 yıl) seçmek için kaydırıcıyı kullanın.
3. Uygulama, ham verileri ve tahmini fiyatlar ile birlikte geçmiş hisse senedi fiyatlarının bir grafiğini görüntüler.

### Başlarken

Bu uygulamayı yerel olarak çalıştırmak için Python ve Streamlit'in kurulu olması gerekir. Aşağıdaki komutu kullanarak gerekli bağımlılıkları kurabilirsiniz:

		pip install streamlit pandas numpy yfinance statsmodels matplotlib


Ardından, aşağıdaki komutu kullanarak uygulamayı çalıştırabilirsiniz:

		streamlit run mainTR.py

mainTR.py'yi yukarıdaki kodu içeren betiğin dosya adıyla değiştirdiğinizden emin olun.

### Koda Genel Bakış

Uygulama Python'da yazılmıştır ve web uygulamasını oluşturmak için Streamlit kitaplığını kullanır. İşte kodun ana bileşenlerine kısa bir genel bakış:

1. **Kitaplıkları İçe Aktarma:** Streamlit, pandas, numpy, yfinance, statsmodels ve matplotlib gibi gerekli kitaplıklar betiğin başında içe aktarılır.

2. **Kullanıcı Girişi:** Kullanıcı, sırasıyla bir açılır menüyü ve kaydırıcıyı kullanarak tahmin için bir hisse senedi ve yıl sayısı seçebilir.

3. **Veri Yükleme:** Seçilen hisse senedi için veriler, yfinance kitaplığı kullanılarak Yahoo Finance'ten alınır. Alınan veriler daha sonra uygulamada ham veri olarak görüntülenir.

4. **Çizelgelendirme**: Geçmiş hisse senedi fiyatları matplotlib kullanılarak çizilir ve uygulamada görüntülenir.

5. **ARIMA Modeli:** ARIMA modeli için geçmiş hisse senedi fiyatları hazırlanır ve model, statsmodels kitaplığı kullanılarak verilere uydurulur.

6. **Tahmin:** ARIMA modeli, seçilen yıl sayısı için gelecekteki fiyat tahminlerini yapmak için kullanılır.

7. **Tahmin Grafiği:** Tahmini fiyatlar, matplotlib kullanılarak geçmiş verilerle birlikte çizilir ve çizim uygulamada görüntülenir.

8. **Tahmin Bileşenleri:** Uygulama, tek tek tahmin bileşenlerinin mevcut uygulamada bulunmadığını belirten bir mesaj görüntüler.

### Önbelleğe almak

Uygulama, kullanıcı TTL dönemi içinde aynı hisse senedinin tahminini tekrar ziyaret ettiğinde gereksiz API çağrılarını önlemek için getirilen verileri belirli bir süre (TTL) boyunca depolamak için Streamlit'in önbelleğe alma özelliğini (@st.cache_data) kullanır.

> *Lütfen bu uygulamanın ARIMA modelini kullanarak temel bir hisse senedi fiyatı tahmini sağladığını unutmayın. Daha gelişmiş ve doğru tahminler için diğer tahmin yöntemlerini kullanmayı ve ek özellikler eklemeyi düşünebilirsiniz.*
