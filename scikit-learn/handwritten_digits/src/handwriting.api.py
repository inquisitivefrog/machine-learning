#!/usr/bin/env python3
# Handwritten Digits Prediction API: Serve predictions using Random Forest model
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

import logging
import joblib
import numpy as np
from flask import Flask, request, jsonify

# Set joblib to use threading backend to avoid multiprocessing issues
joblib.parallel_backend('threading')

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/handwriting_api.log"),
        logging.StreamHandler()
    ]
)

# Load the latest saved Random Forest model and scaler
try:
    logging.info("Attempting to load model and scaler")
    model = joblib.load("output/handwriting_rf_model_latest.pkl")
    scaler = joblib.load("output/scaler.pkl")
    logging.info("Random Forest model and scaler loaded successfully")
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")
    model, scaler = None, None

@app.route('/health', methods=['GET'])
def health():
    """Check if the server is running."""
    logging.info("Health check requested")
    return jsonify({"status": "healthy", "model_loaded": model is not None, "scaler_loaded": scaler is not None}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Predict handwritten digit class for new image data."""
    logging.info("Prediction request received")
    if model is None or scaler is None:
        logging.error("Model or scaler not loaded")
        return jsonify({"error": "Model or scaler not loaded"}), 500

    try:
        data = request.get_json()
        if not data or 'features' not in data:
            logging.error("Invalid input: 'features' key missing")
            return jsonify({"error": "Invalid input: 'features' key required"}), 400

        # Expect 64 features (8x8 pixel values)
        features = np.array(data['features'], dtype=float).reshape(1, -1)
        if features.shape[1] != 64:
            logging.error(f"Invalid feature count: expected 64, got {features.shape[1]}")
            return jsonify({"error": f"Expected 64 features, got {features.shape[1]}"}), 400

        # Validate pixel values (0–16 range typical for digits dataset)
        if np.any(features < 0) or np.any(features > 16):
            logging.error("Pixel values out of expected range (0–16)")
            return jsonify({"error": "Pixel values must be in range 0–16"}), 400

        # Apply scaling
        logging.info("Applying scaler to features")
        features_scaled = scaler.transform(features)

        # Predict class and probability
        logging.info("Making prediction")
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0].tolist()
        logging.info(f"Predicted digit: {prediction}, Probabilities: {probabilities}")

        return jsonify({
            "prediction": int(prediction),
            "probabilities": [round(p, 4) for p in probabilities]
        })
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        logging.info("Starting Flask server")
        app.run(debug=True, host="0.0.0.0", port=5000)
        logging.info("Flask server started successfully")
    except Exception as e:
        logging.error(f"Error starting Flask server: {e}")
