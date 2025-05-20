# NOTE: this is order dependent

aws braket cancel-quantum-task --quantum-task-arn arn:aws:braket:us-east-1:084375569056:quantum-task/<task-id>
aws braket cancel-job --job-arn arn:aws:braket:us-east-1:084375569056:job/<job-id>
aws sagemaker stop-notebook-instance --notebook-instance-name amazon-braket-my-sagemaker-data-2025
aws sagemaker delete-notebook-instance --notebook-instance-name amazon-braket-my-sagemaker-data-2025
aws s3 rm s3://amazon-braket-us-east-1-084375569056/ --recursive
aws s3 rm s3://sagemaker-us-east-1-084375569056/ --recursive
aws ec2 terminate-instances --instance-ids <instance-id>
