#!/bin/bash
# cleanup_aws_resources.sh
# Cleans up AWS resources for a SageMaker environment
# Handles: SageMaker → EFS → VPC (ENIs, endpoints, SGs, subnets, route tables) → S3 → IAM → KMS → DynamoDB → Terraform State
# Usage: ./cleanup_aws_resources.sh [--region REGION] [--vpc-name VPC_NAME] [--s3-bucket S3_BUCKET] [--dry-run]
# Example: ./cleanup_aws_resources.sh --region us-east-1 --vpc-name imaginary-org-vpc --s3-bucket sagemaker-customer-churn-20250603

set -euo pipefail

# Defaults
REGION="us-east-1"
VPC_NAME="imaginary-org-vpc"
S3_BUCKET="sagemaker-customer-churn-20250603"
IAM_ROLE="SageMakerExecutionRole"
DYNAMODB_TABLE="terraform-locks"
LOG_FILE="cleanup_aws_resources_$(date +%Y%m%d_%H%M%S).log"
DRY_RUN=false

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --region) REGION="$2"; shift 2 ;;
    --vpc-name) VPC_NAME="$2"; shift 2 ;;
    --s3-bucket) S3_BUCKET="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# Logging function
log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Check if resource exists
resource_exists() {
  local cmd="$1"
  eval "$cmd" >/dev/null 2>&1
}

# Execute AWS CLI command
execute_aws() {
  local cmd="$1"
  local max_attempts=${2:-1}
  local attempt=1
  if [ "$DRY_RUN" = true ]; then
    log "Dry-run: Would execute: $cmd"
    return 0
  fi
  while [ $attempt -le $max_attempts ]; do
    log "Executing (attempt $attempt/$max_attempts): $cmd"
    if eval "$cmd" 2>&1 | tee -a "$LOG_FILE"; then
      return 0
    else
      log "Warning: Command failed (attempt $attempt/$max_attempts)"
      if [ $attempt -eq $max_attempts ]; then
        return 1
      fi
      sleep 10
      attempt=$((attempt + 1))
    fi
  done
}

# Wait for resource deletion with timeout
wait_for_deletion() {
  local check_cmd="$1"
  local resource_name="$2"
  local timeout=$3
  local interval=10
  local elapsed=0
  while resource_exists "$check_cmd" && [ $elapsed -lt $timeout ]; do
    log "Waiting for $resource_name to delete ($elapsed/$timeout seconds)..."
    sleep $interval
    elapsed=$((elapsed + interval))
  done
  if resource_exists "$check_cmd"; then
    log "Error: $resource_name not deleted after $timeout seconds"
    return 1
  fi
}

log "Starting cleanup in region $REGION"

# Check AWS CLI credentials
if ! aws sts get-caller-identity >/dev/null 2>&1; then
  log "Error: AWS CLI not configured or credentials invalid"
  exit 1
fi

# Get VPC ID dynamically
VPC_ID=$(aws ec2 describe-vpcs --region "$REGION" --filters Name=tag:Name,Values="$VPC_NAME" --query 'Vpcs[0].VpcId' --output text 2>/dev/null)
if [ -z "$VPC_ID" ] || [ "$VPC_ID" = "None" ]; then
  log "Warning: No VPC found with tag Name=$VPC_NAME"
else
  log "Found VPC: $VPC_ID"
fi

# Delete SageMaker Resources
log "Checking SageMaker domains..."
DOMAIN_IDS=$(aws sagemaker list-domains --region "$REGION" --query 'Domains[].DomainId' --output text || echo "")
for DOMAIN_ID in $DOMAIN_IDS; do
  log "Processing domain $DOMAIN_ID"
  APPS=$(aws sagemaker list-apps --domain-id "$DOMAIN_ID" --region "$REGION" --query 'Apps[].[AppName,AppType]' --output text || echo "")
  while read -r APP_NAME APP_TYPE; do
    if [ -n "$APP_NAME" ]; then
      execute_aws "aws sagemaker delete-app --domain-id '$DOMAIN_ID' --app-name '$APP_NAME' --app-type '$APP_TYPE' --region '$REGION'" 3
    fi
  done <<< "$APPS"
  USER_PROFILES=$(aws sagemaker list-user-profiles --domain-id "$DOMAIN_ID" --region "$REGION" --query 'UserProfiles[].UserProfileName' --output text || echo "")
  for USER_PROFILE in $USER_PROFILES; do
    execute_aws "aws sagemaker delete-user-profile --domain-id '$DOMAIN_ID' --user-profile-name '$USER_PROFILE' --region '$REGION'" 3
  done
  SPACES=$(aws sagemaker list-spaces --domain-id "$DOMAIN_ID" --region "$REGION" --query 'Spaces[].SpaceName' --output text || echo "")
  for SPACE in $SPACES; do
    execute_aws "aws sagemaker delete-space --domain-id '$DOMAIN_ID' --space-name '$SPACE' --region '$REGION'" 3
  done
  execute_aws "aws sagemaker delete-domain --domain-id '$DOMAIN_ID' --region '$REGION'" 3
  wait_for_deletion "aws sagemaker describe-domain --domain-id '$DOMAIN_ID' --region '$REGION'" "SageMaker domain $DOMAIN_ID" 180
