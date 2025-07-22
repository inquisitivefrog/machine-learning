#!/usr/bin/env python3

import glob
import joblib
import logging
import matplotlib
matplotlib.use('Agg')
import numpy as np
import os
import pytest
import time
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from diabetes import (
    create_polynomial_features,
    debug,
    evaluate_model,
    load_dataset,
    log_feature_importances,
    measure_model,
    predict_new_patient,
    print_dataset_info,
    reduce_dimensions,
    save_model,
    select_features,
    split_dataset,
    train_linear_model,
    train_model,
    train_stacking_model,
    train_xgb_model,
    transform_features
)

os.makedirs("output", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/test_diabetes.log"),
        logging.StreamHandler()
    ]
)

@pytest.fixture
def diabetes_data():
    """Load diabetes dataset."""
    X, y, diabetes = load_dataset()
    X, y = X[:200], y[:200]  # Match diabetes.py
    return X, y, diabetes

def test_load_dataset(diabetes_data):
    """Verify dataset loads correctly."""
    X, y, diabetes = diabetes_data
    assert X.shape == (200, 10)
    assert y.shape == (200,)
    assert diabetes.feature_names == ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

def test_split_dataset(diabetes_data):
    """Verify dataset splits and scales."""
    X, y, diabetes = diabetes_data
    X_transformed, new_feature_names = transform_features(X, diabetes.feature_names)
    assert X_transformed.shape[1] == 11  # 10 original + bmi_bp_ratio
    X_poly, poly, _ = create_polynomial_features(X_transformed, degree=3, diabetes=diabetes)
    assert X_poly.shape[1] == 363
    feature_names = poly.get_feature_names_out(new_feature_names)
    X_train, X_test, y_train, y_test, scaler = split_dataset(X_poly, y)
    assert X_train.shape[0] + X_test.shape[0] == 200
    assert y_train.shape[0] == X_train.shape[0]
    assert y_test.shape[0] == X_test.shape[0]
    assert X_train.shape[1] == 363
    assert scaler is not None

def prepare_data(X, y, diabetes):
    X_transformed, new_feature_names = transform_features(X, diabetes.feature_names)
    X_poly, poly, diabetes = create_polynomial_features(X_transformed, degree=3, diabetes=diabetes)
    feature_names = poly.get_feature_names_out(new_feature_names)
    X_train, X_test, y_train, y_test, scaler = split_dataset(X_poly, y)
    return X_train, X_test, y_train, y_test, scaler, poly, feature_names, diabetes

def test_train_rf_model(diabetes_data):
    """Verify RandomForest training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_gb_model(diabetes_data):
    """Verify GradientBoosting training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_xgb_model(diabetes_data):
    """Verify XGBoost training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_xgb_model(X_train[:20], y_train[:20])
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_dt_model(diabetes_data):
    """Verify DecisionTree training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    assert model is not None
    assert hasattr(model, 'predict')
    assert model.named_steps['regressor'].random_state == 42

def test_train_knn_model(diabetes_data):
    """Verify KNeighbors training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="knn")
    assert model is not None
    assert hasattr(model, 'predict')

def test_train_svr_model(diabetes_data):
    """Verify SVR training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="svr")
    assert model is not None
    assert hasattr(model, 'predict')

