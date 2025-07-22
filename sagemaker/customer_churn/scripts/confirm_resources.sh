#!/bin/bash

echo ""
echo 'pre-load variables'
echo "------------------"
REGION=us-east-1
echo region=$REGION
DOMAIN=`aws sagemaker list-domains --region $REGION | jq '.Domains[0].DomainName'`
echo domain=$DOMAIN
USER_PROFILE=bluedragon
echo user_profile=$USER_PROFILE
VPC=imaginary-org-vpc
echo vpc=$VPC

echo ""
echo "EC2 Resources"
echo "-------------"
IGW=`aws ec2 describe-internet-gateways --region $REGION --query 'InternetGateways[].InternetGatewayId' --output text`
echo "Internet Gateway: $IGW"
NAT=`aws ec2 describe-nat-gateways --region us-east-1 --query 'NatGateways[].NatGatewayId' --output text`
echo "NAT Gateway: $NAT"
VPC_IDS=`aws ec2 describe-vpcs --region us-east-1 --filters "Name=tag:Name,Values=$VPC" --query 'Vpcs[].VpcId' --output text`
echo "VPC IDs: $VPC_IDS"
VPC_SUBNETS=$(aws ec2 describe-subnets --region us-east-1 --filters "Name=tag:Name,Values=imaginary-org-vpc-subnet-*" --query 'Subnets[].SubnetId' --output text)
#VPC_SUBNETS=$(aws ec2 describe-subnets --region us-east-1 --filters "Name=tag:Name,Values=imaginary-org-vpc-subnet-*" --query 'Subnets[].{SubnetId:SubnetId,Name:Tags[?Key==`Name`].Value | [0]}' --output text)
echo "VPC Subnets: $VPC_SUBNETS"
for i in $(aws ec2 describe-route-tables --region $REGION --query 'RouteTables[].Associations[].RouteTableId' --output text); do
    echo Route: $i
done
for i in $(aws ec2 describe-security-groups --region $REGION --filters "Name=tag:Name,Values=arn:aws:sagemaker:*" --query 'SecurityGroups[].IpPermissionsEgress[].UserIdGroupPairs[].GroupId' --output text); do
    echo Security Group: $i
done

echo ""
echo "IAM Resources"
echo "-------------"
# ROLES=$(aws iam list-roles --query 'Roles[?starts_with(RoleName,`AmazonSageMaker-ExecutionRole`)].RoleName' --region $REGION --output text)
for i in $(aws iam list-roles --query 'Roles[?starts_with(RoleName,`AmazonSageMaker`)].RoleName' --region $REGION --output text); do
    for j in $(aws iam list-role-policies --region us-east-1 --role-name AWSServiceRoleForAmazonSageMakerNotebooks); do 
        echo "Role: $i, Policy: $j"
    done
done
echo ""
for i in $(aws iam list-roles --path-prefix /aws-service-role/SageMaker --region us-east-1 --query 'Roles[].RoleName' --output text); do
    for j in $(aws iam list-role-policies --region us-east-1 --role-name AWSServiceRoleForAmazonSageMakerNotebooks); do 
        echo "Role: $i, Policy: $j"
    done
done 
aws iam list-attached-role-policies --role-name AmazonSageMaker-ExecutionRole-20250521T124726 --region $REGION 

echo "SageMaker AI Resources"
aws sagemaker list-apps --region $REGION
aws sagemaker list-domains --region $REGION 
aws sagemaker list-endpoints --region $REGION 
aws sagemaker list-hyper-parameter-tuning-jobs --region $REGION
aws sagemaker list-models --region $REGION
aws sagemaker list-notebook-instances --region $REGION
aws sagemaker list-spaces --domain $DOMAIN --region $REGION
aws sagemaker list-user-profiles --domain-id $DOMAIN --region $REGION
aws sagemaker list-training-jobs --region $REGION
aws sagemaker list-transform-jobs --region $REGION

echo "VPC and Network Resources"
aws ec2 describe-vpcs --region $REGION
aws ec2 describe-subnets --region $REGION
aws ec2 describe-security-groups --region $REGION
aws ec2 describe-route-tables --region $REGION
aws ec2 describe-network-interfaces --region $REGION
aws ec2 describe-internet-gateways --region $REGION
aws ec2 describe-nat-gateways --region $REGION
aws efs describe-file-systems --region $REGION
aws efs describe-mount-targets --region $REGION


echo "S3 Resources"
aws s3 ls --region $REGION
aws s3api list-buckets --region $REGION
aws s3api list-buckets --query "Buckets[?Name=='sagemaker-customer-churn-20250530']" --region $REGION

echo "CloudWatch Resources"
aws logs describe-log-groups --log-group-name-prefix /aws/sagemaker --region $REGION
