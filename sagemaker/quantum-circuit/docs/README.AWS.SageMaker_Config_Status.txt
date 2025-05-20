
tim@Tims-MBP sagemaker % aws configure
AWS Access Key ID [****************IAEZ]: 
AWS Secret Access Key [****************fWA/]: 
Default region name [us-east-1]: 
Default output format [json]: 
tim@Tims-MBP sagemaker % aws sagemaker list-domains
{
    "Domains": [
        {
            "DomainArn": "arn:aws:sagemaker:us-east-1:084375569056:domain/d-3rxdb5dhdqly",
            "DomainId": "d-3rxdb5dhdqly",
            "DomainName": "QuickSetupDomain-20250513T204280",
            "Status": "InService",
            "CreationTime": "2025-05-13T20:42:21.839000-07:00",
            "LastModifiedTime": "2025-05-13T20:47:36.226000-07:00",
            "Url": "https://d-3rxdb5dhdqly.studio.us-east-1.sagemaker.aws"
        }
    ]
}
tim@Tims-MBP sagemaker % aws sagemaker describe-domain --domain-id d-3rxdb5dhdqly
{
    "DomainArn": "arn:aws:sagemaker:us-east-1:084375569056:domain/d-3rxdb5dhdqly",
    "DomainId": "d-3rxdb5dhdqly",
    "DomainName": "QuickSetupDomain-20250513T204280",
    "HomeEfsFileSystemId": "fs-0020d54439dfbdcf7",
    "Status": "InService",
    "CreationTime": "2025-05-13T20:42:21.839000-07:00",
    "LastModifiedTime": "2025-05-13T20:47:36.226000-07:00",
    "AuthMode": "IAM",
    "DefaultUserSettings": {
        "ExecutionRole": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281",
        "SharingSettings": {
            "NotebookOutputOption": "Allowed",
            "S3OutputPath": "s3://sagemaker-studio-084375569056-jznb41g5nl/sharing"
        },
        "JupyterServerAppSettings": {
            "DefaultResourceSpec": {
                "SageMakerImageArn": "arn:aws:sagemaker:us-east-1:081325390199:image/jupyter-server-3",
                "InstanceType": "system"
            }
        },
        "CanvasAppSettings": {
            "GenerativeAiSettings": {
                "AmazonBedrockRoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonSagemakerCanvasBedrockRole-20250513T204280"
            },
            "EmrServerlessSettings": {
                "ExecutionRoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerCanvasEMRSExecutionAccess-20250513T204280",
                "Status": "ENABLED"
            }
        },
        "DefaultLandingUri": "studio::",
        "StudioWebPortal": "ENABLED",
        "StudioWebPortalSettings": {
            "HiddenAppTypes": [
                "JupyterServer"
            ]
        },
        "AutoMountHomeEFS": "Enabled"
    },
    "AppNetworkAccessType": "PublicInternetOnly",
    "SubnetIds": [
        "subnet-022f529a1e45cbd9e",
        "subnet-0b74f4426cec96c10",
        "subnet-09a51c993c01450b7",
        "subnet-02fa4439bbae7c5a8",
        "subnet-0e3b525ee2500c7f4",
        "subnet-08c7a7a0adb46cc83"
    ],
    "Url": "https://d-3rxdb5dhdqly.studio.us-east-1.sagemaker.aws",
    "VpcId": "vpc-0d76268d482855884",
    "TagPropagation": "DISABLED",
    "DefaultSpaceSettings": {
        "ExecutionRole": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281"
    }
}
tim@Tims-MBP sagemaker % aws sagemaker list-user-profiles --domain-id d-3rxdb5dhdqly
{
    "UserProfiles": [
        {
            "DomainId": "d-3rxdb5dhdqly",
            "UserProfileName": "default-20250513T204280",
            "Status": "InService",
            "CreationTime": "2025-05-13T20:47:40.707000-07:00",
            "LastModifiedTime": "2025-05-13T20:47:44.792000-07:00"
        }
    ]
}
tim@Tims-MBP sagemaker % aws sagemaker list-apps --domain-id d-3rxdb5dhdqly
{
    "Apps": []
}
tim@Tims-MBP sagemaker % aws sagemaker list-notebook-instances
{
    "NotebookInstances": [
        {
            "NotebookInstanceName": "amazon-braket-my-sagemaker-data-2025",
            "NotebookInstanceArn": "arn:aws:sagemaker:us-east-1:084375569056:notebook-instance/amazon-braket-my-sagemaker-data-2025",
            "NotebookInstanceStatus": "InService",
            "Url": "amazon-braket-my-sagemaker-data-2025.notebook.us-east-1.sagemaker.aws",
            "InstanceType": "ml.t3.medium",
            "CreationTime": "2025-05-14T11:19:12.370000-07:00",
            "LastModifiedTime": "2025-05-14T11:24:06.168000-07:00",
            "NotebookInstanceLifecycleConfigName": "amazon-braket-my-sagemaker-data-2025"
        }
    ]
}
tim@Tims-MBP sagemaker % aws sagemaker describe-notebook-instance --notebook-instance-name amazon-braket-my-sagemaker-data-2025
{
    "NotebookInstanceArn": "arn:aws:sagemaker:us-east-1:084375569056:notebook-instance/amazon-braket-my-sagemaker-data-2025",
    "NotebookInstanceName": "amazon-braket-my-sagemaker-data-2025",
    "NotebookInstanceStatus": "InService",
    "Url": "amazon-braket-my-sagemaker-data-2025.notebook.us-east-1.sagemaker.aws",
    "InstanceType": "ml.t3.medium",
    "RoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonBraketServiceSageMakerNotebookRole",
    "LastModifiedTime": "2025-05-14T11:24:06.168000-07:00",
    "CreationTime": "2025-05-14T11:19:12.370000-07:00",
    "NotebookInstanceLifecycleConfigName": "amazon-braket-my-sagemaker-data-2025",
    "DirectInternetAccess": "Enabled",
    "VolumeSizeInGB": 5,
    "RootAccess": "Enabled",
    "PlatformIdentifier": "notebook-al2-v3",
    "InstanceMetadataServiceConfiguration": {
        "MinimumInstanceMetadataServiceVersion": "2"
    }
}
tim@Tims-MBP sagemaker % aws sagemaker list-training-jobs
{
    "TrainingJobSummaries": [
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-16-18-10-50-386",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-16-18-10-50-386",
            "CreationTime": "2025-05-16T11:10:50.603000-07:00",
            "TrainingEndTime": "2025-05-16T11:13:37.265000-07:00",
            "LastModifiedTime": "2025-05-16T11:13:37.530000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-16-16-56-59-277",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-16-16-56-59-277",
            "CreationTime": "2025-05-16T09:56:59.479000-07:00",
            "TrainingEndTime": "2025-05-16T09:59:41.861000-07:00",
            "LastModifiedTime": "2025-05-16T09:59:42.117000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-16-16-52-51-977",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-16-16-52-51-977",
            "CreationTime": "2025-05-16T09:52:52.180000-07:00",
            "TrainingEndTime": "2025-05-16T09:55:37.627000-07:00",
            "LastModifiedTime": "2025-05-16T09:55:37.986000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-22-35-37-193",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-22-35-37-193",
            "CreationTime": "2025-05-15T15:35:37.458000-07:00",
            "TrainingEndTime": "2025-05-15T15:38:24.608000-07:00",
            "LastModifiedTime": "2025-05-15T15:38:24.930000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-22-03-14-706",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-22-03-14-706",
            "CreationTime": "2025-05-15T15:03:14.910000-07:00",
            "TrainingEndTime": "2025-05-15T15:05:57.977000-07:00",
            "LastModifiedTime": "2025-05-15T15:05:58.119000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-21-48-49-811",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-21-48-49-811",
            "CreationTime": "2025-05-15T14:48:50.008000-07:00",
            "TrainingEndTime": "2025-05-15T14:51:31.449000-07:00",
            "LastModifiedTime": "2025-05-15T14:51:31.667000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-21-30-38-685",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-21-30-38-685",
            "CreationTime": "2025-05-15T14:30:38.917000-07:00",
            "TrainingEndTime": "2025-05-15T14:33:24.313000-07:00",
            "LastModifiedTime": "2025-05-15T14:33:24.713000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-21-21-10-815",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-21-21-10-815",
            "CreationTime": "2025-05-15T14:21:11.078000-07:00",
            "TrainingEndTime": "2025-05-15T14:24:00.844000-07:00",
            "LastModifiedTime": "2025-05-15T14:24:01.284000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-21-13-39-500",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-21-13-39-500",
            "CreationTime": "2025-05-15T14:13:39.702000-07:00",
            "TrainingEndTime": "2025-05-15T14:16:18.671000-07:00",
            "LastModifiedTime": "2025-05-15T14:16:19.037000-07:00",
            "TrainingJobStatus": "Failed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-21-05-47-954",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-21-05-47-954",
            "CreationTime": "2025-05-15T14:05:48.148000-07:00",
            "TrainingEndTime": "2025-05-15T14:08:36.586000-07:00",
            "LastModifiedTime": "2025-05-15T14:08:37.095000-07:00",
            "TrainingJobStatus": "Failed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-20-54-48-578",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-20-54-48-578",
            "CreationTime": "2025-05-15T13:54:48.800000-07:00",
            "TrainingEndTime": "2025-05-15T13:57:35.286000-07:00",
            "LastModifiedTime": "2025-05-15T13:57:35.835000-07:00",
            "TrainingJobStatus": "Failed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-20-23-03-969",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-20-23-03-969",
            "CreationTime": "2025-05-15T13:23:04.295000-07:00",
            "TrainingEndTime": "2025-05-15T13:23:42.624000-07:00",
            "LastModifiedTime": "2025-05-15T13:23:42.876000-07:00",
            "TrainingJobStatus": "Failed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-15-20-10-40-589",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-15-20-10-40-589",
            "CreationTime": "2025-05-15T13:10:40.813000-07:00",
            "TrainingEndTime": "2025-05-15T13:11:29.653000-07:00",
            "LastModifiedTime": "2025-05-15T13:11:29.886000-07:00",
            "TrainingJobStatus": "Failed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-14-20-51-09-299",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-14-20-51-09-299",
            "CreationTime": "2025-05-14T13:51:09.516000-07:00",
            "TrainingEndTime": "2025-05-14T13:52:13.900000-07:00",
            "LastModifiedTime": "2025-05-14T13:52:14.170000-07:00",
            "TrainingJobStatus": "Failed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-14-20-45-21-878",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-14-20-45-21-878",
            "CreationTime": "2025-05-14T13:45:22.084000-07:00",
            "TrainingEndTime": "2025-05-14T13:45:59.621000-07:00",
            "LastModifiedTime": "2025-05-14T13:46:00.149000-07:00",
            "TrainingJobStatus": "Failed"
        }
    ]
}
tim@Tims-MBP sagemaker % aws sagemaker describe-training-job --training-job-name sagemaker-xgboost-2025-05-16-18-10-50-386
{
    "TrainingJobName": "sagemaker-xgboost-2025-05-16-18-10-50-386",
    "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-16-18-10-50-386",
    "ModelArtifacts": {
        "S3ModelArtifacts": "s3://sagemaker-us-east-1-084375569056/output/sagemaker-xgboost-2025-05-16-18-10-50-386/output/model.tar.gz"
    },
    "TrainingJobStatus": "Completed",
    "SecondaryStatus": "Completed",
    "HyperParameters": {
        "early_stopping_rounds": "10",
        "eta": "0.2",
        "max_depth": "5",
        "num_round": "100",
        "objective": "reg:squarederror",
        "subsample": "0.8"
    },
    "AlgorithmSpecification": {
        "TrainingImage": "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.5-1",
        "TrainingInputMode": "File",
        "MetricDefinitions": [
            {
                "Name": "train:mae",
                "Regex": ".*\\[[0-9]+\\].*#011train-mae:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:gamma-nloglik",
                "Regex": ".*\\[[0-9]+\\].*#011train-gamma-nloglik:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:mae",
                "Regex": ".*\\[[0-9]+\\].*#011validation-mae:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:logloss",
                "Regex": ".*\\[[0-9]+\\].*#011validation-logloss:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:cox-nloglik",
                "Regex": ".*\\[[0-9]+\\].*#011train-cox-nloglik:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:f1",
                "Regex": ".*\\[[0-9]+\\].*#011validation-f1:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:cox-nloglik",
                "Regex": ".*\\[[0-9]+\\].*#011validation-cox-nloglik:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:accuracy",
                "Regex": ".*\\[[0-9]+\\].*#011train-accuracy:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:mse",
                "Regex": ".*\\[[0-9]+\\].*#011train-mse:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:poisson-nloglik",
                "Regex": ".*\\[[0-9]+\\].*#011validation-poisson-nloglik:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:error",
                "Regex": ".*\\[[0-9]+\\].*#011train-error:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:ndcg",
                "Regex": ".*\\[[0-9]+\\].*#011train-ndcg:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:map",
                "Regex": ".*\\[[0-9]+\\].*#011validation-map:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:gamma-deviance",
                "Regex": ".*\\[[0-9]+\\].*#011validation-gamma-deviance:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:error",
                "Regex": ".*\\[[0-9]+\\].*#011validation-error:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:poisson-nloglik",
                "Regex": ".*\\[[0-9]+\\].*#011train-poisson-nloglik:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:rmse",
                "Regex": ".*\\[[0-9]+\\].*#011train-rmse:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:logloss",
                "Regex": ".*\\[[0-9]+\\].*#011train-logloss:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:accuracy",
                "Regex": ".*\\[[0-9]+\\].*#011validation-accuracy:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:rmse",
                "Regex": ".*\\[[0-9]+\\].*#011validation-rmse:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:gamma-deviance",
                "Regex": ".*\\[[0-9]+\\].*#011train-gamma-deviance:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:mse",
                "Regex": ".*\\[[0-9]+\\].*#011validation-mse:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:ndcg",
                "Regex": ".*\\[[0-9]+\\].*#011validation-ndcg:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:f1",
                "Regex": ".*\\[[0-9]+\\].*#011train-f1:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:r2",
                "Regex": ".*\\[[0-9]+\\].*#011validation-r2:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "train:map",
                "Regex": ".*\\[[0-9]+\\].*#011train-map:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            },
            {
                "Name": "validation:gamma-nloglik",
                "Regex": ".*\\[[0-9]+\\].*#011validation-gamma-nloglik:([-+]?[0-9]*\\.?[0-9]+(?:[eE][-+]?[0-9]+)?).*"
            }
        ],
        "EnableSageMakerMetricsTimeSeries": false
    },
    "RoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281",
    "InputDataConfig": [
        {
            "ChannelName": "train",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "s3://sagemaker-us-east-1-084375569056/abalone_train.libsvm",
                    "S3DataDistributionType": "FullyReplicated"
                }
            },
            "CompressionType": "None",
            "RecordWrapperType": "None"
        },
        {
            "ChannelName": "validation",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "s3://sagemaker-us-east-1-084375569056/abalone_validation.libsvm",
                    "S3DataDistributionType": "FullyReplicated"
                }
            },
            "CompressionType": "None",
            "RecordWrapperType": "None"
        }
    ],
    "OutputDataConfig": {
        "KmsKeyId": "",
        "S3OutputPath": "s3://sagemaker-us-east-1-084375569056/output",
        "CompressionType": "GZIP"
    },
    "ResourceConfig": {
        "InstanceType": "ml.m5.large",
        "InstanceCount": 1,
        "VolumeSizeInGB": 30
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": 86400
    },
    "CreationTime": "2025-05-16T11:10:50.603000-07:00",
    "TrainingStartTime": "2025-05-16T11:11:32.239000-07:00",
    "TrainingEndTime": "2025-05-16T11:13:37.265000-07:00",
    "LastModifiedTime": "2025-05-16T11:13:37.530000-07:00",
    "SecondaryStatusTransitions": [
        {
            "Status": "Starting",
            "StartTime": "2025-05-16T11:10:50.603000-07:00",
            "EndTime": "2025-05-16T11:11:32.239000-07:00",
            "StatusMessage": "Preparing the instances for training"
        },
        {
            "Status": "Downloading",
            "StartTime": "2025-05-16T11:11:32.239000-07:00",
            "EndTime": "2025-05-16T11:13:13.943000-07:00",
            "StatusMessage": "Downloading the training image"
        },
        {
            "Status": "Training",
            "StartTime": "2025-05-16T11:13:13.943000-07:00",
            "EndTime": "2025-05-16T11:13:24.505000-07:00",
            "StatusMessage": "Training image download completed. Training in progress."
        },
        {
            "Status": "Uploading",
            "StartTime": "2025-05-16T11:13:24.505000-07:00",
            "EndTime": "2025-05-16T11:13:37.265000-07:00",
            "StatusMessage": "Uploading generated training model"
        },
        {
            "Status": "Completed",
            "StartTime": "2025-05-16T11:13:37.265000-07:00",
            "EndTime": "2025-05-16T11:13:37.265000-07:00",
            "StatusMessage": "Training job completed"
        }
    ],
    "FinalMetricDataList": [
        {
            "MetricName": "train:rmse",
            "Value": 1.1987600326538086,
            "Timestamp": "2025-05-16T11:13:20-07:00"
        },
        {
            "MetricName": "validation:rmse",
            "Value": 2.3155300617218018,
            "Timestamp": "2025-05-16T11:13:20-07:00"
        }
    ],
    "EnableNetworkIsolation": false,
    "EnableInterContainerTrafficEncryption": false,
    "EnableManagedSpotTraining": false,
    "TrainingTimeInSeconds": 125,
    "BillableTimeInSeconds": 125,
    "DebugHookConfig": {
        "S3OutputPath": "s3://sagemaker-us-east-1-084375569056/output",
        "CollectionConfigurations": []
    },
    "ProfilerConfig": {
        "S3OutputPath": "s3://sagemaker-us-east-1-084375569056/output",
        "ProfilingIntervalInMilliseconds": 500,
        "DisableProfiler": false
    },
    "ProfilingStatus": "Enabled"
}
tim@Tims-MBP sagemaker % aws sagemaker list-models
{
    "Models": [
        {
            "ModelName": "sagemaker-xgboost-2025-05-16-18-14-07-995",
            "ModelArn": "arn:aws:sagemaker:us-east-1:084375569056:model/sagemaker-xgboost-2025-05-16-18-14-07-995",
            "CreationTime": "2025-05-16T11:14:08.493000-07:00"
        },
        {
            "ModelName": "sagemaker-xgboost-2025-05-16-17-00-16-559",
            "ModelArn": "arn:aws:sagemaker:us-east-1:084375569056:model/sagemaker-xgboost-2025-05-16-17-00-16-559",
            "CreationTime": "2025-05-16T10:00:17.110000-07:00"
        },
        {
            "ModelName": "sagemaker-xgboost-2025-05-15-22-06-31-961",
            "ModelArn": "arn:aws:sagemaker:us-east-1:084375569056:model/sagemaker-xgboost-2025-05-15-22-06-31-961",
            "CreationTime": "2025-05-15T15:06:32.504000-07:00"
        },
        {
            "ModelName": "sagemaker-xgboost-2025-05-15-21-52-07-049",
            "ModelArn": "arn:aws:sagemaker:us-east-1:084375569056:model/sagemaker-xgboost-2025-05-15-21-52-07-049",
            "CreationTime": "2025-05-15T14:52:07.555000-07:00"
        }
    ]
}
tim@Tims-MBP sagemaker % aws sagemaker describe-model --model-name sagemaker-xgboost-2025-05-16-18-14-07-995
{
    "ModelName": "sagemaker-xgboost-2025-05-16-18-14-07-995",
    "PrimaryContainer": {
        "Image": "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.5-1",
        "Mode": "SingleModel",
        "ModelDataUrl": "s3://sagemaker-us-east-1-084375569056/output/sagemaker-xgboost-2025-05-16-18-10-50-386/output/model.tar.gz",
        "ModelDataSource": {
            "S3DataSource": {
                "S3Uri": "s3://sagemaker-us-east-1-084375569056/output/sagemaker-xgboost-2025-05-16-18-10-50-386/output/model.tar.gz",
                "S3DataType": "S3Object",
                "CompressionType": "Gzip"
            }
        },
        "Environment": {}
    },
    "ExecutionRoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281",
    "CreationTime": "2025-05-16T11:14:08.493000-07:00",
    "ModelArn": "arn:aws:sagemaker:us-east-1:084375569056:model/sagemaker-xgboost-2025-05-16-18-14-07-995",
    "EnableNetworkIsolation": false,
    "DeploymentRecommendation": {
        "RecommendationStatus": "COMPLETED",
        "RealTimeInferenceRecommendations": [
            {
                "RecommendationId": "sagemaker-xgboost-2025-05-16-18-14-07-995/3y2QuB4W",
                "InstanceType": "ml.c6i.xlarge",
                "Environment": {}
            },
            {
                "RecommendationId": "sagemaker-xgboost-2025-05-16-18-14-07-995/wLKHnTyE",
                "InstanceType": "ml.c6i.large",
                "Environment": {}
            },
            {
                "RecommendationId": "sagemaker-xgboost-2025-05-16-18-14-07-995/ZaQeqCfy",
                "InstanceType": "ml.g4dn.2xlarge",
                "Environment": {}
            }
        ]
    }
}
tim@Tims-MBP sagemaker % aws sagemaker list-endpoints
{
    "Endpoints": [
        {
            "EndpointName": "sagemaker-xgboost-2025-05-16-18-14-07-995",
            "EndpointArn": "arn:aws:sagemaker:us-east-1:084375569056:endpoint/sagemaker-xgboost-2025-05-16-18-14-07-995",
            "CreationTime": "2025-05-16T11:14:09.475000-07:00",
            "LastModifiedTime": "2025-05-16T11:18:38.509000-07:00",
            "EndpointStatus": "InService"
        },
        {
            "EndpointName": "sagemaker-xgboost-2025-05-16-17-00-16-559",
            "EndpointArn": "arn:aws:sagemaker:us-east-1:084375569056:endpoint/sagemaker-xgboost-2025-05-16-17-00-16-559",
            "CreationTime": "2025-05-16T10:00:17.918000-07:00",
            "LastModifiedTime": "2025-05-16T10:04:47.474000-07:00",
            "EndpointStatus": "InService"
        }
    ]
}
tim@Tims-MBP sagemaker % aws sagemaker describe-endpoint --endpoint-name sagemaker-xgboost-2025-05-16-18-14-07-995
{
    "EndpointName": "sagemaker-xgboost-2025-05-16-18-14-07-995",
    "EndpointArn": "arn:aws:sagemaker:us-east-1:084375569056:endpoint/sagemaker-xgboost-2025-05-16-18-14-07-995",
    "EndpointConfigName": "sagemaker-xgboost-2025-05-16-18-14-07-995",
    "ProductionVariants": [
        {
            "VariantName": "AllTraffic",
            "DeployedImages": [
                {
                    "SpecifiedImage": "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.5-1",
                    "ResolvedImage": "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost@sha256:c764382b16cd0c921f1b2e66de8684fb999ccbd0c042c95679f0b69bc9cdd12c",
                    "ResolutionTime": "2025-05-16T11:14:10.180000-07:00"
                }
            ],
            "CurrentWeight": 1.0,
            "DesiredWeight": 1.0,
            "CurrentInstanceCount": 1,
            "DesiredInstanceCount": 1
        }
    ],
    "EndpointStatus": "InService",
    "CreationTime": "2025-05-16T11:14:09.475000-07:00",
    "LastModifiedTime": "2025-05-16T11:18:38.509000-07:00"
}
tim@Tims-MBP sagemaker % aws s3 ls
2025-05-14 12:34:17 amazon-braket-my-quantum-output-20250514-kerstarsoc
2025-05-15 15:32:54 amazon-braket-us-east-1-084375569056
2025-05-13 20:42:20 sagemaker-studio-084375569056-jznb41g5nl
2025-05-13 20:42:22 sagemaker-us-east-1-084375569056
tim@Tims-MBP sagemaker % aws s3 ls s3://sagemaker-us-east-1-084375569056 --recursive | grep sagemaker
2025-05-15 13:57:33          0 output/sagemaker-xgboost-2025-05-15-20-54-48-578/debug-output/training_job_end.ts
2025-05-15 13:57:33          0 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/framework/training_job_end.ts
2025-05-15 13:57:01      64940 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/incremental/2025051520/1747342500.algo-1.json
2025-05-15 13:57:00     184399 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/incremental/2025051520/1747342560.algo-1.json
2025-05-15 13:57:31      92383 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/incremental/2025051520/1747342620.algo-1.json
2025-05-15 13:57:33          0 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/training_job_end.ts
2025-05-15 14:08:31          0 output/sagemaker-xgboost-2025-05-15-21-05-47-954/debug-output/training_job_end.ts
2025-05-15 14:08:31          0 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/framework/training_job_end.ts
2025-05-15 14:08:01      86465 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/incremental/2025051521/1747343160.algo-1.json
2025-05-15 14:08:00     184363 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/incremental/2025051521/1747343220.algo-1.json
2025-05-15 14:08:29      87766 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/incremental/2025051521/1747343280.algo-1.json
2025-05-15 14:08:31          0 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/training_job_end.ts
2025-05-15 14:16:16          0 output/sagemaker-xgboost-2025-05-15-21-13-39-500/debug-output/training_job_end.ts
2025-05-15 14:16:16          0 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/framework/training_job_end.ts
2025-05-15 14:16:01     125018 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/incremental/2025051521/1747343640.algo-1.json
2025-05-15 14:16:00     184456 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/incremental/2025051521/1747343700.algo-1.json
2025-05-15 14:16:13      40044 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/incremental/2025051521/1747343760.algo-1.json
2025-05-15 14:16:16          0 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/training_job_end.ts
2025-05-15 14:23:44          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/claim.smd
2025-05-15 14:23:44       6257 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 14:23:44        104 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 14:23:44        219 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 14:23:59          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/training_job_end.ts
2025-05-15 14:23:58      80685 output/sagemaker-xgboost-2025-05-15-21-21-10-815/output/model.tar.gz
2025-05-15 14:23:59          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/framework/training_job_end.ts
2025-05-15 14:23:01      24788 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/incremental/2025051521/1747344060.algo-1.json
2025-05-15 14:23:00     184799 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/incremental/2025051521/1747344120.algo-1.json
2025-05-15 14:23:54     166212 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/incremental/2025051521/1747344180.algo-1.json
2025-05-15 14:23:59          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/training_job_end.ts
2025-05-15 14:33:07          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/claim.smd
2025-05-15 14:33:07       6276 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 14:33:07        218 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 14:33:07        287 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 14:33:22          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/training_job_end.ts
2025-05-15 14:33:21      80687 output/sagemaker-xgboost-2025-05-15-21-30-38-685/output/model.tar.gz
2025-05-15 14:33:22          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/framework/training_job_end.ts
2025-05-15 14:33:01     126519 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/incremental/2025051521/1747344660.algo-1.json
2025-05-15 14:33:00     184510 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/incremental/2025051521/1747344720.algo-1.json
2025-05-15 14:33:17      52439 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/incremental/2025051521/1747344780.algo-1.json
2025-05-15 14:33:22          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/training_job_end.ts
2025-05-15 14:51:16          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/claim.smd
2025-05-15 14:51:15       6276 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 14:51:15        218 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 14:51:15        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 14:51:15        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 14:51:16        287 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 14:51:15        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 14:51:15        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 14:51:15        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 14:51:30          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/training_job_end.ts
2025-05-15 14:51:29      80687 output/sagemaker-xgboost-2025-05-15-21-48-49-811/output/model.tar.gz
2025-05-15 14:51:30          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/framework/training_job_end.ts
2025-05-15 14:51:01      83387 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/incremental/2025051521/1747345740.algo-1.json
2025-05-15 14:51:00     184427 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/incremental/2025051521/1747345800.algo-1.json
2025-05-15 14:51:26      77070 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/incremental/2025051521/1747345860.algo-1.json
2025-05-15 14:51:30          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/training_job_end.ts
2025-05-15 15:05:42          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/claim.smd
2025-05-15 15:05:42       6276 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 15:05:42        218 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 15:05:42        287 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 15:05:56          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/training_job_end.ts
2025-05-15 15:05:56      82132 output/sagemaker-xgboost-2025-05-15-22-03-14-706/output/model.tar.gz
2025-05-15 15:05:56          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/framework/training_job_end.ts
2025-05-15 15:05:01      15543 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/incremental/2025051522/1747346580.algo-1.json
2025-05-15 15:05:00     184588 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/incremental/2025051522/1747346640.algo-1.json
2025-05-15 15:05:52     158553 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/incremental/2025051522/1747346700.algo-1.json
2025-05-15 15:05:56          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/training_job_end.ts
2025-05-15 15:38:07          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/claim.smd
2025-05-15 15:38:07       6276 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 15:38:07        218 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 15:38:07        287 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 15:38:21          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/training_job_end.ts
2025-05-15 15:38:21      82135 output/sagemaker-xgboost-2025-05-15-22-35-37-193/output/model.tar.gz
2025-05-15 15:38:21          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/framework/training_job_end.ts
2025-05-15 15:38:01     115626 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/incremental/2025051522/1747348560.algo-1.json
2025-05-15 15:38:00     184509 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/incremental/2025051522/1747348620.algo-1.json
2025-05-15 15:38:17      50886 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/incremental/2025051522/1747348680.algo-1.json
2025-05-15 15:38:21          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/training_job_end.ts
2025-05-16 09:55:17          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/claim.smd
2025-05-16 09:55:17       6276 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/collections/000000000/worker_0_collections.json
2025-05-16 09:55:17        218 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-16 09:55:17        287 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000000_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000010_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000020_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000030_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000040_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000050_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000060_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000070_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000080_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000090_worker_0.json
2025-05-16 09:55:33          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/training_job_end.ts
2025-05-16 09:55:31      82136 output/sagemaker-xgboost-2025-05-16-16-52-51-977/output/model.tar.gz
2025-05-16 09:55:33          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/framework/training_job_end.ts
2025-05-16 09:55:01      81927 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/incremental/2025051616/1747414380.algo-1.json
2025-05-16 09:55:00     184478 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/incremental/2025051616/1747414440.algo-1.json
2025-05-16 09:55:27      81698 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/incremental/2025051616/1747414500.algo-1.json
2025-05-16 09:55:33          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/training_job_end.ts
2025-05-16 09:59:26          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/claim.smd
2025-05-16 09:59:26       6276 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/collections/000000000/worker_0_collections.json
2025-05-16 09:59:26        218 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-16 09:59:26        287 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000000_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000010_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000020_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000030_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000040_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000050_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000060_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000070_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000080_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000090_worker_0.json
2025-05-16 09:59:40          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/training_job_end.ts
2025-05-16 09:59:39      82138 output/sagemaker-xgboost-2025-05-16-16-56-59-277/output/model.tar.gz
2025-05-16 09:59:40          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/framework/training_job_end.ts
2025-05-16 09:59:01      61844 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/incremental/2025051616/1747414620.algo-1.json
2025-05-16 09:59:00     184462 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/incremental/2025051616/1747414680.algo-1.json
2025-05-16 09:59:36     107828 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/incremental/2025051616/1747414740.algo-1.json
2025-05-16 09:59:40          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/training_job_end.ts
2025-05-16 11:13:21          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/claim.smd
2025-05-16 11:13:21       6276 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/collections/000000000/worker_0_collections.json
2025-05-16 11:13:21        218 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-16 11:13:21        287 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000000_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000010_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000020_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000030_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000040_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000050_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000060_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000070_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000080_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000090_worker_0.json
2025-05-16 11:13:35          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/training_job_end.ts
2025-05-16 11:13:35      82134 output/sagemaker-xgboost-2025-05-16-18-10-50-386/output/model.tar.gz
2025-05-16 11:13:35          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/framework/training_job_end.ts
2025-05-16 11:13:01      80321 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/incremental/2025051618/1747419060.algo-1.json
2025-05-16 11:13:00     184418 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/incremental/2025051618/1747419120.algo-1.json
2025-05-16 11:13:31      94001 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/incremental/2025051618/1747419180.algo-1.json
2025-05-16 11:13:35          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/training_job_end.ts

