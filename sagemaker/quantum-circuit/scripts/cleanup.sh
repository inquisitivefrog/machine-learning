#!/bin/bash
set -x

# Clean up AWS resources
# Usage: ./cleanup.sh [region]
# Default region: us-east-1

REGION=${1:-us-east-1}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="./backups/logs/cleanup_$TIMESTAMP.log"

# Create log directory
mkdir -p "./backups/logs"
echo "[$TIMESTAMP] Starting cleanup for region $REGION" | tee -a "$LOG_FILE"

# Function to empty and delete S3 bucket
delete_s3_bucket() {
    local bucket=$1
    echo "Emptying and deleting bucket s3://$bucket..." | tee -a "$LOG_FILE"
    aws s3 rm "s3://$bucket" --recursive --region "$REGION" 2>/dev/null
    aws s3api delete-bucket --bucket "$bucket" --region "$REGION" 2>/dev/null && \
        echo "Deleted bucket s3://$bucket" | tee -a "$LOG_FILE" || \
        echo "Failed to delete bucket s3://$bucket" | tee -a "$LOG_FILE"
}

# Delete SageMaker Domain and Dependencies
echo "Deleting SageMaker domain and dependencies..." | tee -a "$LOG_FILE"
DOMAINS=$(aws sagemaker list-domains --region "$REGION" --query "Domains[].DomainId" --output text 2>/dev/null)
for domain_id in $DOMAINS; do
    # Delete spaces
    SPACES=$(aws sagemaker list-spaces --domain-id "$domain_id" --region "$REGION" --query "Spaces[].SpaceName" --output text 2>/dev/null)
    for space in $SPACES; do
        aws sagemaker delete-space --domain-id "$domain_id" --space-name "$space" --region "$REGION" 2>/dev/null && \
            echo "Deleted space $space in domain $domain_id" | tee -a "$LOG_FILE"
    done
    # Delete apps
    APPS=$(aws sagemaker list-apps --domain-id "$domain_id" --region "$REGION" --query "Apps[?Status!='Deleted'].{AppName:AppName,AppType:AppType}" --output text 2>/dev/null)
    for app in "$APPS"; do
        app_name=$(echo "$app" | awk '{print $1}')
        app_type=$(echo "$app" | awk '{print $2}')
        aws sagemaker delete-app --domain-id "$domain_id" --app-name "$app_name" --app-type "$app_type" --region "$REGION" 2>/dev/null && \
            echo "Deleted app $app_name ($app_type) in domain $domain_id" | tee -a "$LOG_FILE"
    done
    # Delete user profiles
    USER_PROFILES=$(aws sagemaker list-user-profiles --domain-id "$domain_id" --region "$REGION" --query "UserProfiles[].UserProfileName" --output text 2>/dev/null)
    for profile in $USER_PROFILES; do
        aws sagemaker delete-user-profile --domain-id "$domain_id" --user-profile-name "$profile" --region "$REGION" 2>/dev/null && \
            echo "Deleted user profile $profile in domain $domain_id" | tee -a "$LOG_FILE"
    done
    # Retry domain deletion
    for attempt in {1..3}; do
        aws sagemaker delete-domain --domain-id "$domain_id" --region "$REGION" 2>/dev/null && \
            echo "Deleted domain $domain_id" | tee -a "$LOG_FILE" && break
        echo "Retrying domain $domain_id deletion (attempt $attempt)..." | tee -a "$LOG_FILE"
        sleep 10
    done
done

# Delete S3 Buckets
echo "Deleting S3 buckets..." | tee -a "$LOG_FILE"
for bucket in amazon-braket-my-quantum-output-20250514-kerstarsoc amazon-braket-us-east-1-084375569056 sagemaker-us-east-1-084375569056; do
    if aws s3 ls "s3://$bucket" --region "$REGION" >/dev/null 2>&1; then
        delete_s3_bucket "$bucket"
    else
        echo "Bucket s3://$bucket does not exist" | tee -a "$LOG_FILE"
    fi
done

# Delete Networking Resources
echo "Deleting networking resources..." | tee -a "$LOG_FILE"
# Delete non-default security groups
SGS=$(aws ec2 describe-security-groups --region "$REGION" --query "SecurityGroups[?GroupName!='default'].GroupId" --output text 2>/dev/null)
for sg in $SGS; do
    aws ec2 delete-security-group --group-id "$sg" --region "$REGION" 2>/dev/null && \
        echo "Deleted security group $sg" | tee -a "$LOG_FILE" || \
        echo "Failed to delete security group $sg" | tee -a "$LOG_FILE"
done

# Delete internet gateways
IGWS=$(aws ec2 describe-internet-gateways --region "$REGION" --query "InternetGateways[].InternetGatewayId" --output text 2>/dev/null)
for igw in $IGWS; do
    VPC_ID=$(aws ec2 describe-internet-gateways --internet-gateway-ids "$igw" --region "$REGION" --query "InternetGateways[].Attachments[].VpcId" --output text 2>/dev/null)
    if [ -n "$VPC_ID" ]; then
        aws ec2 detach-internet-gateway --internet-gateway-id "$igw" --vpc-id "$VPC_ID" --region "$REGION" 2>/dev/null
    fi
    aws ec2 delete-internet-gateway --internet-gateway-id "$igw" --region "$REGION" 2>/dev/null && \
        echo "Deleted internet gateway $igw" | tee -a "$LOG_FILE" || \
        echo "Failed to delete internet gateway $igw" | tee -a "$LOG_FILE"
done

# Delete subnets
SUBNETS=$(aws ec2 describe-subnets --region "$REGION" --query "Subnets[].SubnetId" --output text 2>/dev/null)
for subnet in $SUBNETS; do
    aws ec2 delete-subnet --subnet-id "$subnet" --region "$REGION" 2>/dev/null && \
        echo "Deleted subnet $subnet" | tee -a "$LOG_FILE" || \
        echo "Failed to delete subnet $subnet" | tee -a "$LOG_FILE"
done

# Delete VPC (if non-default)
VPCS=$(aws ec2 describe-vpcs --region "$REGION" --query "Vpcs[?IsDefault==\`false\`].VpcId" --output text 2>/dev/null)
for vpc in $VPCS; do
    aws ec2 delete-vpc --vpc-id "$vpc" --region "$REGION" 2>/dev/null && \
        echo "Deleted VPC $vpc" | tee -a "$LOG_FILE" || \
        echo "Failed to delete VPC $vpc" | tee -a "$LOG_FILE"
done

echo "[$TIMESTAMP] Cleanup completed. Check $LOG_FILE for details" | tee -a "$LOG_FILE"
