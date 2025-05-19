#!/bin/bash

# Verify AWS resource cleanup
# Usage: ./verify_cleanup.sh [region]
# Default region: us-east-1

REGION=${1:-us-east-1}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="./backups/logs/$TIMESTAMP.log"

# Ensure jq is installed
if ! command -v jq >/dev/null; then
    echo "Error: jq is required. Install with 'brew install jq'." | tee -a "$LOG_FILE"
    exit 1
fi

# Create log directory
mkdir -p "./backups/logs"
echo "[$TIMESTAMP] Starting verification for region $REGION" | tee -a "$LOG_FILE"

# Function to check if S3 bucket exists
s3_bucket_exists() {
    local bucket=$1
    aws s3 ls "s3://$bucket" --region "$REGION" >/dev/null 2>&1
    return $?
}

# Check Braket Quantum Tasks
echo "Checking Braket quantum tasks..." | tee -a "$LOG_FILE"
TASK_STATUSES=""
for status in QUEUED RUNNING COMPLETED FAILED CANCELLED; do
    TASKS=$(aws braket search-quantum-tasks --filters "[{\"name\":\"status\",\"operator\":\"EQUAL\",\"values\":[\"$status\"]}]" --region "$REGION" --query "quantumTasks[].quantumTaskArn" --output text 2>>"$LOG_FILE")
    if [ -n "$TASKS" ]; then
        TASK_STATUSES="$TASK_STATUSES $TASKS"
    fi
done
if [ -n "$TASK_STATUSES" ]; then
    echo "Found quantum tasks: $TASK_STATUSES" | tee -a "$LOG_FILE"
else
    echo "No quantum tasks found" | tee -a "$LOG_FILE"
fi

# Check Braket Hybrid Jobs
echo "Checking Braket hybrid jobs..." | tee -a "$LOG_FILE"
JOBS=""
if [ -f "./scripts/search_jobs_by_filter.py" ]; then
    JOB_ARNS=$(python3 ./scripts/search_jobs_by_filter.py 2>>"$LOG_FILE" | jq -r '.[]?.jobArn' 2>/dev/null)
    if [ -n "$JOB_ARNS" ]; then
        JOBS="$JOBS $JOB_ARNS"
    fi
fi
HYBRID_BUCKET="amazon-braket-us-east-1-084375569056"
if s3_bucket_exists "$HYBRID_BUCKET"; then
    JOB_FOLDERS=$(aws s3 ls "s3://$HYBRID_BUCKET/jobs/" --region "$REGION" 2>>"$LOG_FILE" | awk '{print $2}')
    if [ -n "$JOB_FOLDERS" ]; then
        JOBS="$JOBS (S3 folders: $JOB_FOLDERS)"
    fi
fi
if [ -n "$JOBS" ]; then
    echo "Found hybrid jobs: $JOBS" | tee -a "$LOG_FILE"
else
    echo "No hybrid jobs found" | tee -a "$LOG_FILE"
fi

# Check Braket S3 Buckets
echo "Checking Braket S3 buckets..." | tee -a "$LOG_FILE"
QUANTUM_BUCKET="amazon-braket-my-quantum-output-20250514-kerstarsoc"
if s3_bucket_exists "$QUANTUM_BUCKET"; then
    echo "Quantum task bucket s3://$QUANTUM_BUCKET exists" | tee -a "$LOG_FILE"
else
    echo "Quantum task bucket s3://$QUANTUM_BUCKET not found" | tee -a "$LOG_FILE"
fi
if s3_bucket_exists "$HYBRID_BUCKET"; then
    echo "Hybrid job bucket s3://$HYBRID_BUCKET exists" | tee -a "$LOG_FILE"
else
    echo "Hybrid job bucket s3://$HYBRID_BUCKET not found" | tee -a "$LOG_FILE"
fi

# Check SageMaker Resources
echo "Checking SageMaker domains..." | tee -a "$LOG_FILE"
DOMAINS=$(aws sagemaker list-domains --region "$REGION" --query "Domains[].{DomainId:DomainId,DomainName:DomainName}" --output text 2>>"$LOG_FILE")
if [ -n "$DOMAINS" ]; then
    echo "Found domains: $DOMAINS" | tee -a "$LOG_FILE"
else
    echo "No domains found" | tee -a "$LOG_FILE"
fi

echo "Checking SageMaker user profiles..." | tee -a "$LOG_FILE"
USER_PROFILES=$(aws sagemaker list-user-profiles --region "$REGION" --query "UserProfiles[].{UserProfileName:UserProfileName,DomainId:DomainId}" --output text 2>>"$LOG_FILE")
if [ -n "$USER_PROFILES" ]; then
    echo "Found user profiles: $USER_PROFILES" | tee -a "$LOG_FILE"
else
    echo "No user profiles found" | tee -a "$LOG_FILE"
fi

echo "Checking SageMaker apps..." | tee -a "$LOG_FILE"
for domain_id in $(echo "$DOMAINS" | awk '{print $1}' 2>/dev/null); do
    APPS=$(aws sagemaker list-apps --domain-id "$domain_id" --region "$REGION" --query "Apps[?Status!='Deleted'].{AppName:AppName,AppType:AppType,Status:Status}" --output text 2>>"$LOG_FILE")
    if [ -n "$APPS" ]; then
        echo "Found apps in domain $domain_id: $APPS" | tee -a "$LOG_FILE"
    else
        echo "No active apps in domain $domain_id" | tee -a "$LOG_FILE"
    fi
done

