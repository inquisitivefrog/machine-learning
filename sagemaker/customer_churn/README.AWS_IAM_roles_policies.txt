
(py3ml) tim@Tims-MBP customer_churn % aws configure
AWS Access Key ID [****************IAEZ]: 
AWS Secret Access Key [****************fWA/]: 
Default region name [us-east-1]: 
Default output format [json]: 

(py3ml) tim@Tims-MBP customer_churn % aws iam get-role --role-name AmazonSageMaker-ExecutionRole-20250520T093901 --region us-east-1
{
    "Role": {
        "Path": "/service-role/",
        "RoleName": "AmazonSageMaker-ExecutionRole-20250520T093901",
        "RoleId": "AROARHJJNAKQKLJBLLQ7H",
        "Arn": "arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250520T093901",
        "CreateDate": "2025-05-20T16:39:55+00:00",
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
        "MaxSessionDuration": 3600,
        "RoleLastUsed": {
            "LastUsedDate": "2025-05-23T01:52:49+00:00",
            "Region": "us-east-1"
        }
    }
}

(py3ml) tim@Tims-MBP customer_churn % aws iam put-role-policy --role-name "AmazonSageMaker-ExecutionRole-20250520T093901" --policy-name SageMakerS3Access --policy-document file://files/sagemaker-logging-policy.json
(py3ml) tim@Tims-MBP customer_churn % aws iam get-role-policy --role-name "AmazonSageMaker-ExecutionRole-20250520T093901" --policy-name SageMakerS3Access
{
    "RoleName": "AmazonSageMaker-ExecutionRole-20250520T093901",
    "PolicyName": "SageMakerS3Access",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "cloudwatch:PutMetricData"
                ],
                "Resource": "*"
            }
        ]
    }
}
(py3ml) tim@Tims-MBP customer_churn % aws s3 ls                                                                                                           
(py3ml) tim@Tims-MBP customer_churn % aws s3 ls --region us-east-1
(py3ml) tim@Tims-MBP customer_churn %