tim@Tims-MBP sagemaker % aws s3 ls s3://amazon-braket-us-east-1-084375569056 --recursive        
2025-05-15 15:32:54       1667 jobs/run-ghz-hybrid-1747348372775/1747348373051/script/source.tar.gz
2025-05-15 15:42:40       1663 jobs/run-ghz-hybrid-1747348958737/1747348958977/script/source.tar.gz
2025-05-15 15:45:15       1662 jobs/run-ghz-hybrid-1747349113804/1747349114061/script/source.tar.gz
2025-05-15 15:49:58       1661 jobs/run-ghz-hybrid-1747349396435/1747349396678/script/source.tar.gz
2025-05-15 15:55:08       1663 jobs/run-ghz-hybrid-1747349706700/1747349706931/script/source.tar.gz
2025-05-15 16:00:04       1667 jobs/run-ghz-hybrid-1747350001932/1747350002615/script/source.tar.gz
2025-05-15 16:00:53       1663 jobs/run-ghz-hybrid-1747350051923/1747350052171/script/source.tar.gz
2025-05-15 16:17:50        353 jobs/run-ghz-hybrid/1747350952265/data/output/model.tar.gz
2025-05-15 16:15:53       1660 jobs/run-ghz-hybrid/1747350952265/script/source.tar.gz
2025-05-16 10:23:37        352 jobs/run-ghz-hybrid/1747416094973/data/output/model.tar.gz
2025-05-16 10:21:36       1660 jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz
2025-05-16 10:23:21      66862 jobs/run-ghz-hybrid/tasks/012fe2d6-77cb-4430-9f13-2a52de2d1cac/results.json
2025-05-15 16:17:32      66862 jobs/run-ghz-hybrid/tasks/312b6499-b2fa-443d-bcdc-750d8dd3e94d/results.json
tim@Tims-MBP sagemaker % aws sagemaker list-notebook-instances | grep braket
            "NotebookInstanceName": "amazon-braket-my-sagemaker-data-2025",
            "NotebookInstanceArn": "arn:aws:sagemaker:us-east-1:084375569056:notebook-instance/amazon-braket-my-sagemaker-data-2025",
            "Url": "amazon-braket-my-sagemaker-data-2025.notebook.us-east-1.sagemaker.aws",
            "NotebookInstanceLifecycleConfigName": "amazon-braket-my-sagemaker-data-2025"


