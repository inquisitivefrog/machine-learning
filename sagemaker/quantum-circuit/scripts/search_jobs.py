#!/usr/bin/env python

import boto3
braket = boto3.client('braket', region_name='us-east-1')
response = braket.search_jobs(filters=[])
print(response['jobs'])
