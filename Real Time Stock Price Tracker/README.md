## English
## Stock Price Tracker
This project is a simple stock price tracker that allows users to monitor the current price and percentage change of various stock tickers. The tracker provides a user-friendly interface where users can add and remove stock tickers to track. The frontend is built using HTML, CSS, and JavaScript, while the backend uses Flask for handling requests and fetching stock data from Yahoo Finance.

### Features
- Add and Remove Tickers: Users can add new stock tickers to the tracker and remove existing ones.
- Real-time Updates: The tracker updates stock prices and percentage changes in real-time at regular intervals.
- Color Indicators: The UI uses color indicators to represent price changes, making it easier to spot positive and negative changes.
- Flash Animation: Tickers flash with different colors when their prices change, adding visual appeal and highlighting updates.

### Technologies Used
- **Frontend:** HTML, CSS, JavaScript (jQuery)
- **Backend:** Python (Flask)
- **Data Source:** Yahoo Finance (using yfinance library)

### Setup Instructions

1. Clone the repository to your local machine.
2. Install the required Python libraries by running: pip install flask yfinance.
3. Run the Flask application: python app.py.
4. Open a web browser and go to http://localhost:5000 to access the stock price tracker.

### Project Structure
- **static/style.css:** Contains the CSS styles for styling the UI components.
- **static/script.js:** Contains the JavaScript code for managing user interactions and updating stock prices.
- **templates/index.html:** The main HTML file that displays the stock tracker interface.
- **app.py:** The Flask application file that serves the frontend and handles backend requests.

### How It Works

1. Users can add new stock tickers by entering the ticker symbol in the input field and clicking the "Add" button.
2. Existing tickers can be removed by clicking the "Remove" button next to each ticker.
3. The tracker fetches stock data from Yahoo Finance using the get_stock_data route in the backend.
4. Stock data (current price and open price) is displayed for each ticker, along with the percentage change.
5. Price changes are color-coded, and tickers flash with different colors to indicate updates.

### Future Enhancements
- **Additional Stock Data:** Expand the project to display more comprehensive stock data, such as trading volume and historical trends.
- **User Authentication:** Implement user accounts to save personalized ticker lists and preferences.
- **Advanced Tracking:** Allow users to set alerts for price thresholds and receive notifications.


## Türkçe
## Hisse Senedi Fiyat Takibi
Bu proje, kullanıcıların çeşitli hisse senetlerinin mevcut fiyatını ve yüzde değişimini izlemelerine olanak tanıyan basit bir hisse senedi fiyat izleyicisidir. İzleyici, kullanıcıların izlemek için hisse senedi şeritleri ekleyebileceği ve kaldırabileceği kullanıcı dostu bir arayüz sağlar. Ön uç HTML, CSS ve JavaScript kullanılarak oluşturulurken arka uç, istekleri işlemek ve Yahoo Finance'ten stok verilerini almak için Flask'ı kullanır.

### Özellikler
- Hisse Senetleri Ekleme ve Kaldırma: Kullanıcılar, izleyiciye yeni hisse senetleri ekleyebilir ve mevcut olanları kaldırabilir.
- Gerçek Zamanlı Güncellemeler: İzleyici, hisse senedi fiyatlarını ve yüzde değişikliklerini gerçek zamanlı olarak düzenli aralıklarla günceller.
- Renk Göstergeleri: Kullanıcı arabirimi, fiyat değişikliklerini temsil etmek için renk göstergelerini kullanır ve bu da olumlu ve olumsuz değişikliklerin fark edilmesini kolaylaştırır.
- Flash Animasyon: Fiyatlar değiştiğinde şeritler farklı renklerle yanıp sönerek görsel çekicilik katar ve güncellemeleri vurgular.

### Kullanılan Teknolojiler
- **Ön Uç:** HTML, CSS, JavaScript (jQuery)
- **Arka uç:** Python (Flask)
- **Veri Kaynağı:** Yahoo Finance (yfinance kitaplığı kullanılarak)

### Kurulum Talimatları

1. Depoyu yerel makinenize kopyalayın.
2. Aşağıdakileri çalıştırarak gerekli Python kitaplıklarını kurun: pip install flask yfinance.
3. Flask uygulamasını çalıştırın: python app.py.
4. Bir web tarayıcısı açın ve hisse senedi fiyat izleyicisine erişmek için http://localhost:5000 adresine gidin.

### Proje Yapısı
- **statik/style.css:** UI bileşenlerini şekillendirmek için CSS stillerini içerir.
- **static/script.js:** Kullanıcı etkileşimlerini yönetmek ve hisse senedi fiyatlarını güncellemek için JavaScript kodunu içerir.
- **templates/index.html:** Hisse senedi izleyici arayüzünü görüntüleyen ana HTML dosyası.
- **app.py:** Ön uca hizmet eden ve arka uç isteklerini işleyen Flask uygulama dosyası.

### Nasıl çalışır

1. Kullanıcılar, giriş alanına hisse senedi sembolünü girip "Ekle" düğmesini tıklayarak yeni hisse senedi senedi ekleyebilirler.
2. Mevcut şeritler, her bir işaretin yanındaki "Kaldır" düğmesine tıklanarak kaldırılabilir.
3. İzleyici, arka uçtaki get_stock_data yolunu kullanarak Yahoo Finance'ten hisse senedi verilerini alır.
4. Hisse senedi verileri (mevcut fiyat ve açık fiyat), yüzde değişimiyle birlikte her bir şerit için görüntülenir.
5. Fiyat değişiklikleri renk kodludur ve kayan yazılar, güncellemeleri belirtmek için farklı renklerde yanıp söner.

### Gelecekteki Geliştirmeler
- **Ek Stok Verileri:** İşlem hacmi ve geçmiş trendler gibi daha kapsamlı stok verilerini görüntülemek için projeyi genişletin.
- **Kullanıcı Kimlik Doğrulaması:** Kişiselleştirilmiş kayan yazı listelerini ve tercihlerini kaydetmek için kullanıcı hesapları uygulayın.
- **Gelişmiş İzleme:** Kullanıcıların fiyat eşikleri için uyarılar ayarlamasına ve bildirim almasına izin verin.

