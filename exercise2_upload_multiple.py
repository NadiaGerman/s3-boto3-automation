import boto3
import os

folder_name = 'daily_documents'
bucket_name = 'student-nadiagerman-backup'

# Connect to S3
s3 = boto3.client('s3')

# Step 1: Create bucket if it doesn't exist
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' already exists.")

print("\n Starting upload of daily documents…")

# Step 2: Upload all files in the folder
for file in os.listdir(folder_name):
    path = os.path.join(folder_name, file)
    if os.path.isfile(path):
        s3.upload_file(path, bucket_name, file)
        print(f" Uploaded: {file}")
