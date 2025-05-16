sh-4.2$ cat quantum_circuit_ghz_check.py
#!/usr/bin/env python

import boto3
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for EC2
import matplotlib.pyplot as plt
import json
import sagemaker
from sagemaker.estimator import Estimator
import pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split

# Initialize S3 client
s3 = boto3.client('s3')

# Retrieve quantum circuit results from S3
bucket = 'amazon-braket-my-quantum-output-20250514-kerstarsoc'
key = 'quantum-output/1b7eb990-5072-4b81-94ff-cf81c2c227b6/results.json'
response = s3.get_object(Bucket=bucket, Key=key)
results = json.loads(response['Body'].read().decode())

# Convert measurements to measurement counts
measurements = results['measurements']
measurement_counts = Counter(''.join(map(str, m)) for m in measurements)
print(measurement_counts)

# Plot histogram
plt.bar(measurement_counts.keys(), measurement_counts.values())
plt.xlabel('State')
plt.ylabel('Counts')
plt.title('GHZ State Measurement Counts')
plt.savefig('measurement_counts_ghz.png')

# Upload plot to S3
s3.upload_file('measurement_counts_ghz.png', 'sagemaker-us-east-1-084375569056', 'measurement_counts_ghz.png')
plt.close()

# Preprocess abalone.csv to LIBSVM format
response = s3.get_object(Bucket='sagemaker-us-east-1-084375569056', Key='abalone.csv')
csv_content = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_content), header=None)

# Map categorical 'sex' column (M/F/I) to numeric (0/1/2)
sex_mapping = {'M': 0, 'F': 1, 'I': 2}
df[0] = df[0].map(sex_mapping)

# Split into train and validation sets
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

# Function to convert DataFrame to LIBSVM
def df_to_libsvm(df, filename, s3_bucket, s3_key):
    libsvm_lines = []
    for _, row in df.iterrows():
        label = row[8]  # Rings
        features = [f"{i+1}:{row[i]}" for i in range(8) if pd.notnull(row[i])]
        libsvm_line = f"{label} {' '.join(features)}"
        libsvm_lines.append(libsvm_line)
    with open(filename, 'w') as f:
        f.write('\n'.join(libsvm_lines))
    s3.upload_file(filename, s3_bucket, s3_key)

# Save train and validation LIBSVM files
train_key = 'abalone_train.libsvm'
val_key = 'abalone_validation.libsvm'
df_to_libsvm(train_df, 'abalone_train.libsvm', 'sagemaker-us-east-1-084375569056', train_key)
df_to_libsvm(val_df, 'abalone_validation.libsvm', 'sagemaker-us-east-1-084375569056', val_key)

# SageMaker XGBoost training
session = sagemaker.Session()
role = 'arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-20250513T204281'
estimator = Estimator(
    image_uri='683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.5-1',
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    output_path='s3://sagemaker-us-east-1-084375569056/output',
    sagemaker_session=session,
    hyperparameters={
        'num_round': 100,
        'objective': 'reg:squarederror',
        'max_depth': 5,
        'eta': 0.2,
        'subsample': 0.8,
        'early_stopping_rounds': 10
    }
)
estimator.fit({
    'train': f's3://sagemaker-us-east-1-084375569056/{train_key}',
    'validation': f's3://sagemaker-us-east-1-084375569056/{val_key}'
})

# Deploy the model (commented to avoid costs)
# predictor = estimator.deploy(initial_instance_count=1, instance_type='ml.m5.large')
