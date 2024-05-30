## English
## OANDA Trading Bot
### Introduction
This trading bot automates trading on the OANDA platform using historical price data and technical indicators. It is implemented in Python and uses several libraries for data processing, technical analysis, and task scheduling.

### Purpose
The bot aims to automate the trading process by executing trades based on predefined strategies, reducing the need for manual intervention.

### Key Features
- **Automated Trading:** Executes trades based on technical signals.
- **Technical Analysis:** Uses EMA, Bollinger Bands, and ATR to generate signals.
- **Backtesting:** Periodically optimizes strategy parameters.
- **Scheduling:** Runs trading tasks at regular intervals.
- **Risk Management:** Includes stop loss and take profit levels.

### How It Works
**1. Data Collection:** Retrieves historical price data for EUR/USD.
**2. Signal Generation:** Calculates technical indicators and generates buy/sell signals.
**3. Trade Execution:** Places market orders based on signals and current market conditions.
**4. Backtesting and Optimization:** Periodically optimizes strategy parameters using historical data.
**5. Scheduling:** Uses APScheduler to run trading tasks during active trading hours.

### OANDA Account
Obtain your API credentials (access token and account ID) from the OANDA dashboard and configure them in the script.

### Usage
1. **Set Up API Credentials:** Replace placeholders with your OANDA access token and account ID.
2. **Run the Script:** Start the bot.
3. **Monitor Logs:** Check trading_data_file.txt and fitting_data_file.txt for details.

### Risk Management
Trading involves significant risk. The bot uses stop loss and take profit levels, but users should configure the lotsize variable according to their risk tolerance.

### Disclaimer
Trading forex on margin is risky. Consider your investment objectives, experience, and risk tolerance. Only invest money you can afford to lose.

## Türkçe
## OANDA Ticaret Botu
### Giriiş
Bu alım satım botu, geçmiş fiyat verilerini ve teknik göstergeleri kullanarak OANDA platformunda alım satımı otomatikleştirir. Python'da uygulanır ve veri işleme, teknik analiz ve görev planlama için çeşitli kütüphaneler kullanır.

### Amaç
Bot, önceden tanımlanmış stratejilere dayalı olarak alım satımlar gerçekleştirerek, manuel müdahale ihtiyacını azaltarak alım satım sürecini otomatikleştirmeyi amaçlıyor.

### Ana Özellikler
- **Otomatik İşlem:** İşlemleri teknik sinyallere göre gerçekleştirir.
- **Teknik Analiz:** Sinyal oluşturmak için EMA, Bollinger Bantları ve ATR'yi kullanır.
- **Geri Test:** Strateji parametrelerini periyodik olarak optimize eder.
- **Zamanlama:** Ticaret görevlerini düzenli aralıklarla çalıştırır.
- **Risk Yönetimi:** Zarar durdurma ve kar alma seviyelerini içerir.

### Nasıl çalışır
**1. Veri Toplama:** EUR/USD için geçmiş fiyat verilerini alır.
**2. Sinyal Üretimi:** Teknik göstergeleri hesaplar ve alım/satım sinyalleri üretir.
**3. İşlem Gerçekleştirme:** Sinyallere ve mevcut piyasa koşullarına göre piyasa emirleri verir.
**4. Geriye Dönük Test ve Optimizasyon:** Geçmiş verileri kullanarak strateji parametrelerini periyodik olarak optimize eder.
**5. Planlama:** Aktif işlem saatleri sırasında alım satım görevlerini yürütmek için APScheduler'ı kullanır.

### OANDA Hesabı
OANDA kontrol panelinden API kimlik bilgilerinizi (erişim belirteci ve hesap kimliği) alın ve bunları komut dosyasında yapılandırın.

### Kullanım
1. **API Kimlik Bilgilerini Ayarlayın:** Yer tutucuları OANDA erişim belirteciniz ve hesap kimliğiniz ile değiştirin.
2. **Komut Dosyasını Çalıştırın:** Botu başlatın.
3. **Günlükleri İzleyin:** Ayrıntılar için trading_data_file.txt ve fiting_data_file.txt dosyalarını kontrol edin.

### Risk yönetimi
Ticaret önemli riskler içerir. Bot zararı durdurma ve kar alma seviyelerini kullanır, ancak kullanıcılar lot büyüklüğü değişkenini risk toleranslarına göre yapılandırmalıdır.

### Sorumluluk reddi beyanı
Marjin üzerinden forex ticareti yapmak risklidir. Yatırım hedeflerinizi, deneyiminizi ve risk toleransınızı göz önünde bulundurun. Yalnızca kaybetmeyi göze alabileceğiniz parayla yatırım yapın.