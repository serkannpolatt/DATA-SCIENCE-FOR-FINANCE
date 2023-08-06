## English
## Stock Analysis Chatbot Assistant

Stock Analysis Chatbot Assistant is a Python script used to understand user input in natural language and provide stock analysis services using the GPT-3.5 language model. This chatbot can call various functions to get the price of a particular stock, calculate the simple and exponential moving average, calculate the relative strength index and moving average convergence divergence, and plot the price graph of the stock.

### Setup

For the project to work, follow these steps:

1. Install the required libraries:

- json
- openai
- pandas
- matplotlib
- streamlite
- yfinance

2 . Add your OpenAI GPT-3.5 API access key to the "API_KEY.txt" file.
3. Run the python script "stock_analysis_chatbot.py"

### Use

Stock Analysis Chatbot Assistant takes stock name or symbol in natural language from the user and performs various analyzes on the specified stock. The user logs into the chat in natural language and the chatbot presents the analysis results and graphs.

Example Usage:

1. User Login: "Please bring the price of the AAPL (Apple) stock."
- Chatbot Response: "The latest price of AAPL stock: $150.25"

2. User Input: "What is a 50-day simple moving average for MSFT (Microsoft) stock?"
- Chatbot Response: "50-day simple moving average for MSFT stock: $175.60"

3. User Input: "Calculate RSI for GOOGL (Google) stock."
- Chatbot Response: "The RSI of the GOOGL stock: 67.42"

### Functions

This chatbot can provide stock analysis services by calling the following functions:

**one. get_stock_price(ticker):** Gets the latest price of a particular stock.

**2. calculate_SMA(ticker, window):** Calculates a simple moving average (SMA) for a given stock.

**3. calculate_EMA(ticker, window):** Calculates the exponential moving average (EMA) for a given stock.

**4. calculate_RSI(ticker):** Calculates the relative strength index (RSI) for a particular stock.

**5. calculate_MACD(ticker):** Calculates the moving average convergence divergence (MACD) for a given stock.

**6. plot_stock_price(ticker):** Plots the price chart of a particular stock for the last one year.

### Contributing

Please fork, make improvements and create pull requests to contribute to the project. Any contribution, feedback or question is clearly welcome!



## Türkçe
## Stok Analizi Chatbot Asistanı

Stock Analysis Chatbot Assistant, GPT-3.5 dil modelini kullanarak doğal dilde yapılan kullanıcı girişlerini anlamaya ve stok analizi hizmetleri sağlamak için kullanılan bir Python betiğidir. Bu chatbot, belirli bir hisse senedinin fiyatını almak, basit ve üssel hareketli ortalama hesaplamak, göreceli güç endeksini ve hareketli ortalama yakınsaklık sapmasını hesaplamak ve hisse senedinin fiyat grafiğini çizmek için çeşitli işlevleri çağırabilir.

### Kurulum

Projenin çalışması için aşağıdaki adımları izleyin:

1. Gerekli kütüphaneleri yükleyin:

- json
- openai
- pandas
- matplotlib
- streamlit
- yfinance

2 . OpenAI GPT-3.5 API erişim anahtarınızı "API_KEY.txt" dosyasına ekleyin.
3 . Python betiği "stock_analysis_chatbot.py" dosyasını çalıştırın

### Kullanım

Stock Analysis Chatbot Assistant, kullanıcıdan doğal dilde hisse senedi adı veya sembolü alır ve belirtilen hisse senediyle ilgili çeşitli analizler yapar. Kullanıcı, sohbete doğal dilde giriş yapar ve chatbot, analiz sonuçlarını ve grafikleri sunar.

Örnek Kullanım:

1. Kullanıcı Girişi: "Lütfen AAPL (Apple) hisse senedinin fiyatını getir."
	- Chatbot Yanıtı: "AAPL hisse senedinin en son fiyatı: $150.25"

2. Kullanıcı Girişi: "MSFT (Microsoft) hisse senedi için 50 günlük basit hareketli ortalama nedir?"
	- Chatbot Yanıtı: "MSFT hisse senedi için 50 günlük basit hareketli ortalama: $175.60"

3. Kullanıcı Girişi: "GOOGL (Google) hisse senedi için RSI hesapla."
	- Chatbot Yanıtı: "GOOGL hisse senedinin RSI değeri: 67.42"

### İşlevler

Bu chatbot, aşağıdaki işlevleri çağırarak stok analizi hizmetleri sağlayabilir:

**1. get_stock_price(ticker):** Belirli bir hisse senedinin en son fiyatını alır.

**2. calculate_SMA(ticker, window):** Belirli bir hisse senedi için basit hareketli ortalama (SMA) hesaplar.

**3. calculate_EMA(ticker, window):** Belirli bir hisse senedi için üssel hareketli ortalama (EMA) hesaplar.

**4. calculate_RSI(ticker):** Belirli bir hisse senedi için göreceli güç endeksi (RSI) hesaplar.

**5. calculate_MACD(ticker):** Belirli bir hisse senedi için hareketli ortalama yakınsaklık sapması (MACD) hesaplar.

**6. plot_stock_price(ticker):** Belirli bir hisse senedinin son bir yıllık fiyat grafiğini çizer.

### Katkıda Bulunma

Projeye katkıda bulunmak için lütfen forklayın, geliştirmelerinizi yapın ve pull request oluşturun. Her türlü katkı, geri bildirim veya soru için açık bir şekilde hoş geldiniz!
