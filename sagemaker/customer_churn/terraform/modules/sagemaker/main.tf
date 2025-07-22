# modules/sagemaker/main.tf

resource "aws_sagemaker_domain" "imaginary_org_domain" {
  domain_name = var.domain_name
  auth_mode   = var.auth_mode
  vpc_id      = var.vpc_id
  subnet_ids  = var.subnet_ids
  default_user_settings {
    execution_role  = var.execution_role_arn
    security_groups = [var.sagemaker_security_group_id] # Reference security group
    sharing_settings {
      notebook_output_option = "Allowed"
    }
  }
  default_space_settings {
    execution_role  = var.execution_role_arn
    security_groups = [var.sagemaker_security_group_id]
  }
  domain_settings {
    security_group_ids = [var.sagemaker_security_group_id]
  }
  kms_key_id = var.kms_key_id
}

resource "aws_sagemaker_domain" "sagemaker_domain" {
  domain_name = var.domain_name
  auth_mode   = "IAM"
  vpc_id      = var.vpc_id
  subnet_ids  = var.subnet_ids
  default_user_settings {
    execution_role = var.execution_role_arn
    jupyter_server_app_settings {
      default_resource_spec {
        instance_type = "system" 
      }
    }
  }
}

resource "aws_sagemaker_user_profile" "sagemaker_user_profile" {
  domain_id         = aws_sagemaker_domain.sagemaker_domain.id
  user_profile_name = var.user_profile_name
  user_settings {
    execution_role = var.execution_role_arn
  }
}


resource "aws_sagemaker_studio_lifecycle_config" "auto_shutdown" {
  studio_lifecycle_config_name     = "auto-shutdown"
  studio_lifecycle_config_app_type = "JupyterServer"
  content                          = base64encode(file("${path.module}/../../autoshutdown-script.sh"))
}