tim@Tims-MBP sagemaker % aws ec2 describe-instances --filters "Name=tag:braket,Values=*" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}"
[]
tim@Tims-MBP sagemaker % aws iam list-roles | grep -E 'SageMaker|Braket'
            "RoleName": "AmazonBraketJobsExecutionRole",
            "Arn": "arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
            "RoleName": "AmazonBraketServiceSageMakerNotebookRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonBraketServiceSageMakerNotebookRole",
            "RoleName": "AmazonSageMaker-ExecutionRole-20250513T204281",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281",
            "Description": "SageMaker execution role created from the SageMaker AWS Management Console.",
            "RoleName": "AmazonSageMakerCanvasEMRSExecutionAccess-20250513T204280",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerCanvasEMRSExecutionAccess-20250513T204280",
            "RoleName": "AmazonSageMakerServiceCatalogProductsApiGatewayRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsApiGatewayRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS ApiGateway within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsCloudformationRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsCloudformationRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS CloudFormation within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsCodeBuildRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsCodeBuildRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS CodeBuild within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsCodePipelineRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsCodePipelineRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS CodePipeline within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsEventsRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsEventsRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS Events within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsExecutionRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsExecutionRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS SageMaker within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsFirehoseRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsFirehoseRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS Firehose within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsGlueRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsGlueRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS Glue within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsLambdaRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsLambdaRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role will grant permissions required to use AWS Lambda within the Amazon SageMaker portfolio of products.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsLaunchRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsLaunchRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role has the permissions required to launch the Amazon SageMaker portfolio of products from AWS ServiceCatalog.",
            "RoleName": "AmazonSageMakerServiceCatalogProductsUseRole",
            "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerServiceCatalogProductsUseRole",
            "Description": "SageMaker role created from the SageMaker AWS Management Console. This role has the permissions required to use the Amazon SageMaker portfolio of products from AWS ServiceCatalog.",
            "RoleName": "AWSServiceRoleForAmazonBraket",
            "Arn": "arn:aws:iam::084375569056:role/aws-service-role/braket.amazonaws.com/AWSServiceRoleForAmazonBraket",
            "RoleName": "AWSServiceRoleForAmazonSageMakerNotebooks",
            "Arn": "arn:aws:iam::084375569056:role/aws-service-role/sagemaker.amazonaws.com/AWSServiceRoleForAmazonSageMakerNotebooks",
            "Description": "AWS SageMaker Notebooks Service Linked Role",
