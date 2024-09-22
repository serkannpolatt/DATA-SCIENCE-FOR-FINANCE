## English
## Customer Churn Prediction Project in Banking

### Project Overview
This project is developed to predict customer churn in the banking sector. Customer churn can lead to revenue loss and weaken a bank's competitive position. Therefore, churn prediction models are employed to better understand customer behavior and minimize the risk of attrition.

### Project Objective
The goal of this project is to utilize existing customer data to identify which customers are at high risk of leaving the bank. Based on these predictions, banks can make strategic decisions and develop various marketing and loyalty campaigns to reduce churn risk.

### Applications
This project can provide benefits across multiple business processes:

**1. Customer Segmentation**  
Identifying customers at risk of churn allows for tailored services or campaigns to be offered to these groups.

**2. Risk Management**  
Banks can devise proactive intervention strategies for customers identified as high-risk for churn.

**3. Marketing and Loyalty Management**  
Targeted marketing campaigns and customer loyalty programs can be created to enhance customer satisfaction and retention rates.

**4. Revenue Forecasting**  
Reducing churn rates helps prevent revenue loss and improves the financial performance of the company.

### MLOps Model Deployment

This MLOps project encompasses an end-to-end pipeline for a machine learning model using GitHub Actions.

## Customer Churn Prediction Model

This repository contains the code for training a machine learning model to predict customer churn using a dataset from banking customers. The objective is to identify customers who are likely to churn, enabling targeted retention strategies.

The `train.py` script carries out the following tasks:

1. **Data Preparation**: Loads the dataset, addresses missing values, and encodes categorical features.
2. **Feature and Target Variable Extraction**: Separates features from the target variable.
3. **Data Splitting**: Divides the dataset into training and testing sets.
4. **Model Selection and Hyperparameter Tuning**: Assesses multiple classifiers with different hyperparameters using grid search to optimize for recall.  
   - Recall is chosen as the primary evaluation metric since it is crucial for detecting all relevant churn instances, especially in imbalanced datasets. By optimizing recall, we ensure that as many at-risk customers as possible are identified, which aids effective customer retention and minimizes the impact of churn on the business.
5. **Model Training**: Trains the best-performing model based on recall.
6. **Evaluation**: Evaluates model performance using various metrics and saves the evaluation results and visualizations.

## CI/CD Pipeline Analysis

The CI/CD pipeline defined in `.github/workflows/CI_CD.yml` automates the training, testing, building, and deployment of the machine learning model. Here’s an overview of the key components:

### 1. **Trigger**
- The pipeline is triggered with every push to the repository.

### 2. **Jobs**
The pipeline consists of five main jobs:

#### a. **test_before_train**
- **Environment**: Runs on `ubuntu-latest` using a Docker container.
- **Steps**:
  - **Checkout Code**: Checks out the repository code.
  - **Install Dependencies**: Installs required Python packages and CML.
  - **Run Unittest before Train and Log Results**: 
    - Ensures that categorical data (`country` and `gender`) is encoded correctly using `LabelEncoder`.
    - Tests grid search functionality for tuning hyperparameters of classifiers.
    - Validates f0.5 score and optimal classification threshold.
    - Confirms that the model can be saved and loaded from a pickle file correctly.
  - **Report**: Uses CML to comment on the training report.

#### b. **train**
- **Environment**: Runs on `ubuntu-latest` using a Docker container.
- **Steps**:
  - **Checkout Code**: Checks out the repository code.
  - **Install Dependencies**: Installs required Python packages and CML.
  - **Run Train and Log Results**: 
    - Trains the model using various classifiers and scalers.
    - Selects the best model based on the recall score.
    - Saves the trained model to `models/model.pkl`.
    - Logs metrics, including training and test scores, best recall score, and best threshold, to `metrics.txt`.
    - Generates and saves confusion matrix and classification report as images.

#### c. **test_after_train**
- **Environment**: Runs on `ubuntu-latest` using a Docker container.
- **Steps**:
  - **Checkout Code**: Checks out the repository code.
  - **Install Dependencies**: Installs required Python packages and CML.
  - **Run Unittest after Train and Log Results**:
    - Checks if the trained model file `models/model.pkl` is saved correctly.
    - Ensures the saved model can be loaded and used for predictions, with output matching the number of test samples.
    - Validates the computation and shape of the confusion matrix.
    - Confirms that the classification report includes all necessary metrics for each class and overall.
    - Ensures the metrics file `metrics.txt` is generated.
    - Verifies that the threshold for the f0.5 score is within the valid range [0, 1].
  - **Report**: Uses CML to comment on the training report.

#### d. **build**
- **Dependencies**: This job depends on the successful completion of the `train_and_test` job.
- **Steps**:
  - **Checkout Code**: Retrieves the latest code.
  - **Log in to Docker Hub**: Authenticates to Docker Hub using secrets.
  - **Build Docker Image**: Builds a Docker image for the application.
  - **Push Docker Image**: Pushes the built image to Docker Hub.

