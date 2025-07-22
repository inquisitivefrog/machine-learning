
cat > /Users/tim/Documents/workspace/python3/machine-learning/sagemaker/customer_churn/src/churn_notebook.ipynb << EOF
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import boto3\n",
    "\n",
    "s3 = boto3.client(\"s3\")\n",
    "s3.download_file(\"sagemaker-us-east-1-084375569056\", \"data/train.csv\", \"train.csv\")\n",
    "df = pd.read_csv(\"train.csv\")\n",
    "if \"Churn\" not in df.columns:\n",
    "    raise ValueError(\"Column 'Churn' not found.\")\n",
    "df[\"Churn\"] = df[\"Churn'].map({\"Yes\": 1, \"No\": 0})\n",
    "if \"customerID\" in df.columns:\n",
    "    df = df.drop(columns=[\"customerID\"])\n",
    "categorical_cols = df.select_dtypes(include=[\"object\"]).columns\n",
    "for col in categorical_cols:\n",
    "    df[col] = df[col].astype(\"category\").cat.codes\n",
    "for col in df.columns:\n",
    "    if df[col].dtype == \"object\":\n",
    "        df[col] = pd.to_numeric(df[col], errors=\"coerce\").fillna(0)\n",
    "columns = [\"Churn\"] + [col for col in df.columns if col != \"Churn\"]\n",
    "df = df[columns]\n",
    "df.to_csv(\"train_processed.csv\", header=False, index=False)\n",
    "s3.upload_file(\"train_processed.csv\", \"sagemaker-us-east-1-084375569056\", \"data/train_processed.csv\")\n",
    "print(\"Uploaded processed dataset to S3\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sagemaker\n",
    "from sagemaker.estimator import Estimator\n",
    "from sagemaker.inputs import TrainingInput\n",
    "\n",
    "session = sagemaker.Session()\n",
    "estimator = Estimator(\n",
    "    image_uri=sagemaker.image_uris.retrieve(\"xgboost\", region=\"us-east-1\", version=\"latest\"),\n",
    "    role=\"arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-<new-timestamp>\",\n",
    "    instance_count=1,\n",
    "    instance_type=\"ml.m5.large\",\n",
    "    output_path=\"s3://sagemaker-us-east-1-084375569056/output/\",\n",
    "    sagemaker_session=session\n",
    ")\n",
    "estimator.set_hyperparameters(\n",
    "    max_depth=5,\n",
    "    eta=0.2,\n",
    "    gamma=4,\n",
    "    min_child_weight=6,\n",
    "    subsample=0.8,\n",
    "    objective=\"binary:logistic\",\n",
    "    num_round=100\n",
    ")\n",
    "train_input = TrainingInput(\n",
    "    s3_data=\"s3://sagemaker-us-east-1-084375569056/data/train_processed.csv\",\n",
    "    content_type=\"csv\"\n",
    ")\n",
    "estimator.fit({\"train\": train_input})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictor = estimator.deploy(\n",
    "    initial_instance_count=1,\n",
    "    instance_type=\"ml.t2.medium\"\n",
    ")\n",
    "predictor.delete_endpoint()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
EOF

(py3ml) tim@Tims-MBP customer_churn % aws s3 cp /Users/tim/Documents/workspace/python3/machine-learning/sagemaker/customer_churn/src/churn_notebook.ipynb s3://sagemaker-us-east-1-084375569056/notebooks/churn_notebook.ipynb --region us-east-1
upload: src/churn_notebook.ipynb to s3://sagemaker-us-east-1-084375569056/notebooks/churn_notebook.ipynb


curl -o ./files/train.csv https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
(py3ml) tim@Tims-MBP customer_churn % aws s3 cp /Users/tim/Documents/workspace/python3/machine-learning/sagemaker/customer_churn/files/train.csv s3://sagemaker-us-east-1-084375569056/data/train.csv
upload: files/train.csv to s3://sagemaker-us-east-1-084375569056/data/train.csv
(py3ml) tim@Tims-MBP customer_churn % python src/preprocess_data.py
(py3ml) tim@Tims-MBP customer_churn % aws s3 cp /Users/tim/Documents/workspace/python3/machine-learning/sagemaker/customer_churn/files/train_processed.csv s3://sagemaker-us-east-1-084375569056/data/train_processed.csv
upload: files/train_processed.csv to s3://sagemaker-us-east-1-084375569056/data/train_processed.csv