tim@Tims-MBP sagemaker % aws iam get-role --role-name AmazonBraketJobsExecutionRole
{
    "Role": {
        "Path": "/",
        "RoleName": "AmazonBraketJobsExecutionRole",
        "RoleId": "AROARHJJNAKQIEU7RBKFV",
        "Arn": "arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
        "CreateDate": "2025-05-15T22:27:59+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "braket.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "MaxSessionDuration": 3600,
        "RoleLastUsed": {
            "LastUsedDate": "2025-05-16T17:23:36+00:00",
            "Region": "us-east-1"
        }
    }
}
tim@Tims-MBP sagemaker % aws iam list-attached-role-policies --role-name AWSServiceRoleForAmazonBraket
{
    "AttachedPolicies": [
        {
            "PolicyName": "AmazonBraketServiceRolePolicy",
            "PolicyArn": "arn:aws:iam::aws:policy/aws-service-role/AmazonBraketServiceRolePolicy"
        }
    ]
}
tim@Tims-MBP sagemaker % aws iam list-policies | grep PolicyName | wc -l
    1360
tim@Tims-MBP sagemaker % aws iam list-policies          
{
    "Policies": [
        {
            "PolicyName": "AmazonBraketServiceSageMakerNotebookRole",
            "PolicyId": "ANPARHJJNAKQKORAZKOCB",
            "Arn": "arn:aws:iam::084375569056:policy/service-role/AmazonBraketServiceSageMakerNotebookRole",
            "Path": "/service-role/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 1,
            "PermissionsBoundaryUsageCount": 0,
            "IsAttachable": true,
            "CreateDate": "2025-05-14T18:19:10+00:00",
            "UpdateDate": "2025-05-14T18:19:10+00:00"
        },
        {
            "PolicyName": "AmazonSageMaker-ExecutionPolicy-20250513T204281",
            "PolicyId": "ANPARHJJNAKQE2SGFNCFU",
            "Arn": "arn:aws:iam::084375569056:policy/service-role/AmazonSageMaker-ExecutionPolicy-20250513T204281",
            "Path": "/service-role/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 1,
            "PermissionsBoundaryUsageCount": 0,
            "IsAttachable": true,
            "CreateDate": "2025-05-14T03:42:14+00:00",
            "UpdateDate": "2025-05-14T03:42:14+00:00"
        },
        {
            "PolicyName": "AmazonSageMakerServiceCatalogProductsUseRole-20250513T204239",
            "PolicyId": "ANPARHJJNAKQNSEUIA4B3",
            "Arn": "arn:aws:iam::084375569056:policy/service-role/AmazonSageMakerServiceCatalogProductsUseRole-20250513T204239",
            "Path": "/service-role/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 1,
            "PermissionsBoundaryUsageCount": 0,
            "IsAttachable": true,
            "CreateDate": "2025-05-14T03:42:27+00:00",
            "UpdateDate": "2025-05-14T03:42:27+00:00"
        },

tim@Tims-MBP sagemaker % aws iam get-policy --policy-arn arn:aws:iam::084375569056:policy/service-role/AmazonSageMakerServiceCatalogProductsUseRole-20250513T204239
{
    "Policy": {
        "PolicyName": "AmazonSageMakerServiceCatalogProductsUseRole-20250513T204239",
        "PolicyId": "ANPARHJJNAKQNSEUIA4B3",
        "Arn": "arn:aws:iam::084375569056:policy/service-role/AmazonSageMakerServiceCatalogProductsUseRole-20250513T204239",
        "Path": "/service-role/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 1,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2025-05-14T03:42:27+00:00",
        "UpdateDate": "2025-05-14T03:42:27+00:00",
        "Tags": []
    }
}
tim@Tims-MBP sagemaker % aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "bluedragon",
            "UserId": "AIDARHJJNAKQBXQUGMWXF",
            "Arn": "arn:aws:iam::084375569056:user/bluedragon",
            "CreateDate": "2024-12-13T20:45:50+00:00",
            "PasswordLastUsed": "2025-05-16T16:22:34+00:00"
        }
    ]
}
tim@Tims-MBP sagemaker % aws iam list-attached-user-policies --user-name bluedragon
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "AmazonEKSClusterPolicy",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
        },
        {
            "PolicyName": "IAMUserChangePassword",
            "PolicyArn": "arn:aws:iam::aws:policy/IAMUserChangePassword"
        },
        {
            "PolicyName": "AmazonEKSWorkerNodePolicy",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
        }
    ]
}

tim@Tims-MBP quantum_circuit % aws braket get-quantum-task --quantum-task-arn arn:aws:braket:us-east-1:084375569056:quantum-task/012fe2d6-77cb-4430-9f13-2a52de2d1cac
{
    "createdAt": "2025-05-16T17:23:19.107000+00:00",
    "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
    "deviceParameters": "{\"braketSchemaHeader\": {\"name\": \"braket.device_schema.simulators.gate_model_simulator_device_parameters\", \"version\": \"1\"}, \"paradigmParameters\": {\"braketSchemaHeader\": {\"name\": \"braket.device_schema.gate_model_parameters\", \"version\": \"1\"}, \"qubitCount\": 3, \"disableQubitRewiring\": false}}",
    "endedAt": "2025-05-16T17:23:20.613000+00:00",
    "jobArn": "arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10",
    "outputS3Bucket": "amazon-braket-us-east-1-084375569056",
    "outputS3Directory": "jobs/run-ghz-hybrid/tasks/012fe2d6-77cb-4430-9f13-2a52de2d1cac",
    "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/012fe2d6-77cb-4430-9f13-2a52de2d1cac",
    "shots": 1000,
    "status": "COMPLETED",
    "tags": {}
}

