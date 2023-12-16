## English
## Candlestick App with Technical Indicators

This Python script is a Streamlit web application designed for analyzing financial data, particularly for stock market data. It provides interactive candlestick charts with various technical indicators for the specified date range.

### Features:
- **Candlestick Chart:** The main chart displays candlestick patterns for the specified date range, providing insights into the stock's opening, closing, highest, and lowest prices for each trading day.

- **Technical Indicators:** The application supports various technical indicators for technical analysis. Users can select and visualize additional indicators such as Simple Moving Average (SMA), Exponential Moving Average (EMA), Weighted Moving Average (WMA), Relative Strength Index (RSI), Momentum (MOM), Double Exponential Moving Average (DEMA), and Triple Exponential Moving Average (TEMA) along with the candlestick chart.

- **Date Range Selection:** The web app includes a sidebar with a user-friendly date range selection feature. Users can choose the start and end dates to analyze the desired historical data.

- **Close Prices:** Users have the option to display a line plot of the closing prices along with the candlestick chart for better trend analysis.

- **Volume Bars:** The application provides the option to include volume bars in the candlestick chart. This allows users to visualize trading volume along with price movements.

### How to Use:

**1. Installation:** Ensure you have Python installed along with the required packages. If not, you can install them using pip as follows:

	pip install -r requirements.txt

**2. Data:** Prepare your historical stock market data in CSV format. The script assumes that you have a CSV file named "AAPL.csv" containing data for Apple Inc. (AAPL). Replace this file with your own stock data CSV file.

**3. Run:** Execute the script using the following command:

	streamlit run candlestick_app.py

This will launch the Streamlit web app and open it in your default web browser.

**4. Explore:** The web app will present the candlestick chart along with the sidebar for selecting date range, technical indicators, and other options. You can interact with the charts and explore the stock's historical data and technical indicators.

### Important Notes:

- The web app uses Bokeh for plotting. Ensure you have Bokeh version 2.4.3 installed (as specified in the error message). You can downgrade Bokeh by running:

		pip install --force-reinstall --no-deps bokeh==2.4.3

- Customize the "AAPL.csv" file or replace it with your own stock data CSV file to analyze a different stock.

### Disclaimer:

This application is intended for educational and informational purposes only. It does not provide financial advice or recommendations for trading or investment decisions. Always conduct your due diligence and seek advice from a qualified financial advisor before making any investment decisions.

### Usage Example:

1. Run the script in your Python environment using the provided command.
2. The web app will open in your default web browser.
3. Use the sidebar to select the desired date range and the technical indicators you want to analyze.
4. Explore the candlestick chart and the selected technical indicators to gain insights into the historical stock market data.

> **Remember to make any necessary modifications to suit your specific use case. Enjoy analyzing financial data with the Candlestick App with Technical Indicators!****


## Türkçe
## Teknik Göstergelerle Mum Grafiği Uygulaması

Bu Python betiği, özellikle borsa verileri olmak üzere finansal verileri analiz etmek için tasarlanmış bir Streamlit web uygulamasıdır. Belirtilen tarih aralığı için çeşitli teknik göstergelerle etkileşimli mum grafikleri sağlar.

### Özellikler:
- **Mum Grafiği:** Ana grafik, belirtilen tarih aralığı için şamdan kalıplarını görüntüleyerek her bir işlem günü için hisse senedinin açılış, kapanış, en yüksek ve en düşük fiyatları hakkında fikir verir.

- **Teknik Göstergeler:** Uygulama, teknik analiz için çeşitli teknik göstergeleri destekler. Kullanıcılar Basit Hareketli Ortalama (SMA), Üstel Hareketli Ortalama (EMA), Ağırlıklı Hareketli Ortalama (WMA), Göreceli Güç Endeksi (RSI), Momentum (MOM), Çift Üstel Hareketli Ortalama (DEMA) ve Üçlü Üstel Hareketli Ortalama (TEMA) gibi ek göstergeleri şamdan grafiğiyle birlikte seçip görselleştirebilir.

- **Tarih Aralığı Seçimi:** Web uygulaması, kullanıcı dostu bir tarih aralığı seçme özelliğine sahip bir kenar çubuğu içerir. Kullanıcılar, istenen geçmiş verileri analiz etmek için başlangıç ​​ve bitiş tarihlerini seçebilir.

- **Kapanış Fiyatları:** Kullanıcılar, daha iyi trend analizi için mum grafiğiyle birlikte kapanış fiyatlarının bir çizgi grafiğini görüntüleme seçeneğine sahiptir.

- **Hacim Çubukları:** Uygulama, mum grafiğine hacim çubuklarını dahil etme seçeneği sunar. Bu, kullanıcıların işlem hacmini fiyat hareketleriyle birlikte görselleştirmesine olanak tanır.

### Nasıl kullanılır:

**1. Kurulum:** Gerekli paketlerle birlikte Python'un kurulu olduğundan emin olun. Değilse, bunları aşağıdaki gibi pip kullanarak kurabilirsiniz:

	pip install -r requirements.txt

**2. Veri:** Geçmiş borsa verilerinizi CSV formatında hazırlayın. Komut dosyası, Apple Inc. (AAPL) verilerini içeren "AAPL.csv" adlı bir CSV dosyanız olduğunu varsayar. Bu dosyayı kendi stok veri CSV dosyanızla değiştirin.

**3. Çalıştır:** Komut dosyasını aşağıdaki komutu kullanarak yürütün:

	streamlit run candlestick_app.py

Bu, Streamlit web uygulamasını başlatacak ve varsayılan web tarayıcınızda açacaktır.

**4. Keşfedin:** Web uygulaması, tarih aralığını, teknik göstergeleri ve diğer seçenekleri seçmek için kenar çubuğuyla birlikte mum grafiğini sunar. Grafiklerle etkileşim kurabilir ve hisse senedinin geçmiş verilerini ve teknik göstergelerini keşfedebilirsiniz.

### Önemli notlar:

- Web uygulaması çizim için Bokeh kullanır. Bokeh 2.4.3 sürümünün kurulu olduğundan emin olun (hata mesajında ​​belirtildiği gibi). Aşağıdakileri çalıştırarak Bokeh sürümünü düşürebilirsiniz:

		pip install --force-reinstall --no-deps bokeh==2.4.3


- Farklı bir hisse senedini analiz etmek için "AAPL.csv" dosyasını özelleştirin veya kendi stok veri CSV dosyanızla değiştirin.

### Feragatname:

Bu uygulama sadece eğitim ve bilgilendirme amaçlıdır. Ticaret veya yatırım kararları için mali tavsiye veya tavsiye sağlamaz. Herhangi bir yatırım kararı vermeden önce her zaman durum tespiti yapın ve nitelikli bir finansal danışmandan tavsiye alın.

### Kullanım Örneği:

1. Sağlanan komutu kullanarak betiği Python ortamınızda çalıştırın.
2. Web uygulaması, varsayılan web tarayıcınızda açılacaktır.
3. İstediğiniz tarih aralığını ve analiz etmek istediğiniz teknik göstergeleri seçmek için kenar çubuğunu kullanın.
4. Geçmiş borsa verileri hakkında bilgi edinmek için mum grafiğini ve seçilen teknik göstergeleri keşfedin.

> **Özel kullanım durumunuza uyacak gerekli değişiklikleri yapmayı unutmayın. Teknik Göstergeli Şamdan Uygulaması ile finansal verileri analiz etmenin keyfini çıkarın!****
