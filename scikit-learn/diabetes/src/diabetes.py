#!/usr/bin/env python3

import gc
import glob
import logging
import time
from datetime import datetime
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
import xgboost as xgb

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/diabetes.log"),
        logging.StreamHandler()
    ]
)

def load_dataset():
    try:
        diabetes = load_diabetes()
        X, y = diabetes.data, diabetes.target
        logging.info("Dataset loaded successfully")
        return X, y, diabetes
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        return None, None, None

def transform_features(X, feature_names):
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
        assert X_transformed.shape[1] == len(new_feature_names), "Feature count mismatch"
        return X_transformed, new_feature_names
    except Exception as e:
        logging.error(f"Error transforming features: {e}")
        return None, None

def create_polynomial_features(X, degree=3, diabetes=None):
    try:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X_poly = poly.fit_transform(X)
        logging.info("Polynomial feature count: %d", X_poly.shape[1])
        logging.info("Polynomial feature names: %s", poly.get_feature_names_out())
        return X_poly, poly, diabetes
    except Exception as e:
        logging.error(f"Error creating polynomial features: %s", e)
        return None, None, None

def split_dataset(X, y, test_size=0.2, random_state=42):
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        logging.info("Dataset split into %d training and %d test samples", len(X_train), len(X_test))
        return X_train, X_test, y_train, y_test, scaler
    except Exception as e:
        logging.error(f"Error splitting dataset: %s", e)
        return None, None, None, None, None

def train_model(X_train, y_train, model_type="rf"):
    try:
        if model_type == "rf":
            param_grid = {
                'regressor__n_estimators': [50, 100],
                'regressor__max_depth': [None, 10],
                'regressor__min_samples_split': [2, 5]
            }
            model = RandomForestRegressor(random_state=42)
        elif model_type == "gb":
            param_grid = {
                'regressor__n_estimators': [50, 100],
                'regressor__learning_rate': [0.01, 0.05],
                'regressor__max_depth': [2, 3]
            }
            model = GradientBoostingRegressor(random_state=42)
        elif model_type == "dt":
            param_grid = {
                'regressor__max_depth': [None, 5, 10],
                'regressor__min_samples_split': [2, 5]
            }
            model = DecisionTreeRegressor(random_state=42)
        elif model_type == "knn":
            param_grid = {
                'regressor__n_neighbors': [3, 5, 7],
                'regressor__weights': ['uniform', 'distance']
            }
            model = KNeighborsRegressor()
        elif model_type == "svr":
            param_grid = {
                'regressor__C': [0.1, 1.0],
                'regressor__epsilon': [0.1, 0.5]
            }
            model = SVR(kernel='linear')
        else:
            logging.error("Unsupported model type: %s", model_type)
            return None
        pipeline = Pipeline([('regressor', model)])
        grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=1)
        grid_search.fit(X_train, y_train)
        logging.info("Best parameters for %s: %s", model_type, grid_search.best_params_)
        return grid_search.best_estimator_
    except Exception as e:
        logging.error(f"Error training %s model: %s", model_type, e)
        return None

def train_xgb_model(X_train, y_train):
    try:
        param_dist = {
            'regressor__n_estimators': [50, 100],
            'regressor__learning_rate': [0.01, 0.05],
            'regressor__max_depth': [2, 3]
        }
        model = xgb.XGBRegressor(random_state=42, objective='reg:squarederror')
        pipeline = Pipeline([('regressor', model)])
        random_search = RandomizedSearchCV(pipeline, param_dist, n_iter=10, cv=5, scoring='neg_mean_squared_error', n_jobs=1, random_state=42)
        random_search.fit(X_train, y_train)
        logging.info("Best parameters for xgb: %s", random_search.best_params_)
        return random_search.best_estimator_
    except Exception as e:
        logging.error(f"Error training xgb model: %s", e)
        return None

def train_linear_model(X_train, y_train):
    try:
        model = LinearRegression()
        pipeline = Pipeline([('regressor', model)])
        pipeline.fit(X_train, y_train)
        logging.info("Trained linear regression model")
        return pipeline
    except Exception as e:
        logging.error(f"Error training linear model: %s", e)
        return None

