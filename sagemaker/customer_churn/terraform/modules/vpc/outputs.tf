# modules/vpc/outputs.tf

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "subnet_id" {
  description = "ID of the subnet"
  value       = aws_subnet.main.id
}

output "sagemaker_security_group_id" {
  description = "ID of the security group for SageMaker Studio"
  value       = aws_security_group.sagemaker_sg.id
}
