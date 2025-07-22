# Handwriting ML Project

Predicts handwritten digits (0–9) using scikit-learn's `load_digits` dataset (1797 samples, 8x8 images, 64 features). This project serves as a reference for applying scikit-learn models to multi-class classification tasks, with comprehensive tests and documentation for supporting ML applications.

## Models

The project evaluates multiple classification models, with performance metrics (accuracy, precision, recall, F1-score) on the test set (360 samples). All models use scaled features unless specified. Hyperparameters are tuned to minimize overfitting.

- **MLPClassifier (MLP)**: Accuracy=0.9778 (training ~1.00, tests ~0.85–0.90)
  - Best performer, neural network (`hidden_layer_sizes=(20,)`, `alpha=0.05`, `max_iter=1000`), requires scaling. Lower test accuracy due to small training set (200 samples).
- **K-Nearest Neighbors (KNN)**: Accuracy=0.9694
  - Distance-based (`n_neighbors=3`), requires scaling.
- **Logistic Regression (LR)**: Accuracy=0.9639
  - Linear model (`C=0.1`), requires scaling.
- **Gradient Boosting (GB)**: Accuracy=0.9583
  - Sequential ensemble (`n_estimators=100`, `learning_rate=0.05`, `max_depth=3`), no scaling required.
- **XGBoost (XGB)**: Accuracy=0.9556
  - Gradient boosting (`n_estimators=50`, `max_depth=3`, `learning_rate=0.1`), no scaling required.
- **Support Vector Classifier (SVC)**: Accuracy=0.9472
  - RBF kernel (`C=0.1`), requires scaling.
- **Random Forest (RF)**: Accuracy=0.9444
  - Robust ensemble (`max_depth=5`), no scaling required.
- **Random Forest with PCA (RF PCA)**: Accuracy=0.9278
  - RF (`max_depth=5`) with PCA (30 components).

## Features

- **Base Features**: 64 (flattened 8x8 pixel intensities, labeled `pixel_0` to `pixel_63`).
- **Scaling**: Applied via `StandardScaler` (critical for KNN, SVC, LR, MLP; optional for RF, GB, XGB).
- **Dimensionality Reduction**: PCA (30 components, ~90% variance explained) for `RF PCA`.

## Methods

- **Hyperparameter Tuning**: `GridSearchCV` with constrained parameter grids to reduce overfitting (e.g., `max_depth=5` for RF, `C=0.1` for SVC/LR, `alpha=0.05` for MLP, `learning_rate=0.05` for GB, `learning_rate=0.1` for XGB).
- **Dimensionality Reduction**: Principal Component Analysis (PCA) for `RF PCA`.
- **Evaluation Metrics**: Accuracy, confusion matrix, precision/recall/F1-score, saved to `output/model_metrics.csv`.
- **Cross-Validation**: 5-fold CV for training, 3-fold CV in tests for efficiency.
- **Visualizations**: Confusion matrix heatmaps, feature importance plots (for RF, GB, XGB).

## Desired Range

Predicted digits range from **0 to 9**. Predictions outside this range indicate errors.

## Runtime

- **Training (`handwriting.py`)**: ~65–70 seconds for all models (RF, GB, KNN, SVC, LR, MLP, XGB, RF PCA) on a 16GB MacBook Pro (2017, Quad-Core Intel Core i7, 2.9 GHz). Can be optimized to ~50–55 seconds by reducing GB’s `n_estimators` to 75.
- **Testing (`test_handwriting.py`)**: ~24–27 seconds with 200-sample training sets and 32 tests.
- **Memory Management**: Garbage collection (`gc.collect()`), explicit object deletion, and `psutil` monitoring (peak ~180 MB).

## Usage

1. **Train and Save Models**:
   ```bash
   python3 handwriting.py
