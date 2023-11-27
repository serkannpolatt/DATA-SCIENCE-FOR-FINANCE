## Türkçe
## Portföy Optimizasyonu

Bu Python betiği, riski yönetirken getirileri en üst düzeye çıkaran bir yatırım portföyü oluşturmak için finansta yaygın olarak kullanılan bir teknik olan portföy optimizasyonu için tasarlanmıştır. Senaryo, S&P 500 endeksinin yanı sıra Google (GOOG), Apple (AAPL), Facebook (META), Amazon (AMZN) ve Microsoft (MSFT) dahil olmak üzere çeşitli hisse senetlerine odaklanıyor. Optimize edilmiş bir portföy oluşturmak için karar verme sürecine yardımcı olmak amacıyla finansal verileri, istatistiksel analizleri ve görselleştirme tekniklerini kullanır.

### Amaç

**1. Veri Alma**

Komut dosyası, Yahoo Finance'ten belirtilen varlıklara ilişkin geçmiş hisse senedi fiyatı verilerini almak için yfinance kitaplığını kullanır. Veriler geçmiş performansı analiz etmek ve bilinçli yatırım kararları vermek için çok önemlidir.

**2. Veri analizi**

Getirilen stok verileri, pandas kütüphanesi kullanılarak tek bir veri kümesinde birleştirilir. Komut dosyası daha sonra veri kümesinin yapısını analiz eder ve kutu grafikleri ve dağılım matrisleri aracılığıyla hisse senedi fiyatlarını görselleştirir. Portföy optimizasyonu için her varlığın geçmiş performansını anlamak önemlidir.

**3. Risk ve Getiri Analizi**

Komut dosyası, her hisse senedi için günlük getirileri, volatiliteyi ve Sharpe oranlarını hesaplar. Sharpe oranı, risk ve getiri arasındaki optimum dengeyi belirlemeye yardımcı olan önemli bir ölçümdür. Ek olarak, çeşitlendirilmiş bir portföy sağlamak için farklı hisse senetleri arasındaki korelasyonlar analiz edilir.

**4. Portföy Optimizasyonu**

Komut dosyası, matematiksel optimizasyon tekniklerini kullanarak Sharpe oranını maksimuma çıkaran varlık ağırlıklarının kombinasyonunu bulur. Optimize edilmiş portföy, modern portföy teorisine uygun olarak mümkün olan en yüksek riske göre ayarlanmış getiriyi elde etmeyi amaçlamaktadır.

**5. Verimli Sınır**

Etkin sınır, portföy optimizasyonunda çok önemli bir kavramdır. Senaryo, belirli bir risk seviyesi için en yüksek beklenen getiriyi veya belirli bir beklenen getiri seviyesi için en düşük riski sunan optimal portföy setini sergileyerek etkin sınırı çizer.

### Kullanım
**1. Bağımlılıkları Yükle:**

		pip install -r gereksinimleri.txt

**2. Komut Dosyasını Çalıştırın:**
- Betiği kopyalayıp bir Python ortamına veya Jupyter not defterine yapıştırın.
- Mali verileri almak, analiz gerçekleştirmek ve görselleştirmeler oluşturmak için komut dosyasını çalıştırın.

**3. Sonuçları Yorumla:**

- Seçilen varlıkların geçmiş performansını, riskini ve getirisini anlamak için oluşturulan görselleştirmeleri ve analizleri inceleyin.
- Risk-getiri değiş tokuşlarına dayalı olarak optimal portföyleri vurgulayan etkin sınır grafiğine dikkat edin.


### Bağımlılıklar
- **pandalar:** Veri işleme ve analiz kitaplığı.
- **yfinance:** Yahoo Finance'den geçmiş hisse senedi fiyatı verilerini alın.
- **yahoofinancials:** Yahoo Finance'den finansal verileri almak için ek kitaplık.
- **matplotlib:** Görselleştirmeler oluşturmaya yönelik çizim kitaplığı.
- **seaborn:** Matplotlib'e dayalı istatistiksel veri görselleştirmesi.
- **scipy:** Matematiksel ve istatistiksel işlemler için bilimsel kütüphane.

### Önemli Not
- Yahoo Finance'den finansal verileri almak için çalışan bir internet bağlantısı olduğundan emin olun.
- Finansal piyasalar dalgalanmalara tabidir ve geçmiş performans gelecekteki sonuçları öngörmeyebilir.
- Bu komut dosyasını eğitim ve bilgilendirme amaçlı kullanın; Yatırım kararları için finans uzmanlarına danışın.

## English
## Portfolio Optimization

This Python script is designed for portfolio optimization, a technique widely used in finance to construct an investment portfolio that maximizes returns while managing risk. The script focuses on a selection of stocks, including Google (GOOG), Apple (AAPL), Facebook (META), Amazon (AMZN), and Microsoft (MSFT), as well as the S&P 500 index. It utilizes financial data, statistical analysis, and visualization techniques to aid in the decision-making process for constructing an optimized portfolio.

### Purpose

**1. Data Retrieval**

The script uses the yfinance library to fetch historical stock price data for the specified assets from Yahoo Finance. The data is crucial for analyzing past performance and making informed investment decisions.

**2. Data Analysis**

The fetched stock data is combined into a single dataset using the pandas library. The script then analyzes the structure of the dataset and visualizes stock prices through box plots and scatter matrices. Understanding the historical performance of each asset is essential for portfolio optimization.

**3. Risk and Return Analysis**

The script calculates daily returns, volatility, and Sharpe ratios for each stock. The Sharpe ratio is a key metric that helps identify the optimal balance between risk and return. Additionally, correlations among different stocks are analyzed to ensure a diversified portfolio.

**4. Portfolio Optimization**

Using mathematical optimization techniques, the script finds the combination of asset weights that maximizes the Sharpe ratio. The optimized portfolio aims to achieve the highest possible risk-adjusted return, aligning with modern portfolio theory.

**5. Efficient Frontier**

The efficient frontier is a crucial concept in portfolio optimization. The script plots the efficient frontier, showcasing the set of optimal portfolios that offer the highest expected return for a given level of risk or the lowest risk for a specified level of expected return.

### Usage
**1. Install Dependencies:**

		pip install -r requirements.txt

**2. Run the Script:**
- Copy and paste the script into a Python environment or a Jupyter notebook.
- Run the script to retrieve financial data, perform analysis, and generate visualizations.

**3. Interpret Results:**

- Review the generated visualizations and analyses to understand the historical performance, risk, and return of the selected assets.
- Pay attention to the efficient frontier plot, which highlights the optimal portfolios based on risk-return trade-offs.


### Dependencies
- **pandas:** Data manipulation and analysis library.
- **yfinance:** Fetch historical stock price data from Yahoo Finance.
- **yahoofinancials:** Additional library for fetching financial data from Yahoo Finance.
- **matplotlib:** Plotting library for creating visualizations.
- **seaborn:** Statistical data visualization based on Matplotlib.
- **scipy:** Scientific library for mathematical and statistical operations.

### Important Note
- Ensure a working internet connection to fetch financial data from Yahoo Finance.
- Financial markets are subject to volatility, and past performance may not predict future results.
- Use this script for educational and informational purposes; consult financial professionals for investment decisions.