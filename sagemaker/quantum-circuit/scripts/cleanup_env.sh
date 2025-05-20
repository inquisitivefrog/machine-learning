#!/bin/bash

# 1. Delete SageMaker Endpoints
aws sagemaker delete-endpoint --endpoint-name sagemaker-xgboost-2025-05-16-18-14-07-995 --region us-east-1
aws sagemaker delete-endpoint --endpoint-name sagemaker-xgboost-2025-05-16-17-00-16-559 --region us-east-1

# 2. Delete SageMaker Models
aws sagemaker delete-model --model-name sagemaker-xgboost-2025-05-16-18-14-07-995 --region us-east-1
aws sagemaker delete-model --model-name sagemaker-xgboost-2025-05-16-17-00-16-559 --region us-east-1
aws sagemaker delete-model --model-name sagemaker-xgboost-2025-05-15-22-06-31-961 --region us-east-1
aws sagemaker delete-model --model-name sagemaker-xgboost-2025-05-15-21-52-07-049 --region us-east-1

# 3. Stop and Delete SageMaker Notebook Instance
aws sagemaker stop-notebook-instance --notebook-instance-name amazon-braket-my-sagemaker-data-2025 --region us-east-1
# Wait for the notebook to stop (check status with: aws sagemaker list-notebook-instances)
aws sagemaker delete-notebook-instance --notebook-instance-name amazon-braket-my-sagemaker-data-2025 --region us-east-1

# 4. Delete Amazon Braket S3 Buckets
# Quantum tasks
aws s3 rm s3://amazon-braket-my-quantum-output-20250514-kerstarsoc/ --recursive

# Hybrid jobs (first job)
aws s3 rm s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/ --recursive

# Hybrid jobs (second job, replace <timestamp> after checking get-job output)
aws s3 rm s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/<timestamp>/ --recursive

# Check for other job folders and delete if found
aws s3 ls s3://amazon-braket-us-east-1-084375569056/jobs/ --recursive
aws s3 rm s3://amazon-braket-us-east-1-084375569056/jobs/ --recursive

# 5. Delete SageMaker S3 Bucket
aws s3 rm s3://sagemaker-us-east-1-084375569056/ --recursive

# 6. Check and Terminate EC2 Instances
# Braket-related instances
aws ec2 describe-instances --filters "Name=tag:created-by,Values=Braket" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}" --region us-east-1
# SageMaker-related instances
aws ec2 describe-instances --filters "Name=tag:aws:autoscaling:groupName,Values=*SageMaker*" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}" --region us-east-1
# Terminate if any are found (replace <instance-id>)
aws ec2 terminate-instances --instance-ids <instance-id> --region us-east-1
