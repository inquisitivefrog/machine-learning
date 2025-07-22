# modules/sagemaker/outputs.tf

output "domain_id" {
  description = "ID of the SageMaker domain"
  value       = aws_sagemaker_domain.sagemaker_domain.id
}