def test_train_stacking_model(diabetes_data):
    """Verify Stacking training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_stacking_model(X_train[:20], y_train[:20])
    assert model is not None
    assert hasattr(model, 'predict')
    assert isinstance(model.named_steps['regressor'], StackingRegressor)

def test_train_rf_model_pipeline(diabetes_data):
    """Verify RandomForest pipeline."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_gb_model_pipeline(diabetes_data):
    """Verify GradientBoosting pipeline."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_xgb_model_pipeline(diabetes_data):
    """Verify XGBoost pipeline."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_xgb_model(X_train[:20], y_train[:20])
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_dt_model_pipeline(diabetes_data):
    """Verify DecisionTree pipeline."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_knn_model_pipeline(diabetes_data):
    """Verify KNeighbors pipeline."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="knn")
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_svr_model_pipeline(diabetes_data):
    """Verify SVR pipeline."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="svr")
    assert isinstance(model, Pipeline)
    assert list(model.named_steps.keys()) == ['regressor']

def test_train_rf_model_predictions(diabetes_data):
    """Verify RandomForest predictions."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all(predictions >= 0)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_train_xgb_model_predictions(diabetes_data):
    """Verify XGBoost predictions."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_xgb_model(X_train[:20], y_train[:20])
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all(predictions >= 0)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_train_dt_model_predictions(diabetes_data):
    """Verify DecisionTree predictions."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all(predictions >= 0)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_train_knn_model_predictions(diabetes_data):
    """Verify KNeighbors predictions."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="knn")
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all(predictions >= 0)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_train_svr_model_predictions(diabetes_data):
    """Verify SVR predictions."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="svr")
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_train_stacking_model_predictions(diabetes_data):
    """Verify Stacking predictions."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_stacking_model(X_train[:20], y_train[:20])
    predictions = model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all(predictions >= 0)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_evaluate_rf_model(caplog, diabetes_data):
    """Verify RandomForest evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    for file in glob.glob("output/diabetes_rf_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="rf")
    assert "Test Set Metrics (rf)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_rf_scatter_*.png")) == 0

def test_evaluate_gb_model(caplog, diabetes_data):
    """Verify GradientBoosting evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    for file in glob.glob("output/diabetes_gb_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="gb")
    assert "Test Set Metrics (gb)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_gb_scatter_*.png")) == 0

def test_evaluate_xgb_model(caplog, diabetes_data):
    """Verify XGBoost evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_xgb_model(X_train[:20], y_train[:20])
    for file in glob.glob("output/diabetes_xgb_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="xgb")
    assert "Test Set Metrics (xgb)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_xgb_scatter_*.png")) == 0

def test_evaluate_dt_model(caplog, diabetes_data):
    """Verify DecisionTree evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    for file in glob.glob("output/diabetes_dt_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="dt")
    assert "Test Set Metrics (dt)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_dt_scatter_*.png")) == 0

def test_evaluate_knn_model(caplog, diabetes_data):
    """Verify KNeighbors evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="knn")
    for file in glob.glob("output/diabetes_knn_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="knn")
    assert "Test Set Metrics (knn)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_knn_scatter_*.png")) == 0

def test_evaluate_svr_model(caplog, diabetes_data):
    """Verify SVR evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="svr")
    for file in glob.glob("output/diabetes_svr_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="svr")
    assert "Test Set Metrics (svr)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_svr_scatter_*.png")) == 0

def test_evaluate_rf_model_debug(diabetes_data):
    """Verify RandomForest debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="rf", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_rf_scatter_*.png")) > 0

def test_evaluate_gb_model_debug(diabetes_data):
    """Verify GradientBoosting debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="gb", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_gb_scatter_*.png")) > 0

def test_evaluate_xgb_model_debug(diabetes_data):
    """Verify XGBoost debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_xgb_model(X_train[:20], y_train[:20])
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="xgb", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_xgb_scatter_*.png")) > 0

def test_evaluate_dt_model_debug(diabetes_data):
    """Verify DecisionTree debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="dt", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_dt_scatter_*.png")) > 0

def test_evaluate_knn_model_debug(diabetes_data):
    """Verify KNeighbors debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="knn")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="knn")
    assert len(glob.glob("output/diabetes_knn_scatter_*.png")) > 0

def test_evaluate_svr_model_debug(diabetes_data):
    """Verify SVR debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="svr")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="svr")
    assert len(glob.glob("output/diabetes_svr_scatter_*.png")) > 0

def test_measure_rf_model(caplog, diabetes_data):
    """Verify RandomForest RMSE metrics."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    caplog.set_level(logging.INFO, logger="root")
    measure_model(model, X_train, y_train, X_test, y_test, model_type="rf")
    assert "Training Set RMSE (rf)" in caplog.text
    assert "Test Set RMSE (rf)" in caplog.text
    assert "Cross-validated RMSE (rf)" in caplog.text

def test_save_rf_model(tmp_path, diabetes_data):
    """Verify model saving."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, scaler, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    save_model(model, poly, scaler, model_type="rf")
    assert len(glob.glob("output/diabetes_rf_model_*.pkl")) > 0

def test_print_dataset_info(caplog, diabetes_data):
    """Verify dataset info logging."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    caplog.set_level(logging.INFO, logger="root")
    print_dataset_info(X, X_train, diabetes)
    assert "Description: Diabetes dataset" in caplog.text
    assert "Sample Size: 200" in caplog.text
    assert "Training Size: 160" in caplog.text