#### e. **deploy**
- **Dependencies**: This job depends on the successful completion of the `build` job.
- **Steps**:
  - **Checkout Code**: Retrieves the latest code.
  - **Install Kubectl**: Installs the Kubernetes command-line tool.
  - **Configure AWS Credentials**: Sets up AWS credentials for accessing EKS.
  - **Update Kubeconfig for EKS**: Configures access to the EKS cluster.
  - **Replace Docker Hub Username in deployment.yml**: Updates the deployment configuration with the Docker Hub username.
  - **Deploy to Kubernetes**: Applies the Kubernetes deployment configuration.
  - **Verify Deployment**: Checks the status of the deployment to ensure it is running correctly.

### Conclusion
This CI/CD pipeline streamlines the deployment process of machine learning models, ensuring that code changes are automatically tested, built, and deployed to a Kubernetes environment.

### MLOps Integration
The integration of MLOps (Machine Learning Operations) processes facilitates the transition of the project to a production environment and ensures that models can be continuously updated.

**1. Continuous Integration (CI/CD)**  
The processes of model development and training are automated, allowing for the model to be updated and retrained with new data.

**2. Model Monitoring**  
Model performance is continuously monitored, and necessary updates are made in case of performance degradation.

**3. Version Control**  
Versioning of both data and models is implemented, allowing for tracking of project revisions and improvements.

### Machine Learning Algorithms Used in the Project
Various machine learning algorithms are utilized in this project:

- Logistic Regression
- Support Vector Machines (SVM)
- Random Forest
- AdaBoost
- Gradient Boosting
- CatBoost
- XGBoost  
These algorithms are optimized using GridSearchCV, and the best-performing model is selected.

### Technologies and Tools
The technologies and tools used in the project include:

- Python: The primary programming language for the project.
- Pandas: A library for data processing.
- Scikit-learn: The main library used for machine learning models.
- XGBoost, CatBoost, LightGBM: Powerful machine learning algorithms.
- GridSearchCV: Used for model optimization and hyperparameter tuning.
- MLOps Tools: Various MLOps tools are used for model tracking and updates.

### Dataset
The data used in this project is sourced from a CSV file containing customer information from banks. This data includes demographic characteristics, account information, and historical transactions. The data undergoes preprocessing steps to make it ready for use in models.

### Data Categories:
**Demographic Data:** Information such as customer age, gender, and marital status.  
**Financial Data:** Financial indicators like the amount of money in the customer’s account and credit card usage.  
**Behavioral Data:** Customer transactions and past account activities.

## Bankacılık Sektöründe Müşteri Kaybı Tahmin Projesi

### Proje Hakkında
Bu proje, bankacılık alanında müşteri kaybını (churn) tahmin etmek amacıyla geliştirilmiştir. Müşteri kaybı, bankaların finansal kayıplar yaşamasına ve rekabet gücünün azalmasına yol açabilir. Bu sebeple, churn tahmin modelleri, müşteri davranışlarını anlamak ve kayıp riskini azaltmak için kullanılmaktadır.

### Proje Amacı
Projenin hedefi, mevcut müşteri verilerini kullanarak hangi müşterilerin bankadan ayrılma ihtimalinin yüksek olduğunu belirlemektir. Bankalar, bu tahminleri baz alarak stratejik kararlar alabilir ve kaybı azaltmak için çeşitli pazarlama ve sadakat kampanyaları geliştirebilir.

### Kullanım Alanları
Bu proje, birçok iş sürecinde fayda sağlayabilir:

**1. Müşteri Segmentasyonu**  
Churn riski taşıyan müşteriler tanımlanarak, bu gruplara özel hizmetler veya kampanyalar sunulabilir.

**2. Risk Yönetimi**  
Bankalar, yüksek churn riski olan müşteriler için proaktif müdahale stratejileri geliştirebilir.

**3. Pazarlama ve Sadakat Yönetimi**  
Hedef odaklı pazarlama kampanyaları ve müşteri sadakati programları oluşturularak müşteri memnuniyeti ve elde tutma oranı artırılabilir.

**4. Gelir Tahmini**  
Churn oranlarını azaltmak, gelir kaybını önlemeye ve şirketin mali durumunu iyileştirmeye katkıda bulunur.

### MLOps Model Dağıtımı

Bu MLOps projesi, GitHub Actions kullanarak bir Makine Öğrenimi modelinin uçtan uca pipeline'ını içermektedir.

## Müşteri Churn Tahmin Modeli

Bu depo, bankacılık müşteri verilerini kullanarak müşteri kaybını tahmin etmek için bir makine öğrenimi modeli eğitmek üzere kod içermektedir. Amaç, churn riski taşıyan müşterileri tanımlamak ve buna yönelik hedefli koruma stratejileri geliştirmektir.

