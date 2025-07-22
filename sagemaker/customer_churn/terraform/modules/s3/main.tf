resource "aws_s3_bucket" "sagemaker_bucket" {
  bucket = var.bucket_name
  tags = {
    Name = "SageMaker Customer Churn Bucket"
  }
}

resource "aws_s3_bucket_versioning" "sagemaker_bucket_versioning" {
  bucket = aws_s3_bucket.sagemaker_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
