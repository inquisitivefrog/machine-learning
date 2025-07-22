#!/usr/bin/env python3
# Test Breast Cancer Prediction: Unit and integration tests for breast_cancer.py
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

import glob
import joblib
import logging
import matplotlib
matplotlib.use('Agg')
import numpy as np
import os
import pytest
from unittest.mock import patch
from sklearn.pipeline import Pipeline
from breast_cancer import (
    load_dataset,
    split_dataset,
    reduce_dimensions,
    train_model,
    evaluate_model,
    measure_model,
    save_model,
    debug
)

# Create output directory
os.makedirs("output", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/test_breast_cancer.log"),
        logging.StreamHandler()
    ]
)

@pytest.fixture
def breast_cancer_data():
    """Load breast cancer dataset."""
    X, y, data = load_dataset()
    return X, y, data

def test_load_dataset(breast_cancer_data):
    """Verify dataset loads correctly."""
    X, y, data = breast_cancer_data
    assert X.shape == (569, 30)
    assert y.shape == (569,)
    assert len(data.target_names) == 2

def test_split_dataset(breast_cancer_data):
    """Verify dataset splits and scales."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    assert X_train.shape[0] + X_test.shape[0] == 569
    assert y_train.shape[0] == X_train.shape[0]
    assert y_test.shape[0] == X_test.shape[0]
    assert X_train.shape[1] == 30
    assert scaler is not None

def test_reduce_dimensions(breast_cancer_data):
    """Verify PCA dimensionality reduction."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    X_train_pca, X_test_pca, pca = reduce_dimensions(X_train, X_test, n_components=15)
    assert X_train_pca.shape[1] == 15
    assert X_test_pca.shape[1] == 15
    assert pca is not None

def test_train_rf_model(breast_cancer_data):
    """Verify RandomForest training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_gb_model(breast_cancer_data):
    """Verify GradientBoosting training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="gb", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_knn_model(breast_cancer_data):
    """Verify KNeighbors training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="knn", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')

def test_train_svc_model(breast_cancer_data):
    """Verify SVC training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="svc", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_lr_model(breast_cancer_data):
    """Verify LogisticRegression training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="lr", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_mlp_model(breast_cancer_data):
    """Verify MLPClassifier training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="mlp", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_xgb_model(breast_cancer_data):
    """Verify XGBoost training."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="xgb", cv=3)
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_rf_model_pipeline(breast_cancer_data):
    """Verify RandomForest pipeline."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_rf_model_predictions(breast_cancer_data):
    """Verify RandomForest predictions."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all((predictions >= 0) & (predictions <= 1))

def test_evaluate_rf_model(caplog, breast_cancer_data):
    """Verify RandomForest evaluation."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    for file in glob.glob("output/breast_cancer_rf_cm_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    metrics = evaluate_model(model, X_test, y_test, data, debug=False, model_type="rf")
    assert "Test Set Metrics (rf)" in caplog.text
    assert "Accuracy" in caplog.text
    assert len(glob.glob("output/breast_cancer_rf_cm_*.png")) == 0
    assert metrics["accuracy"] >= 0.85

