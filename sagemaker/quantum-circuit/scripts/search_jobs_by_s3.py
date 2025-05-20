#!/usr/bin/env python3
import boto3
import json

# Initialize S3 client
s3 = boto3.client('s3', region_name='us-east-1')
bucket = 'amazon-braket-us-east-1-084375569056'

try:
    response = s3.list_objects_v2(Bucket=bucket, Prefix='jobs/')
    jobs = [{'jobArn': f'arn:aws:braket:us-east-1:084375569056:job/{obj["Key"].split("/")[1]}'} for obj in response.get('Contents', [])]
    print(json.dumps(jobs))
except Exception as e:
    print(json.dumps({'error': str(e), 'bucket': bucket}))
