# eNGLİSH

## Financial News Scraper and Market Volatility Analyzer

### Overview
This project is a Streamlit-based web application that fetches financial news articles from **Financial Times (FT)** and **Bloomberg**, and also analyzes market volatility using **Yahoo Finance** data. It provides users with:
- A search function to find relevant articles based on user-provided keywords.
- Automated web scraping using `requests`, `BeautifulSoup`, and `Selenium`.
- Market volatility analysis by sector using **Yahoo Finance**.
- A personalized greeting based on the current time in Hong Kong.

---

### Features
- **Fetch Articles from Financial Times & Bloomberg**: Users can enter keywords, and the app retrieves top articles.
- **Automated Web Scraping**:
  - FT articles are scraped using `requests` and `BeautifulSoup`.
  - Bloomberg articles are retrieved using `Selenium` and `webdriver_manager`.
- **Market Volatility Analysis**:
  - Uses `yfinance` to get stock market data.
  - Calculates and displays annualized volatility of key sectors.
- **User-Friendly Streamlit Interface**:
  - Dynamic keyword input.
  - Adjustable number of links.
  - Display of news articles and market volatility.

---

#### Interacting with the App
1. Enter keywords (up to 10).
2. Set the number of articles to fetch.
3. Click **Fetch Articles** to retrieve news.
4. View market volatility analysis.

---

### Code Breakdown
#### Key Functions:
- `fetch_ft_articles(keywords, num_links)`: Scrapes FT for articles based on keywords.
- `fetch_bloomberg_article_urls(keywords, num_links)`: Uses Selenium to scrape Bloomberg for article URLs.
- `get_titles_from_urls(urls)`: Extracts meaningful titles from Bloomberg URLs.
- `fetch_volatility_data()`: Retrieves stock sector volatility using Yahoo Finance.

#### Web Scraping:
- Uses `requests` for FT.
- Uses `Selenium` with Firefox WebDriver for Bloomberg (headless mode).
- Implements random user-agents and delays to avoid detection.

#### Market Analysis:
- Fetches historical stock prices.
- Calculates **annualized volatility** for different market sectors.

---

### Notes
- **Selenium setup**: The script automatically installs `GeckoDriver` for Firefox.
- **FT & Bloomberg restrictions**: Some content may be behind paywalls.
- **Time-based greeting**: Adjusts dynamically based on Hong Kong time.

---

### Future Improvements
- Support for additional financial news sources.
- More robust error handling for dynamic web elements.
- Sentiment analysis of fetched news.

---

### Author
Developed by **Serkan Polat**

---

# Türkçe
# README

## Finansal Haber Çekici ve Piyasa Volatilite Analizörü

### Genel Bakış
Bu proje, **Financial Times (FT)** ve **Bloomberg**'den finansal haber makalelerini çeken ve ayrıca **Yahoo Finance** verilerini kullanarak piyasa volatilitesini analiz eden Streamlit tabanlı bir web uygulamasıdır. Kullanıcılara şunları sunar:
- Kullanıcı tarafından sağlanan anahtar kelimelere göre ilgili makaleleri bulma arama fonksiyonu.
- `requests`, `BeautifulSoup` ve `Selenium` kullanarak otomatik web kazıma.
- **Yahoo Finance** kullanarak piyasa volatilitesi analizi.
- Hong Kong'daki mevcut saate göre kişiselleştirilmiş selamlaşma.

---

### Özellikler
- **Financial Times & Bloomberg'den Makale Çekme**: Kullanıcılar anahtar kelimeler girerek uygulamanın en iyi makaleleri çekmesini sağlar.
- **Otomatik Web Kazıma**:
  - FT makaleleri `requests` ve `BeautifulSoup` kullanılarak çekilir.
  - Bloomberg makaleleri `Selenium` ve `webdriver_manager` kullanılarak alınır.
- **Piyasa Volatilite Analizi**:
  - `yfinance` kullanarak borsa verileri alınır.
  - Anahtar sektörlerin yıllık volatilitesi hesaplanır ve görüntülenir.
- **Kullanıcı Dostu Streamlit Arayüzü**:
  - Dinamik anahtar kelime girişi.
  - Bağlantı sayısının ayarlanabilir olması.
  - Haber makaleleri ve piyasa volatilitesinin görüntülenmesi.

---

#### Uygulama ile Etkileşim
1. Anahtar kelimeleri girin (en fazla 10).
2. Çekilecek makale sayısını belirleyin.
3. **Makale Çek** butonuna tıklayarak haberleri çekin.
4. Piyasa volatilite analizini görüntüleyin.

---

### Kodun Parçalara Ayrılması
#### Ana Fonksiyonlar:
- `fetch_ft_articles(keywords, num_links)`: FT'den anahtar kelimelere göre makale çeker.
- `fetch_bloomberg_article_urls(keywords, num_links)`: Bloomberg'den makale URL'lerini almak için Selenium kullanır.
- `get_titles_from_urls(urls)`: Bloomberg URL'lerinden anlamlı başlıklar çıkarır.
- `fetch_volatility_data()`: Yahoo Finance kullanarak borsa sektörü volatilitesini alır.

#### Web Kazıma:
- FT için `requests` kullanılır.
- Bloomberg için `Selenium` ve Firefox WebDriver (headless modu) kullanılır.
- Algılama önlemek için rastgele kullanıcı ajanları ve gecikmeler uygulanır.

#### Piyasa Analizi:
- Tarihsel hisse senedi fiyatları alınır.
- Farklı piyasa sektörleri için **yıllık volatilite** hesaplanır.

---

### Notlar
- **Selenium Kurulumu**: Betik otomatik olarak Firefox için `GeckoDriver` yükler.
- **FT & Bloomberg Kısıtlamaları**: Bazı içerikler ücretli duvarların arkasında olabilir.
- **Zaman Tabanlı Selamlaşma**: Hong Kong saati temel alınarak dinamik olarak ayarlanır.

---

### Gelecek İyileştirmeler
- Ekstra finansal haber kaynakları desteği.
- Dinamik web öğeleri için daha sağlam hata yönetimi.
- Çekilen haberlerin duygu analizi.

---

### Yazar
**Serkan Polat** tarafından geliştirilmiştir.

---
