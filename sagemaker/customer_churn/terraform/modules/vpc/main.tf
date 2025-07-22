# modules/vpc/main.tf

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "sagemaker-vpc"
  }
}

resource "aws_subnet" "main" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "${var.region}a"
  tags = {
    Name = "sagemaker-subnet"
  }
}

# Security Group for SageMaker Studio
resource "aws_security_group" "sagemaker_sg" {
  name        = "${var.vpc_name}-sagemaker-sg"
  description = "Security group for SageMaker Studio in VPC Only mode"
  vpc_id      = aws_vpc.main.id # Adjust to match your VPC resource name

  # Inbound Rules
  ingress {
    description = "Allow NFS traffic for SageMaker Studio EFS"
    from_port   = 2049
    to_port     = 2049
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr] # Use VPC CIDR variable
  }

  # Outbound Rules
  egress {
    description = "Allow outbound traffic within VPC"
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # All protocols
    cidr_blocks = [var.vpc_cidr]
  }

  tags = {
    Name = "${var.vpc_name}-sagemaker-sg"
  }
}

# VPC Endpoint for SageMaker API
resource "aws_vpc_endpoint" "sagemaker_api" {
  vpc_id              = aws_vpc.main.id # Adjust to match your VPC resource name
  service_name        = "com.amazonaws.${var.region}.sagemaker.api"
  vpc_endpoint_type   = "Interface"
  security_group_ids  = [aws_security_group.sagemaker_sg.id]
  subnet_ids          = aws_subnet.private[*].id # Adjust to match your subnet resource name
  private_dns_enabled = true

  tags = {
    Name = "${var.vpc_name}-sagemaker-api-endpoint"
  }
}

# VPC Endpoint for SageMaker Runtime
resource "aws_vpc_endpoint" "sagemaker_runtime" {
  vpc_id              = aws_vpc.main.id # Adjust to match your VPC resource name
  service_name        = "com.amazonaws.${var.region}.sagemaker.runtime"
  vpc_endpoint_type   = "Interface"
  security_group_ids  = [aws_security_group.sagemaker_sg.id]
  subnet_ids          = aws_subnet.private[*].id # Adjust to match your subnet resource name
  private_dns_enabled = true

  tags = {
    Name = "${var.vpc_name}-sagemaker-runtime-endpoint"
  }
}
