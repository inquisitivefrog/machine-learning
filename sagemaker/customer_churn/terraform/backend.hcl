terraform {
  backend "s3" {
    bucket = "bluedragon-employer-prod"
    key    = "sagemaker/customer_churn/terraform.tfstate"
    region = "us-east-1"
  }
}
