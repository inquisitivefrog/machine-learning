#!/usr/bin/env python3
# Iris: Train a RandomForestClassifier to predict flower species from a 150 data point collection
# https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris

import joblib
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/iris.log"),
        logging.StreamHandler()
    ]
)

def load_dataset():
    """Load the Iris dataset."""
    try:
        iris = load_iris()
        return iris.data, iris.target, iris
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        return None, None, None

def split_dataset(X, y):
    """Split dataset into training and test sets."""
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def train_rfc_model(X_train, y_train):
    """Train a RandomForestClassifier."""
    param_grid = {
        'classifier__n_estimators': [50, 100, 200],
        'classifier__max_depth': [None, 5, 10],  # Shallower trees
        'classifier__min_samples_split': [2, 5, 10]  # Prevent overfitting
    }
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    print("Best Parameters:", grid_search.best_params_)
    return grid_search.best_estimator_

def train_svc_model(X_train, y_train):
    """Train a SVC."""
    param_grid = {
        'classifier__C': [0.01, 0.1, 0.5, 1, 5, 10, 50, 100],
        'classifier__kernel': ['linear', 'rbf', 'poly'],
        'classifier__gamma': ['scale', 'auto', 0.01, 0.1, 0.5, 1]
    }
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(random_state=42))
    ])
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    print("Best Parameters:", grid_search.best_params_)
    return grid_search.best_estimator_

def evaluate_model(model, X_test, y_test, iris, debug=False, model_type="rfc"):
    """Evaluate model performance on test set.
    
    Args:
        model: Trained model.
        X_test: Test features.
        y_test: Test labels.
        iris: Iris dataset object.
        debug (bool): If True, display plot and detailed logs.
        model_type (str): Type of model ('rfc' or 'svc') for filename.
    """
    predictions = model.predict(X_test)
    logging.info("Test Set Accuracy: %.3f", accuracy_score(y_test, predictions))
    save_path = f"output/iris_{model_type}_confusion_matrix_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
                xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.title(f"{model_type.upper()} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    logging.info("Confusion matrix saved to %s", save_path)
    if debug:
        logging.debug("\nClassification Report:\n%s", classification_report(y_test, predictions, target_names=iris.target_names))
        plt.show()
    else:
        plt.close() 

def measure_model(model, X_train, y_train, X_test, y_test, debug=False):
    """Measure model performance on training set and via cross-validation."""
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)
    logging.info("Training Set Accuracy: %.3f", train_acc)
    logging.info("Test Set Accuracy: %.3f", test_acc)
    if train_acc - test_acc > 0.05:
        logging.warning("Potential overfitting detected.")
    scores = cross_val_score(model, X_train, y_train, cv=5)
    if debug:
        logging.debug("Cross-validation scores: %s", scores)
    logging.info("Mean CV Accuracy: %.3f", scores.mean())

def print_dataset_info(X, X_train, iris):
    """Print dataset information."""
    logging.info("Description: %s", iris.DESCR.split("\n")[2])
    logging.info("Sample Size: %d", len(X))
    logging.info("Training Size: %d", len(X_train))

def save_model(model, filename="output/iris_model.pkl"):
    """Save the trained model."""
    try:
        joblib.dump(model, filename)
        logging.info("Model saved to %s", filename)
    except Exception as e:
        logging.error(f"Error saving model: {e}")

os.makedirs("output", exist_ok=True)
def debug(X, y, iris, save_path=f"output/iris_pairplot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png", debug_mode=False):
    """Debug dataset with statistics and visualizations.
    
    Args:
        X (array-like): Feature data.
        y (array-like): Target data.
        iris (Bunch): Iris dataset object.
        save_path (str): Path to save the pairplot.
        debug_mode (bool): If True, display the plot.
    """
    logging.debug("Features: %s", iris.feature_names)
    logging.debug("Targets: %s", iris.target_names)
    df = pd.DataFrame(X, columns=iris.feature_names)
    logging.debug("Summary Statistics:\n%s", df.describe())
    logging.debug("Class Distribution:\n%s", pd.Series(y).value_counts(normalize=True))
    pair_plot = sns.pairplot(pd.DataFrame(X, columns=iris.feature_names).assign(Species=iris.target_names[y]))
    pair_plot.figure.savefig(save_path, dpi=300, bbox_inches="tight")
    logging.info("Pairplot saved to %s", save_path)
    if debug_mode:
        plt.show()
    else:
        plt.close()

def predict_new_flower(model_path, flower_data, scaler):
    model = joblib.load(model_path)
    flower_scaled = scaler.transform(flower_data)
    prediction = model.predict(flower_scaled)
    return prediction

if __name__ == "__main__":
    # Load data
    X, y, iris = load_dataset()

    if X is None:
        exit(1)
    debug(X, y, iris, debug_mode=True)

    # Split data
    X_train, X_test, y_train, y_test = split_dataset(X, y)
    print_dataset_info(X, X_train, iris)

    # Train and evaluate RFC
    model_rfc = train_rfc_model(X_train, y_train)
    evaluate_model(model_rfc, X_test, y_test, iris, debug=True, model_type="rfc")
    measure_model(model_rfc, X_train, y_train, X_test, y_test, debug=True)
    
    # Train and evaluate SVC
    model_svc = train_svc_model(X_train, y_train)
    evaluate_model(model_svc, X_test, y_test, iris, debug=True, model_type="svc")
    measure_model(model_svc, X_train, y_train, X_test, y_test, debug=True)

    # Save models
    save_model(model_svc, filename="output/iris_svc_model.pkl")
    save_model(model_rfc, filename="output/iris_rfc_model.pkl")