tim@Tims-MBP quantum_circuit % aws braket get-device --device-arn arn:aws:braket:::device/quantum-simulator/amazon/sv1 | jq .
{
  "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
  "deviceCapabilities": "{\"service\": {\"braketSchemaHeader\": {\"name\": \"braket.device_schema.device_service_properties\", \"version\": \"1\"}, \"executionWindows\": [{\"executionDay\": \"Everyday\", \"windowStartHour\": \"00:00:00\", \"windowEndHour\": \"23:59:59\"}], \"shotsRange\": [0, 100000], \"deviceCost\": {\"price\": 0.075, \"unit\": \"minute\"}, \"deviceDocumentation\": {\"imageUrl\": \"https://d1.awsstatic.com/about-aws/whats-new/lpm-assets/services/SiteMerch_Qx_Editorial-reInvent.d5a91c3e3fa666a2c33b8a912c21d1cb4ef270fb.png\", \"summary\": \"Amazon Braket state vector simulator\", \"externalDocumentationUrl\": \"https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html#choose-a-simulator\"}, \"updatedAt\": \"2022-06-22T10:18:00\"}, \"action\": {\"braket.ir.jaqcd.program\": {\"version\": [\"1.0\", \"1.1\"], \"actionType\": \"braket.ir.jaqcd.program\", \"supportedOperations\": [\"ccnot\", \"cnot\", \"cphaseshift\", \"cphaseshift00\", \"cphaseshift01\", \"cphaseshift10\", \"cswap\", \"cy\", \"cz\", \"ecr\", \"h\", \"i\", \"iswap\", \"pswap\", \"phaseshift\", \"rx\", \"ry\", \"rz\", \"s\", \"si\", \"swap\", \"t\", \"ti\", \"unitary\", \"v\", \"vi\", \"x\", \"xx\", \"xy\", \"y\", \"yy\", \"z\", \"zz\"], \"supportedResultTypes\": [{\"name\": \"Sample\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\", \"hermitian\"], \"minShots\": 1, \"maxShots\": 100000}, {\"name\": \"Expectation\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\", \"hermitian\"], \"minShots\": 0, \"maxShots\": 100000}, {\"name\": \"Variance\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\", \"hermitian\"], \"minShots\": 0, \"maxShots\": 100000}, {\"name\": \"Probability\", \"minShots\": 1, \"maxShots\": 100000}, {\"name\": \"Amplitude\", \"minShots\": 0, \"maxShots\": 0}]}, \"braket.ir.openqasm.program\": {\"version\": [\"1.0\"], \"actionType\": \"braket.ir.openqasm.program\", \"supportedOperations\": [\"ccnot\", \"cnot\", \"cphaseshift\", \"cphaseshift00\", \"cphaseshift01\", \"cphaseshift10\", \"cswap\", \"cy\", \"cz\", \"ecr\", \"h\", \"i\", \"iswap\", \"pswap\", \"phaseshift\", \"rx\", \"ry\", \"rz\", \"s\", \"si\", \"swap\", \"t\", \"ti\", \"v\", \"vi\", \"x\", \"xx\", \"xy\", \"y\", \"yy\", \"z\", \"zz\", \"gpi\", \"gpi2\", \"ms\"], \"supportedPragmas\": [\"braket_unitary_matrix\", \"braket_basis_rotation\", \"braket_result_type_sample\", \"braket_result_type_expectation\", \"braket_result_type_variance\", \"braket_result_type_probability\", \"braket_result_type_amplitude\", \"braket_result_type_adjoint_gradient\"], \"forbiddenPragmas\": [\"braket_result_type_state_vector\", \"braket_result_type_density_matrix\", \"braket_noise_amplitude_damping\", \"braket_noise_bit_flip\", \"braket_noise_depolarizing\", \"braket_noise_kraus\", \"braket_noise_pauli_channel\", \"braket_noise_generalized_amplitude_damping\", \"braket_noise_phase_flip\", \"braket_noise_phase_damping\", \"braket_noise_two_qubit_dephasing\", \"braket_noise_two_qubit_depolarizing\"], \"maximumQubitArrays\": 1, \"maximumClassicalArrays\": 1, \"forbiddenArrayOperations\": [\"concatenation\", \"negativeIndex\", \"range\", \"rangeWithStep\", \"slicing\", \"selection\"], \"requiresAllQubitsMeasurement\": true, \"supportPhysicalQubits\": false, \"requiresContiguousQubitIndices\": true, \"supportsPartialVerbatimBox\": true, \"supportsUnassignedMeasurements\": true, \"disabledQubitRewiringSupported\": false, \"supportedResultTypes\": [{\"name\": \"Sample\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\", \"hermitian\"], \"minShots\": 1, \"maxShots\": 100000}, {\"name\": \"Expectation\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\", \"hermitian\"], \"minShots\": 0, \"maxShots\": 100000}, {\"name\": \"Variance\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\", \"hermitian\"], \"minShots\": 0, \"maxShots\": 100000}, {\"name\": \"Probability\", \"minShots\": 1, \"maxShots\": 100000}, {\"name\": \"Amplitude\", \"minShots\": 0, \"maxShots\": 0}, {\"name\": \"AdjointGradient\", \"observables\": [\"x\", \"y\", \"z\", \"h\", \"i\"], \"minShots\": 0, \"maxShots\": 0}]}}, \"deviceParameters\": {\"title\": \"GateModelSimulatorDeviceParameters\", \"description\": \"This defines the parameters common to all the gatemodel devices.\\n\\nAttributes:\\n    paradigmParameters: Parameters that are common to gatemodel paradigm\\n\\nExamples:\\n    >>> import json\\n    >>> input_json = {\\n    ...    \\\"braketSchemaHeader\\\": {\\n    ...        \\\"name\\\": \\\"braket.device_schema.simulators.gate_model_simulator_device_parameters\\\",\\n    ...        \\\"version\\\": \\\"1\\\",\\n    ...    },\\n    ...    \\\"paradigmParameters\\\": {\\\"braketSchemaHeader\\\": {\\n    ...        \\\"name\\\": \\\"braket.device_schema.gate_model_parameters\\\",\\n    ...        \\\"version\\\": \\\"1\\\",\\n    ...    },\\\"qubitCount\\\": 1},\\n    ... }\\n    >>> GateModelSimulatorDeviceParameters.parse_raw_schema(json.dumps(input_json))\", \"type\": \"object\", \"properties\": {\"braketSchemaHeader\": {\"title\": \"Braketschemaheader\", \"const\": {\"name\": \"braket.device_schema.simulators.gate_model_simulator_device_parameters\", \"version\": \"1\"}}, \"paradigmParameters\": {\"$ref\": \"#/definitions/GateModelParameters\"}}, \"required\": [\"paradigmParameters\"], \"definitions\": {\"GateModelParameters\": {\"title\": \"GateModelParameters\", \"description\": \"This defines the parameters common to all the gatemodel devices.\\n\\nAttributes:\\n    qubitCount: number of qubits for a device\\n\\nExamples:\\n    >>> import json\\n    >>> input_json = {\\n    ...    \\\"braketSchemaHeader\\\": {\\n    ...        \\\"name\\\": \\\"braket.device_schema.gate_model_parameters\\\",\\n    ...        \\\"version\\\": \\\"1\\\",\\n    ...    },\\n    ...    \\\"qubitCount\\\": 1\\n    ... }\\n    >>> GateModelParameters.parse_raw_schema(json.dumps(input_json))\", \"type\": \"object\", \"properties\": {\"braketSchemaHeader\": {\"title\": \"Braketschemaheader\", \"const\": {\"name\": \"braket.device_schema.gate_model_parameters\", \"version\": \"1\"}}, \"qubitCount\": {\"title\": \"Qubitcount\", \"exclusiveMinimum\": 0, \"type\": \"integer\"}}, \"required\": [\"qubitCount\"]}}}, \"braketSchemaHeader\": {\"name\": \"braket.device_schema.simulators.gate_model_simulator_device_capabilities\", \"version\": \"1\"}, \"paradigm\": {\"braketSchemaHeader\": {\"name\": \"braket.device_schema.simulators.gate_model_simulator_paradigm_properties\", \"version\": \"1\"}, \"qubitCount\": 34}}",
  "deviceName": "SV1",
  "deviceQueueInfo": [
    {
      "queue": "QUANTUM_TASKS_QUEUE",
      "queuePriority": "Normal",
      "queueSize": "0"
    },
    {
      "queue": "QUANTUM_TASKS_QUEUE",
      "queuePriority": "Priority",
      "queueSize": "0"
    },
    {
      "queue": "JOBS_QUEUE",
      "queueSize": "0"
    }
  ],
  "deviceStatus": "ONLINE",
  "deviceType": "SIMULATOR",
  "providerName": "Amazon Braket"
}
tim@Tims-MBP quantum_circuit % 

tim@Tims-MBP quantum_circuit % aws sagemaker list-notebook-instances --query 'NotebookInstances[?contains(NotebookInstanceName, `braket`)]'
[
    {
        "NotebookInstanceName": "amazon-braket-my-sagemaker-data-2025",
        "NotebookInstanceArn": "arn:aws:sagemaker:us-east-1:084375569056:notebook-instance/amazon-braket-my-sagemaker-data-2025",
        "NotebookInstanceStatus": "InService",
        "Url": "amazon-braket-my-sagemaker-data-2025.notebook.us-east-1.sagemaker.aws",
        "InstanceType": "ml.t3.medium",
        "CreationTime": "2025-05-14T11:19:12.370000-07:00",
        "LastModifiedTime": "2025-05-14T11:24:06.168000-07:00",
        "NotebookInstanceLifecycleConfigName": "amazon-braket-my-sagemaker-data-2025"
    }
]

tim@Tims-MBP quantum_circuit % aws sagemaker list-tags --resource-arn arn:aws:sagemaker:us-east-1:084375569056:notebook-instance/amazon-braket-my-sagemaker-data-2025
{
    "Tags": []
}

tim@Tims-MBP quantum_circuit % aws ec2 describe-instances --filters "Name=tag:aws:autoscaling:groupName,Values=*SageMaker*" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}"
[]

tim@Tims-MBP quantum_circuit % aws ec2 describe-instances --filters "Name=tag:created-by,Values=Braket" --query "Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Tags:Tags}"
[]

tim@Tims-MBP quantum_circuit % aws s3 ls s3://amazon-braket-us-east-1-084375569056/ --recursive
2025-05-15 15:32:54       1667 jobs/run-ghz-hybrid-1747348372775/1747348373051/script/source.tar.gz
2025-05-15 15:42:40       1663 jobs/run-ghz-hybrid-1747348958737/1747348958977/script/source.tar.gz
2025-05-15 15:45:15       1662 jobs/run-ghz-hybrid-1747349113804/1747349114061/script/source.tar.gz
2025-05-15 15:49:58       1661 jobs/run-ghz-hybrid-1747349396435/1747349396678/script/source.tar.gz
2025-05-15 15:55:08       1663 jobs/run-ghz-hybrid-1747349706700/1747349706931/script/source.tar.gz
2025-05-15 16:00:04       1667 jobs/run-ghz-hybrid-1747350001932/1747350002615/script/source.tar.gz
2025-05-15 16:00:53       1663 jobs/run-ghz-hybrid-1747350051923/1747350052171/script/source.tar.gz
2025-05-15 16:17:50        353 jobs/run-ghz-hybrid/1747350952265/data/output/model.tar.gz
2025-05-15 16:15:53       1660 jobs/run-ghz-hybrid/1747350952265/script/source.tar.gz
2025-05-16 10:23:37        352 jobs/run-ghz-hybrid/1747416094973/data/output/model.tar.gz
2025-05-16 10:21:36       1660 jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz
2025-05-16 10:23:21      66862 jobs/run-ghz-hybrid/tasks/012fe2d6-77cb-4430-9f13-2a52de2d1cac/results.json
2025-05-15 16:17:32      66862 jobs/run-ghz-hybrid/tasks/312b6499-b2fa-443d-bcdc-750d8dd3e94d/results.json

