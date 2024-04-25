## English
## Trading Strategy with Pivot and Breakout Detection

### Overview
This repository contains Python code for implementing a trading strategy that leverages pivot points and breakout detection techniques. The strategy aims to identify potential entry and exit points in financial markets, particularly suitable for algorithmic trading.

### Key Components
- **Pivot Detection:** The code includes functions to detect pivot points within market data. These pivot points can indicate possible reversals or shifts in price direction.

- **Channel Formation:** Another feature of the code is the ability to form channels based on pivot points observed within a specified window. This assists in recognizing trend directions and potential breakout scenarios.

- **Breakout Detection:** The strategy integrates breakout detection logic to identify significant price movements beyond established channels. This is crucial for initiating trades in alignment with the breakout direction.

- **Strategy Implementation:** The core of the repository comprises the implementation of a trading strategy using pivot and breakout information. The strategy dynamically places buy and sell orders based on predefined conditions and risk management parameters.

- **Backtesting Capability:** The code facilitates backtesting of the trading strategy using historical market data. This allows for the evaluation of strategy performance across various market conditions and enables refinement for improved results.

### How to Use
**1. Installation:** Begin by installing the required Python dependencies listed in the requirements.txt file using pip.

**2. Data Preparation:** Provide historical market data in DataFrame format with columns such as Open, High, Low, Close, and Volume.

**3. Strategy Execution:** Execute the MyStrat class with desired parameters to run the trading strategy on the provided market data.

**4. Analysis:** Analyze the backtest results, including statistics such as returns, drawdowns, and Sharpe ratio, to evaluate the performance of the strategy.


## Türkçe 
## Pivot ve Koparma Tespiti ile Ticaret Stratejisi

### Genel Bakış
Bu depo, pivot noktalarından ve kırılma tespit tekniklerinden yararlanan bir ticaret stratejisinin uygulanmasına yönelik Python kodunu içerir. Strateji, finansal piyasalara özellikle algoritmik ticarete uygun potansiyel giriş ve çıkış noktalarını belirlemeyi amaçlıyor.

### Anahtar bileşenler
- **Pivot Tespiti:** Kod, piyasa verileri içindeki pivot noktalarını tespit etmeye yönelik işlevler içerir. Bu pivot noktaları, fiyat yönündeki olası geri dönüşleri veya değişimleri gösterebilir.

- **Kanal Oluşumu:** Kodun bir diğer özelliği de belirli bir pencerede gözlemlenen pivot noktalarına göre kanal oluşturabilmesidir. Bu, trend yönlerinin ve potansiyel kırılma senaryolarının tanınmasına yardımcı olur.

- **Açılış Tespiti:** Strateji, yerleşik kanalların ötesindeki önemli fiyat hareketlerini belirlemek için kırılma tespit mantığını entegre eder. Bu, kırılma yönüne uygun olarak işlemleri başlatmak için çok önemlidir.

- **Strateji Uygulaması:** Havuzun özü, pivot ve çıkış bilgileri kullanılarak bir ticaret stratejisinin uygulanmasından oluşur. Strateji, önceden tanımlanmış koşullara ve risk yönetimi parametrelerine dayalı olarak alım ve satım emirlerini dinamik olarak yerleştirir.

- **Geri Test Yeteneği:** Kod, geçmiş piyasa verilerini kullanarak ticaret stratejisinin geriye doğru test edilmesini kolaylaştırır. Bu, çeşitli piyasa koşullarında strateji performansının değerlendirilmesine olanak tanır ve daha iyi sonuçlar için iyileştirme yapılmasına olanak tanır.

### Nasıl kullanılır
**1. Kurulum:** Gereksinimler.txt dosyasında listelenen gerekli Python bağımlılıklarını pip kullanarak yükleyerek başlayın.

**2. Veri Hazırlama:** Açılış, Yüksek, Düşük, Kapanış ve Hacim gibi sütunlarla geçmiş piyasa verilerini DataFrame formatında sağlayın.

**3. Stratejinin Yürütülmesi:** Sağlanan piyasa verileri üzerinde ticaret stratejisini yürütmek için MyStrat sınıfını istenen parametrelerle yürütün.

**4. Analiz:** Stratejinin performansını değerlendirmek için getiriler, düşüşler ve Sharpe oranı gibi istatistikler dahil olmak üzere arka test sonuçlarını analiz edin.