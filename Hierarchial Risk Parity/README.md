## English
## Mean-Variance Portfolio Optimization
This project demonstrates the process of mean-variance portfolio optimization using hierarchical clustering techniques. The goal is to construct optimal portfolios based on historical stock returns.

### Project Description
The main objective of this project is to showcase the implementation of mean-variance portfolio optimization using hierarchical clustering. The steps involved in the project include:

**1. Data Loading:** The project starts by loading the required packages and reading the stock data from the 'SP500Data.csv' file.

**2. Data Cleaning:** The dataset is checked for any missing values and dropped if necessary. Missing values are filled using the last available value in the dataset.

**3. Data Preprocessing:** The dataset is preprocessed to create the necessary input variables for portfolio optimization.

**4. Hierarchical Clustering:** The correlation matrix is calculated using the returns data, and hierarchical clustering is performed to determine the quasi-diagonal order of the stocks.

**5. Portfolio Construction:** Two portfolio construction methods, namely Minimum Variance Portfolio (MVP) and Hierarchical Risk Parity (HRP), are implemented to construct optimal portfolios.

**6. Portfolio Performance:** The performance of the constructed portfolios is evaluated using in-sample and out-of-sample data. Metrics such as standard deviation and Sharpe ratio are calculated.

> *Please note that the code snippets provided in this README are for reference purposes only and may need to be adapted to your specific project requirements.*


## Türkçe
## Ortalama Varyans Portföy Optimizasyon
Bu proje, hiyerarşik kümeleme tekniklerini kullanarak ortalama varyans portföy optimizasyonunun sürecini göstermektedir. Amaç, geçmiş hisse senedi getirilerine dayalı olarak optimal portföyler oluşturmaktır.

### **Proje Açıklaması**
Bu proje, hiyerarşik kümeleme kullanarak ortalama varyans portföy optimizasyonunun uygulanışını sergilemeyi amaçlamaktadır. Projede şu adımlar yer almaktadır:

**1. Veri Yükleme:** Proje, gerekli paketleri yükleyerek ve 'SP500Data.csv' dosyasından hisse senedi verilerini okuyarak başlar.

**2. Veri Temizleme:** Veri seti eksik değerler için kontrol edilir ve gerekirse düşürülür. Eksik değerler, veri setindeki en son mevcut değerle doldurulur.

**3. Veri Ön İşleme:** Portföy optimizasyonu için gerekli girdi değişkenlerini oluşturmak için veri seti ön işlemden geçirilir.

**4. Hiyerarşik Kümeleme:** Getiri verileri kullanılarak korelasyon matrisi hesaplanır ve hisse senetlerinin kısmi diyagonal sırasını belirlemek için hiyerarşik kümeleme gerçekleştirilir.

**5. Portföy Oluşturma:** Minimum Varyans Portföyü (MVP) ve Hiyerarşik Risk Paritesi (HRP) olmak üzere iki portföy oluşturma yöntemi uygulanarak optimal portföyler oluşturulur.

**6. Portföy Performansı:** Oluşturulan portföylerin performansı içerik örneği ve örnekleme dışı veriler kullanılarak değerlendirilir. Standart sapma ve Sharpe oranı gibi ölçütler hesaplanır.

Lütfen bu README'de sağlanan kod örneklerinin yalnızca referans amaçlı olduğunu ve belirli proje gereksinimlerinize göre uyarlanması gerekebileceğini unutmayın.
