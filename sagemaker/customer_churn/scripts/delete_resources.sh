#!/bin/bash

aws sagemaker list-endpoints --region us-east-1

aws iam list-attached-role-policies --role-name AmazonSageMaker-ExecutionRole-20250513T204281 --region us-east-1
aws iam detach-role-policy --role-name AmazonSageMaker-ExecutionRole-20250513T204281 --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess --region us-east-1 || true
aws iam list-role-policies --role-name AmazonSageMaker-ExecutionRole-20250513T204281 --region us-east-1
aws iam delete-role-policy --role-name AmazonSageMaker-ExecutionRole-20250513T204281 --policy-name SageMakerS3Access --region us-east-1 || true
aws iam delete-role --role-name AmazonSageMaker-ExecutionRole-20250513T204281 --region us-east-1

aws iam list-attached-role-policies --role-name AmazonSageMaker-ExecutionRole-20250521T124726 --region us-east-1
aws iam detach-role-policy --role-name AmazonSageMaker-ExecutionRole-20250521T124726 --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess --region us-east-1 || true
aws iam list-role-policies --role-name AmazonSageMaker-ExecutionRole-20250521T124726 --region us-east-1
aws iam delete-role-policy --role-name AmazonSageMaker-ExecutionRole-20250521T124726 --policy-name SageMakerS3Access --region us-east-1 || true
aws iam delete-role --role-name AmazonSageMaker-ExecutionRole-20250521T124726 --region us-east-1

aws iam list-roles --query 'Roles[?starts_with(RoleName,`AmazonSageMaker-ExecutionRole`)]' --region us-east-1

aws sagemaker list-apps --region us-east-1 
aws sagemaker list-endpoints --region us-east-1 
aws sagemaker list-domains --region us-east-1 
aws sagemaker list-spaces --region us-east-1

aws sagemaker delete-app --domain-id d-kgivm4s6ihtt --space-name customer-churn --app-type JupyterLab --app-name default --region us-east-1
aws sagemaker delete-space --domain-id d-kgivm4s6ihtt --space-name customer-churn --region us-east-1
aws sagemaker delete-domain --domain-id d-kgivm4s6ihtt --region us-east-1
aws s3 rm s3://sagemaker-us-east-1-084375569056 --recursive --region us-east-1
aws sagemaker list-user-profiles --domain-id d-kgivm4s6ihtt --region us-east-1
aws sagemaker delete-user-profile --domain-id d-kgivm4s6ihtt --user-profile-name bluedragon --region us-east-1
aws sagemaker list-domains --region us-east-1
aws sagemaker delete-domain --domain-id d-kgivm4s6ihtt --region us-east-1


cd terraform
terraform state list

module.iam.aws_iam_role.sagemaker_execution_role
module.iam.aws_iam_role_policy.sagemaker_s3_access
module.iam.aws_iam_role_policy_attachment.sagemaker_full_access
module.s3.aws_s3_bucket.sagemaker_bucket
module.s3.aws_s3_bucket_versioning.sagemaker_bucket_versioning
module.sagemaker.aws_sagemaker_domain.sagemaker_domain
module.sagemaker.aws_sagemaker_user_profile.sagemaker_user_profile
module.vpc.aws_subnet.main
module.vpc.aws_vpc.main

aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/jumpstart-dft-xgb-classification-model --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/sagemaker-xgboost-2025-05-15-21-52-07-049 --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/sagemaker-xgboost-2025-05-15-22-06-31-961 --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/sagemaker-xgboost-2025-05-16-17-00-16-559 --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/sagemaker-xgboost-2025-05-16-18-14-07-995 --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/xgboost-2025-05-28-01-24-25-795 --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/NotebookInstances --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/Studio/d-nehutxreazmp --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/TrainingJobs --region us-east-1
aws logs delete-log-group --log-group-name /aws/sagemaker/studio --region us-east-1

