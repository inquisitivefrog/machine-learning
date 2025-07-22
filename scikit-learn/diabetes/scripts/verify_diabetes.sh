#!/bin/bash
#set -x
#latest_model=$(ls -t ../output/diabetes_gb_model_*.pkl | head -n 1)
#cp "$latest_model" ./diabetes_gb_model_latest.pkl
#python3 diabetes.api.py &
#sleep 5

HOST=localhost
PORT=5000
HEADER="Content-Type: application/json"
DATA='{"features": [0.01, -0.04, 0.05, 0.02, -0.03, -0.02, -0.01, 0.0, 0.04, 0.01]}'
curl -X POST -H "$HEADER" -d "$DATA" http://$HOST:$PORT/predict
#kill %1
