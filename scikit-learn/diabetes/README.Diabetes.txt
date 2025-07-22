
# Diabetes ML Project

Predicts diabetes progression using scikit-learn's dataset (200 samples). The target is a quantitative measure of disease progression one year after baseline. This project serves as a reference for applying various scikit-learn models to regression tasks, with comprehensive tests and documentation for supporting ML applications.

## Models

The project evaluates multiple regression models, with performance metrics (R², RMSE, MAE) on the test set (40 samples). All models use polynomial features (degree=3) unless specified.

- **Support Vector Regressor (SVR)**: R²=0.48, RMSE=53.69, MAE=41.78
  - Best performer, leveraging linear kernel with scaled polynomial features.
- **Stacking Regressor (RF+GB+XGB+Linear)**: R²=0.40, RMSE=57.77, MAE=46.19
  - Combines Random Forest, Gradient Boosting, and XGBoost with Linear Regression as meta-learner.
- **Random Forest (RF)**: R²=0.39, RMSE=58.32, MAE=46.75
  - Robust ensemble, no scaling required.
- **Random Forest with Feature Selection (RF Selected)**: R²=0.37, RMSE=59.29, MAE=47.56
  - Uses Recursive Feature Elimination (RFE) to select 10 features.
- **K-Nearest Neighbors (KNN)**: R²=0.36, RMSE=59.66, MAE=48.78
  - Distance-based, requires scaling.
- **Gradient Boosting (GB)**: R²=0.32, RMSE=61.22, MAE=48.20
  - Sequential ensemble, no scaling required.
- **XGBoost**: R²=0.30, RMSE=62.48, MAE=49.53
  - Optimized gradient boosting, no scaling required.
- **Gradient Boosting with Feature Selection (GB Selected)**: R²=0.21, RMSE=66.10, MAE=50.84
  - Uses RFE to select 10 features.
- **Random Forest with PCA (RF PCA)**: R²=0.18, RMSE=67.30, MAE=53.23
  - Uses PCA (10 components, 65% variance explained), reduced performance.
- **Decision Tree (DT)**: R²=-0.08, RMSE=77.27, MAE=61.70
  - Simple tree, prone to overfitting.
- **Linear Regression (LR)**: R²=-11.59, RMSE=264.24, MAE=185.52
  - Unsuitable due to high-dimensional polynomial features causing overfitting.

## Features

- **Base Features**: 11 (age, sex, bmi, bp, s1–s6, bmi_bp_ratio).
  - `bmi` and `s5` are log-transformed for stability.
  - `bmi_bp_ratio` is derived as `bmi / (bp + 1e-6)`.
- **Polynomial Features**: Degree=3, resulting in 363 features.
- **Scaling**: Applied via `StandardScaler` (critical for SVR, KNN, LR; optional for others).
- **Feature Selection**: RFE selects 10 features for `RF Selected` and `GB Selected`.
- **Dimensionality Reduction**: PCA (10 components) used for `RF PCA`.

## Methods

- **Hyperparameter Tuning**: `GridSearchCV` for most models, `RandomizedSearchCV` for XGBoost.
- **Feature Selection**: Recursive Feature Elimination (RFE) for `RF Selected` and `GB Selected`.
- **Dimensionality Reduction**: Principal Component Analysis (PCA) for `RF PCA`.
- **Evaluation Metrics**: Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), R² Score.
- **Cross-Validation**: 5-fold CV for robust performance estimates.
- **Visualizations**: Scatter plots, residual plots, feature importance plots (for tree-based models).

## Desired Range

Predicted progression typically ranges from **50 to 300**, based on the dataset’s target range (~25–346). Values <50 or >300 are rare and may indicate outliers or data issues. Tests in `test_diabetes.py` verify predictions fall within this range.

## Runtime

- **Training (`diabetes.py`)**: ~14.6 minutes (877 seconds) on a 16GB MacBook Pro (2017, Quad-Core Intel Core i7, 2.9 GHz).
- **Testing (`test_diabetes.py`)**: ~22 minutes (1320 seconds).
- **Memory Management**: Garbage collection (`gc.collect()`) after each model prevents swapping.

## Usage

1. **Train and Save Models**:
   ```bash
   python3 diabetes.py
2. **Functional Test Models**:
   ```bash
   python3 test_diabetes.py -v
3. **Performance Test Models**:
   ```bash
   MPROF_OUTPUT=output/knn_main_memory_profile.log python -m memory_profiler diabetes.py 
   MPROF_OUTPUT=output/knn_memory_profile.log pytest test_diabetes.py::test_evaluate_knn_model -v