(py3ml) tim@Tims-MBP terraform % pwd
/Users/tim/Documents/workspace/python3/machine-learning/sagemaker/customer_churn/terraform
(py3ml) tim@Tims-MBP terraform % find . -name "*.tf" -o -name "*.tfvars" -o -name "*.hcl"
./backend.hcl
./main.tf
./terraform.tfvars
./variables.tf
./modules/s3/outputs.tf
./modules/s3/main.tf
./modules/s3/variables.tf
./modules/iam/outputs.tf
./modules/iam/main.tf
./modules/iam/variables.tf
./modules/vpc/outputs.tf
./modules/vpc/main.tf
./modules/vpc/variables.tf
./modules/sagemaker/outputs.tf
./modules/sagemaker/main.tf
./modules/sagemaker/variables.tf

tim@Tims-MBP terraform % aws iam list-roles --query 'Roles[?starts_with(RoleName,`AmazonSageMaker-ExecutionRole`)]' --region us-east-1
[
    {
        "Path": "/service-role/",
        "RoleName": "AmazonSageMaker-ExecutionRole-20250513T204281",
        "RoleId": "AROARHJJNAKQO7RWM5FYL",
        "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281",
        "CreateDate": "2025-05-14T03:42:14+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "sagemaker.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "Description": "SageMaker execution role created from the SageMaker AWS Management Console.",
        "MaxSessionDuration": 3600
    },
    {
        "Path": "/service-role/",
        "RoleName": "AmazonSageMaker-ExecutionRole-20250521T124726",
        "RoleId": "AROARHJJNAKQNM5GEDUNL",
        "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250521T124726",
        "CreateDate": "2025-05-21T19:47:52+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "sagemaker.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "Description": "SageMaker execution role created from the SageMaker AWS Management Console.",
        "MaxSessionDuration": 3600
    }
]

tim@Tims-MBP terraform % aws s3 mb s3://bluedragon-employer-prod --region us-east-1
make_bucket: bluedragon-employer-prod
tim@Tims-MBP terraform % terraform init
Initializing the backend...
Initializing modules...
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/aws v5.94.1

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

tim@Tims-MBP terraform % aws s3 ls s3://bluedragon-employer-prod 
tim@Tims-MBP terraform % terraform state list

tim@Tims-MBP terraform % terraform validate
Success! The configuration is valid.

