import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    MinMaxScaler,
    RobustScaler,
    StandardScaler,
    LabelEncoder,
)
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    make_scorer,
    fbeta_score,
    precision_score,
    recall_score,
)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from catboost import CatBoostClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pickle


class ChurnPredictionModel:
    def __init__(self, data_path):
        """Initialize dataset, encoders, classifiers, scalers, and split data."""

        self.df = pd.read_csv(data_path)
        self._encode_labels()
        self.X = self.df.drop(["customer_id", "churn"], axis=1)
        self.Y = self.df["churn"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.Y, test_size=0.2, random_state=42
        )
        self._initialize_classifiers_and_scalers()
        self.stratified_kfold = StratifiedKFold(
            n_splits=3, shuffle=True, random_state=42
        )
        self.recall_scorer = make_scorer(recall_score)
        self.precision_scorer = make_scorer(precision_score)

    def get_X_test(self):
        return self.X_test

    def get_y_test(self):
        return self.y_test

    def _encode_labels(self):
        """Encode categorical features using LabelEncoder."""

        self.label_country_encoder = LabelEncoder()
        self.df["country"] = self.label_country_encoder.fit_transform(
            self.df["country"]
        )
        self.label_gender_encoder = LabelEncoder()
        self.df["gender"] = self.label_gender_encoder.fit_transform(self.df["gender"])

    def _initialize_classifiers_and_scalers(self):
        """Initialize classifiers and scalers."""

        self.classifiers = {
            "Logistic Regression": (
                LogisticRegression(),
                {"classifier__C": [0.01, 0.1, 1, 10], "classifier__max_iter": [1000]},
            ),
            "Support Vector Classifier": (
                SVC(probability=True),
                {
                    "classifier__C": [0.1, 1, 10],
                    "classifier__kernel": ["linear", "rbf"],
                },
            ),
            "Naive Bayes": (GaussianNB(), {}),
            "Decision Tree": (
                DecisionTreeClassifier(),
                {"classifier__max_depth": [None, 10, 20, 40]},
            ),
            "Random Forest": (
                RandomForestClassifier(),
                {"classifier__n_estimators": [50, 100, 200, 500]},
            ),
            "AdaBoost": (
                AdaBoostClassifier(),
                {"classifier__n_estimators": [50, 100, 200, 500]},
            ),
            "Gradient Boosting": (
                GradientBoostingClassifier(),
                {"classifier__n_estimators": [50, 100, 200, 500]},
            ),
            "XGBoost": (XGBClassifier(), {"classifier__n_estimators": [50, 100, 200]}),
            "Catboost": (
                CatBoostClassifier(silent=True),
                {"classifier__iterations": [50, 100, 200]},
            ),
            "K Nearest Neighbors": (
                KNeighborsClassifier(),
                {"classifier__n_neighbors": [3, 5, 7, 9]},
            ),
            "Gaussian Process": (GaussianProcessClassifier(), {}),
        }

        self.scalers = {
            "Standard Scaler": StandardScaler(),
            "Min Max Scaler": MinMaxScaler(),
            "Robust Scaler": RobustScaler(),
            "No Scaler": None,
        }

    def get_classifiers(self):
        return self.classifiers

    def get_scalers(self):
        return self.scalers

    def grid_search_for_best_model(self):
        """Perform grid search with cross-validation to find the best classifier and scaler."""

        best_recall = 0
        self.best_classifier = None
        self.best_scaler = None
        self.best_params = None

        for classifier_name, (classifier, param_grid) in self.classifiers.items():
            for scaler_name, scaler in self.scalers.items():
                pipeline = Pipeline([("scaler", scaler), ("classifier", classifier)])
                grid_search = GridSearchCV(
                    pipeline,
                    param_grid,
                    cv=self.stratified_kfold,
                    scoring=self.recall_scorer,
                    n_jobs=-1,
                )
                grid_search.fit(self.X_train, self.y_train)

                mean_recall = grid_search.best_score_
                if mean_recall > best_recall:
                    best_recall = mean_recall
                    self.best_classifier = classifier_name
                    self.best_scaler = scaler_name
                    self.best_params = grid_search.best_params_

    def train_best_model(self):
        """Train the best model found by the grid search."""

        best_model = self.classifiers[self.best_classifier][0]
        best_scaler = self.scalers[self.best_scaler]
        best_params_cleaned = {
            k.split("__")[-1]: v for k, v in self.best_params.items()
        }

        self.best_pipeline = Pipeline(
            [
                ("scaler", best_scaler),
                ("classifier", best_model.set_params(**best_params_cleaned)),
            ]
        )
        self.best_pipeline.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """Evaluate the trained model and calculate the optimal threshold based on f0.5 score."""

        train_score = self.best_pipeline.score(self.X_train, self.y_train) * 100
        test_score = self.best_pipeline.score(self.X_test, self.y_test) * 100

        y_train_proba = self.best_pipeline.predict_proba(self.X_train)[:, 1]
        best_f05_score = 0
        best_threshold = 0

        for i in range(10000):
            y_pred_thresholded = (y_train_proba >= i / 10000).astype(int)
            f05 = fbeta_score(self.y_train, y_pred_thresholded, beta=0.5)
            if f05 > best_f05_score:
                best_f05_score = f05
                best_threshold = i / 10000

        return train_score, test_score, best_threshold

    def save_model_and_metrics(self, train_score, test_score, best_threshold):
        """Save the trained model and evaluation metrics to files."""

        if not os.path.exists("models"):
            os.makedirs("models")

        with open("models/model.pkl", "wb") as f:
            pickle.dump(self.best_pipeline, f)

        with open("metrics.txt", "w") as outfile:
            outfile.write(f"Training variance explained: {train_score:.1f}%\n")
            outfile.write(f"Test variance explained: {test_score:.1f}%\n")
            outfile.write(f"Best classifier: {self.best_classifier}\n")
            outfile.write(f"Best scaler: {self.best_scaler}\n")
            outfile.write(f"Best params: {self.best_params}\n")
            outfile.write(f"Best recall: {best_threshold:.4f}\n")

    def plot_results(self):
        """Generate and save confusion matrix and classification report as images."""

        y_pred = self.best_pipeline.predict(self.X_test)

        cm = confusion_matrix(self.y_test, y_pred)
        plt.figure(figsize=(10, 7))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=["Negative", "Positive"],
            yticklabels=["Negative", "Positive"],
        )
        plt.xlabel("Predicted Labels")
        plt.ylabel("True Labels")
        plt.title("Confusion Matrix")
        plt.savefig("confusion_matrix.png")

        cr = classification_report(self.y_test, y_pred, output_dict=True)
        cr_df = pd.DataFrame(cr).transpose()

        plt.figure(figsize=(10, 7))
        plt.title("Classification Report")
        ax = plt.gca()
        ax.axis("off")
        table = plt.table(
            cellText=cr_df.values,
            colLabels=cr_df.columns,
            rowLabels=cr_df.index,
            cellLoc="center",
            loc="center",
        )
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width(list(range(len(cr_df.columns))))
        plt.savefig("classification_report.png", bbox_inches="tight")


if __name__ == "__main__":
    model = ChurnPredictionModel(data_path="data/Bank_Customer_Churn_Prediction.csv")
    model.grid_search_for_best_model()
    model.train_best_model()
    train_score, test_score, best_threshold = model.evaluate_model()
    model.save_model_and_metrics(train_score, test_score, best_threshold)
    model.plot_results()
    print("Model training and evaluation completed!")