def train_stacking_model(X_train, y_train):
    try:
        estimators = [
            ('rf', RandomForestRegressor(n_estimators=50, random_state=42)),
            ('gb', GradientBoostingRegressor(n_estimators=50, random_state=42)),
            ('xgb', xgb.XGBRegressor(n_estimators=50, random_state=42))
        ]
        model = StackingRegressor(estimators=estimators, final_estimator=LinearRegression(), cv=5)
        pipeline = Pipeline([('regressor', model)])
        pipeline.fit(X_train, y_train)
        logging.info("Trained stacking model")
        return pipeline
    except Exception as e:
        logging.error(f"Error training stacking model: %s", e)
        return None

def select_features(X_train, y_train, X_test, model, n_features=10):
    try:
        selector = RFE(model.named_steps['regressor'], n_features_to_select=n_features)
        selector.fit(X_train, y_train)
        X_train_selected = selector.transform(X_train)
        X_test_selected = selector.transform(X_test)
        selected_features = selector.support_
        logging.info("Selected %d features", n_features)
        return X_train_selected, X_test_selected, selected_features
    except Exception as e:
        logging.error(f"Error selecting features: %s", e)
        return None, None, None

def reduce_dimensions(X_train, X_test, n_components=10):
    try:
        pca = PCA(n_components=n_components)
        X_train_pca = pca.fit_transform(X_train)
        X_test_pca = pca.transform(X_test)
        logging.info("Reduced to %d components, explained variance ratio: %.2f", n_components, sum(pca.explained_variance_ratio_))
        return X_train_pca, X_test_pca, pca
    except Exception as e:
        logging.error(f"Error reducing dimensions: %s", e)
        return None, None, None

def evaluate_model(model, X_test, y_test, diabetes, debug=False, model_type="rf", poly=None, feature_names=None):
    try:
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        logging.info("Test Set Metrics (%s):", model_type)
        logging.info("  Mean Squared Error: %.2f", mse)
        logging.info("  Root Mean Squared Error: %.2f", rmse)
        logging.info("  Mean Absolute Error: %.2f", mae)
        logging.info("  R² Score: %.2f", r2)
        if debug:
            save_path = f"output/diabetes_{model_type}_scatter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=y_test, y=predictions, alpha=0.5)
            plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
            plt.xlabel("Actual Progression")
            plt.ylabel("Predicted Progression")
            plt.title(f"{model_type.upper()} Actual vs Predicted Disease Progression")
            plt.savefig(save_path, dpi=100, bbox_inches="tight")
            logging.info("Scatter plot saved to %s", save_path)
            plt.close('all')

            residual_save_path = f"output/diabetes_{model_type}_residuals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.figure(figsize=(8, 6))
            residuals = y_test - predictions
            sns.scatterplot(x=predictions, y=residuals, alpha=0.5)
            plt.axhline(0, color='r', linestyle='--')
            plt.xlabel("Predicted Progression")
            plt.ylabel("Residuals")
            plt.title(f"{model_type.upper()} Residual Plot")
            plt.savefig(residual_save_path, dpi=100, bbox_inches="tight")
            logging.info("Residual plot saved to %s", residual_save_path)
            plt.close('all')

            if model_type in ["rf", "gb", "xgb", "dt"] and feature_names is not None:
                importances = model.named_steps['regressor'].feature_importances_
                importance_save_path = f"output/diabetes_{model_type}_importances_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                plt.figure(figsize=(10, 6))
                top_indices = np.argsort(importances)[-10:]
                top_importances = importances[top_indices]
                top_names = [feature_names[i] for i in top_indices]
                sns.barplot(x=top_importances, y=top_names)
                plt.title(f"{model_type.upper()} Feature Importances")
                plt.savefig(importance_save_path, dpi=100, bbox_inches="tight")
                logging.info("Feature importance plot saved to %s", importance_save_path)
                plt.close('all')
    except Exception as e:
        logging.error(f"Error evaluating %s model: %s", model_type, e)

