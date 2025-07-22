#!/bin/bash
set -x

# Check if port 5000 is in use
if lsof -i :5000 > /dev/null; then
    echo "Error: Port 5000 is already in use. Please free the port and try again."
    exit 1
fi

# Copy the latest timestamped Random Forest model
latest_model=$(ls -t output/handwriting_rf_model_*.pkl | grep -v latest | head -n 1)
if [ -z "$latest_model" ]; then
    echo "Error: No Random Forest model found in output/"
    exit 1
fi
cp "$latest_model" output/handwriting_rf_model_latest.pkl

# Start the Flask API
python3 handwriting.api.py > output/handwriting_api_startup.log 2>&1 &
API_PID=$!
sleep 10

# Check if the server is running
if ! ps -p $API_PID > /dev/null; then
    echo "Error: Flask server failed to start. Check output/handwriting_api_startup.log for details."
    cat output/handwriting_api_startup.log
    exit 1
fi

# Check server health
HOST=localhost
PORT=5000
if ! curl -s -o /dev/null -w "%{http_code}" http://$HOST:$PORT/health | grep -q 200; then
    echo "Error: Server health check failed. Check output/handwriting_api_startup.log for details."
    cat output/handwriting_api_startup.log
    kill -SIGTERM $API_PID
    wait $API_PID
    exit 1
fi

# Test the API with a sample input (64 features from digits dataset, digit 0)
HEADER="Content-Type: application/json"
DATA='{"features": [0, 0, 5, 13, 9, 1, 0, 0, 0, 0, 13, 15, 10, 15, 5, 0, 0, 3, 15, 2, 0, 11, 8, 0, 0, 4, 12, 0, 0, 8, 8, 0, 0, 5, 8, 0, 0, 9, 8, 0, 0, 4, 11, 0, 1, 12, 7, 0, 0, 2, 14, 5, 10, 12, 0, 0, 0, 0, 6, 13, 10, 0, 0, 0]}'
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
