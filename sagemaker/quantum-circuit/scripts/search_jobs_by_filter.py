#!/usr/bin/env python3
import boto3
import json

braket = boto3.client('braket', region_name='us-east-1')
try:
    response = braket.search_jobs(filters=[])  # Empty filter to list all jobs
    print(json.dumps(response['jobs'], default=str))
except Exception as e:
    print(json.dumps({'error': str(e), 'filter_used': 'none'}))
