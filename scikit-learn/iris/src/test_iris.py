#!/usr/bin/env python3

import glob
import logging
import os
import pytest
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from iris import load_dataset, print_dataset_info, train_rfc_model, train_svc_model
from iris import evaluate_model, save_model, debug, measure_model

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/test_iris.log"),
        logging.StreamHandler()
    ]
)

def test_load_dataset():
    X, y, iris = load_dataset()
    assert X.shape == (150, 4)
    assert y.shape == (150,)
    assert iris.target_names.tolist() == ['setosa', 'versicolor', 'virginica']

def test_train_rfc_model():
    X, y, _ = load_dataset()
    model = train_rfc_model(X[:100], y[:100])
    assert hasattr(model, 'predict')
    assert model.named_steps['classifier'].random_state == 42

def test_train_rfc_model_pipeline():
    X, y, _ = load_dataset()
    model = train_rfc_model(X[:100], y[:100])
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['scaler', 'classifier']

def test_train_rfc_model_predictions():
    X, y, _ = load_dataset()
    model = train_rfc_model(X[:100], y[:100])
    predictions = model.predict(X[100:])
    assert predictions.shape == (50,)
    assert set(predictions).issubset({0, 1, 2})

def test_train_rfc_model_best_params():
    X, y, _ = load_dataset()
    model = train_rfc_model(X[:100], y[:100])
    assert model.named_steps['classifier'].n_estimators in [50, 100, 200]
    assert model.named_steps['classifier'].max_depth in [None, 5, 10]
    assert model.named_steps['classifier'].min_samples_split in [2, 5, 10]

def test_evaluate_rfc_model():
    X, y, iris = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_rfc_model(X_train, y_train)
    evaluate_model(model, X_test, y_test, iris, debug=False, model_type="rfc")
    assert len(glob.glob("output/iris_rfc_confusion_matrix_*.png")) > 0

def test_measure_model(caplog):
    X, y, iris = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_rfc_model(X_train, y_train)
    with caplog.at_level(logging.INFO):
        measure_model(model, X_train, y_train, X_test, y_test, debug=False)
    assert "Training Set Accuracy" in caplog.text
    assert "Test Set Accuracy" in caplog.text
    assert "Mean CV Accuracy" in caplog.text

def test_save_rfc_model(tmp_path):
    X, y, _ = load_dataset()
    model = train_rfc_model(X[:100], y[:100])
    filename = tmp_path / "test_rfc_model.pkl"
    save_model(model, filename=str(filename))
    assert os.path.exists(filename)

def test_evaluate_rfc_classification_report(caplog):
    X, y, iris = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_rfc_model(X_train, y_train)
    caplog.set_level(logging.DEBUG, logger="root")
    evaluate_model(model, X_test, y_test, iris, debug=True, model_type="rfc")
    print("caplog.text:", caplog.text)
    assert "Classification Report" in caplog.text
    assert "setosa" in caplog.text
    assert "versicolor" in caplog.text
    assert "virginica" in caplog.text

def test_train_svc_model():
    X, y, _ = load_dataset()
    model = train_svc_model(X[:100], y[:100])
    assert hasattr(model, 'predict')
    assert model.named_steps['classifier'].random_state == 42

def test_train_svc_model_pipeline():
    X, y, _ = load_dataset()
    model = train_svc_model(X[:100], y[:100])
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['scaler', 'classifier']

def test_train_svc_model_predictions():
    X, y, _ = load_dataset()
    model = train_svc_model(X[:100], y[:100])
    predictions = model.predict(X[100:])
    assert predictions.shape == (50,)
    assert set(predictions).issubset({0, 1, 2})

def test_train_svc_model_best_params():
    X, y, _ = load_dataset()
    model = train_svc_model(X[:100], y[:100])
    assert model.named_steps['classifier'].C in [0.01, 0.1, 0.5, 1, 5, 10, 50, 100]
    assert model.named_steps['classifier'].kernel in ['linear', 'rbf', 'poly']
    assert model.named_steps['classifier'].gamma in ['scale', 'auto', 0.01, 0.1, 0.5, 1]

def test_evaluate_svc_model():
    X, y, iris = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_svc_model(X_train, y_train)
    evaluate_model(model, X_test, y_test, iris, debug=False, model_type="svc")
    assert len(glob.glob("output/iris_svc_confusion_matrix_*.png")) > 0

def test_save_svc_model(tmp_path):
    X, y, _ = load_dataset()
    model = train_svc_model(X[:100], y[:100])
    filename = tmp_path / "test_svc_model.pkl"
    save_model(model, filename=str(filename))
    assert os.path.exists(filename)

def test_evaluate_svc_classification_report(caplog):
    X, y, iris = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_svc_model(X_train, y_train)
    caplog.set_level(logging.DEBUG, logger="root")
    evaluate_model(model, X_test, y_test, iris, debug=True, model_type="svc")
    assert "Classification Report" in caplog.text
    assert "setosa" in caplog.text
    assert "versicolor" in caplog.text
    assert "virginica" in caplog.text

def test_debug():
    X, y, iris = load_dataset()
    debug(X, y, iris, debug_mode=False)
    assert len(glob.glob("output/iris_pairplot_*.png")) > 0

def test_print_dataset_info(caplog):
    X, y, iris = load_dataset()
    X_train = X[:120]
    with caplog.at_level(logging.INFO):
        print_dataset_info(X, X_train, iris)
    assert "Description: Iris plants dataset" in caplog.text
    assert "Sample Size: 150" in caplog.text
    assert "Training Size: 120" in caplog.text

def test_load_dataset_error(monkeypatch):
    def mock_load_iris():
        raise Exception("Mock error")
    monkeypatch.setattr("iris.load_iris", mock_load_iris)
    X, y, iris = load_dataset()
    assert X is None
    assert y is None
    assert iris is None

def test_predict_new_flower():
    X, y, iris = load_iris()
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train, y_train)
    joblib.dump(model, "output/iris_model.pkl")
    prediction = predict_new_flower("output/iris_model.pkl", X_test[:1], scaler)
    assert prediction.shape == (1,)
    assert prediction[0] in [0, 1, 2]
