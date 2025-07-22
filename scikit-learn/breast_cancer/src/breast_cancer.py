#!/usr/bin/env python3
# Breast Cancer Prediction: 569 samples from scikit-learn breast cancer dataset
# Binary classification (malignant vs. benign) with multiple models
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

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
import psutil
import os
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from xgboost import XGBClassifier

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/breast_cancer.log"),
        logging.StreamHandler()
    ]
)

def log_memory_usage():
    """Log current memory usage."""
    process = psutil.Process()
    mem_info = process.memory_info()
    logging.info("Memory usage: %.2f MB", mem_info.rss / 1024 / 1024)

def save_plot(fig, save_path, title):
    """Save a plot and ensure figure is closed."""
    try:
        fig.savefig(save_path, dpi=80, bbox_inches="tight")
        logging.info("%s saved to %s", title, save_path)
        plt.close(fig)
    except Exception as e:
        logging.error("Error saving %s: %s", title, e)

def load_dataset():
    """Load the breast cancer dataset."""
    try:
        data = load_breast_cancer()
        X, y = data.data, data.target
        logging.info("Dataset loaded: %d samples, %d features", X.shape[0], X.shape[1])
        log_memory_usage()
        return X, y, data
    except Exception as e:
        logging.error("Error loading dataset: %s", e)
        return None, None, None

def split_dataset(X, y, test_size=0.2, random_state=42):
    """Split and scale the dataset."""
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        logging.info("Dataset split: %d training, %d test samples", len(X_train), len(X_test))
        log_memory_usage()
        return X_train, X_test, y_train, y_test, scaler
    except Exception as e:
        logging.error("Error splitting dataset: %s", e)
        return None, None, None, None, None

def reduce_dimensions(X_train, X_test, n_components=15):
    """Apply PCA for dimensionality reduction."""
    try:
        pca = PCA(n_components=n_components)
        X_train_pca = pca.fit_transform(X_train)
        X_test_pca = pca.transform(X_test)
        logging.info("Reduced to %d components, explained variance ratio: %.2f", n_components, sum(pca.explained_variance_ratio_))
        log_memory_usage()
        return X_train_pca, X_test_pca, pca
    except Exception as e:
        logging.error("Error reducing dimensions: %s", e)
        return None, None, None

def train_model(X_train, y_train, model_type="rf", cv=5):
    """Train a model with hyperparameter tuning."""
    try:
        logging.info("Initializing model: %s", model_type)
        if model_type == "rf":
            param_grid = {'regressor__n_estimators': [50], 'regressor__max_depth': [5]}
            model = RandomForestClassifier(random_state=42)
        elif model_type == "gb":
            param_grid = {'regressor__n_estimators': [100], 'regressor__learning_rate': [0.05], 'regressor__max_depth': [3]}
            model = GradientBoostingClassifier(random_state=42)
        elif model_type == "knn":
            param_grid = {'regressor__n_neighbors': [3], 'regressor__weights': ['uniform']}
            model = KNeighborsClassifier()
        elif model_type == "svc":
            param_grid = {'regressor__C': [0.1], 'regressor__kernel': ['rbf']}
            model = SVC(random_state=42)
        elif model_type == "lr":
            param_grid = {'regressor__C': [0.1], 'regressor__solver': ['liblinear']}
            model = LogisticRegression(max_iter=300, random_state=42)
        elif model_type == "mlp":
            param_grid = {'regressor__hidden_layer_sizes': [(20,)], 'regressor__alpha': [0.05]}
            model = MLPClassifier(max_iter=1000, random_state=42)
        elif model_type == "xgb":
            param_grid = {'regressor__n_estimators': [50], 'regressor__max_depth': [3], 'regressor__learning_rate': [0.1]}
            model = XGBClassifier(random_state=42, eval_metric='logloss')
        else:
            logging.error("Unsupported model type: %s", model_type)
            return None
        pipeline = Pipeline([('regressor', model)])
        grid_search = GridSearchCV(pipeline, param_grid, cv=cv, scoring='accuracy', n_jobs=1)
        logging.info("Starting GridSearchCV for %s", model_type)
        grid_search.fit(X_train, y_train)
        logging.info("Best parameters for %s: %s", model_type, grid_search.best_params_)
        log_memory_usage()
        return grid_search.best_estimator_
    except Exception as e:
        logging.error("Error training %s model: %s", model_type, e)
        return None

def evaluate_model(model, X_test, y_test, data, debug=False, model_type="rf"):
    """Evaluate model performance."""
    try:
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        cm = confusion_matrix(y_test, predictions)
        report = classification_report(y_test, predictions, output_dict=True, zero_division=0)
        logging.info("Test Set Metrics (%s):", model_type)
        logging.info("  Accuracy: %.2f", accuracy)
        logging.info("  Confusion Matrix:\n%s", cm)
        logging.info("  Classification Report:\n%s", pd.DataFrame(report).transpose().to_string())
        if debug:
            save_path = f"output/breast_cancer_{model_type}_cm_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            fig = plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
            plt.title(f"{model_type.upper()} Confusion Matrix")
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            save_plot(fig, save_path, "Confusion matrix")
            if model_type in ["rf", "gb", "xgb"]:
                importances = model.named_steps['regressor'].feature_importances_
                importance_save_path = f"output/breast_cancer_{model_type}_importances_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                fig = plt.figure(figsize=(10, 6))
                top_indices = np.argsort(importances)[-10:]
                top_importances = importances[top_indices]
                top_names = [f"feature_{i}" for i in top_indices]
                sns.barplot(x=top_importances, y=top_names)
                plt.title(f"{model_type.upper()} Feature Importances")
                save_plot(fig, importance_save_path, "Feature importance plot")
        log_memory_usage()
        return {"accuracy": accuracy, "cm": cm, "report": report}
    except Exception as e:
        logging.error("Error evaluating %s model: %s", model_type, e)
        return None