`train.py` scripti aşağıdaki görevleri yerine getirir:

1. **Veri Hazırlığı**: Veriyi yükler, eksik değerlerle ilgilenir ve kategorik özellikleri kodlar.
2. **Özellik ve Hedef Değişken Çıkarımı**: Özellikleri hedef değişkenden ayırır.
3. **Veri Bölme**: Veriyi eğitim ve test setlerine ayırır.
4. **Model Seçimi ve Hiperparametre Ayarlaması**: Farklı hiperparametrelerle birden fazla sınıflandırıcıyı değerlendirir ve geri çağırmayı optimize etmek için grid search kullanır.  
   - Geri çağırma, modelin ana değerlendirme ölçütü olarak seçilmiştir, çünkü dengesiz veri setlerinde churn'un tüm ilgili örneklerini tespit etmek kritik öneme sahiptir. Geri çağırmayı optimize ederek, risk altında olan müşterilerin mümkün olduğunca fazla sayıda tanımlanmasını sağlarız, bu da etkili müşteri koruma stratejileri geliştirilmesine yardımcı olur.
5. **Model Eğitimi**: Geri çağırma temelinde en iyi performansı gösteren modeli eğitir.
6. **Değerlendirme**: Model performansını çeşitli metrikler kullanarak değerlendirir ve sonuçları ve görselleştirmeleri kaydeder.

## CI/CD Pipeline Analizi

`.github/workflows/CI_CD.yml` dosyasında tanımlanan CI/CD pipeline'ı, makine öğrenimi modelinin eğitimi, testi, oluşturulması ve dağıtımını otomatikleştirir. İşte ana bileşenlerin bir analizi:

### 1. **Tetkik**
- Pipeline, her repoya itme işlemi gerçekleştiğinde tetiklenir.

### 2. **İşlemler**
Pipeline beş ana işlemden oluşmaktadır:

#### a. **test_before_train**
- **Ortam**: `ubuntu-latest` üzerinde Docker konteyneri kullanarak çalışır.
- **Adımlar**:
  - **Kodu Al**: Depodaki kodu kontrol eder.
  - **Bağımlılıkları Yükle**: Gerekli Python paketlerini ve CML'yi yükler.
  - **Eğitim Öncesi Testi Çalıştır ve Sonuçları Kaydet**: 
    - Kategorik verilerin (`country` ve `gender`) doğru şekilde kodlandığını kontrol eder.
    - Sınıflandırıcıların hiperparametre ayarları için grid search fonksiyonunu test eder.
    - f0.5 skoru ve optimal sınıflandırma eşiğini doğrular.
    - Modelin bir pickle dosyasından doğru bir şekilde kaydedilip yüklenebildiğini onaylar.
  - **Rapor**: Eğitim raporuna yorum eklemek için CML kullanır.

#### b. **train**
- **Ortam**: `ubuntu-latest` üzerinde Docker konteyneri kullanarak çalışır.
- **Adımlar**:
  - **Kodu Al**: Depodaki kodu kontrol eder.
  - **Bağımlılıkları Yükle**: Gerekli Python paketlerini ve CML'yi yükler.
  - **Eğitim Çalıştır ve Sonuçları Kaydet**: 
    - Çeşitli sınıflandırıcılar ve ölçekleyiciler kullanarak modeli eğitir.
    - Geri çağırma puanına göre en iyi modeli seçer.
    - Eğitilmiş modeli `models/model.pkl` dosyasına kaydeder.
    - Eğitim ve test puanları, en iyi geri çağırma puanı ve en iyi eşik dahil olmak üzere metrikleri `metrics.txt` dosyasına kaydeder.
    - Karışıklık matrisini ve sınıflandırma raporunu görüntü olarak oluşturur ve kaydeder.

#### c. **test_after_train**
- **Ortam**: `ubuntu-latest` üzerinde Docker konteyneri kullanarak çalışır.
- **Adımlar**:
  - **Kodu Al**: Depodaki kodu kontrol eder.
  - **Bağımlılıkları Yükle**: Gerekli Python paketlerini ve CML'yi yükler.
  - **Eğitim Sonrası Testi Çalıştır ve Sonuçları Kaydet**:
    - Eğitilen model dosyasının `models/model.pkl` dosyasına doğru bir şekilde kaydedilip kaydedilmediğini kontrol eder.
    - Kaydedilen modelin yüklenebilir ve tahminlerde kullanılabilir olduğunu doğrular, çıktının test örnekleri sayısıyla eşleştiğini kontrol eder.
    - Karışıklık matrisinin hesaplaması ve boyutunu doğrular.
    - Sınıflandırma raporunun her sınıf ve genel için gerekli tüm metrikleri içerdiğini onaylar.
    - Metrik dosyasının `metrics.txt` olarak oluşturulduğunu sağlar.
    - f0.5 skoru için eşik değerinin geçerli aralıkta [0, 1] olduğunu doğrular.
  - **Rapor**: Eğitim raporuna yorum eklemek için CML kullanır.

