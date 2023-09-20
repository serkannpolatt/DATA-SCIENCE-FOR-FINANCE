## English
## Portfolio Optimization

This README file describes Python's script for portfolio expansion and analysis using financial data. Using the Yahoo Finance API, the script retrieves posted stock prices, calculates portfolio statistics, and optimizes the portfolio for maximum Sharpe ratio.

### Purpose

The main purpose of this solution is the following goal:

1. **Stock Selection:** Provides users with portfolios containing specific assets and weight assignments of these assets.

2. **Return and Risk Calculation:** It calculates portable statistics such as expected return, volatility and variance by using the historical prices of the sentiment involved in the project.

3. **Portfolio Optimization:** Optimizes the portfolio for maximum Sharpe using the PyPortfolioOpt library. This helps users find the optimal asset allocation based on their risk and return preferences.


### Entrance

This Python script is designed for portfolio structure and analysis. It performs the following operations:

1. Retrieves dated stock prices for the specified list of assets.
2. Portfolio statistics, returns, volatility and variance calculations.
3. It uses the PyPortfolioOpt library when optimizing the portfolio for maximum Sharpe ratio.

### Requirements

- Python 3.x
- Pandas
- Soap opera
- Matplotlib
- yfinance (Yahoo Finance API)
- PyPortfolioOpt (for portfolio configuration)

You can install the necessary operations with the following command:

    pip install pandas numpy matplotlib yfinance pyportfolioopt

### Use
1. Clone this repository or download the script.

2. Open the Python script in your preferred code editor.

3. Edit the assets list to include the ticker symbols of the assets in your portfolio.

4. Adjust the weights array to assign weights to each asset in your portfolio.

5. Set the variables stockStartDate and today to determine dated data.

6. Run the script.

### Code Description

- The script retrieves dated stock prices using the Yahoo Finance API.

- Calculates portfolio statistics including return, volatility and variance.

- Portfolio is optimized for maximum Sharpe ratio using PyPortfolioOpt.

### Results

This project provides investors with:

- A tool they can use to optimize their portfolio.
- Information about expected returns and risk levels.
- Data and forecasts to help them better manage their portfolio.

By using the project, investors can make their financial decisions more consciously.



## Türkçe
## Portföy Optimizasyonu 

Bu README dosyası, finansal verileri kullanarak portföy optimizasyonu ve analizi için Python betiğini anlatmaktadır. Betik, Yahoo Finance API'sini kullanarak tarihli hisse senedi fiyatlarını alır, portföy istatistiklerini hesaplar ve portföyü maksimum Sharpe oranı için optimize eder.

### Amacı

Bu projenin temel amacı aşağıdaki hedefleri gerçekleştirmektir:

1. **Hisse Senedi Seçimi:** Kullanıcıların belirli hisse senetlerini portföylerine dahil etmelerini ve bu varlıklara ağırlıklar atamalarını sağlar.

2. **Getiri ve Risk Hesaplama:** Projede yer alan hisse senetlerinin geçmiş fiyat verilerini kullanarak beklenen getiri, oynaklık ve varyans gibi portföy istatistiklerini hesaplar.

3. **Portföy Optimizasyonu:** PyPortfolioOpt kütüphanesini kullanarak portföyü maksimum Sharpe oranına göre optimize eder. Bu, kullanıcıların risk ve getiri tercihlerine göre en uygun varlık tahsisini bulmalarına yardımcı olur.



### Giriş

Bu Python betiği, portföy optimizasyonu ve analizi için tasarlanmıştır. Aşağıdaki görevleri yerine getirir:

1. Belirtilen varlık listesi için tarihli hisse senedi fiyatlarını alır.
2. Portföy istatistiklerini, getiri, oynaklık ve varyansı hesaplar.
3. Portföyü maksimum Sharpe oranı için optimize ederken PyPortfolioOpt kütüphanesini kullanır.

### Gereksinimler

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- yfinance (Yahoo Finance API)
- PyPortfolioOpt (portföy optimizasyonu için)

Gereken kütüphaneleri aşağıdaki komutla kurabilirsiniz:

	pip install pandas numpy matplotlib yfinance pyportfolioopt

### Kullanım
1. Bu depoyu klonlayın veya betiği indirin.

2. Tercih ettiğiniz kod düzenleyicide Python betiğini açın.

3. assets listesini portföyünüzdeki varlıkların hisse sembollerini içerecek şekilde düzenleyin.

4. Her varlığa portföyünüzdeki her varlığa ağırlık atamak için weights dizisini ayarlayın.

5. Tarihli verilerin belirlemek için stockStartDate ve today değişkenlerini ayarlayın.

6. Betiği çalıştırın.

### Kod Açıklaması

- Betik, Yahoo Finance API'sini kullanarak tarihli hisse senedi fiyatlarını alır.

- Getiri, oynaklık ve varyans dahil olmak üzere portföy istatistiklerini hesaplar.

- Portföy, PyPortfolioOpt kullanarak maksimum Sharpe oranı için optimize edilir.

### Sonuçlar

Bu proje, yatırımcılara şunları sağlar:

- Portföylerini optimize etmek için kullanabilecekleri bir araç.
- Beklenen getiri ve risk seviyeleri hakkında bilgi.
- Portföylerini daha iyi yönetmelerine yardımcı olacak veriler ve tahminler.

Projeyi kullanarak yatırımcılar, finansal kararlarını daha bilinçli bir şekilde alabilirler.