def measure_model(model, X_train, y_train, X_test, y_test, model_type="rf"):
    try:
        train_predictions = model.predict(X_train)
        train_rmse = np.sqrt(mean_squared_error(y_train, train_predictions))
        test_predictions = model.predict(X_test)
        test_rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
        cv_rmse = np.sqrt(-cv_scores.mean())
        logging.info("Training Set RMSE (%s): %.2f", model_type, train_rmse)
        logging.info("Test Set RMSE (%s): %.2f", model_type, test_rmse)
        logging.info("Cross-validated RMSE (%s): %.2f", model_type, cv_rmse)
    except Exception as e:
        logging.error(f"Error measuring %s model: %s", model_type, e)

def log_feature_importances(model, model_type, poly, feature_names):
    try:
        importances = model.named_steps['regressor'].feature_importances_
        indices = np.argsort(importances)[::-1]
        logging.info("Feature Importances (%s):", model_type)
        for i in indices[:10]:
            logging.info("  %s: %.4f", feature_names[i], importances[i])
    except Exception as e:
        logging.error(f"Error logging feature importances for %s: %s", model_type, e)

def print_dataset_info(X, X_train, diabetes):
    try:
        logging.info("Dataset Information:")
        logging.info("  Description: Diabetes dataset")
        logging.info("  Sample Size: %d", X.shape[0])
        logging.info("  Features: %d", X.shape[1])
        logging.info("  Feature Names: %s", diabetes.feature_names)
        if X_train is not None:
            logging.info("  Training Size: %d", X_train.shape[0])
    except Exception as e:
        logging.error(f"Error printing dataset info: %s", e)

def debug(X, y, diabetes, debug_mode=False, poly=None, feature_names=None):
    try:
        if feature_names is None:
            feature_names = diabetes.feature_names if poly is None else poly.get_feature_names_out(diabetes.feature_names)
        if X.shape[1] != len(feature_names):
            logging.error("Shape mismatch: X has %d features, but %d feature names provided", X.shape[1], len(feature_names))
            return
        logging.debug("Features: %s", feature_names)
        logging.debug("Target: Disease Progression")
        logging.debug("Source: %s", diabetes.data_filename)
        df = pd.DataFrame(X, columns=feature_names)
        logging.debug("Sample:\n%s", df.iloc[10:12])
        logging.debug("Summary Statistics:\n%s", df.describe())
        logging.debug("Target Distribution:\n%s", pd.Series(y).describe())
        if debug_mode:
            save_path = f"output/diabetes_heatmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.figure(figsize=(10, 8))
            sns.heatmap(df.corr(), annot=(poly is None), cmap='coolwarm', fmt='.2f')
            plt.title("Feature Correlation Heatmap")
            plt.savefig(save_path, dpi=100, bbox_inches="tight")
            logging.info("Correlation heatmap saved to %s", save_path)
            plt.close('all')
    except Exception as e:
        logging.error(f"Error debugging dataset: %s", e)

def save_model(model, poly, scaler, model_type="rf"):
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"output/diabetes_{model_type}_model_{timestamp}.pkl"
        joblib.dump(model, filename)
        joblib.dump(poly, f"output/poly_{timestamp}.pkl")
        joblib.dump(scaler, f"output/scaler_{timestamp}.pkl")
        # Update latest models
        joblib.dump(model, f"output/diabetes_{model_type}_model_latest.pkl")
        joblib.dump(poly, "output/poly.pkl")
        joblib.dump(scaler, "output/scaler.pkl")
        logging.info("Model saved to %s", filename)
    except Exception as e:
        logging.error(f"Error saving %s model: %s", model_type, e)

def predict_new_patient(model_path, patient_data, poly, scaler, feature_names):
    try:
        model = joblib.load(model_path)
        patient_transformed, _ = transform_features(patient_data, feature_names)
        patient_poly = poly.transform(patient_transformed)
        patient_scaled = scaler.transform(patient_poly)
        prediction = model.predict(patient_scaled)
        logging.info("Predicted progression: %.2f", prediction[0])
        return prediction
    except Exception as e:
        logging.error("Error predicting: %s", e)
        return None