#### d. **build**
- **Bağımlılıklar**: Bu iş, `train_and_test` işinin başarılı bir şekilde tamamlanmasına bağlıdır.
- **Adımlar**:
  - **Kodu Al**: En son kodu alır.
  - **Docker Hub'a Giriş Yap**: Gizli bilgileri kullanarak Docker Hub'a kimlik doğrulaması yapar.
  - **Docker imajını oluştur**: Uygulama için bir Docker imajı oluşturur.
  - **Docker imajını gönder**: Oluşturulan imajı Docker Hub'a gönderir.

#### e. **deploy**
- **Bağımlılıklar**: Bu iş, `build` işinin başarılı bir şekilde tamamlanmasına bağlıdır.
- **Adımlar**:
  - **Kodu Al**: En son kodu alır.
  - **Kubectl'i Yükle**: Kubernetes komut satırı aracını yükler.
  - **AWS kimlik bilgilerini yapılandır**: EKS'ye erişim için AWS kimlik bilgilerini ayarlar.
  - **EKS için kubeconfig'i güncelle**: EKS kümesine erişimi yapılandırır.
  - **deployment.yml dosyasındaki Docker Hub kullanıcı adını değiştir**: Dağıtım yapılandırmasını Docker Hub kullanıcı adı ile günceller.
  - **Kubernetes'e dağıtım yap**: Kubernetes dağıtım yapılandırmasını uygular.
  - **Dağıtımı doğrula**: Dağıtımın düzgün çalıştığını kontrol eder.

### Sonuç
Bu CI/CD pipeline'ı, makine öğrenimi modellerinin dağıtım sürecini kolaylaştırır, kod değişikliklerinin otomatik olarak test edilmesini, oluşturulmasını ve Kubernetes ortamına dağıtılmasını sağlar.

### MLOps Entegrasyonu
MLOps (Makine Öğrenimi Operasyonları) süreçlerinin entegrasyonu, projenin üretim ortamına geçişini kolaylaştırmakta ve modellerin sürekli olarak güncellenebilmesini sağlamaktadır.

**1. Sürekli Entegrasyon (CI/CD)**  
Model geliştirme ve eğitim süreçleri otomatikleştirilerek, modelin yeni verilerle güncellenmesi ve yeniden eğitilmesi sağlanır.

**2. Model İzleme**  
Modelin performansı sürekli olarak izlenir ve performans düşüşü durumunda gerekli güncellemeler yapılır.

**3. Versiyon Kontrolü**  
Veri ve model versiyonlama uygulanarak, projedeki geri dönüşler ve iyileştirmeler takip edilebilir.

### Projede Kullanılan Makine Öğrenimi Algoritmaları
Bu projede çeşitli makine öğrenimi algoritmaları kullanılmıştır:

- Lojistik Regresyon
- Destek Vektör Makineleri (SVM)
- Rastgele Orman
- AdaBoost
- Gradient Boosting
- CatBoost
- XGBoost  
Bu algoritmalar GridSearchCV ile optimize edilmiş ve en iyi performans gösteren model seçilmiştir.

### Teknolojiler ve Araçlar
Projede kullanılan teknolojiler ve araçlar şunlardır:

- Python: Projenin ana programlama dili.
- Pandas: Veri işleme kütüphanesi.
- Scikit-learn: Makine öğrenimi modelleri için ana kütüphane.
- XGBoost, CatBoost, LightGBM: Güçlü makine öğrenimi algoritmaları.
- GridSearchCV: Model optimizasyonu ve hiperparametre ayarlaması için kullanılır.
- MLOps Araçları: Model takibi ve güncellemeleri için çeşitli MLOps araçları kullanılmıştır.

### Veri Seti
Projede kullanılan veriler, bankaların müşteri bilgilerini içeren bir CSV dosyasından elde edilmiştir. Bu veriler, müşterilerin demografik özellikleri, hesap bilgileri ve geçmiş işlemleri gibi bilgileri içermektedir. Veriler, ön işleme adımlarından geçirilmiş ve modellerde kullanılmak üzere hazır hale getirilmiştir.

### Veri Kategorileri:
**Demografik Veri:** Müşteri yaşı, cinsiyeti, medeni durumu gibi bilgiler.  
**Finansal Veri:** Müşterinin hesabındaki para miktarı ve kredi kartı kullanımı gibi finansal göstergeler.  
**Davranışsal Veri:** Müşteri işlemleri ve geçmiş hesap aktiviteleri.
