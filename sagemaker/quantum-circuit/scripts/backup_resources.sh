#!/bin/bash

# Backup AWS resources to ./backups/
# Usage: ./backup_resources.sh [region]
# Default region: us-east-1

REGION=${1:-us-east-1}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="./backups/$TIMESTAMP"
LOG_FILE="./backups/logs/$TIMESTAMP.log"

# Ensure jq is installed
if ! command -v jq >/dev/null; then
    echo "Error: jq is required. Install with 'brew install jq'."
    exit 1
fi

# Create backup and log directories
mkdir -p "$BACKUP_DIR"/{quantum-tasks,hybrid-jobs,sagemaker} "$BACKUP_DIR"/logs
echo "[$TIMESTAMP] Starting backup for region $REGION" | tee -a "$LOG_FILE"

# Function to check if S3 bucket exists
s3_bucket_exists() {
    local bucket=$1
    aws s3 ls "s3://$bucket" --region "$REGION" >/dev/null 2>&1
    return $?
}

# Backup Braket Quantum Tasks
echo "Checking Braket quantum task S3 bucket..." | tee -a "$LOG_FILE"
QUANTUM_BUCKET="amazon-braket-my-quantum-output-20250514-kerstarsoc"
if s3_bucket_exists "$QUANTUM_BUCKET"; then
    echo "Backing up quantum tasks from s3://$QUANTUM_BUCKET/quantum-output/" | tee -a "$LOG_FILE"
    aws s3 cp "s3://$QUANTUM_BUCKET/quantum-output/" "$BACKUP_DIR/quantum-tasks/" --recursive --region "$REGION" >>"$LOG_FILE" 2>&1
else
    echo "Quantum task bucket s3://$QUANTUM_BUCKET not found" | tee -a "$LOG_FILE"
fi

# Backup Braket Hybrid Jobs
echo "Checking Braket hybrid job S3 bucket..." | tee -a "$LOG_FILE"
HYBRID_BUCKET="amazon-braket-us-east-1-084375569056"
if s3_bucket_exists "$HYBRID_BUCKET"; then
    echo "Listing hybrid job folders..." | tee -a "$LOG_FILE"
    JOB_FOLDERS=$(aws s3 ls "s3://$HYBRID_BUCKET/jobs/run-ghz-hybrid/" --region "$REGION" | awk '{print $2}')
    if [ -n "$JOB_FOLDERS" ]; then
        for folder in $JOB_FOLDERS; do
            folder_name=$(echo "$folder" | tr -d '/')
            echo "Backing up hybrid job s3://$HYBRID_BUCKET/jobs/run-ghz-hybrid/$folder_name/" | tee -a "$LOG_FILE"
            aws s3 cp "s3://$HYBRID_BUCKET/jobs/run-ghz-hybrid/$folder_name/" "$BACKUP_DIR/hybrid-jobs/$folder_name/" --recursive --region "$REGION" >>"$LOG_FILE" 2>&1
        done
    else
        echo "No hybrid job folders found in s3://$HYBRID_BUCKET/jobs/run-ghz-hybrid/" | tee -a "$LOG_FILE"
    fi
else
    echo "Hybrid job bucket s3://$HYBRID_BUCKET not found" | tee -a "$LOG_FILE"
fi

# Backup SageMaker Outputs
echo "Checking SageMaker S3 bucket..." | tee -a "$LOG_FILE"
SAGEMAKER_BUCKET="sagemaker-us-east-1-084375569056"
if s3_bucket_exists "$SAGEMAKER_BUCKET"; then
    echo "Backing up SageMaker outputs from s3://$SAGEMAKER_BUCKET/" | tee -a "$LOG_FILE"
    aws s3 cp "s3://$SAGEMAKER_BUCKET/" "$BACKUP_DIR/sagemaker/" --recursive --region "$REGION" >>"$LOG_FILE" 2>&1
else
    echo "SageMaker bucket s3://$SAGEMAKER_BUCKET not found" | tee -a "$LOG_FILE"
fi

echo "[$TIMESTAMP] Backup completed. Outputs saved to $BACKUP_DIR" | tee -a "$LOG_FILE"