def test_debug(diabetes_data):
    """Verify debug heatmap."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    debug(X, y, diabetes, debug_mode=True, poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_heatmap_*.png")) > 0

def test_load_dataset_error(monkeypatch):
    """Verify dataset load error handling."""
    def mock_load_diabetes():
        raise Exception("Mock error")
    monkeypatch.setattr("diabetes.load_diabetes", mock_load_diabetes)
    X, y, diabetes = load_dataset()
    assert X is None
    assert y is None
    assert diabetes is None

def test_split_dataset_error(monkeypatch, diabetes_data):
    """Verify split error handling."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    def mock_fit_transform(*args, **kwargs):
        raise Exception("Mock error")
    monkeypatch.setattr("sklearn.preprocessing.StandardScaler.fit_transform", mock_fit_transform)
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    assert X_train is None
    assert X_test is None
    assert y_train is None
    assert y_test is None
    assert scaler is None

def test_train_model_error(monkeypatch, diabetes_data):
    """Verify training error handling."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    def mock_fit(*args, **kwargs):
        raise Exception("Mock error")
    monkeypatch.setattr("sklearn.model_selection.GridSearchCV.fit", mock_fit)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    assert model is None

def test_evaluate_model_error(monkeypatch, caplog, diabetes_data):
    """Verify evaluation error handling."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    def mock_predict(*args, **kwargs):
        raise Exception("Mock error")
    monkeypatch.setattr("sklearn.pipeline.Pipeline.predict", mock_predict)
    caplog.set_level(logging.ERROR, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="rf")
    assert "Error evaluating rf model" in caplog.text

def test_train_lr_model(diabetes_data):
    """Verify LinearRegression training."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_linear_model(X_train[:20], y_train[:20])
    assert model is not None
    assert hasattr(model, 'predict')
    assert isinstance(model.named_steps['regressor'], LinearRegression)

def test_evaluate_lr_model(caplog, diabetes_data):
    """Verify LinearRegression evaluation."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_linear_model(X_train[:20], y_train[:20])
    for file in glob.glob("output/diabetes_lr_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="lr")
    assert "Test Set Metrics (lr)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_lr_scatter_*.png")) == 0

def test_evaluate_lr_model_debug(diabetes_data):
    """Verify LinearRegression debug plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_linear_model(X_train[:20], y_train[:20])
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="lr")
    assert len(glob.glob("output/diabetes_lr_scatter_*.png")) > 0

def test_debug_with_poly(diabetes_data):
    """Verify debug with polynomial features."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    debug(X, y, diabetes, debug_mode=True, poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_heatmap_*.png")) > 0

def test_evaluate_rf_model_residuals(diabetes_data):
    """Verify RandomForest residual plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="rf", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_rf_residuals_*.png")) > 0

def test_evaluate_gb_model_residuals(diabetes_data):
    """Verify GradientBoosting residual plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="gb", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_gb_residuals_*.png")) > 0

def test_evaluate_dt_model_residuals(diabetes_data):
    """Verify DecisionTree residual plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="dt", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_dt_residuals_*.png")) > 0

def test_evaluate_knn_model_residuals(diabetes_data):
    """Verify KNeighbors residual plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="knn")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="knn")
    assert len(glob.glob("output/diabetes_knn_residuals_*.png")) > 0

def test_evaluate_svr_model_residuals(diabetes_data):
    """Verify SVR residual plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="svr")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="svr")
    assert len(glob.glob("output/diabetes_svr_residuals_*.png")) > 0

def test_evaluate_rf_model_importances(diabetes_data):
    """Verify RandomForest feature importance plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="rf", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_rf_importances_*.png")) > 0

def test_evaluate_dt_model_importances(diabetes_data):
    """Verify DecisionTree feature importance plots."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="dt")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="dt", poly=poly, feature_names=feature_names)
    assert len(glob.glob("output/diabetes_dt_importances_*.png")) > 0

def test_select_features(diabetes_data):
    """Verify feature selection."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    X_train_selected, X_test_selected, selected_features = select_features(X_train, y_train, X_test, model)
    assert X_train_selected.shape[1] <= X_train.shape[1]
    assert X_test_selected.shape[1] == X_train_selected.shape[1]
    assert len(selected_features) == X_train.shape[1]

