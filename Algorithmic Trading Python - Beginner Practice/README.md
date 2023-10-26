## English
## SMA Backtester

### Aim
This Python code contains the SMABucktester class, a Python class used to test the performance of a moving average (SMA)-based trading strategy using financial data. This README file provides information on how to use the code, its purpose and basic functioning.

### Use
This class of code shows how to test financial asset performance with SMA based trading strategy. Here are the usage steps:

1. **Installing Requirements:** Install the libraries required for the code to run.
pip install yfinance pandas numpy matplotlib

2. **Download Code:** Copy the code into this project's directory or include it in your own project.

3. **Copying the Code:** Copy the code to your own project directory or a directory of your choice.

4. Example Usage:

backtester = SMABucktester(symbol='AAPL', SMA_S=50, SMA_L=200, start='2020-01-01', end='2021-01-01')
backtester.test_results()
backtester.plot_results()

- **symbol:** The financial asset code to be tracked (for example, 'AAPL' for Apple stock).
- **SMA_S and SMA_L:** Short and long term moving average periods.
- **start and end:** Data extraction interval.

### Purpose
The purpose of this code is to test the performance of an SMA-based trading strategy on a specific financial asset. SMA is a type of indicator widely used in technical analysis, and this code allows measuring the success of a moving average strategy on an asset.

### How does it work?
This code pulls financial data using the yfinance library and then calculates moving averages on that data. It calculates the performance of the SMA strategy and compares this performance with the performance of the buy-and-hold strategy.

### Results
The test_results method measures the performance of the strategy and returns the results. The plot_results method visualizes the results in a graph.



## Türkçe
## SMA Denetleyici 
### Amaç
Bu Python kodu, finansal verileri kullanarak hareketli ortalama (SMA) tabanlı bir ticaret stratejisinin performansını test etmek için kullanılan bir Python sınıfı olan SMABacktester sınıfını içerir. Bu README dosyası, kodun nasıl kullanılacağı, amacı ve temel işleyişi hakkında bilgi sağlar.

### Kullanım
Kodun bu sınıfı, finansal varlık performansının SMA tabanlı ticaret stratejisi ile nasıl test edileceğini gösterir. İşte kullanım adımları:

1. **Gereksinimlerin Kurulumu:** Kodun çalışması için gerekli olan kütüphaneleri yükleyin.
		pip install yfinance pandas numpy matplotlib

2. **Kodu İndirleyin:** Kodu bu projenin dizinine kopyalayın veya kendi projenize dahil edin.

3. **Kodu Kopyalama:** Kodu kendi proje dizininize veya belirlediğiniz bir dizine kopyalayın.

4. Örnek Kullanım:

		backtester = SMABacktester(symbol='AAPL', SMA_S=50, SMA_L=200, start='2020-01-01', end='2021-01-01')
		backtester.test_results()
		backtester.plot_results()

- **symbol:** İzlenmek istenen finansal varlık kodu (örneğin, 'AAPL' Apple hisse senedi için).
- **SMA_S ve SMA_L:** Kısa ve uzun dönemli hareketli ortalama periyotları.
- **start ve end:** Veri çekme aralığı.

### Amacı
Bu kodun amacı, belirli bir finansal varlık üzerinde SMA tabanlı bir ticaret stratejisinin performansını test etmektir. SMA, teknik analizde yaygın olarak kullanılan bir gösterge türüdür ve bu kod, bir varlık üzerindeki hareketli ortalama stratejisinin başarısını ölçmeye olanak tanır.

### Nasıl Çalışır?
Bu kod, yfinance kütüphanesini kullanarak finansal verileri çeker ve ardından bu veriler üzerinde hareketli ortalamaları hesaplar. SMA stratejisinin performansını hesaplar ve bu performansı buy-and-hold stratejisinin performansı ile karşılaştırır.

### Sonuçlar
test_results metodu, stratejinin performansını ölçer ve sonuçları döndürür. plot_results metodu, sonuçları bir grafikte görselleştirir.