def measure_model(model, X_train, y_train, X_test, y_test, model_type="rf"):
    """Measure model performance with cross-validation."""
    try:
        train_pred = model.predict(X_train)
        train_accuracy = accuracy_score(y_train, train_pred)
        test_pred = model.predict(X_test)
        test_accuracy = accuracy_score(y_test, test_pred)
        cv_scores = cross_val_score(model, X_train, y_train, cv=3, scoring='accuracy')
        logging.info("Training Set Accuracy (%s): %.2f", model_type, train_accuracy)
        logging.info("Test Set Accuracy (%s): %.2f", model_type, test_accuracy)
        logging.info("Cross-validated Accuracy (%s): %.2f", model_type, cv_scores.mean())
        log_memory_usage()
    except Exception as e:
        logging.error("Error measuring %s model: %s", model_type, e)

def save_model(model, scaler, model_type="rf"):
    """Save model and scaler."""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"output/breast_cancer_{model_type}_model_{timestamp}.pkl"
        joblib.dump(model, filename)
        joblib.dump(scaler, f"output/scaler_{timestamp}.pkl")
        joblib.dump(model, f"output/breast_cancer_{model_type}_model_latest.pkl")
        joblib.dump(scaler, "output/scaler.pkl")
        logging.info("Model saved to %s", filename)
        log_memory_usage()
    except Exception as e:
        logging.error("Error saving %s model: %s", model_type, e)

def debug(X, y, data, debug_mode=False):
    """Log dataset details and generate correlation heatmap."""
    try:
        feature_names = data.feature_names
        logging.debug("Features: %s", feature_names)
        logging.debug("Target: Malignant (0), Benign (1)")
        logging.debug("Sample Size: %d", X.shape[0])
        logging.debug("Features: %d", X.shape[1])
        df = pd.DataFrame(X, columns=feature_names)
        logging.debug("Sample:\n%s", df.iloc[0:2])
        logging.debug("Summary Statistics:\n%s", df.describe())
        logging.debug("Target Distribution:\n%s", pd.Series(y).value_counts().to_string())
        if debug_mode:
            save_path = f"output/breast_cancer_heatmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            fig = plt.figure(figsize=(10, 8))
            sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
            plt.title("Feature Correlation Heatmap")
            save_plot(fig, save_path, "Correlation heatmap")
        log_memory_usage()
    except Exception as e:
        logging.error("Error debugging dataset: %s", e)

def main():
    """Main function to train and evaluate models."""
    start_time = time.time()
    logging.info("Starting breast cancer prediction script at %s", datetime.now())
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # Load and preprocess data
    X, y, data = load_dataset()
    if X is None or y is None:
        logging.error("Failed to load dataset")
        return
    debug(X, y, data, debug_mode=True)
    X_train, X_test, y_train, y_test, scaler = split_dataset(X, y)
    if X_train is None:
        logging.error("Failed to split dataset")
        return

    # Train and evaluate models
    model_types = ["rf", "gb", "knn", "svc", "lr", "mlp", "xgb", "rf_pca"]
    metrics_summary = []
    for model_type in model_types:
        logging.info("Processing model: %s", model_type)
        try:
            if model_type == "rf_pca":
                X_train_pca, X_test_pca, pca = reduce_dimensions(X_train, X_test, n_components=15)
                if X_train_pca is None:
                    logging.error("Failed to reduce dimensions for rf_pca")
                    continue
                model = train_model(X_train_pca, y_train, model_type="rf")
                if model is None:
                    logging.error("Failed to train rf_pca model")
                    continue
                metrics = evaluate_model(model, X_test_pca, y_test, data, debug=True, model_type="rf_pca")
                measure_model(model, X_train_pca, y_train, X_test_pca, y_test, model_type="rf_pca")
                save_model(model, scaler, model_type="rf_pca")
                if metrics:
                    metrics_summary.append({
                        "model": model_type,
                        "accuracy": metrics["accuracy"],
                        "precision": metrics["report"]["weighted avg"]["precision"],
                        "recall": metrics["report"]["weighted avg"]["recall"],
                        "f1-score": metrics["report"]["weighted avg"]["f1-score"]
                    })
                del X_train_pca, X_test_pca, pca, metrics
            else:
                model = train_model(X_train, y_train, model_type=model_type)
                if model is None:
                    logging.error("Failed to train %s model", model_type)
                    continue
                metrics = evaluate_model(model, X_test, y_test, data, debug=True, model_type=model_type)
                measure_model(model, X_train, y_train, X_test, y_test, model_type=model_type)
                save_model(model, scaler, model_type=model_type)
                if metrics:
                    metrics_summary.append({
                        "model": model_type,
                        "accuracy": metrics["accuracy"],
                        "precision": metrics["report"]["weighted avg"]["precision"],
                        "recall": metrics["report"]["weighted avg"]["recall"],
                        "f1-score": metrics["report"]["weighted avg"]["f1-score"]
                    })
                del metrics
            del model
            gc.collect()
            log_memory_usage()
        except Exception as e:
            logging.error("Error processing %s model: %s", model_type, e)
            continue

    # Save metrics summary to CSV
    if metrics_summary:
        pd.DataFrame(metrics_summary).to_csv("output/breast_cancer_metrics.csv", index=False)
        logging.info("Metrics summary saved to output/breast_cancer_metrics.csv")

    logging.info("Script completed in %.2f seconds", time.time() - start_time)

if __name__ == "__main__":
    main()