def test_evaluate_rf_selected_model(caplog, diabetes_data):
    """Verify RandomForest with selected features."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    X_train_selected, X_test_selected, selected_features = select_features(X_train, y_train, X_test, model)
    selected_names = [feature_names[i] for i, selected in enumerate(selected_features) if selected]
    model_selected = train_model(X_train_selected[:20], y_train[:20], model_type="rf")
    for file in glob.glob("output/diabetes_rf_selected_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model_selected, X_test_selected, y_test, diabetes, debug=False, model_type="rf_selected", feature_names=selected_names)
    assert "Test Set Metrics (rf_selected)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_rf_selected_scatter_*.png")) == 0

def test_evaluate_rf_selected_model_debug(diabetes_data):
    """Verify RandomForest debug with selected features."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    X_train_selected, X_test_selected, selected_features = select_features(X_train, y_train, X_test, model)
    selected_names = [feature_names[i] for i, selected in enumerate(selected_features) if selected]
    model_selected = train_model(X_train_selected[:20], y_train[:20], model_type="rf")
    evaluate_model(model_selected, X_test_selected, y_test, diabetes, debug=True, model_type="rf_selected", feature_names=selected_names)
    assert len(glob.glob("output/diabetes_rf_selected_scatter_*.png")) > 0
    assert len(glob.glob("output/diabetes_rf_selected_residuals_*.png")) > 0

def test_evaluate_gb_selected_model(caplog, diabetes_data):
    """Verify GradientBoosting with selected features."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    X_train_selected, X_test_selected, selected_features = select_features(X_train, y_train, X_test, model)
    selected_names = [feature_names[i] for i, selected in enumerate(selected_features) if selected]
    model_selected = train_model(X_train_selected[:20], y_train[:20], model_type="gb")
    for file in glob.glob("output/diabetes_gb_selected_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model_selected, X_test_selected, y_test, diabetes, debug=False, model_type="gb_selected", feature_names=selected_names)
    assert "Test Set Metrics (gb_selected)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_gb_selected_scatter_*.png")) == 0

def test_evaluate_rf_pca_model(caplog, diabetes_data):
    """Verify RandomForest with PCA."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    X_train_pca, X_test_pca, _ = reduce_dimensions(X_train[:20], X_test, n_components=10)
    model = train_model(X_train_pca, y_train[:20], model_type="rf")
    for file in glob.glob("output/diabetes_rf_pca_scatter_*.png"):
        os.remove(file)
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test_pca, y_test, diabetes, debug=False, model_type="rf_pca")
    assert "Test Set Metrics (rf_pca)" in caplog.text
    assert "Mean Squared Error" in caplog.text
    assert len(glob.glob("output/diabetes_rf_pca_scatter_*.png")) == 0

def test_measure_rf_pca_model(caplog, diabetes_data):
    """Verify PCA RMSE metrics."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    X_train_pca, X_test_pca, _ = reduce_dimensions(X_train[:20], X_test, n_components=10)
    model = train_model(X_train_pca, y_train[:20], model_type="rf")
    caplog.set_level(logging.INFO, logger="root")
    measure_model(model, X_train_pca, y_train[:20], X_test_pca, y_test, model_type="rf_pca")
    assert "Training Set RMSE (rf_pca)" in caplog.text
    assert "Test Set RMSE (rf_pca)" in caplog.text
    assert "Cross-validated RMSE (rf_pca)" in caplog.text

def test_log_feature_importances_rf(caplog, diabetes_data):
    """Verify RandomForest feature importances."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    caplog.set_level(logging.INFO, logger="root")
    log_feature_importances(model, "rf", poly, feature_names)
    assert "Feature Importances (rf)" in caplog.text
    assert "bmi" in caplog.text

