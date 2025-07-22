#!/bin/bash

aws sagemaker list-models --region us-east-1
aws sagemaker list-training-jobs --region us-east-1
aws sagemaker list-processing-jobs --region us-east-1
aws sagemaker list-apps --region us-east-1
aws sagemaker list-endpoints --region us-east-1
aws sagemaker list-spaces --region us-east-1
aws sagemaker list-notebook-instances --region us-east-1
aws sagemaker list-domains --region us-east-1
aws sagemaker list-user-profiles --region us-east-1
aws ec2 describe-vpcs --region us-east-1
aws logs describe-log-groups --log-group-name-prefix /aws/sagemaker --region us-east-1
aws iam list-roles --path-prefix /aws-service-role/SageMaker
aws s3 ls --region us-east-1