tim@Tims-MBP quantum_circuit % aws s3 ls s3://sagemaker-us-east-1-084375569056/ --recursive
2025-05-14 13:49:20     191873 abalone.csv
2025-05-15 14:13:40     191879 abalone_preprocessed.csv
2025-05-15 14:48:50     275418 abalone_preprocessed.libsvm
2025-05-16 11:10:51     220237 abalone_train.libsvm
2025-05-16 11:10:51      55180 abalone_validation.libsvm
2025-05-14 11:23:28      28510 data/corpus.txt
2025-05-16 09:37:29      15255 measurement_counts_eb234307.png
2025-05-16 11:10:50      14947 measurement_counts_ghz.png
2025-05-15 13:57:33          0 output/sagemaker-xgboost-2025-05-15-20-54-48-578/debug-output/training_job_end.ts
2025-05-15 13:57:33          0 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/framework/training_job_end.ts
2025-05-15 13:57:01      64940 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/incremental/2025051520/1747342500.algo-1.json
2025-05-15 13:57:00     184399 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/incremental/2025051520/1747342560.algo-1.json
2025-05-15 13:57:31      92383 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/incremental/2025051520/1747342620.algo-1.json
2025-05-15 13:57:33          0 output/sagemaker-xgboost-2025-05-15-20-54-48-578/profiler-output/system/training_job_end.ts
2025-05-15 14:08:31          0 output/sagemaker-xgboost-2025-05-15-21-05-47-954/debug-output/training_job_end.ts
2025-05-15 14:08:31          0 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/framework/training_job_end.ts
2025-05-15 14:08:01      86465 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/incremental/2025051521/1747343160.algo-1.json
2025-05-15 14:08:00     184363 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/incremental/2025051521/1747343220.algo-1.json
2025-05-15 14:08:29      87766 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/incremental/2025051521/1747343280.algo-1.json
2025-05-15 14:08:31          0 output/sagemaker-xgboost-2025-05-15-21-05-47-954/profiler-output/system/training_job_end.ts
2025-05-15 14:16:16          0 output/sagemaker-xgboost-2025-05-15-21-13-39-500/debug-output/training_job_end.ts
2025-05-15 14:16:16          0 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/framework/training_job_end.ts
2025-05-15 14:16:01     125018 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/incremental/2025051521/1747343640.algo-1.json
2025-05-15 14:16:00     184456 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/incremental/2025051521/1747343700.algo-1.json
2025-05-15 14:16:13      40044 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/incremental/2025051521/1747343760.algo-1.json
2025-05-15 14:16:16          0 output/sagemaker-xgboost-2025-05-15-21-13-39-500/profiler-output/system/training_job_end.ts
2025-05-15 14:23:44          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/claim.smd
2025-05-15 14:23:44       6257 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 14:23:44        104 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 14:23:44        107 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 14:23:44        219 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 14:23:44        220 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 14:23:59          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/debug-output/training_job_end.ts
2025-05-15 14:23:58      80685 output/sagemaker-xgboost-2025-05-15-21-21-10-815/output/model.tar.gz
2025-05-15 14:23:59          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/framework/training_job_end.ts
2025-05-15 14:23:01      24788 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/incremental/2025051521/1747344060.algo-1.json
2025-05-15 14:23:00     184799 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/incremental/2025051521/1747344120.algo-1.json
2025-05-15 14:23:54     166212 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/incremental/2025051521/1747344180.algo-1.json
2025-05-15 14:23:59          0 output/sagemaker-xgboost-2025-05-15-21-21-10-815/profiler-output/system/training_job_end.ts
2025-05-15 14:33:07          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/claim.smd
2025-05-15 14:33:07       6276 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 14:33:07        218 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 14:33:07        224 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 14:33:07        287 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 14:33:07        288 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 14:33:22          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/debug-output/training_job_end.ts
2025-05-15 14:33:21      80687 output/sagemaker-xgboost-2025-05-15-21-30-38-685/output/model.tar.gz
2025-05-15 14:33:22          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/framework/training_job_end.ts
2025-05-15 14:33:01     126519 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/incremental/2025051521/1747344660.algo-1.json
2025-05-15 14:33:00     184510 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/incremental/2025051521/1747344720.algo-1.json
2025-05-15 14:33:17      52439 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/incremental/2025051521/1747344780.algo-1.json
2025-05-15 14:33:22          0 output/sagemaker-xgboost-2025-05-15-21-30-38-685/profiler-output/system/training_job_end.ts
2025-05-15 14:51:16          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/claim.smd
2025-05-15 14:51:15       6276 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 14:51:15        218 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 14:51:15        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 14:51:15        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 14:51:16        224 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 14:51:16        287 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 14:51:15        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 14:51:15        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 14:51:15        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 14:51:16        288 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 14:51:30          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/debug-output/training_job_end.ts
2025-05-15 14:51:29      80687 output/sagemaker-xgboost-2025-05-15-21-48-49-811/output/model.tar.gz
2025-05-15 14:51:30          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/framework/training_job_end.ts
2025-05-15 14:51:01      83387 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/incremental/2025051521/1747345740.algo-1.json
2025-05-15 14:51:00     184427 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/incremental/2025051521/1747345800.algo-1.json
2025-05-15 14:51:26      77070 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/incremental/2025051521/1747345860.algo-1.json
2025-05-15 14:51:30          0 output/sagemaker-xgboost-2025-05-15-21-48-49-811/profiler-output/system/training_job_end.ts
2025-05-15 15:05:42          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/claim.smd
2025-05-15 15:05:42       6276 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 15:05:42        218 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 15:05:42        224 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 15:05:42        287 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 15:05:42        288 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 15:05:56          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/debug-output/training_job_end.ts
2025-05-15 15:05:56      82132 output/sagemaker-xgboost-2025-05-15-22-03-14-706/output/model.tar.gz
2025-05-15 15:05:56          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/framework/training_job_end.ts
2025-05-15 15:05:01      15543 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/incremental/2025051522/1747346580.algo-1.json
2025-05-15 15:05:00     184588 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/incremental/2025051522/1747346640.algo-1.json
2025-05-15 15:05:52     158553 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/incremental/2025051522/1747346700.algo-1.json
2025-05-15 15:05:56          0 output/sagemaker-xgboost-2025-05-15-22-03-14-706/profiler-output/system/training_job_end.ts
2025-05-15 15:38:07          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/claim.smd
2025-05-15 15:38:07       6276 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/collections/000000000/worker_0_collections.json
2025-05-15 15:38:07        218 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-15 15:38:07        224 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-15 15:38:07        287 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000000_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000010_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000020_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000030_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000040_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000050_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000060_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000070_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000080_worker_0.json
2025-05-15 15:38:07        288 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/index/000000000/000000000090_worker_0.json
2025-05-15 15:38:21          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/debug-output/training_job_end.ts
2025-05-15 15:38:21      82135 output/sagemaker-xgboost-2025-05-15-22-35-37-193/output/model.tar.gz
2025-05-15 15:38:21          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/framework/training_job_end.ts
2025-05-15 15:38:01     115626 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/incremental/2025051522/1747348560.algo-1.json
2025-05-15 15:38:00     184509 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/incremental/2025051522/1747348620.algo-1.json
2025-05-15 15:38:17      50886 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/incremental/2025051522/1747348680.algo-1.json
2025-05-15 15:38:21          0 output/sagemaker-xgboost-2025-05-15-22-35-37-193/profiler-output/system/training_job_end.ts
2025-05-16 09:55:17          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/claim.smd
2025-05-16 09:55:17       6276 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/collections/000000000/worker_0_collections.json
2025-05-16 09:55:17        218 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-16 09:55:17        224 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-16 09:55:17        287 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000000_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000010_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000020_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000030_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000040_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000050_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000060_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000070_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000080_worker_0.json
2025-05-16 09:55:17        288 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/index/000000000/000000000090_worker_0.json
2025-05-16 09:55:33          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/debug-output/training_job_end.ts
2025-05-16 09:55:31      82136 output/sagemaker-xgboost-2025-05-16-16-52-51-977/output/model.tar.gz
2025-05-16 09:55:33          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/framework/training_job_end.ts
2025-05-16 09:55:01      81927 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/incremental/2025051616/1747414380.algo-1.json
2025-05-16 09:55:00     184478 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/incremental/2025051616/1747414440.algo-1.json
2025-05-16 09:55:27      81698 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/incremental/2025051616/1747414500.algo-1.json
2025-05-16 09:55:33          0 output/sagemaker-xgboost-2025-05-16-16-52-51-977/profiler-output/system/training_job_end.ts
2025-05-16 09:59:26          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/claim.smd
2025-05-16 09:59:26       6276 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/collections/000000000/worker_0_collections.json
2025-05-16 09:59:26        218 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-16 09:59:26        224 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-16 09:59:26        287 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000000_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000010_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000020_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000030_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000040_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000050_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000060_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000070_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000080_worker_0.json
2025-05-16 09:59:26        288 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/index/000000000/000000000090_worker_0.json
2025-05-16 09:59:40          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/debug-output/training_job_end.ts
2025-05-16 09:59:39      82138 output/sagemaker-xgboost-2025-05-16-16-56-59-277/output/model.tar.gz
2025-05-16 09:59:40          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/framework/training_job_end.ts
2025-05-16 09:59:01      61844 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/incremental/2025051616/1747414620.algo-1.json
2025-05-16 09:59:00     184462 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/incremental/2025051616/1747414680.algo-1.json
2025-05-16 09:59:36     107828 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/incremental/2025051616/1747414740.algo-1.json
2025-05-16 09:59:40          0 output/sagemaker-xgboost-2025-05-16-16-56-59-277/profiler-output/system/training_job_end.ts
2025-05-16 11:13:21          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/claim.smd
2025-05-16 11:13:21       6276 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/collections/000000000/worker_0_collections.json
2025-05-16 11:13:21        218 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000000/000000000000_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000010/000000000010_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000020/000000000020_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000030/000000000030_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000040/000000000040_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000050/000000000050_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000060/000000000060_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000070/000000000070_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000080/000000000080_worker_0.tfevents
2025-05-16 11:13:21        224 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/events/000000000090/000000000090_worker_0.tfevents
2025-05-16 11:13:21        287 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000000_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000010_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000020_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000030_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000040_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000050_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000060_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000070_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000080_worker_0.json
2025-05-16 11:13:21        288 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/index/000000000/000000000090_worker_0.json
2025-05-16 11:13:35          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/debug-output/training_job_end.ts
2025-05-16 11:13:35      82134 output/sagemaker-xgboost-2025-05-16-18-10-50-386/output/model.tar.gz
2025-05-16 11:13:35          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/framework/training_job_end.ts
2025-05-16 11:13:01      80321 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/incremental/2025051618/1747419060.algo-1.json
2025-05-16 11:13:00     184418 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/incremental/2025051618/1747419120.algo-1.json
2025-05-16 11:13:31      94001 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/incremental/2025051618/1747419180.algo-1.json
2025-05-16 11:13:35          0 output/sagemaker-xgboost-2025-05-16-18-10-50-386/profiler-output/system/training_job_end.ts
tim@Tims-MBP quantum_circuit % 

tim@Tims-MBP quantum_circuit % aws iam list-attached-role-policies --role-name AmazonBraketJobsExecutionRole
{
    "AttachedPolicies": [
        {
            "PolicyName": "BraketAndS3Access",
            "PolicyArn": "arn:aws:iam::084375569056:policy/BraketAndS3Access"
        }
    ]
}

tim@Tims-MBP quantum_circuit % aws iam list-roles | grep RoleName | grep AmazonSageMaker-ExecutionRole
            "RoleName": "AmazonSageMaker-ExecutionRole-20250513T204281",
tim@Tims-MBP quantum_circuit % aws iam list-attached-role-policies --role-name AmazonSageMaker-ExecutionRole-20250513T204281
{
    "AttachedPolicies": [
        {
            "PolicyName": "AmazonSageMakerFullAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
        },
        {
            "PolicyName": "AmazonSageMakerCanvasSMDataScienceAssistantAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonSageMakerCanvasSMDataScienceAssistantAccess"
        },
        {
            "PolicyName": "AmazonSageMakerCanvasAIServicesAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonSageMakerCanvasAIServicesAccess"
        },
        {
            "PolicyName": "AmazonSageMakerCanvasFullAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonSageMakerCanvasFullAccess"
        },
        {
            "PolicyName": "AmazonBraketFullAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonBraketFullAccess"
        },
        {
            "PolicyName": "AmazonSageMakerCanvasDataPrepFullAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonSageMakerCanvasDataPrepFullAccess"
        },
        {
            "PolicyName": "AmazonSageMaker-ExecutionPolicy-20250513T204281",
            "PolicyArn": "arn:aws:iam::084375569056:policy/service-role/AmazonSageMaker-ExecutionPolicy-20250513T204281"
        }
    ]
}