done

# Delete EFS File Systems
log "Checking EFS file systems..."
EFS_IDS=$(aws efs describe-file-systems --region "$REGION" --query 'FileSystems[].FileSystemId' --output text || echo "")
for EFS_ID in $EFS_IDS; do
  log "Processing EFS $EFS_ID"
  MOUNT_TARGETS=$(aws efs describe-mount-targets --file-system-id "$EFS_ID" --region "$REGION" --query 'MountTargets[].MountTargetId' --output text || echo "")
  for MT_ID in $MOUNT_TARGETS; do
    execute_aws "aws efs delete-mount-target --mount-target-id '$MT_ID' --region '$REGION'" 3
  done
  wait_for_deletion "aws efs describe-mount-targets --file-system-id '$EFS_ID' --region '$REGION'" "EFS mount targets for $EFS_ID" 120
  execute_aws "aws efs delete-file-system --file-system-id '$EFS_ID' --region '$REGION'" 3
  wait_for_deletion "aws efs describe-file-systems --file-system-id '$EFS_ID' --region '$REGION'" "EFS $EFS_ID" 60
done

# Delete VPC Resources (if VPC_ID exists)
if [ -n "$VPC_ID" ]; then
  # Delete ENIs with retries
  log "Checking ENIs..."
  ENI_IDS=$(aws ec2 describe-network-interfaces --filters "Name=vpc-id,Values=$VPC_ID" --region "$REGION" --query 'NetworkInterfaces[].NetworkInterfaceId' --output text || echo "")
  for ENI in $ENI_IDS; do
    ATTACHMENT=$(aws ec2 describe-network-interfaces --network-interface-ids "$ENI" --region "$REGION" --query 'NetworkInterfaces[0].Attachment.AttachmentId' --output text || echo "")
    if [ -n "$ATTACHMENT" ] && [ "$ATTACHMENT" != "None" ]; then
      execute_aws "aws ec2 detach-network-interface --attachment-id '$ATTACHMENT' --region '$REGION' --force" 3
      wait_for_deletion "aws ec2 describe-network-interfaces --network-interface-ids '$ENI' --region '$REGION' --query 'NetworkInterfaces[0].Attachment.AttachmentId'" "ENI attachment for $ENI" 120
    fi
    execute_aws "aws ec2 delete-network-interface --network-interface-id '$ENI' --region '$REGION'" 5
  done
  wait_for_deletion "aws ec2 describe-network-interfaces --filters 'Name=vpc-id,Values=$VPC_ID' --region '$REGION'" "ENIs for $VPC_ID" 180

  # Delete VPC Endpoints
  log "Checking VPC endpoints..."
  VPCE_IDS=$(aws ec2 describe-vpc-endpoints --filters "Name=vpc-id,Values=$VPC_ID" --region "$REGION" --query 'VpcEndpoints[].VpcEndpointId' --output text || echo "")
  for VPCE_ID in $VPCE_IDS; do
    execute_aws "aws ec2 delete-vpc-endpoints --vpc-endpoint-ids '$VPCE_ID' --region '$REGION'" 3
  done
  wait_for_deletion "aws ec2 describe-vpc-endpoints --filters 'Name=vpc-id,Values=$VPC_ID' --region '$REGION'" "VPC endpoints for $VPC_ID" 180

  # Delete Security Groups
  log "Checking security groups..."
  SG_IDS=$(aws ec2 describe-security-groups --filters "Name=vpc-id,Values=$VPC_ID" --region "$REGION" --query 'SecurityGroups[].GroupId' --output text || echo "")
  for SG in $SG_IDS; do
    INGRESS_RULES=$(aws ec2 describe-security-group-rules --filters "Name=group-id,Values=$SG" --query 'SecurityGroupRules[?IsEgress==`false`].SecurityGroupRuleId' --output text --region "$REGION" || echo "")
    if [ -n "$INGRESS_RULES" ]; then
      execute_aws "aws ec2 revoke-security-group-ingress --group-id '$SG' --security-group-rule-ids $INGRESS_RULES --region '$REGION'" 3
    fi
    EGRESS_RULES=$(aws ec2 describe-security-group-rules --filters "Name=group-id,Values=$SG" --query 'SecurityGroupRules[?IsEgress==`true`].SecurityGroupRuleId' --output text --region "$REGION" || echo "")
    if [ -n "$EGRESS_RULES" ]; then
      execute_aws "aws ec2 revoke-security-group-egress --group-id '$SG' --security-group-rule-ids $EGRESS_RULES --region '$REGION'" 3
    fi
    execute_aws "aws ec2 delete-security-group --group-id '$SG' --region '$REGION'" 3
  done

  # Delete Subnets
  log "Checking subnets..."
  SUBNET_IDS=$(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$VPC_ID" --region "$REGION" --query 'Subnets[].SubnetId' --output text || echo "")
  for SUBNET in $SUBNET_IDS; do
    execute_aws "aws ec2 delete-subnet --subnet-id '$SUBNET' --region '$REGION'" 3
  done

  # Delete Route Tables
  log "Checking route tables..."
  ROUTE_TABLE_IDS=$(aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$VPC_ID" --region "$REGION" --query 'RouteTables[].RouteTableId' --output text || echo "")
  for RT in $ROUTE_TABLE_IDS; do
    ASSOCIATIONS=$(aws ec2 describe-route-tables --route-table-ids "$RT" --region "$REGION" --query 'RouteTables[].Associations[].RouteTableAssociationId' --output text || echo "")
    for ASSOC in $ASSOCIATIONS; do
      if [ -n "$ASSOC" ] && [ "$ASSOC" != "Main" ]; then
        execute_aws "aws ec2 disassociate-route-table --association-id '$ASSOC' --region '$REGION'" 3
      fi
    done
    execute_aws "aws ec2 delete-route-table --route-table-id '$RT' --region '$REGION'" 3
  done

  # Delete VPC
  log "Deleting VPC $VPC_ID..."
  execute_aws "aws ec2 delete-vpc --vpc-id '$VPC_ID' --region '$REGION'" 3
fi

# Delete S3 Bucket
log "Checking S3 bucket $S3_BUCKET..."
if resource_exists "aws s3 ls s3://'$S3_BUCKET'"; then
  execute_aws "aws s3 rb s3://'$S3_BUCKET' --force --region '$REGION'" 3
fi

# Delete IAM Role
log "Checking IAM role $IAM_ROLE..."
if resource_exists "aws iam get-role --role-name '$IAM_ROLE'"; then
  POLICIES=$(aws iam list-role-policies --role-name "$IAM_ROLE" --query 'PolicyNames[]' --output text || echo "")
  for POLICY in $POLICIES; do
    execute_aws "aws iam delete-role-policy --role-name '$IAM_ROLE' --policy-name '$POLICY'" 3
  done
  ATTACHED_POLICIES=$(aws iam list-attached-role-policies --role-name "$IAM_ROLE" --query 'AttachedPolicies[].PolicyArn' --output text || echo "")
  for POLICY_ARN in $ATTACHED_POLICIES; do
    execute_aws "aws iam detach-role-policy --role-name '$IAM_ROLE' --policy-arn '$POLICY_ARN'" 3
  done
  execute_aws "aws iam delete-role --role-name '$IAM_ROLE'" 3
fi

# Delete KMS Keys
log "Checking KMS keys..."
KEY_IDS=$(aws kms list-keys --region "$REGION" --query 'Keys[].KeyId' --output text || echo "")
for KEY in $KEY_IDS; do
  if resource_exists "aws kms describe-key --key-id '$KEY' --region '$REGION'"; then
    KEY_STATE=$(aws kms describe-key --key-id "$KEY" --region "$REGION" --query 'KeyMetadata.KeyState' --output text || echo "NotFound")
    if [ "$KEY_STATE" != "PendingDeletion" ] && [ "$KEY_STATE" != "NotFound" ]; then
      execute_aws "aws kms schedule-key-deletion --key-id '$KEY' --pending-window-in-days 7 --region '$REGION'" 3
    else
      log "KMS key $KEY is $KEY_STATE"
    fi
  fi
done

# Delete DynamoDB Table
log "Checking DynamoDB table $DYNAMODB_TABLE..."
if resource_exists "aws dynamodb describe-table --table-name '$DYNAMODB_TABLE' --region '$REGION'"; then
  execute_aws "aws dynamodb delete-table --table-name '$DYNAMODB_TABLE' --region '$REGION'" 3
  wait_for_deletion "aws dynamodb describe-table --table-name '$DYNAMODB_TABLE' --region '$REGION'" "DynamoDB table $DYNAMODB_TABLE" 60
fi

# Clear Terraform State
log "Clearing Terraform state..."
STATE_RESOURCES=$(terraform state list 2>/dev/null || echo "")
if [ -n "$STATE_RESOURCES" ]; then
  for RESOURCE in $STATE_RESOURCES; do
    execute_aws "terraform state rm -lock=false '$RESOURCE'" 3
  done
else
  log "No resources found in Terraform state"
fi

log "Cleanup completed"
