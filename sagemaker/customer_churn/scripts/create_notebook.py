#!/usr/bin/env python3

import boto3
sagemaker = boto3.client('sagemaker')
s3 = boto3.client('s3')

# Create a notebook file in S3
notebook_content = '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}'
s3.put_object(
    Bucket='sagemaker-customer-churn-20250530',
    Key='notebooks/default_notebook.ipynb',
    Body=notebook_content
)

# Share notebook path with user
print("Notebook created at s3://sagemaker-customer-churn-20250530/notebooks/default_notebook.ipynb")
