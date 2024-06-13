## English
## Technical Analysis and Backtesting Project

### Overview
This project is designed to perform technical analysis and backtesting on financial market data. Utilizing various technical indicators and trading strategies, the project aims to provide insights into potential trading signals and optimize trading performance. The primary libraries used are pandas for data manipulation, pandas_ta for technical indicators, and backtesting for backtesting trading strategies.

### Objectives
- **Data Preparation:** Load and preprocess financial data to ensure it is suitable for analysis.
- **Technical Indicators:** Calculate various technical indicators to identify trading signals.
- **Signal Generation:** Implement logic to generate buy/sell signals based on the calculated indicators.
- **Visualization:** Plot the data and indicators for visual analysis.
- **Backtesting:** Test trading strategies on historical data to evaluate their performance.
- **Optimization:** Optimize strategy parameters to maximize returns.

### Data Preparation
The data preparation involves loading a CSV file containing financial market data and performing necessary cleaning steps. This includes:

- Removing rows where the high and low prices are equal.
- Dropping rows with missing closing prices.
- Resetting the index of the DataFrame.

### Technical Indicators
Several technical indicators are calculated to assist in identifying trading signals:

- **Exponential Moving Average (EMA):** A weighted moving average that gives more significance to recent price data.
- **Average True Range (ATR):** A measure of market volatility.
- **Bollinger Bands (BB):** A volatility indicator that consists of a middle band (SMA) and two outer bands.

Custom Bollinger Bands are calculated with different standard deviation multipliers to analyze price behavior:

- Standard deviation of 4.
- Standard deviation of 0.5.

### Signal Generation
Signals are generated based on specific conditions involving the EMA and Bollinger Bands:

- **EMA Signals:** Generated when the closing prices for a defined number of previous periods are all above their respective EMAs.
- **Total Signal:** Combines EMA signals with additional conditions related to Bollinger Bands to provide a comprehensive signal for trading decisions.

### Visualization
The data and calculated indicators are visualized using Plotly. Candlestick charts are plotted along with the EMA and Bollinger Bands to provide a clear visual representation of the market data and signals.

### Backtesting
Trading strategies are backtested on historical data to evaluate their performance. The strategies are defined using the Strategy class from the backtesting library, and the Backtest class is used to execute the backtest.

- **Stop-Loss Mechanism:** Implemented to manage risk by setting stop-loss levels based on the ATR or a fixed percentage of the closing price.
- **Trade Execution:** Conditions for entering and exiting trades are defined based on the generated signals.

### Optimization
Strategy parameters are optimized to maximize returns. The optimization process involves:

- Testing different values for the stop-loss percentage and ATR ratio.
- Identifying the parameter set that yields the highest return.

The results of the optimization process provide insights into the most effective strategy configurations for the given historical data.


## Türkçe 
## Teknik Analiz ve Geriye Dönük Test Projesi

### Genel Bakış
Bu proje, finansal piyasa verileri üzerinde teknik analiz ve geriye dönük testlerin gerçekleştirilmesi amacıyla tasarlanmıştır. Çeşitli teknik göstergeler ve ticaret stratejileri kullanan proje, potansiyel ticaret sinyallerine ilişkin içgörü sağlamayı ve ticaret performansını optimize etmeyi amaçlıyor. Kullanılan birincil kütüphaneler veri manipülasyonu için pandas, teknik göstergeler için pandas_ta ve ticaret stratejilerinin geriye dönük testi için backtesting'dir.

### Hedefler
- **Veri Hazırlama:** Analize uygun olduğundan emin olmak için finansal verileri yükleyin ve ön işleme tabi tutun.
- **Teknik Göstergeler:** Ticaret sinyallerini tanımlamak için çeşitli teknik göstergeleri hesaplayın.
- **Sinyal Üretimi:** Hesaplanan göstergelere dayalı olarak alım/satım sinyalleri oluşturmak için mantığı uygulayın.
- **Görselleştirme:** Görsel analiz için verileri ve göstergeleri çizin.
- **Geriye dönük test:** Performanslarını değerlendirmek için ticaret stratejilerini geçmiş veriler üzerinde test edin.
- **Optimizasyon:** Getirileri en üst düzeye çıkarmak için strateji parametrelerini optimize edin.

### Veri Hazırlama
Veri hazırlığı, finansal piyasa verilerini içeren bir CSV dosyasının yüklenmesini ve gerekli temizleme adımlarının gerçekleştirilmesini içerir. Bu içerir:

- Yüksek ve düşük fiyatların eşit olduğu satırların kaldırılması.
- Eksik kapanış fiyatlarına sahip satırların bırakılması.
- DataFrame'in dizininin sıfırlanması.

### Teknik Göstergeler
Ticaret sinyallerinin belirlenmesine yardımcı olmak için çeşitli teknik göstergeler hesaplanır:

- **Üstel Hareketli Ortalama (EMA):** Güncel fiyat verilerine daha fazla önem veren ağırlıklı hareketli ortalama.
- **Ortalama Gerçek Aralık (ATR):** Piyasa oynaklığının bir ölçüsü.
- **Bollinger Bantları (BB):** Bir orta bant (SMA) ve iki dış banttan oluşan bir volatilite göstergesidir.

Özel Bollinger Bantları, fiyat davranışını analiz etmek için farklı standart sapma çarpanlarıyla hesaplanır:

- Standart sapma 4.
- 0,5'lik standart sapma.

### Sinyal Üretimi
Sinyaller, EMA ve Bollinger Bantlarını içeren belirli koşullara göre üretilir:

- **EMA Sinyalleri:** Belirli sayıda önceki döneme ait kapanış fiyatlarının tümü ilgili EMA'ların üzerinde olduğunda oluşturulur.
- **Toplam Sinyal:** Ticaret kararları için kapsamlı bir sinyal sağlamak üzere EMA sinyallerini Bollinger Bantlarıyla ilgili ek koşullarla birleştirir.

### Görselleştirme
Veriler ve hesaplanan göstergeler Plotly kullanılarak görselleştirilir. Şamdan grafikleri, piyasa verilerinin ve sinyallerinin net bir görsel temsilini sağlamak için EMA ve Bollinger Bantları ile birlikte çizilir.

### Geriye dönük test
Ticaret stratejileri, performanslarını değerlendirmek için geçmiş verilerle geriye doğru test edilir. Stratejiler, geriye dönük test kitaplığındaki Strateji sınıfı kullanılarak tanımlanır ve Backtest sınıfı, arka testi yürütmek için kullanılır.

- **Zararı Durdurma Mekanizması:** ATR'ye veya kapanış fiyatının sabit bir yüzdesine dayalı olarak zararı durdurma seviyelerini belirleyerek riski yönetmek için uygulanır.
- **İşlem Gerçekleştirme:** İşlemlere giriş ve çıkış koşulları, oluşturulan sinyallere göre tanımlanır.

### Optimizasyon
Strateji parametreleri, getirileri en üst düzeye çıkaracak şekilde optimize edilmiştir. Optimizasyon süreci şunları içerir:

- Zararı durdurma yüzdesi ve ATR oranı için farklı değerlerin test edilmesi.
- En yüksek getiriyi sağlayan parametre setinin belirlenmesi.

Optimizasyon sürecinin sonuçları, verilen geçmiş veriler için en etkili strateji yapılandırmalarına ilişkin bilgiler sağlar.