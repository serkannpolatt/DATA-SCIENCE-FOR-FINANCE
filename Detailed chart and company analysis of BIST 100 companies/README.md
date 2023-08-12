## English
## Stock Price LSTM Prediction Code
This code can be used to predict stock prices using the LSTM (Long Short-Term Memory) model. The code has a general structure and can be applied to different stocks.

### **Description**
The code uses some commonly used libraries for investment data analysis, especially Pandas, NumPy, Matplotlib, and Keras libraries. The LSTM model is used to predict stock prices using historical data.

### **Steps in the Code**
- **Reading Stock Data:** The price data of the relevant stock is read from a source that provides investment data.
- **Data Preprocessing:** The read price data is converted to the appropriate format and scaled if necessary.
- **Creating Training and Test Data Sets:** The data set is split into training and test data sets. The training data set is used for the model to learn, while the test data set is used to evaluate the model's performance.
- **Creating the Model:** The LSTM model is created using the Keras library. The model learns by applying it to the training data set.
- **Training the Model:** The created model is trained on the training data set for a certain number of epochs.
- ** Making Predictions:** The model makes predictions on the test data set.
- **Evaluating the Results:** The model's performance is evaluated by comparing the actual and predicted price values.
- **Visualizing the Results:** The actual and predicted price values are visualized as a graph.

### **How to Use**
- Read the data from a source that provides the relevant stock data.
- Perform data preprocessing steps, including converting the data set to the appropriate format and scaling.
- Create training and test data sets. Typically, a large portion of the data set is used for training, while the remaining part is used for testing.
- Create an LSTM model and adjust the model's hyperparameters if necessary.
- Train the model by applying it to the training data set for a certain number of epochs.
- Evaluate the model on the test data set and make predictions.
- Evaluate the model's performance by comparing the obtained predictions with the actual values.
- Visualize the results by creating a graph comparing the actual and predicted price values.

> *Note: Make sure to install the necessary libraries and provide the data in the correct format before using the code.*

## Türkçe
## Hisse Senedi Fiyatı LSTM Tahmini Kodu
Bu kod, hisse senedi fiyatlarını LSTM (Uzun Kısa Vadeli Bellek) modeli kullanarak tahmin etmek için kullanılabilir. Kod, genel bir yapıya sahip olup farklı hisse senetleri için uygulanabilir.

### **Açıklama**
Kod, yatırım veri analitiği için yaygın olarak kullanılan bazı kütüphaneleri kullanır, özellikle Pandas, NumPy, Matplotlib ve Keras kütüphaneleri. LSTM modeli, geçmiş verileri kullanarak hisse senedi fiyatlarını tahmin etmek için kullanılır.

### **Kodun İçerdiği Adımla**r
- **Hisse Senedi Verilerinin Okunması:** İlgili hisse senedinin fiyat verileri, yatırım verilerini sağlayan bir kaynaktan okunur.
- **Veri Ön İşleme:** Okunan fiyat verileri uygun formata dönüştürülür ve gerektiğinde ölçeklendirme işlemi uygulanır.
- **Eğitim ve Test Veri Setlerinin Oluşturulması:** Veri seti, eğitim ve test veri setlerine ayrılır. Eğitim veri seti, modelin öğrenmesi için kullanılırken test veri seti, modelin performansını değerlendirmek için kullanılır.
- **Modelin Oluşturulması:** LSTM modeli, Keras kütüphanesi kullanılarak oluşturulur. Model, eğitim veri setine uygulanarak öğrenme işlemi gerçekleştirir.
- **Modelin Eğitilmesi:** Oluşturulan model, eğitim veri seti üzerinde belirli bir sayıda epoch (dönem) için eğitilir.
- **Tahminlerin Yapılması:** Model, test veri seti üzerinde tahminlerde bulunur.
- **Sonuçların Değerlendirilmesi:** Gerçek ve tahmin edilen fiyat değerleri karşılaştırılarak modelin performansı değerlendirilir.
- **Sonuçların Görselleştirilmesi:** Gerçek ve tahmin edilen fiyat değerleri, grafik olarak görselleştirilir.

### **Nasıl Kullanılır**
- İlgili hisse senedi verilerini sağlayan bir kaynaktan verileri okuyun.
- Veri ön işleme adımlarını gerçekleştirin, veri setini uygun formata dönüştürme ve ölçeklendirme işlemini uygulayın.
- Eğitim ve test veri setlerini oluşturun. Genellikle veri setinin büyük bir bölümü eğitim için kullanılırken geri kalan kısım test için kullanılır.
- LSTM modelini oluşturun ve gerektiğinde modelin hiperparametrelerini ayarlayın.
- Modeli eğitin, eğitim veri seti üzerinde belirli bir sayıda epoch için modeli eğitin.
- Modeli test veri seti üzerinde değerlendirin ve tahminler yapın.
- Elde edilen tahminleri gerçek değerlerle karşılaştırarak modelin performansını değerlendirin.
- Sonuçları grafik olarak görselleştirin, gerçek ve tahmin edilen fiyat değerlerini karşılaştıran bir grafik oluşturun.

> *Not: Kodu kullanmadan önce gerekli kütüphaneleri yüklediğinizden ve verileri doğru formatta sağladığınızdan emin olun.*
