import pandas as pd
import boto3

s3 = boto3.client("s3")
s3.download_file("sagemaker-us-east-1-084375569056", "data/train.csv", "train.csv")
df = pd.read_csv("train.csv")
if "Churn" not in df.columns:
    raise ValueError("Column 'Churn' not found.")
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
if "customerID" in df.columns:
    df = df.drop(columns=["customerID"])
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = df[col].astype("category").cat.codes
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
columns = ["Churn"] + [col for col in df.columns if col != "Churn"]
df = df[columns]
df.to_csv("train_processed.csv", header=False, index=False)
s3.upload_file("train_processed.csv", "sagemaker-us-east-1-084375569056", "data/train_processed.csv")
print("Uploaded processed dataset to S3")
