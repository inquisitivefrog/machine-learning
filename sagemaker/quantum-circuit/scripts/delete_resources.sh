#!/bin/bash

 ejecutables

# Delete AWS resources after checking existence
# Usage: ./delete_resources.sh [region]
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
echo "[$TIMESTAMP] Starting deletion for region $REGION" | tee -a "$LOG_FILE"

# Function to check if S3 bucket exists
s3_bucket_exists() {
    local bucket=$1
    aws s3 ls "s3://$bucket" --region "$REGION" >/dev/null 2>&1
    return $?
}

# Function to delete S3 bucket with retries
delete_s3_bucket() {
    local bucket=$1
    local path=$2
    for attempt in {1..3}; do
        echo "Attempt $attempt: Deleting s3://$bucket/$path..." | tee -a "$LOG_FILE"
        aws s3 rm "s3://$bucket/$path" --recursive --region "$REGION" >>"$LOG_FILE" 2>&1
        if ! s3_bucket_exists "$bucket" || [ -z "$(aws s3 ls "s3://$bucket/$path" --region "$REGION")" ]; then
            echo "Successfully deleted s3://$bucket/$path" | tee -a "$LOG_FILE"
            aws s3 rb "s3://$bucket" --region "$REGION" >>"$LOG_FILE" 2>&1
            return 0
        fi
        sleep 10
    done
    echo "Failed to delete s3://$bucket/$path after 3 attempts" | tee -a "$LOG_FILE"
    return 1
}

# 1. Delete Braket Quantum Tasks
echo "Checking Braket quantum tasks..." | tee -a "$LOG_FILE"
for status in QUEUED RUNNING; do
    TASKS=$(aws braket search-quantum-tasks --filters "[{\"name\":\"status\",\"operator\":\"EQUAL\",\"values\":[\"$status\"]}]" --region "$REGION" --query "quantumTasks[].quantumTaskArn" --output text 2>>"$LOG_FILE")
    if [ -n "$TASKS" ]; then
        for task_arn in $TASKS; do
            echo "Canceling quantum task $task_arn..." | tee -a "$LOG_FILE"
            aws braket cancel-quantum-task --quantum-task-arn "$task_arn" --region "$REGION" >>"$LOG_FILE" 2>&1
            for i in {1..30}; do
                STATUS=$(aws braket get-quantum-task --quantum-task-arn "$task_arn" --region "$REGION" --query "status" --output text 2>>"$LOG_FILE")
                if [ "$STATUS" == "CANCELLED" ] || [ "$STATUS" == "FAILED" ]; then
                    break
                fi
                sleep 5
            done
        done
    else
        echo "No $status quantum tasks found" | tee -a "$LOG_FILE"
    fi
done

# 2. Delete Braket Hybrid Jobs
echo "Checking Braket hybrid jobs..." | tee -a "$LOG_FILE"
if [ -f "./scripts/search_jobs_by_filter.py" ]; then
    JOB_ARNS=$(python3 ./scripts/search_jobs_by_filter.py 2>>"$LOG_FILE" | jq -r '.[]?.jobArn' 2>/dev/null)
    if [ -n "$JOB_ARNS" ]; then
        for job_arn in $JOB_ARNS; do
            JOB_STATUS=$(aws braket get-job --job-arn "$job_arn" --region "$REGION" --query "status" --output text 2>>"$LOG_FILE")
            if [ "$JOB_STATUS" == "QUEUED" ] || [ "$JOB_STATUS" == "RUNNING" ]; then
                echo "Canceling job $job_arn..." | tee -a "$LOG_FILE"
                aws braket cancel-job --job-arn "$job_arn" --region "$REGION" >>"$LOG_FILE" 2>&1
                for i in {1..30}; do
                    STATUS=$(aws braket get-job --job-arn "$job_arn" --region "$REGION" --query "status" --output text 2>>"$LOG_FILE")
                    if [ "$STATUS" == "CANCELLED" ] || [ "$STATUS" == "FAILED" ]; then
                        break
                    fi
                    sleep 10
                done
            else
                echo "Job $job_arn is $JOB_STATUS, skipping cancellation" | tee -a "$LOG_FILE"
            fi
        done
    else
        echo "No hybrid jobs found via script" | tee -a "$LOG_FILE"
    fi
else
    echo "Warning: search_jobs_by_filter.py not found, skipping job check" | tee -a "$LOG_FILE"
fi

# 3. Delete SageMaker Endpoints
echo "Checking SageMaker endpoints..." | tee -a "$LOG_FILE"
ENDPOINTS=$(aws sagemaker list-endpoints --region "$REGION" --query "Endpoints[].EndpointName" --output text 2>>"$LOG_FILE")
if [ -n "$ENDPOINTS" ]; then
    for endpoint in $ENDPOINTS; do
        echo "Deleting endpoint $endpoint..." | tee -a "$LOG_FILE"
        aws sagemaker delete-endpoint --endpoint-name "$endpoint" --region "$REGION" >>"$LOG_FILE" 2>&1
    done
else
    echo "No endpoints found" | tee -a "$LOG_FILE"
fi

# 4. Delete SageMaker Models
echo "Checking SageMaker models..." | tee -a "$LOG_FILE"
MODELS=$(aws sagemaker list-models --region "$REGION" --query "Models[].ModelName" --output text 2>>"$LOG_FILE")
if [ -n "$MODELS" ]; then
    for model in $MODELS; do
        echo "Deleting model $model..." | tee -a "$LOG_FILE"
        aws sagemaker delete-model --model-name "$model" --region "$REGION" >>"$LOG_FILE" 2>&1
    done
else
    echo "No models found" | tee -a "$LOG_FILE"
fi

# 5. Delete SageMaker Notebook Instances
echo "Checking SageMaker notebook instances..." | tee -a "$LOG_FILE"
NOTEBOOKS=$(aws sagemaker list-notebook-instances --region "$REGION" --query "NotebookInstances[].NotebookInstanceName" --output text 2>>"$LOG_FILE")
if [ -n "$NOTEBOOKS" ]; then
    for notebook in $NOTEBOOKS; do
        STATUS=$(aws sagemaker describe-notebook-instance --notebook-instance-name "$notebook" --region "$REGION" --query "NotebookInstanceStatus" --output text 2>>"$LOG_FILE")
        if [ -n "$STATUS" ] && [ "$STATUS" != "Stopped" ] && [ "$STATUS" != "Failed" ]; then
            echo "Stopping notebook instance $notebook..." | tee -a "$LOG_FILE"
            aws sagemaker stop-notebook-instance --notebook-instance-name "$notebook" --region "$REGION" >>"$LOG_FILE" 2>&1
            for i in {1..30}; do
                STATUS=$(aws sagemaker describe-notebook-instance --notebook-instance-name "$notebook" --region "$REGION" --query "NotebookInstanceStatus" --output text 2>>"$LOG_FILE")
                if [ "$STATUS" == "Stopped" ]; then
                    break
                fi
                sleep 10
            done
        fi
        echo "Deleting notebook instance $notebook..." | tee -a "$LOG_FILE"
        aws sagemaker delete-notebook-instance --notebook-instance-name "$notebook" --region "$REGION" >>"$LOG_FILE" 2>&1
    done
else
    echo "No notebook instances found" | tee -a "$LOG_FILE"
fi

# 6. Delete EFS File Systems
echo "Checking EFS file systems..." | tee -a "$LOG_FILE"
EFS_IDS=$(aws efs describe-file-systems --region "$REGION" --query "FileSystems[].FileSystemId" --output text 2>>"$LOG_FILE")
if [ -n "$EFS_IDS" ]; then
    for efs_id in $EFS_IDS; do
        # Delete mount targets
        MOUNT_TARGETS=$(aws efs describe-mount-targets --file-system-id "$efs_id" --region "$REGION" --query "MountTargets[].MountTargetId" --output text 2>>"$LOG_FILE")
        for mt_id in $MOUNT_TARGETS; do
            echo "Deleting mount target $mt_id for EFS $efs_id..." | tee -a "$LOG_FILE"
            aws efs delete-mount-target --mount-target-id "$mt_id" --region "$REGION" >>"$LOG_FILE" 2>&1
            for i in {1..30}; do
                if ! aws efs describe-mount-targets --file-system-id "$efs_id" --region "$REGION" --query "MountTargets[?MountTargetId=='$mt_id']" --output text >/dev/null 2>>"$LOG_FILE"; then
                    break
                fi
                sleep 5
            done
        done
        # Delete EFS
        echo "Deleting EFS $efs_id..." | tee -a "$LOG_FILE"
        aws efs delete-file-system --file-system-id "$efs_id" --region "$REGION" >>"$LOG_FILE" 2>&1
    done
else
    echo "No EFS file systems found" | tee -a "$LOG_FILE"
fi

# 7. Delete SageMaker Domains, User Profiles, and Apps
echo "Checking SageMaker domains..." | tee -a "$LOG_FILE"
DOMAINS=$(aws sagemaker list-domains --region "$REGION" --query "Domains[].DomainId" --output text 2>>"$LOG_FILE")
if [ -n "$DOMAINS" ]; then
    for domain_id in $DOMAINS; do
        # Delete apps
        APPS=$(aws sagemaker list-apps --domain-id "$domain_id" --region "$REGION" --query "Apps[?Status!='Deleted'].{UserProfileName:UserProfileName,AppName:AppName,AppType:AppType}" --output json 2>>"$LOG_FILE" | jq -r '.[] | "\(.UserProfileName) \(.AppName) \(.AppType)"')
        if [ -n "$APPS" ]; then
            while read -r user_profile app_name app_type; do
                echo "Deleting app $app_name (type: $app_type) for user $user_profile in domain $domain_id..." | tee -a "$LOG_FILE"
                aws sagemaker delete-app --domain-id "$domain_id" --user-profile-name "$user_profile" --app-type "$app_type" --app-name "$app_name" --region "$REGION" >>"$LOG_FILE" 2>&1
                for i in {1..30}; do
                    if ! aws sagemaker list-apps --domain-id "$domain_id" --region "$REGION" --query "Apps[?AppName=='$app_name' && AppType=='$app_type' && Status!='Deleted']" --output text >/dev/null 2>>"$LOG_FILE"; then
                        break
                    fi
                    sleep 10
                done
            done <<<"$APPS"
        else
            echo "No active apps in domain $domain_id" | tee -a "$LOG_FILE"
        fi
        # Delete user profiles
        USER_PROFILES=$(aws sagemaker list-user-profiles --domain-id "$domain_id" --region "$REGION" --query "UserProfiles[].UserProfileName" --output text 2>>"$LOG_FILE")
        if [ -n "$USER_PROFILES" ]; then
            for user_profile in $USER_PROFILES; do
                echo "Deleting user profile $user_profile in domain $domain_id..." | tee -a "$LOG_FILE"
                aws sagemaker delete-user-profile --domain-id "$domain_id" --user-profile-name "$user_profile" --region "$REGION" >>"$LOG_FILE" 2>&1
            done
        else
            echo "No user profiles in domain $domain_id" | tee -a "$LOG_FILE"
        fi
        # Delete domain with retry
        for attempt in {1..3}; do
            echo "Attempt $attempt: Deleting domain $domain_id..." | tee -a "$LOG_FILE"
            aws sagemaker delete-domain --domain-id "$domain_id" --region "$REGION" >>"$LOG_FILE" 2>&1
            if ! aws sagemaker list-domains --region "$REGION" --query "Domains[?DomainId=='$domain_id']" --output text >/dev/null 2>>"$LOG_FILE"; then
                echo "Successfully deleted domain $domain_id" | tee -a "$LOG_FILE"
                break
            fi
            sleep 10
        done
    done
else
    echo "No domains found" | tee -a "$LOG_FILE"
fi

# 8. Delete Amazon Braket S3 Buckets
echo "Checking Braket S3 buckets..." | tee -a "$LOG_FILE"
QUANTUM_BUCKET="amazon-braket-my-quantum-output-20250514-kerstarsoc"
if s3_bucket_exists "$QUANTUM_BUCKET"; then
    delete_s3_bucket "$QUANTUM_BUCKET" ""
else
    echo "Quantum task bucket s3://$QUANTUM_BUCKET not found" | tee -a "$LOG_FILE"
fi

HYBRID_BUCKET="amazon-braket-us-east-1-084375569056"
if s3_bucket_exists "$HYBRID_BUCKET"; then
    JOB_FOLDERS=$(aws s3 ls "s3://$HYBRID_BUCKET/jobs/" --region "$REGION" | awk '{print $2}' 2>>"$LOG_FILE")
    if [ -n "$JOB_FOLDERS" ]; then
        for folder in $JOB_FOLDERS; do
            folder_name=$(echo "$folder" | tr -d '/')
            delete_s3_bucket "$HYBRID_BUCKET" "jobs/$folder_name/"
        done
    fi
    delete_s3_bucket "$HYBRID_BUCKET" ""
else
    echo "Hybrid job bucket s3://$HYBRID_BUCKET not found" | tee -a "$LOG_FILE"
fi

# 9. Delete SageMaker S3 Bucket
echo "Checking SageMaker S3 bucket..." | tee -a "$LOG_FILE"
SAGEMAKER_BUCKET="sagemaker-us-east-1-084375569056"
if s3_bucket_exists "$SAGEMAKER_BUCKET"; then
    delete_s3_bucket "$SAGEMAKER_BUCKET" ""
else
    echo "SageMaker bucket s3://$SAGEMAKER_BUCKET not found" | tee -a "$LOG_FILE"
fi

# 10. Delete EC2 Instances
echo "Checking EC2 instances..." | tee -a "$LOG_FILE"
INSTANCE_IDS=$(aws ec2 describe-instances --filters "Name=instance-state-name,Values=running,pending" --region "$REGION" --query "Reservations[].Instances[].InstanceId" --output text 2>>"$LOG_FILE")
if [ -n "$INSTANCE_IDS" ]; then
    for instance_id in $INSTANCE_IDS; do
        echo "Terminating instance $instance_id..." | tee -a "$LOG_FILE"
        aws ec2 terminate-instances --instance-ids "$instance_id" --region "$REGION" >>"$LOG_FILE" 2>&1
    done
else
    echo "No running EC2 instances found" | tee -a "$LOG_FILE"
fi

# 11. Delete Security Groups
echo "Checking security groups..." | tee -a "$LOG_FILE"
SGS=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=*sagemaker*" --region "$REGION" --query "SecurityGroups[].GroupId" --output text 2>>"$LOG_FILE")
if [ -n "$SGS" ]; then
    for sg_id in $SGS; do
        # Remove dependencies by clearing rules
        echo "Clearing rules for security group $sg_id..." | tee -a "$LOG_FILE"
        INGRESS_RULES=$(aws ec2 describe-security-groups --group-ids "$sg_id" --region "$REGION" --query "SecurityGroups[0].IpPermissions" --output json 2>>"$LOG_FILE")
        if [ "$INGRESS_RULES" != "[]" ]; then
            aws ec2 revoke-security-group-ingress --group-id "$sg_id" --security-group-rule-ids $(aws ec2 describe-security-groups --group-ids "$sg_id" --region "$REGION" --query "SecurityGroups[0].IpPermissions[].SecurityGroupRuleId" --output text) --region "$REGION" >>"$LOG_FILE" 2>&1
        fi
        EGRESS_RULES=$(aws ec2 describe-security-groups --group-ids "$sg_id" --region "$REGION" --query "SecurityGroups[0].IpPermissionsEgress" --output json 2>>"$LOG_FILE")
        if [ "$EGRESS_RULES" != "[]" ]; then
            aws ec2 revoke-security-group-egress --group-id "$sg_id" --security-group-rule-ids $(aws ec2 describe-security-groups --group-ids "$sg_id" --region "$REGION" --query "SecurityGroups[0].IpPermissionsEgress[].SecurityGroupRuleId" --output text) --region "$REGION" >>"$LOG_FILE" 2>&1
        fi
        # Delete security group
        for attempt in {1..3}; do
            echo "Attempt $attempt: Deleting security group $sg_id..." | tee -a "$LOG_FILE"
            aws ec2 delete-security-group --group-id "$sg_id" --region "$REGION" >>"$LOG_FILE" 2>&1
            if ! aws ec2 describe-security-groups --group-ids "$sg_id" --region "$REGION" >/dev/null 2>>"$LOG_FILE"; then
                echo "Successfully deleted security group $sg_id" | tee -a "$LOG_FILE"
                break
            fi
            sleep 10
        done
    done
else
    echo "No SageMaker-related security groups found" | tee -a "$LOG_FILE"
fi

# 12. Delete VPC and Networking Resources
echo "Checking all VPCs..." | tee -a "$LOG_FILE"
VPCS=$(aws ec2 describe-vpcs --region "$REGION" --query "Vpcs[].VpcId" --output text 2>>"$LOG_FILE")
if [ -n "$VPCS" ]; then
    for vpc_id in $VPCS; do
        # Skip default VPC if it has no SageMaker-related tags
        TAGS=$(aws ec2 describe-vpcs --vpc-ids "$vpc_id" --region "$REGION" --query "Vpcs[].Tags[?Key=='aws:createdBy' && Value=='SageMaker'].Key" --output text 2>>"$LOG_FILE")
        IS_DEFAULT=$(aws ec2 describe-vpcs --vpc-ids "$vpc_id" --region "$REGION" --query "Vpcs[].IsDefault" --output text 2>>"$LOG_FILE")
        if [ "$IS_DEFAULT" == "True" ] && [ -z "$TAGS" ]; then
            echo "Skipping default VPC $vpc_id (no SageMaker tags)" | tee -a "$LOG_FILE"
            continue
        fi
        echo "Processing VPC $vpc_id..." | tee -a "$LOG_FILE"
        # Delete subnets
        SUBNETS=$(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$vpc_id" --region "$REGION" --query "Subnets[].SubnetId" --output text 2>>"$LOG_FILE")
        for subnet_id in $SUBNETS; do
            echo "Deleting subnet $subnet_id..." | tee -a "$LOG_FILE"
            aws ec2 delete-subnet --subnet-id "$subnet_id" --region "$REGION" >>"$LOG_FILE" 2>&1
        done
        # Delete route tables (non-main)
        ROUTE_TABLES=$(aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$vpc_id" --region "$REGION" --query "RouteTables[?Associations[0].Main==\`false\`].RouteTableId" --output text 2>>"$LOG_FILE")
        for rt_id in $ROUTE_TABLES; do
            echo "Deleting route table $rt_id..." | tee -a "$LOG_FILE"
            aws ec2 delete-route-table --route-table-id "$rt_id" --region "$REGION" >>"$LOG_FILE" 2>&1
        done
        # Delete internet gateways
        IGWS=$(aws ec2 describe-internet-gateways --filters "Name=attachment.vpc-id,Values=$vpc_id" --region "$REGION" --query "InternetGateways[].InternetGatewayId" --output text 2>>"$LOG_FILE")
        for igw_id in $IGWS; do
            echo "Detaching and deleting internet gateway $igw_id..." | tee -a "$LOG_FILE"
            aws ec2 detach-internet-gateway --internet-gateway-id "$igw_id" --vpc-id "$vpc_id" --region "$REGION" >>"$LOG_FILE" 2>&1
            aws ec2 delete-internet-gateway --internet-gateway-id "$igw_id" --region "$REGION" >>"$LOG_FILE" 2>&1
        done
        # Delete NAT gateways
        NAT_GWS=$(aws ec2 describe-nat-gateways --filter "Name=vpc-id,Values=$vpc_id" --region "$REGION" --query "NatGateways[].NatGatewayId" --output text 2>>"$LOG_FILE")
        for nat_id in $NAT_GWS; do
            echo "Deleting NAT gateway $nat_id..." | tee -a "$LOG_FILE"
            aws ec2 delete-nat-gateway --nat-gateway-id "$nat_id" --region "$REGION" >>"$LOG_FILE" 2>&1
            for i in {1..30}; do
                if ! aws ec2 describe-nat-gateways --nat-gateway-ids "$nat_id" --region "$REGION" >/dev/null 2>>"$LOG_FILE"; then
                    break
                fi
                sleep 10
            done
        done
        # Delete Elastic IPs
        EIPS=$(aws ec2 describe-addresses --filters "Name=tag:vpc-id,Values=$vpc_id" --region "$REGION" --query "Addresses[].AllocationId" --output text 2>>"$LOG_FILE")
        for eip_id in $EIPS; do
            echo "Releasing Elastic IP $eip_id..." | tee -a "$LOG_FILE"
            aws ec2 release-address --allocation-id "$eip_id" --region "$REGION" >>"$LOG_FILE" 2>&1
        done
        # Delete security groups (non-default)
        SGS=$(aws ec2 describe-security-groups --filters "Name=vpc-id,Values=$vpc_id" "Name=group-name,Values=!default" --region "$REGION" --query "SecurityGroups[].GroupId" --output text 2>>"$LOG_FILE")
        for sg_id in $SGS; do
            echo "Deleting security group $sg_id..." | tee -a "$LOG_FILE"
            aws ec2 delete-security-group --group-id "$sg_id" --region "$REGION" >>"$LOG_FILE" 2>&1
        done
        # Delete VPC
        for attempt in {1..3}; do
            echo "Attempt $attempt: Deleting VPC $vpc_id..." | tee -a "$LOG_FILE"
            aws ec2 delete-vpc --vpc-id "$vpc_id" --region "$REGION" >>"$LOG_FILE" 2>&1
            if ! aws ec2 describe-vpcs --vpc-ids "$vpc_id" --region "$REGION" >/dev/null 2>>"$LOG_FILE"; then
                echo "Successfully deleted VPC $vpc_id" | tee -a "$LOG_FILE"
                break
            fi
            sleep 10
        done
    done
else
    echo "No VPCs found" | tee -a "$LOG_FILE"
fi

echo "[$TIMESTAMP] Deletion completed. Check $LOG_FILE for details" | tee -a "$LOG_FILE"
