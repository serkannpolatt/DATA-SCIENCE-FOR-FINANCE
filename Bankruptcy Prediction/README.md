## English
## Bankruptcy Prediction Model
This repository contains code for a bankruptcy prediction model using machine learning algorithms. The model aims to predict whether a company will go bankrupt based on various financial indicators.

### Dataset
The dataset used for training and evaluation is stored in the file Bankruptcy_data_Final (2).xlsx. It consists of financial features such as EPS, liquidity, profitability, productivity, leverage ratio, asset turnover, operational margin, return on equity, market book ratio, assets growth, sales growth, employee growth, and the target variable "BK" indicating bankruptcy (1 for bankrupt, 0 for non-bankrupt).

### Code Files
The code is written in Python and divided into sections.

**1. Data Preprocessing and Exploration**
In this section, the dataset is loaded, explored, and preprocessed. Missing values are imputed using the K-Nearest Neighbors (KNN) imputer. Outliers are winsorized, and the dataset is split into independent variables and the target variable.

**2. Imbalanced Data Handling**
To handle the imbalanced dataset, under-sampling and over-sampling techniques are applied. Edited Nearest Neighbours (ENN) and Tomek Links are used for under-sampling, while SMOTE, BorderlineSMOTE, and SVMSMOTE are used for over-sampling. The combination methods SMOTEENN and SMOTETomek are also used.

**3. Feature Scaling**
Three different feature scaling methods are employed: Min-Max scaling, Standard scaling, and Robust scaling. These techniques ensure that all features are on a similar scale, which can improve the performance of certain machine learning algorithms.

**4. Model Training and Evaluation**
Four different classifiers are used for model training: Random Forest, Logistic Regression, Support Vector Machines (SVM), and Naive Bayes. A Voting Classifier is also implemented to combine the predictions of these models. The models are evaluated using various performance metrics such as accuracy, precision, recall, F1 score, and AUC.

**5. Results and Model Selection**
The performance metrics of each model are compared, and the results are presented in a tabular format. The confusion matrix and a heatmap visualization are also provided for better understanding of the model's performance.


### Usage
- Clone this repository to your local machine.
- Install the required dependencies.
- Place the dataset file (Bankruptcy_data_Final (2).xlsx) in the same directory as the code files.
- Run the code in your preferred Python environment (e.g., Jupyter Notebook, Spyder, or any Python IDE).

### Conclusion
The bankruptcy prediction model presented in this repository utilizes machine learning algorithms to predict whether a company will go bankrupt. By preprocessing the data, handling imbalanced classes, applying feature scaling, and training multiple classifiers, the model aims to achieve accurate predictions. The results and performance metrics can be used to assess the effectiveness of the model and make informed decisions regarding bankruptcy risk.

> *Please note that the accuracy of the model may vary depending on the dataset and the specific problem domain. Further adjustments and fine-tuning may be required to achieve optimal results in different scenarios.*

## Türkçe
## İflas Tahmin Modeli
Bu depo, çeşitli finansal göstergeler temelinde bir şirketin iflas edip etmeyeceğini tahmin etmek için makine öğrenimi algoritmaları kullanan bir iflas tahmin modeli için kod içermektedir.

### **Veri Kümesi**
Eğitim ve değerlendirme için kullanılan veri kümesi, "Bankruptcy_data_Final (2).xlsx" adlı dosyada saklanmaktadır. EPS, likidite, karlılık, verimlilik, kaldıraç oranı, varlık devri, işletme marjı, öz kaynak getirisi, piyasa değeri/defter değeri oranı, varlık büyümesi, satış büyümesi, çalışan sayısı büyümesi gibi finansal özellikler ve iflası gösteren "BK" hedef değişkeni (1 iflas eden, 0 iflas etmeyen) içermektedir.

### Kod Dosyaları
Kod Python dilinde yazılmış olup bölümlere ayrılmıştır.

**1. Veri Ön İşleme ve Keşfi**
Bu bölümde veri kümesi yüklenir, incelenir ve önişleme işlemlerine tabi tutulur. Eksik değerler K-En Yakın Komşu (KNN) doldurucusu kullanılarak tamamlanır. Aykırı değerler düzeltilir ve veri kümesi bağımsız değişkenlere ve hedef değişkene ayrılır.

**2. Dengesiz Veri İşleme**
Dengesiz veri kümesiyle başa çıkmak için azaltma ve artırma teknikleri uygulanır. Azaltma için Düzenlenmiş En Yakın Komşular (ENN) ve Tomek Bağlantıları kullanılırken, artırma için SMOTE, BorderlineSMOTE ve SVMSMOTE kullanılır. SMOTEENN ve SMOTETomek gibi kombinasyon yöntemleri de kullanılır.

**3. Özellik Ölçeklendirme**
Üç farklı özellik ölçeklendirme yöntemi kullanılır: Min-Max ölçeklendirme, Standart ölçeklendirme ve Robust ölçeklendirme. Bu teknikler, tüm özelliklerin benzer bir ölçekte olmasını sağlayarak belirli makine öğrenimi algoritmalarının performansını artırabilir.

**4. Model Eğitimi ve Değerlendirmesi**
Model eğitimi için dört farklı sınıflandırıcı kullanılır: Rastgele Orman (Random Forest), Lojistik Regresyon (Logistic Regression), Destek Vektör Makineleri (SVM) ve Naive Bayes. Bu modellerin tahminlerini birleştirmek için Oylama Sınıflandırıcısı (Voting Classifier) uygulanır. Modeller, doğruluk, hassasiyet, geri çağırma, F1 skoru ve AUC gibi çeşitli performans metrikleri kullanılarak değerlendirilir.

**5. Sonuçlar ve Model Seçimi**
Her bir modelin performans metrikleri karşılaştırılır ve sonuçlar tablo formatında sunulur. Modelin performansını daha iyi anlamak için karmaşıklık matrisi ve ısı haritası görselleştirmesi de sağlanır.

### Kullanım
- Bu depoyu yerel makinenize klonlayın.
- Gerekli bağımlılıkları kurun.
- Veri kümesi dosyasını (Bankruptcy_data_Final (2).xlsx) kod dosyalarıyla aynı dizine yerleştirin.
- Kodu tercih ettiğiniz Python ortamında (örneğin Jupyter Notebook, Spyder veya herhangi bir Python IDE) çalıştırın.

### Sonuç
Bu depoda sunulan iflas tahmin modeli, makine öğrenimi algoritmalarını kullanarak bir şirketin iflas edip etmeyeceğini tahmin etmek için tasarlanmıştır. Veriyi önişleme, dengesiz sınıfların ele alınması, özellik ölçeklendirme ve birden fazla sınıflandırıcı eğitimiyle modelin doğru tahminler yapması hedeflenmektedir. Sonuçlar ve performans metrikleri, modelin etkinliğini değerlendirmek ve iflas riskine ilişkin bilinçli kararlar vermek için kullanılabilir.

> *Lütfen modelin doğruluğu, veri kümesi ve belirli problem alanına bağlı olarak değişebileceğini unutmayın. Farklı senaryolarda optimal sonuçlar elde etmek için daha fazla ayarlama ve ince ayar yapılması gerekebilir.*
