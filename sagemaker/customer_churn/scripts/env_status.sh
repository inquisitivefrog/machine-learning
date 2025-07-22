#!/usr/bash

1010  aws sagemaker list-apps
 1011  aws sagemaker delete-app --app-name default --spacename my-notebook --domain-id d-nehutxreazmp --region us-east-1
 1012  aws sagemaker delete-app --app-name default --app-type JupyterLab--spacename my-notebook --domain-id d-nehutxreazmp --region us-east-1
 1013  aws sagemaker delete-app --app-name default --app-type JupyterLab --spacename my-notebook --domain-id d-nehutxreazmp --region us-east-1
 1014  aws sagemaker delete-app --app-name default --app-type JupyterLab --domain-id d-nehutxreazmp --region us-east-1
 1015  ws sagemaker list-notebook-instances --region us-east-1
 1016  aws sagemaker list-notebook-instances --region us-east-1
 1017  aws sagemaker list-domains --region us-east-1
 1018  aws sagemaker list-endpoints --region us-east-1
 1019  aws sagemaker delete-app --domain-id d-nehutxreazmp --user-profile-name bluedragon --app-type JupyterLab --app-name default --space-name customer-churn --region us-east-1
 1020  aws sagemaker delete-app --domain-id d-nehutxreazmp --user-profile-name bluedragon --app-type JupyterLab --app-name default --space-name my-notebook --region us-east-1
 1021  aws sagemaker delete-app help
 1022  aws sagemaker delete-app --domain-id d-nehutxreazmp --user-profile-name bluedragon --app-type JupyterLab --app-name default  --region us-east-1
 1023  aws sagemaker delete-app --domain-id d-nehutxreazmp --user-profile-name bluedragon --app-type JupyterLab --app-name customer-churn  --region us-east-1
 1024  aws sagemaker list-apps --region us-east-1
 1025  aws sagemaker delete-app --domain-id d-nehutxreazmp --space-name customer-churn --app-type JupyterLab --app-name customer-churn  --region us-east-1
 1026  aws sagemaker delete-app --domain-id d-nehutxreazmp --space-name customer-churn --app-type JupyterLab --app-name default  --region us-east-1
 1027  aws sagemaker list-apps --region us-east-1
 1028  aws sagemaker delete-app --domain-id d-nehutxreazmp --space-name my-notebook --app-type JupyterLab --app-name default  --region us-east-1
 1029  aws sagemaker list-apps --region us-east-1
 1030  aws sagemaker list-domains
 1031  aws sagemaker delete-domain --domain-id d-nehutxreazmp --region us-east-1
 1032  aws sagemaker list-training-jobs --region us-east-1
 1033  aws sagemaker list-notebook-instances --region us-east-1
 1034  aws s3 ls s3://sagemaker-us-east-1-084375569056 --region us-east-1
 1035  aws s3 ls --region us-east-1
 1036  aws s3 ls s3://sagemaker-studio-084375569056-jznb41g5nl
 1037  aws s3 rb s3://sagemaker-studio-084375569056-jznb41g5nl --region us-east-1
 1038  aws s3 rb s3://sagemaker-studio-084375569056-lhlbozhzvv --region us-east-1
 1039  aws s3 rb s3://sagemaker-studio-084375569056-xw4a783m8j --region us-east-1
 1040  aws sagemaker list-domains
 1041  aws sagemaker delete-domain --domain-id d-nehutxreazmp --region us-east-1
 1042  aws sagemaker list-apps --region us-east-1
 1043  aws sagemaker list-endpoints --region us-east-1
 1044  aws sagemaker list-notebook-instances --region us-east-1
 1045  aws sagemaker list-user-profiles --domain-id d-nehutxreazmp --region us-east-1
 1046  aws ls s3
 1047  aws s3 ls --region us-east-1
 1048  aws sagemaker list-training-jobs --region us-east-1
 1049  aws sagemaker list-user-profiles
 1050  aws sagemaker delete-user-profile --user-profile-name default-20250520T093900 --region us-east-1
 1051  aws sagemaker delete-user-profile --user-profile-name default-20250520T093900 --domain-id d-nehutxreazmp --region us-east-1
 1052  aws sagemaker list-spaces
 1053  aws sagemaker help > sm.txt
 1054  grep job sm.txt
 1055  aws sagemaker delete-space --domain-id d-nehutxreazmp --space-name my-notebook --region us-east-1
 1056  aws sagemaker delete-space --domain-id d-nehutxreazmp --space-name customer-churn --region us-east-1
 1057  aws sagemaker list-spaces --domain-id d-nehutxreazmp --region us-east-1
 1058  aws sagemaker list-apps --domain-id d-nehutxreazmp --region us-east-1
 1059  aws sagemaker delete-user-profile --domain-id d-nehutxreazmp --user-profile-name default-20250520T093900 --region us-east-1
 1060  aws sagemaker list-user-profiles --domain-id d-nehutxreazmp --region us-east-1
 1061  aws sagemaker list-domains --region us-east-1
 1062  aws sagemaker delete-domain --domain-id d-nehutxreazmp --region us-east-1
 1063  aws sagemaker list-domains --region us-east-1
 1064  aws s3 ls s3://sagemaker-us-east-1-084375569056 --region us-east-1
 1065  aws s3 ls --region us-east-1
 1066  aws sagemaker describe-training-job --training-job-name sagemaker-xgboost-2025-05-16-18-10-50-386 --region us-east-1
 1067  aws sagemaker list-models --region us-east-1
 1068  aws sagemaker list-transform-jobs --region us-east-1
 1069  aws sagemaker list-hyper-parameter-tuning-jobs --region us-east-1
 1070  aws s3api list-buckets --region us-east-1
 1071  aws sts get-caller-identity

