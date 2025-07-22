#!/usr/bin/env python3

import logging
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/diabetes_api.log"),
        logging.StreamHandler()
    ]
)

# Load the latest saved model, polynomial transformer, and scaler
try:
    model = joblib.load("output/diabetes_gb_model_latest.pkl")
    poly = joblib.load("output/poly.pkl")
    scaler = joblib.load("output/scaler.pkl")
    logging.info("Model, polynomial transformer, and scaler loaded successfully")
except Exception as e:
    logging.error(f"Error loading model, poly, or scaler: {e}")
    model, poly, scaler = None, None, None

def transform_features(X, feature_names):
    """Apply feature transformations (log and bmi_bp_ratio) to original features."""
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
        return X_transformed, new_feature_names
    except Exception as e:
        logging.error(f"Error transforming features: {e}")
        return None, None

@app.route('/predict', methods=['POST'])
def predict():
    """Predict diabetes progression for new patient data."""
    if model is None or poly is None or scaler is None:
        logging.error("Model, poly, or scaler not loaded")
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json()
        if not data or 'features' not in data:
            logging.error("Invalid input: 'features' key missing")
            return jsonify({"error": "Invalid input: 'features' key required"}), 400

        # Expect 10 features: age, sex, bmi, bp, s1, s2, s3, s4, s5, s6
        features = np.array(data['features'], dtype=float).reshape(1, -1)
        if features.shape[1] != 10:
            logging.error(f"Invalid feature count: expected 10, got {features.shape[1]}")
            return jsonify({"error": f"Expected 10 features, got {features.shape[1]}"}), 400

        # Apply feature transformations
        feature_names = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
        patient_transformed, _ = transform_features(features, feature_names)
        if patient_transformed is None:
            logging.error("Feature transformation failed")
            return jsonify({"error": "Feature transformation failed"}), 500

        # Apply polynomial features and scaling
        patient_poly = poly.transform(patient_transformed)
        patient_scaled = scaler.transform(patient_poly)

        # Predict
        prediction = model.predict(patient_scaled)[0]
        logging.info(f"Predicted progression: {prediction:.2f}")

        # Validate prediction range
        if not (50 <= prediction <= 300):
            logging.warning(f"Prediction {prediction:.2f} outside desired range (50–300)")

        return jsonify({"prediction": round(float(prediction), 2)})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
