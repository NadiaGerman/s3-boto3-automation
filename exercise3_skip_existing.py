import boto3
import os

folder_name = 'daily_documents'
bucket_name = 'student-nadiagerman-backup'

s3 = boto3.client('s3')

# Step 1: List existing files in the bucket
existing_files = set()
response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        existing_files.add(obj['Key'])

# Step 2: Check and upload if not already in S3
for file in os.listdir(folder_name):
    path = os.path.join(folder_name, file)
    if os.path.isfile(path):
        if file in existing_files:
            print(f"⚠️S File already exists: {file}")
        else:
            s3.upload_file(path, bucket_name, file)
            print(f"✅ Uploaded: {file}")
