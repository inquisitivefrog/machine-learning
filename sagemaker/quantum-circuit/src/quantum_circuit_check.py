#!/usr/bin/env python

import boto3
from collections import Counter
import matplotlib.pyplot as plt
import json

# Initialize S3 client
s3 = boto3.client('s3')

# Retrieve quantum circuit results from S3
bucket = 'amazon-braket-my-quantum-output-20250514-kerstarsoc'
key = 'quantum-output/eb234307-c746-4b4a-8fae-5d0c332dee3e/results.json'
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
plt.title('Quantum Circuit Measurement Counts')
plt.savefig('measurement_counts_eb234307.png')

# Upload **Upload plot to S3
s3.upload_file('measurement_counts_eb234307.png', 'sagemaker-us-east-1-084375569056', 'measurement_counts_eb234307.png')
plt.close()
