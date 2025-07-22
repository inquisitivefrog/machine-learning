#!/bin/bash
set -x

# Check if port 5000 is in use
if lsof -i :5000 > /dev/null; then
    echo "Error: Port 5000 is already in use. Please free the port and try again."
    exit 1
fi

# Copy the latest timestamped Random Forest model
latest_model=$(ls -t output/breast_cancer_rf_model_*.pkl | grep -v latest | head -n 1)
if [ -z "$latest_model" ]; then
    echo "Error: No Random Forest model found in output/"
    exit 1
fi
cp "$latest_model" output/breast_cancer_rf_model_latest.pkl

# Start the Flask API
python3 breast_cancer.api.py > output/breast_cancer_api_startup.log 2>&1 &
API_PID=$!
sleep 10

# Check if the server is running
if ! ps -p $API_PID > /dev/null; then
    echo "Error: Flask server failed to start. Check output/breast_cancer_api_startup.log for details."
    cat output/breast_cancer_api_startup.log
    exit 1
fi

# Check server health
HOST=localhost
PORT=5000
if ! curl -s -o /dev/null -w "%{http_code}" http://$HOST:$PORT/health | grep -q 200; then
    echo "Error: Server health check failed. Check output/breast_cancer_api_startup.log for details."
    cat output/breast_cancer_api_startup.log
    kill -SIGTERM $API_PID
    wait $API_PID
    exit 1
fi

# Test the API with a sample input (30 features from breast cancer dataset)
HEADER="Content-Type: application/json"
DATA='{"features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]}'
for attempt in {1..3}; do
    echo "Attempt $attempt to send prediction request"
    if curl -X POST -H "$HEADER" -d "$DATA" http://$HOST:$PORT/predict; then
        break
    else
        echo "Prediction request failed, retrying..."
        sleep 2
    fi
done

# Gracefully shut down the Flask server
kill -SIGTERM $API_PID
wait $API_PID
