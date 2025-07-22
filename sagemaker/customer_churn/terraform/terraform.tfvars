# terraform.tfvars

auth_mode           = "IAM" # or "SSO"
domain_name         = "ImaginaryOrgDomain"
bucket_name         = "sagemaker-us-east-1-084375569056"
region              = "us-east-1"
sagemaker_role_name = "AmazonSageMaker-ExecutionRole-20250520T093901"
user_profile_name   = "bluedragon"
vpc_cidr            = "10.0.0.0/16"
vpc_name            = "imaginary-org-vpc"
