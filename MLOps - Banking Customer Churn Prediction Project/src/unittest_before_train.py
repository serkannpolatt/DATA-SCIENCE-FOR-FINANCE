import unittest
import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.metrics import fbeta_score, recall_score, make_scorer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from train import ChurnPredictionModel  # Ensure this import is correct

class TestBeforeTrain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Setup method for loading and preprocessing the dataset. """

        cls.df = pd.read_csv('data/Bank_Customer_Churn_Prediction.csv')
        cls.label_country_encoder = LabelEncoder()
        cls.df['country'] = cls.label_country_encoder.fit_transform(cls.df['country'])
        cls.label_gender_encoder = LabelEncoder()
        cls.df['gender'] = cls.label_gender_encoder.fit_transform(cls.df['gender'])
        cls.X = cls.df.drop(['customer_id', 'churn'], axis=1)
        cls.Y = cls.df['churn']
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(cls.X, cls.Y, test_size=0.2, random_state=42)

    def test_data_encoding(self):
        """ Test to verify if the data encoding with LabelEncoder is applied correctly. """

        self.assertIn('country', self.df.columns)
        self.assertIn('gender', self.df.columns)

        self.assertTrue(pd.api.types.is_integer_dtype(self.df['country']))
        self.assertTrue(pd.api.types.is_integer_dtype(self.df['gender']))

    def test_grid_search(self):
        """ Test the performance of GridSearchCV for model hyperparameter tuning. """

        stratified_kfold = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
        recall_scorer = make_scorer(recall_score)

        model = ChurnPredictionModel(data_path='data/Bank_Customer_Churn_Prediction.csv')

        classifiers = model.get_classifiers()
        scalers = model.get_scalers()

        classifier_name, (classifier, param_grid) = 'Logistic Regression', classifiers['Logistic Regression']
        scaler = scalers['Standard Scaler']
        
        pipeline = Pipeline([
            ('scaler', scaler),
            ('classifier', classifier)
        ])
        
        grid_search = GridSearchCV(pipeline, param_grid, cv=stratified_kfold, scoring=recall_scorer, n_jobs=-1)
        grid_search.fit(self.X_train, self.y_train)
        
        best_recall = grid_search.best_score_
        self.assertGreaterEqual(best_recall, 0)
        self.assertIsNotNone(grid_search.best_params_)
        self.assertIn('classifier__C', grid_search.best_params_)

    def test_f05_threshold(self):
        """ Test the calculation of the optimal threshold based on the f0.5 score. """

        model = LogisticRegression(max_iter=1000).fit(self.X_train, self.y_train)
        y_train_proba = model.predict_proba(self.X_train)[:, 1]

        best_f05_score = 0
        best_threshold = 0
        thresholds = [i / 1000 for i in range(1001)]
        for threshold in thresholds:
            y_pred_thresholded = (y_train_proba >= threshold).astype(int)
            f05 = fbeta_score(self.y_train, y_pred_thresholded, beta=0.5)
            if f05 > best_f05_score:
                best_f05_score = f05
                best_threshold = threshold

        self.assertGreater(best_f05_score, 0)
        self.assertGreaterEqual(best_threshold, 0)
        self.assertLessEqual(best_threshold, 1)

    def test_model_saving_loading(self):
        """ Test the saving and loading of the trained model. """

        model = LogisticRegression(max_iter=1000)
        model.fit(self.X_train, self.y_train)
        
        model_dir = 'models'
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

        model_path = os.path.join(model_dir, 'test_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)

        with open(model_path, 'rb') as f:
            loaded_model = pickle.load(f)

        self.assertIsNotNone(loaded_model)
        self.assertTrue(hasattr(loaded_model, 'predict'))

        os.remove(model_path)

if __name__ == '__main__':
    with open('test_results_before_train.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)
