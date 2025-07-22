#!/bin/bash
set -x

aws sagemaker list-domains --region us-east-1 --query "Domains[].DomainId" --output text
aws efs describe-file-systems --region us-east-1 --query "FileSystems[].FileSystemId" --output text
aws s3api list-buckets --query "Buckets[?contains(Name,'sagemaker')].Name" --output text --region us-east-1
aws iam list-roles --query "Roles[?contains(RoleName,'SageMaker')].RoleName" --output text --region us-east-1
aws ec2 describe-vpcs --region us-east-1 --query "Vpcs[].VpcId" --output text
aws ec2 describe-security-groups --region us-east-1 --query "SecurityGroups[].GroupId" --output text
aws ec2 describe-route-tables --region us-east-1 --query "RouteTables[].RouteTableId" --output text
aws ec2 describe-network-interfaces --region us-east-1 --query "NetworkInterfaces[].NetworkInterfaceId" --output text
aws kms list-keys --region us-east-1 --query "Keys[].KeyId" --output text
