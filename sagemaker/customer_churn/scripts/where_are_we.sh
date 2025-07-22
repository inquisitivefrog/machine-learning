#!/bin/bash
# where_are_we.sh
# Diagnostic script for SageMaker infrastructure
# Usage: ./where_are_we.sh [--region REGION] [--vpc-name VPC_NAME]
# Example: ./where_are_we.sh --region us-east-1 --vpc-name imaginary-org-vpc

set -euo pipefail

DEFAULT_REGION="us-east-1"
DEFAULT_VPC_NAME="imaginary-org-vpc"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --region) REGION="$2"; shift 2 ;;
    --vpc-name) VPC_NAME="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

REGION="${REGION:-$DEFAULT_REGION}"
VPC_NAME="${VPC_NAME:-$DEFAULT_VPC_NAME}"

# Check AWS CLI
if ! aws sts get-caller-identity >/dev/null 2>&1; then
  echo "Error: AWS CLI not configured or credentials invalid"
  exit 1
fi

# Get VPC ID
VPC_ID=$(aws ec2 describe-vpcs --region "$REGION" --filters Name=tag:Name,Values="$VPC_NAME" --query 'Vpcs[0].VpcId' --output text 2>/dev/null)
if [ -z "$VPC_ID" ] || [ "$VPC_ID" = "None" ]; then
  echo "Warning: No VPC found with tag Name=$VPC_NAME"
  VPC_ID=""
fi

# Print section
print_section() {
  echo -e "\n=== $1 ==="
}

# Terraform output (check if state exists)
get_terraform_output() {
  if [ -f terraform.tfstate ] && [ -s terraform.tfstate ]; then
    terraform output -raw "$1" 2>/dev/null || echo "N/A"
  else
    echo "N/A (No Terraform state)"
  fi
}

print_section "VPC ($VPC_NAME${VPC_ID:+, ID: $VPC_ID})"
[ -n "$VPC_ID" ] && aws ec2 describe-vpcs --region "$REGION" --vpc-ids "$VPC_ID" --query 'Vpcs[0].[VpcId,CidrBlock,Tags[?Key==`Name`].Value|[0]]' --output table

print_section "Subnets"
[ -n "$VPC_ID" ] && aws ec2 describe-subnets --region "$REGION" --filters "Name=vpc-id,Values=$VPC_ID" --query 'Subnets[*].[AvailabilityZoneId,SubnetId,CidrBlock,Tags[?Key==`Name`].Value|[0]]' --output table

print_section "Security Groups"
[ -n "$VPC_ID" ] && aws ec2 describe-security-groups --region "$REGION" --filters "Name=vpc-id,Values=$VPC_ID" --query 'SecurityGroups[*].[GroupId,GroupName,Description]' --output table

print_section "VPC Endpoints"
[ -n "$VPC_ID" ] && aws ec2 describe-vpc-endpoints --region "$REGION" --filters "Name=vpc-id,Values=$VPC_ID" --query 'VpcEndpoints[*].[VpcEndpointId,ServiceName,State]' --output table

print_section "S3 Buckets (SageMaker)"
aws s3api list-buckets --region "$REGION" --query 'Buckets[?contains(Name,`sagemaker`)].[Name,CreationDate]' --output table

print_section "SageMaker Domain"
aws sagemaker list-domains --region "$REGION" --query 'Domains[*].[DomainId,DomainName,Status]' --output table

print_section "SageMaker Spaces"
aws sagemaker list-spaces --region "$REGION" --query 'Spaces[*].[DomainId,SpaceName,Status]' --output table

print_section "SageMaker User Profiles"
aws sagemaker list-user-profiles --region "$REGION" --query 'UserProfiles[*].[DomainId,UserProfileName,Status]' --output table

print_section "Terraform Outputs"
echo "S3 Bucket: $(get_terraform_output s3_bucket_name)"
echo "SageMaker Domain ID: $(get_terraform_output sagemaker_domain_id)"
echo "SageMaker Domain URL: $(get_terraform_output sagemaker_domain_url)"
