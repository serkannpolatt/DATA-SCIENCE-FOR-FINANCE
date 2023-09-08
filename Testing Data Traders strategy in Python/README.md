## English
## Bitcoin Trading Strategy README

This README document explains the basic workings of the Bitcoin (BTC-USD) trading strategy. This strategy aims to generate buy and sell signals using technical analysis indicators. Please note that cryptocurrency trading is highly speculative and risky. It is important that you review this piece of code carefully before using it and seek professional advice as needed.

### Libraries Used

The following Python libraries were used to implement this strategy:

**yfinance:** Used to pull and analyze financial data.
**ta (Technical Analysis Library):** Used to calculate technical analysis indicators.
**numpy:** Used for mathematical operations.
**pandas:** Used for data analysis and manipulation.
**datetime:** Used for date and time operations.
**matplotlib:** Used for plotting and visualization.


### Functions

This piece of code performs the following operations:

1. It pulls Bitcoin price data using the yfinance library.
2. Technical analysis indicators Stochastic Oscillator (%K and %D), Relative Strength Index (RSI) and Moving Average Convergence Difference (MACD) are calculated.
3. Stochastic Oscillator based buy and sell triggers are calculated and added to the DataFrame.
4. Buy and sell signals based on certain conditions are generated and added to the DataFrame.
5. Purchase and sale dates are determined and data are analyzed.
6. Functions are used to calculate the profit of buying and selling transactions.
7. The chart is created and the buying/selling transactions are visualized.

*Please use this README as a reference to understand the strategy and use the code safely. However, extensive testing and risk management are required when creating real trading strategies.*

*Please be cautious about running code or using trading strategies in the real world. Cryptocurrency trading involves high risk and it is important to do a good research before investing and seek expert advice when necessary.*

## Türkçe
## Bitcoin Ticaret Stratejisi README

Bu README belgesi, Bitcoin (BTC-USD) ticaret stratejisinin temel işleyişini açıklar. Bu strateji, teknik analiz göstergelerini kullanarak alım ve satım sinyalleri oluşturmayı amaçlar. Lütfen unutmayın ki kripto para ticareti oldukça spekülatif ve risklidir. Bu kod parçasını kullanmadan önce dikkatli bir şekilde incelemeniz ve gerektiğinde profesyonel danışmanlık almanız önemlidir.

### Kullanılan Kütüphaneler

Bu stratejiyi uygulamak için aşağıdaki Python kütüphaneleri kullanılmıştır:

**yfinance:** Finansal verileri çekmek ve analiz etmek için kullanılır.
**ta (Technical Analysis Library):** Teknik analiz göstergeleri hesaplamak için kullanılır.
**numpy:** Matematiksel işlemler için kullanılır.
**pandas:** Veri analizi ve manipülasyonu için kullanılır.
**datetime:** Tarih ve saat işlemleri için kullanılır.
**matplotlib:** Grafik çizimi ve görselleştirme için kullanılır.


### İşlevler

Bu kod parçası aşağıdaki işlemleri gerçekleştirir:

1. Bitcoin fiyat verilerini yfinance kütüphanesi kullanarak çeker.
2. Teknik analiz göstergeleri olan Stokastik Osilatör (%K ve %D), Göreceli Güç Endeksi (RSI) ve Hareketli Ortalama Yakınsaklık Farkı (MACD) hesaplanır.
3. Stokastik Osilatör bazlı alım ve satım tetikleyiciler hesaplanır ve DataFrame'e eklenir.
4. Belirli koşullara dayalı alım ve satım sinyalleri oluşturulur ve DataFrame'e eklenir.
5. Alım ve satım tarihleri belirlenir ve veriler analiz edilir.
6. Alım ve satım işlemlerinin karını hesaplamak için işlevler kullanılır.
7. Grafik oluşturulur ve alım/satım işlemleri görselleştirilir.

*Lütfen bu README belgesini stratejiyi anlamak ve kodu güvenli bir şekilde kullanmak için referans olarak kullanın. Ancak, gerçek ticaret stratejileri oluştururken kapsamlı testler ve risk yönetimi gereklidir.*

*Lütfen kodun çalıştırılması veya ticaret stratejilerinin gerçek dünyada kullanılması konusunda dikkatli olun. Kripto para ticareti yüksek risk içerir ve yatırım yapmadan önce iyi bir araştırma yapmanız ve gerektiğinde uzmanlardan görüş almanız önemlidir.*