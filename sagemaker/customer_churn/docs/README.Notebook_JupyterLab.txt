
sh-4.2$ hostname -f
ip-172-16-37-252.ec2.internal
sh-4.2$ cat /etc/os-release
NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"
SUPPORT_END="2026-06-30"

sh-4.2$ pwd
/home/ec2-user/SageMaker
sh-4.2$ git clone https://github.com/aws/amazon-sagemaker-examples.git
Cloning into 'amazon-sagemaker-examples'...
remote: Enumerating objects: 36814, done.
remote: Counting objects: 100% (102/102), done.
remote: Compressing objects: 100% (70/70), done.
remote: Total 36814 (delta 78), reused 32 (delta 32), pack-reused 36712 (from 3)
Receiving objects: 100% (36814/36814), 649.56 MiB | 44.58 MiB/s, done.
Resolving deltas: 100% (21015/21015), done.
Updating files: 100% (2960/2960), done.

sh-4.2$ cd "amazon-sagemaker-examples/     deploy_and_monitor/sm-model_monitor_introduction/model/"
sh-4.2$ ls -l
total 36
-rw-rw-r-- 1 ec2-user ec2-user 33916 May 21 20:17 xgb-churn-prediction-model.tar.gz
sh-4.2$ which gzip
/usr/bin/gzip
sh-4.2$ gzip -d xgb-churn-prediction-model.tar.gz 
sh-4.2$ ls -l
total 92
-rw-rw-r-- 1 ec2-user ec2-user 92160 May 21 20:17 xgb-churn-prediction-model.tar
sh-4.2$ tar tvf xgb

sh-4.2$ tar xvf xgb-churn-prediction-model.tar 
xgboost-model
sh-4.2$ ls -l
total 176
-rw-rw-r-- 1 ec2-user ec2-user 92160 May 21 20:17 xgb-churn-prediction-model.tar
-rw-r--r-- 1 ec2-user ec2-user 85611 Nov 20  2019 xgboost-model

sh-4.2$ cd "/home/ec2-user/SageMaker/amazon-sagemaker-examples/        end_to_end_ml_lifecycle/"
sh-4.2$ ls -l
total 148
-rw-rw-r-- 1 ec2-user ec2-user   694 May 21 20:17 README.md
-rw-rw-r-- 1 ec2-user ec2-user 57410 May 21 20:17 sm-autopilot_customer_churn.ipynb
-rw-rw-r-- 1 ec2-user ec2-user 37746 May 21 20:17 sm-autopilot_linear_regression_california_housing.ipynb
-rw-rw-r-- 1 ec2-user ec2-user 44071 May 21 20:17 sm-autopilot_time_series_forecasting.ipynb
sh-4.2$ cat README.md 
# Amazon SageMaker Examples

### End To End ML Lifecycle

These examples are a diverse collection of end-to-end notebooks that demonstrate how to build, train, and deploy machine learning models using Amazon SageMaker. These notebooks cover a wide range of machine learning tasks and use cases, providing you with a comprehensive understanding of the SageMaker workflow.

- [Customer Churn Prediction with Amazon SageMaker Autopilot](sm-autopilot_customer_churn.ipynb)
- [Housing Price Prediction with Amazon SageMaker Autopilot](sm-autopilot_linear_regression_california_housing.ipynb)
- [Time-Series Forecasting with Amazon SageMaker Autopilot](sm-sm-autopilot_time_series_forecasting.ipynb)
