output "role_arn" {
  description = "ARN of the IAM role"
  value       = aws_iam_role.sagemaker_execution_role.arn
}