tim@Tims-MBP terraform % terraform plan -out=tfplan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.iam.aws_iam_role.sagemaker_execution_role will be created
  + resource "aws_iam_role" "sagemaker_execution_role" {
      + arn                   = (known after apply)
      + assume_role_policy    = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = "sts:AssumeRole"
                      + Effect    = "Allow"
                      + Principal = {
                          + Service = "sagemaker.amazonaws.com"
                        }
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + create_date           = (known after apply)
      + force_detach_policies = false
      + id                    = (known after apply)
      + managed_policy_arns   = (known after apply)
      + max_session_duration  = 3600
      + name                  = "AmazonSageMaker-ExecutionRole-20250520T093901"
      + name_prefix           = (known after apply)
      + path                  = "/service-role/"
      + tags_all              = (known after apply)
      + unique_id             = (known after apply)

      + inline_policy (known after apply)
    }

  # module.iam.aws_iam_role_policy.sagemaker_s3_access will be created
  + resource "aws_iam_role_policy" "sagemaker_s3_access" {
      + id          = (known after apply)
      + name        = "SageMakerS3Access"
      + name_prefix = (known after apply)
      + policy      = (known after apply)
      + role        = (known after apply)
    }

  # module.iam.aws_iam_role_policy_attachment.sagemaker_full_access will be created
  + resource "aws_iam_role_policy_attachment" "sagemaker_full_access" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
      + role       = "AmazonSageMaker-ExecutionRole-20250520T093901"
    }

  # module.s3.aws_s3_bucket.sagemaker_bucket will be created
  + resource "aws_s3_bucket" "sagemaker_bucket" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      + bucket                      = "sagemaker-us-east-1-084375569056"
      + bucket_domain_name          = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags                        = {
          + "Name" = "SageMaker Customer Churn Bucket"
        }
      + tags_all                    = {
          + "Name" = "SageMaker Customer Churn Bucket"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + cors_rule (known after apply)

      + grant (known after apply)

      + lifecycle_rule (known after apply)

      + logging (known after apply)

      + object_lock_configuration (known after apply)

      + replication_configuration (known after apply)

      + server_side_encryption_configuration (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

  # module.s3.aws_s3_bucket_versioning.sagemaker_bucket_versioning will be created
  + resource "aws_s3_bucket_versioning" "sagemaker_bucket_versioning" {
      + bucket = (known after apply)
      + id     = (known after apply)

      + versioning_configuration {
          + mfa_delete = (known after apply)
          + status     = "Enabled"
        }
    }

  # module.sagemaker.aws_sagemaker_domain.sagemaker_domain will be created
  + resource "aws_sagemaker_domain" "sagemaker_domain" {
      + app_network_access_type                        = "PublicInternetOnly"
      + arn                                            = (known after apply)
      + auth_mode                                      = "IAM"
      + domain_name                                    = "customer-churn-domain"
      + home_efs_file_system_id                        = (known after apply)
      + id                                             = (known after apply)
      + security_group_id_for_domain_boundary          = (known after apply)
      + single_sign_on_application_arn                 = (known after apply)
      + single_sign_on_managed_application_instance_id = (known after apply)
      + subnet_ids                                     = (known after apply)
      + tag_propagation                                = "DISABLED"
      + tags_all                                       = (known after apply)
      + url                                            = (known after apply)
      + vpc_id                                         = (known after apply)

      + default_user_settings {
          + auto_mount_home_efs = (known after apply)
          + default_landing_uri = (known after apply)
          + execution_role      = (known after apply)
          + studio_web_portal   = (known after apply)

          + jupyter_server_app_settings {
              + default_resource_spec {
                  + instance_type = "system"
                }
            }

          + space_storage_settings (known after apply)
        }
    }

  # module.sagemaker.aws_sagemaker_user_profile.sagemaker_user_profile will be created
  + resource "aws_sagemaker_user_profile" "sagemaker_user_profile" {
      + arn                      = (known after apply)
      + domain_id                = (known after apply)
      + home_efs_file_system_uid = (known after apply)
      + id                       = (known after apply)
      + tags_all                 = (known after apply)
      + user_profile_name        = "bluedragon"

      + user_settings {
          + auto_mount_home_efs = (known after apply)
          + execution_role      = (known after apply)
          + studio_web_portal   = (known after apply)

          + space_storage_settings (known after apply)
        }
    }

  # module.vpc.aws_subnet.main will be created
  + resource "aws_subnet" "main" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "us-east-1a"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.0.1.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + tags                                           = {
          + "Name" = "sagemaker-subnet"
        }
      + tags_all                                       = {
          + "Name" = "sagemaker-subnet"
        }
      + vpc_id                                         = (known after apply)
    }

  # module.vpc.aws_vpc.main will be created
  + resource "aws_vpc" "main" {
      + arn                                  = (known after apply)
      + cidr_block                           = "10.0.0.0/16"
      + default_network_acl_id               = (known after apply)
      + default_route_table_id               = (known after apply)
      + default_security_group_id            = (known after apply)
      + dhcp_options_id                      = (known after apply)
      + enable_dns_hostnames                 = (known after apply)
      + enable_dns_support                   = true
      + enable_network_address_usage_metrics = (known after apply)
      + id                                   = (known after apply)
      + instance_tenancy                     = "default"
      + ipv6_association_id                  = (known after apply)
      + ipv6_cidr_block                      = (known after apply)
      + ipv6_cidr_block_network_border_group = (known after apply)
      + main_route_table_id                  = (known after apply)
      + owner_id                             = (known after apply)
      + tags                                 = {
          + "Name" = "sagemaker-vpc"
        }
      + tags_all                             = {
          + "Name" = "sagemaker-vpc"
        }
    }

Plan: 9 to add, 0 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "tfplan"

tim@Tims-MBP terraform % terraform apply tfplan
module.vpc.aws_vpc.main: Creating...
module.iam.aws_iam_role.sagemaker_execution_role: Creating...
module.s3.aws_s3_bucket.sagemaker_bucket: Creating...
module.iam.aws_iam_role.sagemaker_execution_role: Creation complete after 1s [id=AmazonSageMaker-ExecutionRole-20250520T093901]
module.iam.aws_iam_role_policy_attachment.sagemaker_full_access: Creating...
module.iam.aws_iam_role_policy_attachment.sagemaker_full_access: Creation complete after 0s [id=AmazonSageMaker-ExecutionRole-20250520T093901-20250527215540649600000001]
module.vpc.aws_vpc.main: Creation complete after 2s [id=vpc-0441870840048bbdf]
module.vpc.aws_subnet.main: Creating...
module.vpc.aws_subnet.main: Creation complete after 1s [id=subnet-0d9a1efe383db6930]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Creating...
module.s3.aws_s3_bucket.sagemaker_bucket: Creation complete after 3s [id=sagemaker-us-east-1-084375569056]
module.s3.aws_s3_bucket_versioning.sagemaker_bucket_versioning: Creating...
module.iam.aws_iam_role_policy.sagemaker_s3_access: Creating...
module.iam.aws_iam_role_policy.sagemaker_s3_access: Creation complete after 0s [id=AmazonSageMaker-ExecutionRole-20250520T093901:SageMakerS3Access]
module.s3.aws_s3_bucket_versioning.sagemaker_bucket_versioning: Creation complete after 2s [id=sagemaker-us-east-1-084375569056]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [10s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [20s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [30s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [40s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [50s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [1m0s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [1m10s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [1m20s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [1m30s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [1m40s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Still creating... [1m50s elapsed]
module.sagemaker.aws_sagemaker_domain.sagemaker_domain: Creation complete after 1m55s [id=d-kgivm4s6ihtt]
module.sagemaker.aws_sagemaker_user_profile.sagemaker_user_profile: Creating...
module.sagemaker.aws_sagemaker_user_profile.sagemaker_user_profile: Creation complete after 4s [id=arn:aws:sagemaker:us-east-1:084375569056:user-profile/d-kgivm4s6ihtt/bluedragon]

Apply complete! Resources: 9 added, 0 changed, 0 destroyed.

tim@Tims-MBP terraform % terraform state list
module.iam.aws_iam_role.sagemaker_execution_role
module.iam.aws_iam_role_policy.sagemaker_s3_access
module.iam.aws_iam_role_policy_attachment.sagemaker_full_access
module.s3.aws_s3_bucket.sagemaker_bucket
module.s3.aws_s3_bucket_versioning.sagemaker_bucket_versioning
module.sagemaker.aws_sagemaker_domain.sagemaker_domain
module.sagemaker.aws_sagemaker_user_profile.sagemaker_user_profile
module.vpc.aws_subnet.main
module.vpc.aws_vpc.main

AWS UI
https://us-east-1.console.aws.amazon.com/sagemaker/home?region=us-east-1#/studio/d-kgivm4s6ihtt?tab=users
Select Domains
Click on recently created domain: customer-churn-domain
Select User Profiles tab
For user profile: bluedragon, select Launch and choose Studio
Open new Window and Select Create JupyterLab Space
Create space: customer-churn
Click Run Space
Click Open Jupyter Lab
Open new Window 
File/Open From URL



Jupyter Terminal
sagemaker-user@default:~$ aws s3 cp s3://sagemaker-us-east-1-084375569056/notebooks/churn_notebook.ipynb ./churn_notebook.ipynb
download: s3://sagemaker-us-east-1-084375569056/notebooks/churn_notebook.ipynb to ./churn_notebook.ipynb
sagemaker-user@default:~$ head -5 churn_notebook.ipynb 
{
 "cells": [
  {
   "cell_type": "code",^C
sagemaker-user@default:~$ sudo apt-get update
sagemaker-user@default:~$ sudo apt-get install -y jq vim
sagemaker-user@default:~$ cat churn_notebook.ipynb | jq .

