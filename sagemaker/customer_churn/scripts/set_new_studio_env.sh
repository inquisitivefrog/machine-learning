aws sagemaker update-domain --domain-id d-nehutxreazmp --region us-east-1 --default-user-settings '{
        "ExecutionRole": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250520T093901",
        "SharingSettings": {
            "NotebookOutputOption": "Allowed",
            "S3OutputPath": "s3://sagemaker-studio-084375569056-lhlbozhzvv/sharing"
        },
        "JupyterServerAppSettings": {
            "DefaultResourceSpec": {
                "SageMakerImageArn": "arn:aws:sagemaker:us-east-1:081325390199:image/jupyter-server-3",
                "InstanceType": "system"
            }
        },
        "CanvasAppSettings": {
            "GenerativeAiSettings": {
                "AmazonBedrockRoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonSagemakerCanvasBedrockRole-20250520T093900"
            },
            "EmrServerlessSettings": {
                "ExecutionRoleArn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMakerCanvasEMRSExecutionAccess-20250520T093900",
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
    }'
