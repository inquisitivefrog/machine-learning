#!/bin/bash
set -x

# Quantum Tasks
for task_status in QUEUED RUNNING COMPLETED FAILED CANCELLED; do
  aws braket search-quantum-tasks --filters "name=status,operator=EQUAL,values=$task_status" --region us-east-1
done
aws braket search-quantum-tasks --filters 'name=deviceArn,operator=EQUAL,values=arn:aws:braket:::device/quantum-simulator/amazon/sv1' --region us-east-1

# Hybrid Jobs
aws s3 ls s3://amazon-braket-us-east-1-084375569056/jobs/ --recursive
aws braket search-jobs --filters 'name=jobArn,operator=EQUAL,values=arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10' --region us-east-1
aws braket get-job --job-arn arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10 --region us-east-1

# Devices
aws braket search-devices --filters 'name=deviceType,values=SIMULATOR' --region us-east-1
aws braket search-devices --filters 'name=providerName,values=Amazon Braket' --region us-east-1
aws braket search-devices --filters 'name=deviceType,values=QPU' --region us-east-1

# S3
aws s3 ls s3://amazon-braket-my-quantum-output-20250514-kerstarsoc/quantum-output/ --recursive
aws s3 ls s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/data/ --recursive
aws s3 ls s3://sagemaker-us-east-1-084375569056/ --recursive

# SageMaker
aws sagemaker list-notebook-instances
aws sagemaker list-training-jobs
aws sagemaker list-models
aws sagemaker list-endpoints

# EC2
aws ec2 describe-instances --filters "Name=tag:created-by,Values=Braket" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}" --region us-east-1
aws ec2 describe-instances --filters "Name=tag:aws:autoscaling:groupName,Values=*SageMaker*" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}" --region us-east-1
