# modules/sagemaker/variables.tf

variable "domain_name" {
  description = "SageMaker domain name"
  type        = string
}

variable "execution_role_arn" {
  description = "ARN of the SageMaker execution role"
  type        = string
}

variable "sagemaker_security_group_id" {
  description = "ID of the security group for SageMaker Studio"
  type        = string
}

variable "subnet_ids" {
  description = "Subnet IDs for SageMaker domain"
  type        = list(string)
}

variable "user_profile_name" {
  description = "SageMaker user profile name"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID for SageMaker domain"
  type        = string
}
