## English
## Simple Trading Strategy using LSMA Indicator

This project demonstrates the usage of Python to process financial data and implement a simple trading strategy. This strategy generates buy and sell signals by utilizing the Least Squares Moving Average (LSMA) indicator.

### Requirements

To run this project, you need to install the following Python libraries:

- yfinance
- pandas
- statsmodels
- matplotlib

### Code Explanation

1. Downloading Financial Data:
   - The `yfinance` library is used to download financial data based on the specified symbol (e.g., "AAPL" for Apple Inc.) and date range.

2. Regression Analysis:
   - Regression analysis is performed on a specific window of the data set.
   - The Least Squares Moving Average (LSMA) indicator is calculated.

3. Trading Strategy:
   - The LSMA indicator is employed to generate buy and sell signals.
   - The strategy executes buy or sell transactions based on specific conditions.

4. Results:
   - Profit/loss calculations and win rate are computed.
   - Results are visualized using charts.

### Usage

1. Before running the project, install the required libraries: `pip install yfinance pandas statsmodels matplotlib`

2. Run the `main.py` file to apply the trading strategy.

3. Examine the generated chart window to view the obtained results and visualizations.

### Notes

- This code example is for educational purposes only. Real trading operations require more analysis and risk management.

- Carefully review your data and trading strategy, and seek guidance from professional financial advisors if needed.

- Trading strategies should be tested based on historical performance and do not guarantee future results.

This project showcases the creation of a basic trading strategy and the analysis of financial data to understand its implementation.


## Türkçe
## Basit Ticaret Stratejisi Kullanımı

Bu proje, finansal verileri işlemek ve basit bir ticaret stratejisi uygulamak için Python kullanımını göstermektedir. Bu strateji, Least Squares Moving Average (LSMA) göstergesi ile ticaret sinyalleri oluşturarak alım ve satım işlemleri gerçekleştirir.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerini kurmanız gerekmektedir:

- yfinance
- pandas
- statsmodels
- matplotlib

### Kod Açıklaması

1. Finansal Verilerin İndirilmesi:
   - `yfinance` kütüphanesi kullanılarak belirtilen sembol (örneğin, "AAPL" - Apple Inc.) ve tarih aralığına göre finansal veriler indirilir.

2. Regresyon Analizi:
   - Veri setinin belirli bir penceresi üzerinde regresyon analizi gerçekleştirilir.
   - Least Squares Moving Average (LSMA) göstergesi hesaplanır.

3. Ticaret Stratejisi:
   - Alım ve satım sinyalleri üretmek için LSMA göstergesi kullanılır.
   - Strateji, belirli koşullar sağlandığında alım veya satım işlemi yapar.

4. Sonuçlar:
   - Elde edilen kar/zarar hesaplamaları ve kazanma oranı hesaplanır.
   - Grafiklerle sonuçlar görselleştirilir.

### Kullanım

1. Projeyi çalıştırmadan önce gerekli kütüphaneleri yükleyin: `pip install yfinance pandas statsmodels matplotlib`

2. `main.py` dosyasını çalıştırarak ticaret stratejisini uygulayabilirsiniz.

3. Elde edilen sonuçları ve grafikleri görmek için oluşturulan grafik penceresini inceleyin.

### Notlar

- Bu kod örneği sadece eğitim amaçlıdır. Gerçek ticaret işlemleri için daha fazla analiz ve risk yönetimi gerekmektedir.

- Verilerinizi ve ticaret stratejinizi dikkatlice inceleyin ve gerektiğinde profesyonel finansal danışmanlardan destek alın.

- Ticaret stratejileri geçmiş performanslarına dayalı olarak test edilmelidir ve gelecekteki sonuçları garanti etmez.

Bu proje, temel bir ticaret stratejisinin nasıl oluşturulacağını ve finansal verilerin nasıl analiz edileceğini anlamak için bir örnek sunmaktadır.