tim@Tims-MBP quantum_circuit % aws iam list-attached-user-policies --user-name bluedragon  
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "AmazonEKSClusterPolicy",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
        },
        {
            "PolicyName": "IAMUserChangePassword",
            "PolicyArn": "arn:aws:iam::aws:policy/IAMUserChangePassword"
        },
        {
            "PolicyName": "AmazonEKSWorkerNodePolicy",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
        }
    ]
}
tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters '[ {"name": "status", "operator": "EQUAL", "values": ["COMPLETED"]}]'
{
    "quantumTasks": [
        {
            "createdAt": "2025-05-16T18:06:03.765000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:06:05.133000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/d5992705-d208-4567-a297-a969bd3e5f5a",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:05:04.423000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:05:06.135000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:02:24.002000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:02:25.494000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/aa330f99-39d0-4056-b1e1-45858244a029",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/aa330f99-39d0-4056-b1e1-45858244a029",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T17:47:53.408000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:47:54.574000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/63dfda73-ca27-41b5-a54a-8ce285d359f6",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/63dfda73-ca27-41b5-a54a-8ce285d359f6",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T17:23:19.107000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:23:20.613000+00:00",
            "outputS3Bucket": "amazon-braket-us-east-1-084375569056",
            "outputS3Directory": "jobs/run-ghz-hybrid/tasks/012fe2d6-77cb-4430-9f13-2a52de2d1cac",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/012fe2d6-77cb-4430-9f13-2a52de2d1cac",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T16:52:27.525000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T16:52:29.160000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/dd611075-0876-4c9f-a662-9989714861b7",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/dd611075-0876-4c9f-a662-9989714861b7",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T16:33:47.296000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T16:33:48.784000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/ae11e7d3-a3ac-4a3f-afb7-7aaa0a063453",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/ae11e7d3-a3ac-4a3f-afb7-7aaa0a063453",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T23:17:30.451000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T23:17:31.755000+00:00",
            "outputS3Bucket": "amazon-braket-us-east-1-084375569056",
            "outputS3Directory": "jobs/run-ghz-hybrid/tasks/312b6499-b2fa-443d-bcdc-750d8dd3e94d",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/312b6499-b2fa-443d-bcdc-750d8dd3e94d",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:52:58.791000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:53:00.560000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/1b7eb990-5072-4b81-94ff-cf81c2c227b6",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/1b7eb990-5072-4b81-94ff-cf81c2c227b6",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:31:35.741000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:31:37.164000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/0eff39e1-95a3-4598-8ef3-726872921ad2",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/0eff39e1-95a3-4598-8ef3-726872921ad2",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:27:58.991000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:28:00.683000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3703b5fc-ef89-4986-ac7e-a37bf0cd6190",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3703b5fc-ef89-4986-ac7e-a37bf0cd6190",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:22:29.429000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:22:30.980000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/ed9e774e-35d6-4c26-858f-e6414660f3a5",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/ed9e774e-35d6-4c26-858f-e6414660f3a5",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:16:26.263000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:16:27.836000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/aebdc610-4f2b-4931-a085-390ed8838381",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/aebdc610-4f2b-4931-a085-390ed8838381",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:10:27.181000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:10:28.661000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/6b5bcb82-7635-469a-b2b1-797b3ce165bf",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/6b5bcb82-7635-469a-b2b1-797b3ce165bf",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T20:15:56.820000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T20:15:58.676000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/62b126fb-942f-4e89-8a28-951fd6ac1d8d",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/62b126fb-942f-4e89-8a28-951fd6ac1d8d",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:54:28.310000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:54:30.149000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/371cb545-cd13-4641-af3f-f334d3f259dd",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/371cb545-cd13-4641-af3f-f334d3f259dd",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:52:43.494000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:52:45.014000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3c15312f-3014-4050-bddd-d513464b5b99",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3c15312f-3014-4050-bddd-d513464b5b99",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:50:29.011000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:50:30.319000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/eb234307-c746-4b4a-8fae-5d0c332dee3e",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/eb234307-c746-4b4a-8fae-5d0c332dee3e",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:46:25.937000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:46:27.323000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/a5b2e398-ec45-44ea-b208-67b03ae08d73",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/a5b2e398-ec45-44ea-b208-67b03ae08d73",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        }
    ]
}
tim@Tims-MBP quantum_circuit % 

tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters '[ {"name": "deviceArn", "operator": "EQUAL", "values": ["arn:aws:braket:us-east-1::device/quantum-simulator/amazon/sv1"]}]'
{
    "quantumTasks": []
}

tim@Tims-MBP quantum_circuit % aws braket get-job --job-arn arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10
{
    "algorithmSpecification": {
        "containerImage": {
            "uri": "292282985366.dkr.ecr.us-east-1.amazonaws.com/amazon-braket-base-jobs:latest"
        },
        "scriptModeConfig": {
            "compressionType": "GZIP",
            "entryPoint": "decorator_job_ha23ymcu.entry_point:run_ghz_hybrid",
            "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz"
        }
    },
    "billableDuration": 80000,
    "checkpointConfig": {
        "localPath": "/opt/jobs/checkpoints",
        "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/checkpoints"
    },
    "createdAt": "2025-05-16T17:21:38.893000+00:00",
    "deviceConfig": {
        "device": "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
    },
    "endedAt": "2025-05-16T17:23:41.078000+00:00",
    "events": [
        {
            "eventType": "STARTING_INSTANCE",
            "message": "Provisioning job instance",
            "timeOfEvent": "2025-05-16T17:21:40.406000+00:00"
        },
        {
            "eventType": "DOWNLOADING_DATA",
            "message": "Downloading input data",
            "timeOfEvent": "2025-05-16T17:22:21.724000+00:00"
        },
        {
            "eventType": "RUNNING",
            "message": "Job is in progress",
            "timeOfEvent": "2025-05-16T17:23:02.940000+00:00"
        },
        {
            "eventType": "UPLOADING_RESULTS",
            "message": "Uploading job output to S3",
            "timeOfEvent": "2025-05-16T17:23:28.508000+00:00"
        },
        {
            "eventType": "COMPLETED",
            "message": "Job has completed",
            "timeOfEvent": "2025-05-16T17:23:41.078000+00:00"
        }
    ],
    "hyperParameters": {},
    "inputDataConfig": [],
    "instanceConfig": {
        "instanceCount": 1,
        "instanceType": "ml.m5.large",
        "volumeSizeInGb": 30
    },
    "jobArn": "arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10",
    "jobName": "run-ghz-hybrid",
    "outputDataConfig": {
        "s3Path": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/data"
    },
    "roleArn": "arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
    "startedAt": "2025-05-16T17:22:21.724000+00:00",
    "status": "COMPLETED",
    "stoppingCondition": {
        "maxRuntimeInSeconds": 432000
    },
    "tags": {}
}
tim@Tims-MBP quantum_circuit % 

tim@Tims-MBP quantum_circuit % aws sagemaker list-training-jobs
{
    "TrainingJobSummaries": [
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-16-18-10-50-386",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-16-18-10-50-386",
            "CreationTime": "2025-05-16T11:10:50.603000-07:00",
            "TrainingEndTime": "2025-05-16T11:13:37.265000-07:00",
            "LastModifiedTime": "2025-05-16T11:13:37.530000-07:00",
            "TrainingJobStatus": "Completed"
        },
        {
            "TrainingJobName": "sagemaker-xgboost-2025-05-16-16-56-59-277",
            "TrainingJobArn": "arn:aws:sagemaker:us-east-1:084375569056:training-job/sagemaker-xgboost-2025-05-16-16-56-59-277",
            "CreationTime": "2025-05-16T09:56:59.479000-07:00",
            "TrainingEndTime": "2025-05-16T09:59:41.861000-07:00",
            "LastModifiedTime": "2025-05-16T09:59:42.117000-07:00",
            "TrainingJobStatus": "Completed"
        },

tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters 'name=status,operator=EQUAL,values=COMPLETED' --region us-east-1
{
    "quantumTasks": [
        {
            "createdAt": "2025-05-16T18:06:03.765000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:06:05.133000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/d5992705-d208-4567-a297-a969bd3e5f5a",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:05:04.423000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:05:06.135000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:02:24.002000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:02:25.494000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/aa330f99-39d0-4056-b1e1-45858244a029",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/aa330f99-39d0-4056-b1e1-45858244a029",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T17:47:53.408000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:47:54.574000+00:00",
tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters 'name=status,operator=IN,values=QUEUED,RUNNING,COMPLETED,FAILED,CANCELLED' --region us-east-1

An error occurred (BadRequestException) when calling the SearchQuantumTasks operation: Invalid request body
tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters 'name=status,operator=IN,values=QUEUED,RUNNING,COMPLETED,FAILED,CANCELLED' --region us-east-2

Could not connect to the endpoint URL: "https://braket.us-east-2.amazonaws.com/quantum-tasks"
tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters 'name=deviceArn,operator=EQUAL,values=arn:aws:braket:::device/quantum-simulator/amazon/sv1' --region us-east-1
{
    "quantumTasks": [
        {
            "createdAt": "2025-05-16T18:06:03.765000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:06:05.133000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/d5992705-d208-4567-a297-a969bd3e5f5a",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:05:04.423000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:05:06.135000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:02:24.002000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:02:25.494000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/aa330f99-39d0-4056-b1e1-45858244a029",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/aa330f99-39d0-4056-b1e1-45858244a029",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T17:47:53.408000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:47:54.574000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/63dfda73-ca27-41b5-a54a-8ce285d359f6",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/63dfda73-ca27-41b5-a54a-8ce285d359f6",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T17:23:19.107000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:23:20.613000+00:00",
            "outputS3Bucket": "amazon-braket-us-east-1-084375569056",
            "outputS3Directory": "jobs/run-ghz-hybrid/tasks/012fe2d6-77cb-4430-9f13-2a52de2d1cac",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/012fe2d6-77cb-4430-9f13-2a52de2d1cac",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T16:52:27.525000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T16:52:29.160000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/dd611075-0876-4c9f-a662-9989714861b7",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/dd611075-0876-4c9f-a662-9989714861b7",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T16:33:47.296000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T16:33:48.784000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/ae11e7d3-a3ac-4a3f-afb7-7aaa0a063453",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/ae11e7d3-a3ac-4a3f-afb7-7aaa0a063453",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T23:17:30.451000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T23:17:31.755000+00:00",
            "outputS3Bucket": "amazon-braket-us-east-1-084375569056",
            "outputS3Directory": "jobs/run-ghz-hybrid/tasks/312b6499-b2fa-443d-bcdc-750d8dd3e94d",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/312b6499-b2fa-443d-bcdc-750d8dd3e94d",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:52:58.791000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:53:00.560000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/1b7eb990-5072-4b81-94ff-cf81c2c227b6",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/1b7eb990-5072-4b81-94ff-cf81c2c227b6",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:31:35.741000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:31:37.164000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/0eff39e1-95a3-4598-8ef3-726872921ad2",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/0eff39e1-95a3-4598-8ef3-726872921ad2",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:27:58.991000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:28:00.683000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3703b5fc-ef89-4986-ac7e-a37bf0cd6190",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3703b5fc-ef89-4986-ac7e-a37bf0cd6190",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:22:29.429000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:22:30.980000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/ed9e774e-35d6-4c26-858f-e6414660f3a5",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/ed9e774e-35d6-4c26-858f-e6414660f3a5",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:16:26.263000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:16:27.836000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/aebdc610-4f2b-4931-a085-390ed8838381",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/aebdc610-4f2b-4931-a085-390ed8838381",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-15T20:10:27.181000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-15T20:10:28.661000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/6b5bcb82-7635-469a-b2b1-797b3ce165bf",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/6b5bcb82-7635-469a-b2b1-797b3ce165bf",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T20:15:56.820000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T20:15:58.676000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/62b126fb-942f-4e89-8a28-951fd6ac1d8d",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/62b126fb-942f-4e89-8a28-951fd6ac1d8d",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:54:28.310000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:54:30.149000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/371cb545-cd13-4641-af3f-f334d3f259dd",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/371cb545-cd13-4641-af3f-f334d3f259dd",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:52:43.494000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:52:45.014000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3c15312f-3014-4050-bddd-d513464b5b99",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3c15312f-3014-4050-bddd-d513464b5b99",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:50:29.011000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:50:30.319000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/eb234307-c746-4b4a-8fae-5d0c332dee3e",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/eb234307-c746-4b4a-8fae-5d0c332dee3e",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-14T19:46:25.937000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-14T19:46:27.323000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/a5b2e398-ec45-44ea-b208-67b03ae08d73",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/a5b2e398-ec45-44ea-b208-67b03ae08d73",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        }
    ]
}
tim@Tims-MBP quantum_circuit % 

tim@Tims-MBP quantum_circuit % aws braket get-quantum-task --quantum-task-arn arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a --region us-east-1
{
    "createdAt": "2025-05-16T18:06:03.765000+00:00",
    "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
    "deviceParameters": "{\"braketSchemaHeader\": {\"name\": \"braket.device_schema.simulators.gate_model_simulator_device_parameters\", \"version\": \"1\"}, \"paradigmParameters\": {\"braketSchemaHeader\": {\"name\": \"braket.device_schema.gate_model_parameters\", \"version\": \"1\"}, \"qubitCount\": 2, \"disableQubitRewiring\": false}}",
    "endedAt": "2025-05-16T18:06:05.133000+00:00",
    "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
    "outputS3Directory": "quantum-output/d5992705-d208-4567-a297-a969bd3e5f5a",
    "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a",
    "shots": 1000,
    "status": "COMPLETED",
    "tags": {}
}

tim@Tims-MBP quantum_circuit % aws braket get-job --job-arn arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10 --region us-east-1
{
    "algorithmSpecification": {
        "containerImage": {
            "uri": "292282985366.dkr.ecr.us-east-1.amazonaws.com/amazon-braket-base-jobs:latest"
        },
        "scriptModeConfig": {
            "compressionType": "GZIP",
            "entryPoint": "decorator_job_ha23ymcu.entry_point:run_ghz_hybrid",
            "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz"
        }
    },
    "billableDuration": 80000,
    "checkpointConfig": {
        "localPath": "/opt/jobs/checkpoints",
        "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/checkpoints"
    },
    "createdAt": "2025-05-16T17:21:38.893000+00:00",
    "deviceConfig": {
        "device": "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
    },
    "endedAt": "2025-05-16T17:23:41.078000+00:00",
    "events": [
        {
            "eventType": "STARTING_INSTANCE",
            "message": "Provisioning job instance",
            "timeOfEvent": "2025-05-16T17:21:40.406000+00:00"
        },
        {
            "eventType": "DOWNLOADING_DATA",
            "message": "Downloading input data",
            "timeOfEvent": "2025-05-16T17:22:21.724000+00:00"
        },
        {
            "eventType": "RUNNING",
            "message": "Job is in progress",
            "timeOfEvent": "2025-05-16T17:23:02.940000+00:00"
        },
        {
            "eventType": "UPLOADING_RESULTS",
            "message": "Uploading job output to S3",
            "timeOfEvent": "2025-05-16T17:23:28.508000+00:00"
        },
        {
            "eventType": "COMPLETED",
            "message": "Job has completed",
            "timeOfEvent": "2025-05-16T17:23:41.078000+00:00"
        }
    ],
    "hyperParameters": {},
    "inputDataConfig": [],
    "instanceConfig": {
        "instanceCount": 1,
        "instanceType": "ml.m5.large",
        "volumeSizeInGb": 30
    },
    "jobArn": "arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10",
    "jobName": "run-ghz-hybrid",
    "outputDataConfig": {
        "s3Path": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/data"
    },
    "roleArn": "arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
    "startedAt": "2025-05-16T17:22:21.724000+00:00",
    "status": "COMPLETED",
    "stoppingCondition": {
        "maxRuntimeInSeconds": 432000
    },
    "tags": {}
}

tim@Tims-MBP quantum_circuit % aws braket get-job --job-arn arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10 --region us-east-1
{
    "algorithmSpecification": {
        "containerImage": {
            "uri": "292282985366.dkr.ecr.us-east-1.amazonaws.com/amazon-braket-base-jobs:latest"
        },
        "scriptModeConfig": {
            "compressionType": "GZIP",
            "entryPoint": "decorator_job_ha23ymcu.entry_point:run_ghz_hybrid",
            "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz"
        }
    },
    "billableDuration": 80000,
    "checkpointConfig": {
        "localPath": "/opt/jobs/checkpoints",
        "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/checkpoints"
    },
    "createdAt": "2025-05-16T17:21:38.893000+00:00",
    "deviceConfig": {
        "device": "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
    },
    "endedAt": "2025-05-16T17:23:41.078000+00:00",
    "events": [
        {
            "eventType": "STARTING_INSTANCE",
            "message": "Provisioning job instance",
            "timeOfEvent": "2025-05-16T17:21:40.406000+00:00"
        },
        {
            "eventType": "DOWNLOADING_DATA",
            "message": "Downloading input data",
            "timeOfEvent": "2025-05-16T17:22:21.724000+00:00"
        },
        {
            "eventType": "RUNNING",
            "message": "Job is in progress",
            "timeOfEvent": "2025-05-16T17:23:02.940000+00:00"
        },
        {
            "eventType": "UPLOADING_RESULTS",
            "message": "Uploading job output to S3",
            "timeOfEvent": "2025-05-16T17:23:28.508000+00:00"
        },
        {
            "eventType": "COMPLETED",
            "message": "Job has completed",
            "timeOfEvent": "2025-05-16T17:23:41.078000+00:00"
        }
    ],
    "hyperParameters": {},
    "inputDataConfig": [],
    "instanceConfig": {
        "instanceCount": 1,
        "instanceType": "ml.m5.large",
        "volumeSizeInGb": 30
    },
    "jobArn": "arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10",
    "jobName": "run-ghz-hybrid",
    "outputDataConfig": {
        "s3Path": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/data"
    },
    "roleArn": "arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
    "startedAt": "2025-05-16T17:22:21.724000+00:00",
    "status": "COMPLETED",
    "stoppingCondition": {
        "maxRuntimeInSeconds": 432000
    },
    "tags": {}
}

tim@Tims-MBP quantum_circuit % for task_status in QUEUED RUNNING COMPLETED FAILED CANCELLED; do
  aws braket search-quantum-tasks --filters "name=status,operator=EQUAL,values=$task_status" --region us-east-1
done
{
    "quantumTasks": []
}
{
    "quantumTasks": []
}
{
    "quantumTasks": [
        {
            "createdAt": "2025-05-16T18:06:03.765000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:06:05.133000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/d5992705-d208-4567-a297-a969bd3e5f5a",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:05:04.423000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:05:06.135000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:02:24.002000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:02:25.494000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/aa330f99-39d0-4056-b1e1-45858244a029",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/aa330f99-39d0-4056-b1e1-45858244a029",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T17:47:53.408000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:47:54.574000+00:00",
{
    "quantumTasks": []
}
{
    "quantumTasks": []
}


tim@Tims-MBP quantum_circuit % aws braket search-quantum-tasks --filters 'name=deviceArn,operator=EQUAL,values=arn:aws:braket:::device/quantum-simulator/amazon/sv1' --region us-east-1
{
    "quantumTasks": [
        {
            "createdAt": "2025-05-16T18:06:03.765000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:06:05.133000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/d5992705-d208-4567-a297-a969bd3e5f5a",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/d5992705-d208-4567-a297-a969bd3e5f5a",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },
        {
            "createdAt": "2025-05-16T18:05:04.423000+00:00",
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T18:05:06.135000+00:00",
            "outputS3Bucket": "amazon-braket-my-quantum-output-20250514-kerstarsoc",
            "outputS3Directory": "quantum-output/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "quantumTaskArn": "arn:aws:braket:us-east-1:084375569056:quantum-task/3d698abb-d51c-4d4f-9ed6-1de032c982f3",
            "shots": 1000,
            "status": "COMPLETED",
            "tags": {}
        },

tim@Tims-MBP quantum_circuit % aws braket get-job --job-arn arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10 --region us-east-1
{
    "algorithmSpecification": {
        "containerImage": {
            "uri": "292282985366.dkr.ecr.us-east-1.amazonaws.com/amazon-braket-base-jobs:latest"
        },
        "scriptModeConfig": {
            "compressionType": "GZIP",
            "entryPoint": "decorator_job_ha23ymcu.entry_point:run_ghz_hybrid",
            "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz"
        }
    },
    "billableDuration": 80000,
    "checkpointConfig": {
        "localPath": "/opt/jobs/checkpoints",
        "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/checkpoints"
    },
    "createdAt": "2025-05-16T17:21:38.893000+00:00",
    "deviceConfig": {
        "device": "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
    },
    "endedAt": "2025-05-16T17:23:41.078000+00:00",
    "events": [
        {
            "eventType": "STARTING_INSTANCE",
            "message": "Provisioning job instance",
            "timeOfEvent": "2025-05-16T17:21:40.406000+00:00"
        },
        {
            "eventType": "DOWNLOADING_DATA",
            "message": "Downloading input data",
            "timeOfEvent": "2025-05-16T17:22:21.724000+00:00"
        },
        {
            "eventType": "RUNNING",
            "message": "Job is in progress",
            "timeOfEvent": "2025-05-16T17:23:02.940000+00:00"
        },
        {
            "eventType": "UPLOADING_RESULTS",
            "message": "Uploading job output to S3",
            "timeOfEvent": "2025-05-16T17:23:28.508000+00:00"
        },
        {
            "eventType": "COMPLETED",
            "message": "Job has completed",
            "timeOfEvent": "2025-05-16T17:23:41.078000+00:00"
        }
    ],
    "hyperParameters": {},
    "inputDataConfig": [],
    "instanceConfig": {
        "instanceCount": 1,
        "instanceType": "ml.m5.large",
        "volumeSizeInGb": 30
    },
    "jobArn": "arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10",
    "jobName": "run-ghz-hybrid",
    "outputDataConfig": {
        "s3Path": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/data"
    },
    "roleArn": "arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
    "startedAt": "2025-05-16T17:22:21.724000+00:00",
    "status": "COMPLETED",
    "stoppingCondition": {
        "maxRuntimeInSeconds": 432000
    },
    "tags": {}
}

(py3ml) tim@Tims-MBP quantum_circuit % aws braket get-job --job-arn arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10 --region us-east-1
{
    "algorithmSpecification": {
        "containerImage": {
            "uri": "292282985366.dkr.ecr.us-east-1.amazonaws.com/amazon-braket-base-jobs:latest"
        },
        "scriptModeConfig": {
            "compressionType": "GZIP",
            "entryPoint": "decorator_job_ha23ymcu.entry_point:run_ghz_hybrid",
            "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/script/source.tar.gz"
        }
    },
    "billableDuration": 80000,
    "checkpointConfig": {
        "localPath": "/opt/jobs/checkpoints",
        "s3Uri": "s3://amazon-braket-us-east-1-084375569056/jobs/run-ghz-hybrid/1747416094973/checkpoints"
    },
    "createdAt": "2025-05-16T17:21:38.893000+00:00",
    "deviceConfig": {
        "device": "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
    },
    "endedAt": "2025-05-16T17:23:41.078000+00:00",
    "events": [
        {
            "eventType": "STARTING_INSTANCE",
            "message": "Provisioning job instance",
            "timeOfEvent": "2025-05-16T17:21:40.406000+00:00"
        },
        {
            "eventType": "DOWNLOADING_DATA",
            "message": "Downloading input data",
            "timeOfEvent": "2025-05-16T17:22:21.724000+00:00"
        },
        {
            "eventType": "RUNNING",
            "message": "Job is in progress",
            "timeOfEvent": "2025-05-16T17:23:02.940000+00:00"
        },
        {
            "eventType": "UPLOADING_RESULTS",
(py3ml) tim@Tims-MBP quantum_circuit % aws braket search-jobs --filters 'name=jobArn,operator=EQUAL,values=arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10' --region us-east-1
{
    "jobs": [
        {
            "createdAt": "2025-05-16T17:21:38.893000+00:00",
            "device": "arn:aws:braket:::device/quantum-simulator/amazon/sv1",
            "endedAt": "2025-05-16T17:23:41.078000+00:00",
            "jobArn": "arn:aws:braket:us-east-1:084375569056:job/acc51817-2b7a-48ed-8dee-fffc87703b10",
            "jobName": "run-ghz-hybrid",
            "startedAt": "2025-05-16T17:22:21.724000+00:00",
            "status": "COMPLETED",
            "tags": {}
        }
    ]
}