echo "Checking SageMaker notebook instances..." | tee -a "$LOG_FILE"
NOTEBOOKS=$(aws sagemaker list-notebook-instances --region "$REGION" --query "NotebookInstances[].NotebookInstanceName" --output text 2>>"$LOG_FILE")
if [ -n "$NOTEBOOKS" ]; then
    echo "Found notebook instances: $NOTEBOOKS" | tee -a "$LOG_FILE"
else
    echo "No notebook instances found" | tee -a "$LOG_FILE"
fi

echo "Checking SageMaker models..." | tee -a "$LOG_FILE"
MODELS=$(aws sagemaker list-models --region "$REGION" --query "Models[].ModelName" --output text 2>>"$LOG_FILE")
if [ -n "$MODELS" ]; then
    echo "Found models: $MODELS" | tee -a "$LOG_FILE"
else
    echo "No models found" | tee -a "$LOG_FILE"
fi

echo "Checking SageMaker endpoints..." | tee -a "$LOG_FILE"
ENDPOINTS=$(aws sagemaker list-endpoints --region "$REGION" --query "Endpoints[].EndpointName" --output text 2>>"$LOG_FILE")
if [ -n "$ENDPOINTS" ]; then
    echo "Found endpoints: $ENDPOINTS" | tee -a "$LOG_FILE"
else
    echo "No endpoints found" | tee -a "$LOG_FILE"
fi

echo "Checking SageMaker S3 bucket..." | tee -a "$LOG_FILE"
SAGEMAKER_BUCKET="sagemaker-us-east-1-084375569056"
if s3_bucket_exists "$SAGEMAKER_BUCKET"; then
    echo "SageMaker bucket s3://$SAGEMAKER_BUCKET exists" | tee -a "$LOG_FILE"
else
    echo "SageMaker bucket s3://$SAGEMAKER_BUCKET not found" | tee -a "$LOG_FILE"
fi

# Check EFS File Systems
echo "Checking EFS file systems..." | tee -a "$LOG_FILE"
EFS_SYSTEMS=$(aws efs describe-file-systems --region "$REGION" --query "FileSystems[].{FileSystemId:FileSystemId,Tags:Tags}" --output text 2>>"$LOG_FILE")
if [ -n "$EFS_SYSTEMS" ]; then
    echo "Found EFS file systems: $EFS_SYSTEMS" | tee -a "$LOG_FILE"
else
    echo "No EFS file systems found" | tee -a "$LOG_FILE"
fi

# Check EC2 and Networking
echo "Checking EC2 instances..." | tee -a "$LOG_FILE"
INSTANCE_IDS=$(aws ec2 describe-instances --filters "Name=instance-state-name,Values=running,pending" --region "$REGION" --query "Reservations[].Instances[].{InstanceId:InstanceId,Tags:Tags}" --output text 2>>"$LOG_FILE")
if [ -n "$INSTANCE_IDS" ]; then
    echo "Found running EC2 instances: $INSTANCE_IDS" | tee -a "$LOG_FILE"
else
    echo "No running EC2 instances found" | tee -a "$LOG_FILE"
fi

echo "Checking all VPCs..." | tee -a "$LOG_FILE"
VPCS=$(aws ec2 describe-vpcs --region "$REGION" --query "Vpcs[].{VpcId:VpcId,IsDefault:IsDefault,Tags:Tags}" --output text 2>>"$LOG_FILE")
if [ -n "$VPCS" ]; then
    echo "Found VPCs: $VPCS" | tee -a "$LOG_FILE"
else
    echo "No VPCs found" | tee -a "$LOG_FILE"
fi

echo "Checking subnets..." | tee -a "$LOG_FILE"
SUBNETS=$(aws ec2 describe-subnets --region "$REGION" --query "Subnets[].{SubnetId:SubnetId,VpcId:VpcId,Tags:Tags}" --output text 2>>"$LOG_FILE")
if [ -n "$SUBNETS" ]; then
    echo "Found subnets: $SUBNETS" | tee -a "$LOG_FILE"
else
    echo "No subnets found" | tee -a "$LOG_FILE"
fi

echo "Checking internet gateways..." | tee -a "$LOG_FILE"
IGWS=$(aws ec2 describe-internet-gateways --region "$REGION" --query "InternetGateways[].{InternetGatewayId:InternetGatewayId,Attachments:Attachments}" --output text 2>>"$LOG_FILE")
if [ -n "$IGWS" ]; then
    echo "Found internet gateways: $IGWS" | tee -a "$LOG_FILE"
else
    echo "No internet gateways found" | tee -a "$LOG_FILE"
fi

echo "Checking NAT gateways..." | tee -a "$LOG_FILE"
NAT_GWS=$(aws ec2 describe-nat-gateways --region "$REGION" --query "NatGateways[].{NatGatewayId:NatGatewayId,VpcId:VpcId}" --output text 2>>"$LOG_FILE")
if [ -n "$NAT_GWS" ]; then
    echo "Found NAT gateways: $NAT_GWS" | tee -a "$LOG_FILE"
else
    echo "No NAT gateways found" | tee -a "$LOG_FILE"
fi

echo "Checking security groups..." | tee -a "$LOG_FILE"
SGS=$(aws ec2 describe-security-groups --region "$REGION" --query "SecurityGroups[].{GroupId:GroupId,GroupName:GroupName,VpcId:VpcId,Tags:Tags}" --output text 2>>"$LOG_FILE")
if [ -n "$SGS" ]; then
    echo "Found security groups: $SGS" | tee -a "$LOG_FILE"
else
    echo "No security groups found" | tee -a "$LOG_FILE"
fi

echo "[$TIMESTAMP] Verification completed. Check $LOG_FILE for details" | tee -a "$LOG_FILE"
