provider "aws" {
  region = var.region
}

module "iam" {
  source       = "./modules/iam"
  role_name    = var.sagemaker_role_name
  s3_bucket_arn = module.s3.bucket_arn
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = var.bucket_name
}

module "sagemaker" {
  source                      = "./modules/sagemaker"
  domain_name                 = var.domain_name
  auth_mode                   = var.auth_mode
  vpc_id                      = module.vpc.vpc_id # Adjust to your VPC module output
  subnet_ids                  = module.vpc.private_subnet_ids # Adjust to your VPC module output
  execution_role_arn          = module.iam.sagemaker_role_arn # Adjust to your IAM module output
  kms_key_id                  = module.kms.kms_key_id # Adjust if you have a KMS module
  user_profile_name           = var.user_profile_name
  sagemaker_security_group_id = module.vpc.sagemaker_security_group_id
}

module "vpc" {
  source = "./modules/vpc"
  region   = var.region
  vpc_name = var.vpc_name
  vpc_cidr = var.vpc_cidr
}