def test_log_feature_importances_rf_selected(caplog, diabetes_data):
    """Verify feature importances for selected features."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    X_train_selected, X_test_selected, selected_features = select_features(X_train, y_train, X_test, model)
    selected_names = [feature_names[i] for i, selected in enumerate(selected_features) if selected]
    model_selected = train_model(X_train_selected[:20], y_train[:20], model_type="rf")
    caplog.set_level(logging.INFO, logger="root")
    log_feature_importances(model_selected, "rf_selected", None, selected_names)
    assert "Feature Importances (rf_selected)" in caplog.text
    assert any(name in caplog.text for name in selected_names)

def transform_features(X, feature_names):
    """Transform features."""
    try:
        X_transformed = X.copy()
        feature_names_list = list(feature_names)
        bmi_idx = feature_names_list.index('bmi')
        bp_idx = feature_names_list.index('bp')
        s5_idx = feature_names_list.index('s5')
        X_transformed[:, bmi_idx] = np.log1p(X[:, bmi_idx] - X[:, bmi_idx].min() + 1)
        X_transformed[:, s5_idx] = np.log1p(X[:, s5_idx] - X[:, s5_idx].min() + 1)
        bmi_bp_ratio = X[:, bmi_idx] / (X[:, bp_idx] + 1e-6)
        X_transformed = np.c_[X_transformed, bmi_bp_ratio]
        new_feature_names = feature_names_list + ['bmi_bp_ratio']
        logging.info("Transformed features: %s", new_feature_names)
        logging.info("X_transformed shape: %s", X_transformed.shape)
        assert X_transformed.shape[1] == len(new_feature_names), "Feature count mismatch"
        return X_transformed, new_feature_names
    except Exception as e:
        logging.error(f"Error transforming features: {e}")
        return None, None

def test_train_stacking_model_all_features(caplog, diabetes_data):
    """Verify Stacking with transformed features."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_stacking_model(X_train[:20], y_train[:20])
    assert model is not None
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="stack")
    assert "Test Set Metrics (stack)" in caplog.text
    assert "Mean Squared Error" in caplog.text

def test_debug_with_transformed_features(caplog, diabetes_data):
    """Verify debug with transformed features."""
    X, y, diabetes = diabetes_data
    X_transformed, new_feature_names = transform_features(X, diabetes.feature_names)
    X_poly, poly, _ = create_polynomial_features(X_transformed, degree=3, diabetes=diabetes)
    feature_names = poly.get_feature_names_out(new_feature_names)
    caplog.set_level(logging.DEBUG, logger="root")
    debug(X_poly, y, diabetes, debug_mode=False, poly=poly, feature_names=feature_names)
    assert "Features: {}".format(feature_names) in caplog.text
    assert "bmi_bp_ratio" in caplog.text
    assert "Sample:" in caplog.text

def test_evaluate_model_feature_names(caplog, diabetes_data):
    """Verify feature importance plot."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, _, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="rf")
    caplog.set_level(logging.INFO, logger="root")
    evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type="rf", poly=poly, feature_names=feature_names)
    assert "Feature importance plot saved" in caplog.text
    assert len(glob.glob("output/diabetes_rf_importances_*.png")) > 0

def test_use_saved_model(diabetes_data):
    """Verify loading and predicting with saved model."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, scaler, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    save_model(model, poly, scaler, model_type="gb")
    model_files = glob.glob("output/diabetes_gb_model_*.pkl")
    assert len(model_files) > 0, "No saved model found"
    loaded_model = joblib.load(model_files[-1])
    predictions = loaded_model.predict(X_test)
    assert predictions.shape == (y_test.shape[0],)
    assert np.all(predictions >= 0)
    assert all(50 <= pred <= 300 for pred in predictions)

def test_predict_new_patient(diabetes_data):
    """Verify prediction for new patient."""
    X, y, diabetes = diabetes_data
    X_train, X_test, y_train, y_test, scaler, poly, feature_names, _ = prepare_data(X, y, diabetes)
    model = train_model(X_train[:20], y_train[:20], model_type="gb")
    save_model(model, poly, scaler, model_type="gb")
    model_path = glob.glob("output/diabetes_gb_model_*.pkl")[-1]
    patient_data = X[:1]
    prediction = predict_new_patient(model_path, patient_data, poly, scaler, diabetes.feature_names)
    assert prediction is not None
    assert prediction.shape == (1,)
    assert prediction[0] >= 0
    assert 50 <= prediction[0] <= 300

if __name__ == "__main__":
    pytest.main(["-v", "--log-cli-level=INFO"])
