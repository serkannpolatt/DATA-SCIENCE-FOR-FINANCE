## English
## Stock Price Prediction
This project aims to predict stock prices from news headlines using natural language processing and machine learning techniques. The project is written in the Python programming language and involves processing the dataset, transforming text data into features, and training a classifier model.

### Dataset
The dataset used for the project is obtained from a CSV file that contains daily news headlines and stock prices. The dataset consists of columns such as 'Date', 'Label', and 'Top1' to 'Top25'. The 'Date' column represents the dates, the 'Label' column represents whether the stock price has increased or decreased (0 or 1), and the 'Top1' to 'Top25' columns contain the daily news headlines.

### Preprocessing
The following steps are applied to process the dataset:

- Removal of punctuation and special characters.
- Conversion of texts to lowercase.
- Removal of stop words (conjunctions, pronouns, etc.).
- Stemming of words to their roots.
- Feature Generation
- Text data is transformed into features using the Bag of Words model. A word distribution vector is created for each news headline using CountVectorizer. These vectors are used to convert the text data into numerical features.

### Classifier Model
The project utilizes a logistic regression classifier to predict stock prices. The classifier model is trained using the training data and used to make predictions on the test data.

### Performance Evaluation
The following evaluation metrics are used to assess the performance of the classifier model:

- **Accuracy:** Indicates how close the predictions are to the correct classes.
- **Precision:** Measures how well the positive predictions match the actual positives.
- **Recall:** Shows how many of the actual positives are correctly predicted.

### Usage
After downloading the project files, you can make stock price predictions by following these steps:

- Prepare the dataset named 'veri_kumesi.csv' in an appropriate format and place the file in the project's main directory.
- Install the required Python libraries (pandas, nltk, sklearn, wordcloud, matplotlib, seaborn, etc.).
- Open the Python file named 'proje.py' and review the code sections that load the dataset, perform preprocessing, generate features, and train the classifier model.
- Run the project file to make stock price predictions.
- Analyze the results and check the performance evaluation.

### Purpose
This project is developed to examine and predict the impact of news headlines on stock prices in financial markets. The goal is to forecast future stock price movements by utilizing the semantic information contained in the news headlines and provide guidance to investors.

Additionally, it involves combining natural language processing and machine learning techniques, including the conversion of news articles from textual data to numerical features and the training of a classifier model. This project aims to contribute to making text-based predictions in financial data analysis by applying these techniques.


## Türkçe
## Hisse Senedi Fiyatı Tahmini
Bu proje, doğal dil işleme ve makine öğrenimi yöntemlerini kullanarak haber başlıklarından hisse senedi fiyatı tahmini yapmayı amaçlamaktadır. Proje, veri kümesini işlemek, metin verilerini özelliklere dönüştürmek ve bir sınıflandırıcı modeli eğitmek için Python programlama dilinde yazılmıştır.

### **Veri Kümesi**
Proje için kullanılan veri kümesi, günlük haber başlıklarını ve hisse senedi fiyatlarını içeren bir CSV dosyasından elde edilmiştir. Veri kümesi, 'Date', 'Label' ve 'Top1' ila 'Top25' sütunlarından oluşmaktadır. 'Date' sütunu tarihleri, 'Label' sütunu hisse senedi fiyatının yükselme veya düşme durumunu (0 veya 1) temsil etmektedir. 'Top1' ila 'Top25' sütunları ise günlük haber başlıklarını içermektedir.

### **Ön İşleme**
Veri kümesini işlemek için aşağıdaki adımlar uygulanmıştır:

- Noktalama işaretleri ve özel karakterler kaldırılmıştır.
- Metinler küçük harfe dönüştürülmüştür.
- Stop kelimeleri (bağlaçlar, zamirler vb.) kaldırılmıştır.
- Köklerine dönüştürülmek için kelimeler stemlenmiştir.
- Özelliklerin Oluşturulması
- Metin verileri, metinden özelliklere dönüştürmek için Bag of Words modeli kullanılmıştır.
- CountVectorizer kullanılarak her bir haber başlığı için bir kelime dağılımı vektörü oluşturulmuştur. Bu vektörler, metin verilerini sayısal özelliklere dönüştürmek için kullanılmıştır.

### **Sınıflandırıcı Modeli**
Proje, lojistik regresyon sınıflandırıcısını kullanarak hisse senedi fiyatı tahmini yapmaktadır. Eğitim verileri kullanılarak sınıflandırıcı modeli eğitilmiş ve test verileri üzerinde tahminler yapılmıştır.

### Performans Değerlendirmesi
Sınıflandırıcı modelinin performansını değerlendirmek için aşağıdaki değerlendirme metrikleri kullanılmıştır:

- **Doğruluk (Accuracy):** Tahminlerin doğru sınıflara ne kadar yakın olduğunu gösterir.
- **Kesinlik (Precision):** Pozitif olarak tahmin edilenlerin gerçekten pozitif olduğunu ne kadar iyi gösterir.
- **Hassasiyet (Recall):** Gerçek pozitiflerin kaçının doğru şekilde tahmin edildiğini gösterir.

### Kullanım
Proje dosyalarını indirdikten sonra aşağıdaki adımları izleyerek hisse senedi fiyatı tahmini yapabilirsiniz:

- 'veri_kumesi.csv' adlı veri kümesini uygun bir şekilde hazırlayın ve dosyayı projenin ana dizinine yerleştirin.
- Gerekli Python kütüphanelerini yükleyin (pandas, nltk, sklearn, wordcloud, matplotlib, seaborn vb.)
- 'proje.py' adlı Python dosyasını açın ve veri kümesini yükleyen, ön işlemleri yapan, özellikleri oluşturan ve sınıflandırıcı modelini eğiten kod parçalarını gözden geçirin.
- Proje dosyasını çalıştırarak hisse senedi fiyatı tahmini yapabilirsiniz.
- Sonuçları analiz edin ve performans değerlendirmesini kontrol edin.

### Amaç
Bu proje, finansal piyasalarda haberlerin hisse senedi fiyatlarına etkisini incelemek ve tahmin etmek amacıyla geliştirilmiştir. Haber başlıklarının içerdikleri anlamsal bilgileri kullanarak, gelecekteki hisse senedi fiyat hareketlerini öngörmek ve yatırımcılara rehberlik etmek hedeflenmektedir.

Aynı zamanda, doğal dil işleme ve makine öğrenimi tekniklerini birleştirerek, haberlerin metin verilerinden sayısal özelliklere dönüştürülmesi ve sınıflandırıcı modelin eğitilmesi gibi önemli adımları içermektedir. Bu proje, bu teknikleri uygulayarak finansal veri analizinde metin tabanlı öngörülerin yapılabilmesine katkı sağlamayı hedeflemektedir.