def test_evaluate_rf_model_debug(breast_cancer_data):
    """Verify RandomForest debug plots."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    for file in glob.glob("output/breast_cancer_rf_cm_*.png"):
        os.remove(file)
    for file in glob.glob("output/breast_cancer_rf_importances_*.png"):
        os.remove(file)
    evaluate_model(model, X_test, y_test, data, debug=True, model_type="rf")
    assert len(glob.glob("output/breast_cancer_rf_cm_*.png")) > 0
    assert len(glob.glob("output/breast_cancer_rf_importances_*.png")) > 0

def test_evaluate_gb_model(caplog, breast_cancer_data):
    """Verify GradientBoosting evaluation."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="gb", cv=3)
    for file in glob.glob("output/breast_cancer_gb_cm_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    metrics = evaluate_model(model, X_test, y_test, data, debug=False, model_type="gb")
    assert "Test Set Metrics (gb)" in caplog.text
    assert "Accuracy" in caplog.text
    assert len(glob.glob("output/breast_cancer_gb_cm_*.png")) == 0
    assert metrics["accuracy"] >= 0.85

def test_evaluate_xgb_model(caplog, breast_cancer_data):
    """Verify XGBoost evaluation."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="xgb", cv=3)
    for file in glob.glob("output/breast_cancer_xgb_cm_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    metrics = evaluate_model(model, X_test, y_test, data, debug=False, model_type="xgb")
    assert "Test Set Metrics (xgb)" in caplog.text
    assert "Accuracy" in caplog.text
    assert len(glob.glob("output/breast_cancer_xgb_cm_*.png")) == 0
    assert metrics["accuracy"] >= 0.85

def test_evaluate_rf_pca_model(caplog, breast_cancer_data):
    """Verify RandomForest with PCA."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    X_train_pca, X_test_pca, pca = reduce_dimensions(X_train, X_test, n_components=15)
    model = train_model(X_train_pca[:100], y_train[:100], model_type="rf", cv=3)
    for file in glob.glob("output/breast_cancer_rf_pca_cm_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    metrics = evaluate_model(model, X_test_pca, y_test, data, debug=False, model_type="rf_pca")
    assert "Test Set Metrics (rf_pca)" in caplog.text
    assert "Accuracy" in caplog.text
    assert len(glob.glob("output/breast_cancer_rf_pca_cm_*.png")) == 0
    assert metrics["accuracy"] >= 0.85

def test_evaluate_lr_model(caplog, breast_cancer_data):
    """Verify LogisticRegression evaluation."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="lr", cv=3)
    for file in glob.glob("output/breast_cancer_lr_cm_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    metrics = evaluate_model(model, X_test, y_test, data, debug=False, model_type="lr")
    assert "Test Set Metrics (lr)" in caplog.text
    assert "Accuracy" in caplog.text
    assert len(glob.glob("output/breast_cancer_lr_cm_*.png")) == 0
    assert metrics["accuracy"] >= 0.85

def test_evaluate_mlp_model(caplog, breast_cancer_data):
    """Verify MLPClassifier evaluation."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="mlp", cv=3)
    for file in glob.glob("output/breast_cancer_mlp_cm_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    metrics = evaluate_model(model, X_test, y_test, data, debug=False, model_type="mlp")
    assert "Test Set Metrics (mlp)" in caplog.text
    assert "Accuracy" in caplog.text
    assert len(glob.glob("output/breast_cancer_mlp_cm_*.png")) == 0
    assert metrics["accuracy"] >= 0.85

def test_measure_rf_model(caplog, breast_cancer_data):
    """Verify RandomForest accuracy metrics."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    caplog.set_level(logging.INFO, logger="root")
    measure_model(model, X_train[:100], y_train[:100], X_test, y_test, model_type="rf")
    assert "Training Set Accuracy (rf)" in caplog.text
    assert "Test Set Accuracy (rf)" in caplog.text
    assert "Cross-validated Accuracy (rf)" in caplog.text

def test_save_rf_model(breast_cancer_data):
    """Verify model saving."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    save_model(model, scaler, model_type="rf")
    assert len(glob.glob("output/breast_cancer_rf_model_*.pkl")) > 0

def test_debug(breast_cancer_data):
    """Verify debug heatmap."""
    X, y, data = breast_cancer_data
    debug(X, y, data, debug_mode=True)
    assert len(glob.glob("output/breast_cancer_heatmap_*.png")) > 0

def test_load_dataset_error(caplog):
    """Verify dataset load error handling."""
    with patch("breast_cancer.load_breast_cancer") as mock_load_breast_cancer:
        mock_load_breast_cancer.side_effect = Exception("Mock error")
        caplog.set_level(logging.ERROR, logger="root")
        X, y, data = load_dataset()
        assert "Error loading dataset: Mock error" in caplog.text
        assert X is None
        assert y is None
        assert data is None

def test_split_dataset_error(monkeypatch, breast_cancer_data):
    """Verify split error handling."""
    X, y, data = breast_cancer_data
    def mock_fit_transform(*args, **kwargs):
        raise Exception("Mock error")
    monkeypatch.setattr("sklearn.preprocessing.StandardScaler.fit_transform", mock_fit_transform)
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    assert X_train is None
    assert X_test is None
    assert y_train is None
    assert y_test is None
    assert scaler is None

def test_train_model_error(monkeypatch, breast_cancer_data):
    """Verify training error handling."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    def mock_fit(*args, **kwargs):
        raise Exception("Mock error")
    monkeypatch.setattr("sklearn.model_selection.GridSearchCV.fit", mock_fit)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    assert model is None

def test_evaluate_model_error(monkeypatch, caplog, breast_cancer_data):
    """Verify evaluation error handling."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    def mock_predict(*args, **kwargs):
        raise Exception("Mock error")
    monkeypatch.setattr("sklearn.pipeline.Pipeline.predict", mock_predict)
    caplog.set_level(logging.ERROR, logger="root")
    evaluate_model(model, X_test, y_test, data, debug=False, model_type="rf")
    assert "Error evaluating rf model" in caplog.text

def test_predict_new_sample(breast_cancer_data):
    """Verify prediction for new sample."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    save_model(model, scaler, model_type="rf")
    model_path = glob.glob("output/breast_cancer_rf_model_*.pkl")[-1]
    sample_data = X[:1]
    prediction = joblib.load(model_path).predict(scaler.transform(sample_data))
    assert prediction is not None
    assert prediction.shape == (1,)
    assert 0 <= prediction[0] <= 1

def test_predict_noisy_sample(breast_cancer_data):
    """Verify prediction robustness with Gaussian noise."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    np.random.seed(42)
    noisy_sample = X_test[:1].copy()
    noise = np.random.normal(0, 0.5, noisy_sample.shape)
    noisy_sample += noise
    prediction = model.predict(scaler.transform(noisy_sample))
    assert prediction.shape == (1,)
    assert 0 <= prediction[0] <= 1

def test_predict_missing_features(breast_cancer_data):
    """Verify prediction robustness with 20% missing features."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    np.random.seed(42)
    missing_sample = X_test[:1].copy()
    mask = np.random.choice([0, 1], size=missing_sample.shape, p=[0.2, 0.8])
    missing_sample *= mask
    prediction = model.predict(scaler.transform(missing_sample))
    assert prediction.shape == (1,)
    assert 0 <= prediction[0] <= 1

def test_predict_high_noise_sample(breast_cancer_data):
    """Verify prediction robustness with high-variance Gaussian noise."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    np.random.seed(42)
    noisy_sample = X_test[:1].copy()
    noise = np.random.normal(0, 1.0, noisy_sample.shape)
    noisy_sample += noise
    prediction = model.predict(scaler.transform(noisy_sample))
    assert prediction.shape == (1,)
    assert 0 <= prediction[0] <= 1

def test_predict_high_missing_features(breast_cancer_data):
    """Verify prediction robustness with 50% missing features."""
    X, y, data = breast_cancer_data
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    model = train_model(X_train[:100], y_train[:100], model_type="rf", cv=3)
    np.random.seed(42)
    missing_sample = X_test[:1].copy()
    mask = np.random.choice([0, 1], size=missing_sample.shape, p=[0.5, 0.5])
    missing_sample *= mask
    prediction = model.predict(scaler.transform(missing_sample))
    assert prediction.shape == (1,)
    assert 0 <= prediction[0] <= 1

if __name__ == "__main__":
    pytest.main(["-v", "--log-cli-level=INFO"])
