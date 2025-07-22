# variables.tf

variable "auth_mode" {
  description = "Authentication mode for SageMaker domain"
  type        = string
  default     = "SSO" # or "IAM"
}

variable "bucket_name" {
  description = "S3 bucket name for SageMaker"
  type        = string
  default     = "sagemaker-us-east-1-084375569056"
}

variable "domain_name" {
  description = "SageMaker domain name"
  type        = string
  default     = "ImaginaryOrgDomain"
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "sagemaker_role_name" {
  description = "Name of the SageMaker execution role"
  type        = string
  default     = "AmazonSageMaker-ExecutionRole-20250520T093901"
}

variable "user_profile_name" {
  description = "SageMaker user profile name"
  type        = string
  default     = "bluedragon"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "vpc_name" {
  description = "Name of the VPC"
  type        = string
  default     = "imaginary-org-vpc"
}
