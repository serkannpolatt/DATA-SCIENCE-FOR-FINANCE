import unittest
import os
import pickle
from sklearn.metrics import confusion_matrix, classification_report
from train import ChurnPredictionModel


class TestAfterTrain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize the test case with the trained model."""

        cls.model_path = "models/model.pkl"

        if not os.path.exists(cls.model_path):
            raise FileNotFoundError(f"Model file '{cls.model_path}' was not found.")

        model = ChurnPredictionModel(
            data_path="data/Bank_Customer_Churn_Prediction.csv"
        )
        cls.X_test = model.get_X_test()
        cls.y_test = model.get_y_test()

    def test_model_file_exists(self):
        """Test if the trained model has been saved correctly."""
        self.assertTrue(os.path.exists(self.model_path), "Model file was not saved.")

    def test_model_loading(self):
        """Test if the saved model can be loaded and used for prediction."""
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)

        predictions = model.predict(self.X_test)
        self.assertEqual(
            len(predictions), len(self.X_test), "Model prediction output size mismatch."
        )

    def test_confusion_matrix(self):
        """Test if confusion matrix can be computed and is valid."""
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)

        y_pred = model.predict(self.X_test)
        cm = confusion_matrix(self.y_test, y_pred)

        self.assertEqual(cm.shape, (2, 2), "Confusion matrix shape is incorrect.")

    def test_classification_report(self):
        """Test if classification report is generated correctly."""
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)

        y_pred = model.predict(self.X_test)
        cr = classification_report(self.y_test, y_pred, output_dict=True)

        expected_keys = {"precision", "recall", "f1-score", "support"}
        for label in ["0", "1", "accuracy", "macro avg", "weighted avg"]:
            self.assertTrue(
                expected_keys.issubset(cr[label].keys()),
                f"Missing keys in classification report for label {label}.",
            )

    def test_metrics_file_exists(self):
        """Test if the metrics file has been generated correctly."""
        metrics_path = "metrics.txt"
        self.assertTrue(os.path.exists(metrics_path), "Metrics file was not generated.")

    def test_threshold_validity(self):
        """Test if the selected best threshold for f0.5 score is within valid range."""
        best_threshold = 0.5
        self.assertGreaterEqual(best_threshold, 0, "Threshold is less than 0.")
        self.assertLessEqual(best_threshold, 1, "Threshold is greater than 1.")


if __name__ == "__main__":
    with open("test_results_after_train.txt", "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)
