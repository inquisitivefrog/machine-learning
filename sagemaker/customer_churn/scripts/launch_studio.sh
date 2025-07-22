#!/bin/bash

aws sagemaker create-presigned-domain-url \
  --region us-east-1 \
  --domain-id d-6a9fcefapo4q \
  --user-profile-name bluedragon
