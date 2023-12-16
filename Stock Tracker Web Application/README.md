## English
## Stock Tracker Web Application

### Purpose and Usage

The Stock Tracker Web Application is designed for investors, traders, or anyone interested in monitoring and managing their stock portfolio. It provides an easy-to-use interface for viewing and filtering stocks based on various financial indicators. Users can quickly identify potential investment opportunities by filtering stocks that match specific criteria.

The application fetches key statistics for each stock using the yfinance library, ensuring that the data is up-to-date and accurate. Users can then save notes or add stocks to a watchlist for further analysis or reference.

The web application serves as a valuable tool for making informed investment decisions, tracking portfolio performance, and staying updated with stock market trends.

### Future Enhancements

The project can be expanded and improved in several ways:

- Add user authentication and user-specific dashboards for personalization.
- Implement real-time stock price updates using web sockets for live market data.
- Integrate with financial news APIs to display relevant news for each stock.
- Enhance the user interface with additional features, charts, and graphs.

Contributions from the open-source community are welcome to help enhance and evolve the application further.

### Overview

The Stock Tracker Web Application is a powerful tool for tracking and managing stock data. It allows users to view and filter a list of stocks based on various criteria such as forward P/E ratio, dividend yield, and moving averages. Users can also add new stocks to the database and fetch key statistics using the yfinance library.

### Features

**1. Stock List and Filtering**

The home page displays a list of all the stocks in the database. Users can apply filters to this list to view stocks that meet specific criteria. The available filters include:

-**forward_pe:** Filter by forward price-to-earnings (P/E) ratio.
- **dividend_yield:** Filter by dividend yield.
- **ma50:** Filter by the 50-day moving average.
- **ma200:** Filter by the 200-day moving average.

**2. Add Stocks and Fetch Key Statistics**

Users can add new stocks to the database by providing the stock symbol. When a new stock is added, the application initiates a background task to fetch key statistics using the yfinance library. These statistics include the 50-day and 200-day moving averages, stock price, forward P/E ratio, forward earnings per share (EPS), and dividend yield.

**3. Delete Stocks**

Each stock in the list has a "Delete" button that allows users to remove the stock from the database.

**4. Save Notes**

Next to each stock, users can find a button to add a note or save the stock for later reference. This feature is useful for users who want to keep track of additional information or insights about specific stocks.

### Technologies Used

- **FastAPI:** A modern, fast, web framework for building APIs with Python.
- **SQLAlchemy:** A powerful and flexible Object-Relational Mapping (ORM) library for working with databases in Python.
- **SQLite:**A lightweight, serverless, and self-contained SQL database engine used for data storage.
- **yfinance:** A popular Python library for fetching stock market data from Yahoo Finance.


## Türkçe
## Hisse Takibi Web Uygulaması

### Amaç ve Kullanım

Hisse Takibi Web Uygulaması, yatırımcılar, tüccarlar veya hisse senedi portföylerini izlemek ve yönetmekle ilgilenen herkes için tasarlanmıştır. Çeşitli finansal göstergelere göre hisse senetlerini görüntülemek ve filtrelemek için kullanımı kolay bir arayüz sağlar. Kullanıcılar, belirli kriterlere uyan hisse senetlerini filtreleyerek potansiyel yatırım fırsatlarını hızla belirleyebilir.

Uygulama, yfinance kitaplığını kullanarak her hisse senedi için önemli istatistikleri getirir ve verilerin güncel ve doğru olmasını sağlar. Kullanıcılar daha sonra daha fazla analiz veya referans için notları kaydedebilir veya bir izleme listesine hisse senedi ekleyebilir.

Web uygulaması, bilinçli yatırım kararları vermek, portföy performansını izlemek ve borsa trendlerinden haberdar olmak için değerli bir araç olarak hizmet eder.

### Gelecekteki Geliştirmeler

Proje birkaç şekilde genişletilebilir ve geliştirilebilir:

- Kişiselleştirme için kullanıcı kimlik doğrulaması ve kullanıcıya özel panolar ekleyin.
- Canlı piyasa verileri için web soketlerini kullanarak gerçek zamanlı hisse senedi fiyatı güncellemelerini uygulayın.
- Her hisse senedi için ilgili haberleri görüntülemek için finansal haber API'leri ile entegre edin.
- Kullanıcı arayüzünü ek özellikler, çizelgeler ve grafiklerle geliştirin.

Açık kaynak topluluğunun katkıları, uygulamayı daha da geliştirmeye ve geliştirmeye yardımcı olmaya açıktır.

### Genel Bakış

Stock Tracker Web Uygulaması, stok verilerini izlemek ve yönetmek için güçlü bir araçtır. Kullanıcıların, ileri P/E oranı, temettü getirisi ve hareketli ortalamalar gibi çeşitli kriterlere dayalı olarak bir hisse senedi listesini görüntülemesine ve filtrelemesine olanak tanır. Kullanıcılar ayrıca veritabanına yeni hisse senetleri ekleyebilir ve yfinance kitaplığını kullanarak önemli istatistikleri alabilir.

### Özellikler

**1. Stok Listesi ve Filtreleme**

Ana sayfa, veritabanındaki tüm stokların bir listesini görüntüler. Kullanıcılar, belirli kriterleri karşılayan stokları görüntülemek için bu listeye filtre uygulayabilir. Mevcut filtreler şunları içerir:

-**forward_pe:** Vadeli fiyat-kazanç (F/K) oranına göre filtreleyin.
- **temettü_verimi:** Temettü verimine göre filtreleyin.
- **ma50:** 50 günlük hareketli ortalamaya göre filtreleyin.
- **ma200:** 200 günlük hareketli ortalamaya göre filtreleyin.

**2. Hisse Senedi Ekleme ve Önemli İstatistikleri Getirme**

Kullanıcılar, hisse senedi sembolünü sağlayarak veritabanına yeni hisse senetleri ekleyebilirler. Yeni bir hisse senedi eklendiğinde uygulama, yfinance kitaplığını kullanarak önemli istatistikleri almak için bir arka plan görevi başlatır. Bu istatistikler, 50 günlük ve 200 günlük hareketli ortalamaları, hisse senedi fiyatını, vadeli F/K oranını, hisse başına vadeli kazançları (EPS) ve temettü verimini içerir.

**3. Stokları Sil**

Listedeki her hisse senedinin, kullanıcıların hisse senedini veri tabanından kaldırmasına olanak tanıyan bir "Sil" düğmesi vardır.

**4. Notları Kaydet**

Her hisse senedinin yanında, kullanıcılar not eklemek veya hisse senedini daha sonra başvurmak üzere kaydetmek için bir düğme bulabilir. Bu özellik, belirli hisse senetleri hakkında ek bilgileri veya içgörüleri takip etmek isteyen kullanıcılar için kullanışlıdır.

### Kullanılan Teknolojiler

- **FastAPI:** Python ile API'ler oluşturmak için modern, hızlı bir web çerçevesi.
- **SQLAlchemy:** Python'da veritabanlarıyla çalışmak için güçlü ve esnek bir Nesne-İlişkisel Eşleme (ORM) kitaplığı.
- **SQLite:** Veri depolama için kullanılan hafif, sunucusuz ve bağımsız bir SQL veritabanı motoru.
- **yfinance:** Yahoo Finance'ten borsa verilerini almak için kullanılan popüler bir Python kitaplığı.
