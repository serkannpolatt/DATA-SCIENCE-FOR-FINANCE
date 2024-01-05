## Türkçe
## Finansal Veri Analizi
Bu proje, Kamuyu Aydınlatma Platformu'ndan (KAP) hisse senedi kodlarını çeken, ardından bu kodlarla Yahoo Finance'ten günlük kapanış fiyatlarını çeken ve son olarak bu fiyat verilerini birleştirip korelasyon analizi yapan bir Python scriptini içerir.

### Adımlar

**1. Şirket Kodlarını Çekme:**

- İlk olarak, requests ve BeautifulSoup kütüphaneleri kullanılarak belirtilen URL'den (KAP - Kamuyu Aydınlatma Platformu) hisse senedi kodlarını çeker.
- Kodlar, "Tickers.csv" adlı bir CSV dosyasına kaydedilir.

**2. Hisse Senedi Fiyat Verilerini Çekme ve Kaydetme:**

- pandas_datareader ve yfinance kütüphaneleri kullanılarak CSV dosyasından alınan hisse senedi kodlarıyla Yahoo Finance'ten günlük kapanış fiyatları çekilir.
- Her bir hisse senedi için ayrı bir CSV dosyasına kaydedilir.
- Bu dosyalar, "History Data" klasörü altına kaydedilir.

**3. Fiyat Verilerini Birleştirme:**

- Tüm hisse senedi fiyat verileri birleştirilerek "MergedData.csv" adlı bir CSV dosyası oluşturulur.
- Bu adım, hisse senedi fiyatlarının zaman içindeki performanslarını karşılaştırmak amacıyla kullanılır.

**4. Korelasyon Analizi:**

- Kullanıcıdan kaç hisse senedinin korelasyonunu incelemek istediği sorulur.
- Kullanıcıdan hisse senedi kodları alınır.
- Seçilen hisse senetlerinin kapanış fiyatları arasındaki korelasyon matrisi hesaplanır.
- Korelasyon matrisi, seaborn ve matplotlib kütüphaneleri kullanılarak ısı haritası olarak görselleştirilir.

**5. Görselleştirme:**

- Elde edilen korelasyon matrisi, seaborn kütüphanesi ile ısı haritası olarak çizilir.
- matplotlib kullanılarak çizilen ısı haritası ekrana gösterilir.

Bu kodları kullanarak, belirli hisse senetlerinin birbirleriyle olan ilişkilerini anlamak ve portföy çeşitlendirmesi veya risk yönetimi konularında kararlar almak mümkündür.

## English
## Financial Data Analysis
This project includes a Python script that pulls stock codes from the Public Disclosure Platform (PDP), then pulls daily closing prices from Yahoo Finance with these codes, and finally combines this price data and performs correlation analysis.

### Steps

**one. Capturing Company Codes:**

- First, it retrieves stock codes from the specified URL (Public Disclosure Platform) using the requests and BeautifulSoup libraries.
- Codes are saved in a CSV file named "Tickers.csv".

**2. Capturing and Saving Stock Price Data:**

- Using pandas_datareader and yfinance libraries, daily closing prices are retrieved from Yahoo Finance with stock codes taken from the CSV file.
- Saved in a separate CSV file for each stock.
- These files are saved under the "History Data" folder.

**3. Combining Price Data:**

- All stock price data is merged to create a CSV file called "MergedData.csv".
- This step is used to compare the performance of stock prices over time.

**4. Correlation Analysis:**

- The user is asked how many stocks they want to examine the correlation of.
- Stock codes are received from the user.
- The correlation matrix between the closing prices of the selected stocks is calculated.
- The correlation matrix is ​​visualized as a heat map using seaborn and matplotlib libraries.

**5. Visualization:**

- The resulting correlation matrix is ​​drawn as a heat map with the seaborn library.
- The heat map drawn using matplotlib is displayed on the screen.

Using these codes, it is possible to understand how specific stocks relate to each other and make decisions on portfolio diversification or risk management.