def main():
    start_time = time.time()
    logging.info("Starting diabetes prediction script at %s", datetime.now())
    X, y, diabetes = load_dataset()
    if X is None or y is None:
        logging.error("Failed to load dataset")
        return
    X, y = X[:200], y[:200]
    print_dataset_info(X, None, diabetes)
    debug(X, y, diabetes, debug_mode=True)
    X_transformed, new_feature_names = transform_features(X, diabetes.feature_names)
    if X_transformed is None:
        logging.error("Failed to transform features")
        return
    X_poly, poly, diabetes = create_polynomial_features(X_transformed, degree=3, diabetes=diabetes)
    if X_poly is None:
        logging.error("Failed to create polynomial features")
        return
    feature_names = poly.get_feature_names_out(new_feature_names)
    X_train, X_test, y_train, y_test, scaler = split_dataset(X_poly, y)
    if X_train is None:
        logging.error("Failed to split dataset")
        return
    # Train and evaluate models
    for model_type in ["rf", "gb", "xgb", "stack", "lr", "rf_pca", "dt", "knn", "svr"]:
        if model_type == "rf_pca":
            X_train_pca, X_test_pca, pca = reduce_dimensions(X_train, X_test, n_components=10)
            model = train_model(X_train_pca, y_train, model_type="rf")
            if model is None:
                logging.error("Failed to train rf_pca model")
                continue
            evaluate_model(model, X_test_pca, y_test, diabetes, debug=True, model_type="rf_pca")
            measure_model(model, X_train_pca, y_train, X_test_pca, y_test, model_type="rf_pca")
            save_model(model, poly, scaler, model_type="rf_pca")
        else:
            if model_type == "xgb":
                model = train_xgb_model(X_train, y_train)
            elif model_type == "stack":
                model = train_stacking_model(X_train, y_train)
            elif model_type == "lr":
                model = train_linear_model(X_train, y_train)
            else:  # rf, gb, dt, knn, svr
                model = train_model(X_train, y_train, model_type=model_type)
            if model is None:
                logging.error("Failed to train %s model", model_type)
                continue
            evaluate_model(model, X_test, y_test, diabetes, debug=True, model_type=model_type, poly=poly, feature_names=feature_names)
            measure_model(model, X_train, y_train, X_test, y_test, model_type=model_type)
            save_model(model, poly, scaler, model_type=model_type)
        gc.collect()
    # Feature selection
    for model_type in ["rf", "gb"]:
        model = train_model(X_train, y_train, model_type=model_type)
        if model is None:
            logging.error("Failed to train %s model for feature selection", model_type)
            continue
        X_train_selected, X_test_selected, selected_features = select_features(X_train, y_train, X_test, model)
        if X_train_selected is None:
            logging.error("Failed to select features for %s", model_type)
            continue
        selected_names = [feature_names[i] for i, selected in enumerate(selected_features) if selected]
        model_selected = train_model(X_train_selected, y_train, model_type=model_type)
        if model_selected is None:
            logging.error("Failed to train %s selected model", model_type)
            continue
        evaluate_model(model_selected, X_test_selected, y_test, diabetes, debug=True, model_type=f"{model_type}_selected", feature_names=selected_names)
        measure_model(model_selected, X_train_selected, y_train, X_test_selected, y_test, model_type=f"{model_type}_selected")
        save_model(model_selected, poly, scaler, model_type=f"{model_type}_selected")
        log_feature_importances(model_selected, f"{model_type}_selected", None, selected_names)
        gc.collect()
    # Predict new patient
    model_path = glob.glob("output/diabetes_gb_model_*.pkl")[-1]
    patient_data = X[:1]
    prediction = predict_new_patient(model_path, patient_data, poly, scaler, diabetes.feature_names)
    if prediction is not None:
        logging.info("Predicted progression for new patient: %.2f", prediction[0])
    logging.info("Script completed in %.2f seconds", time.time() - start_time)

if __name__ == "__main__":
    main()
