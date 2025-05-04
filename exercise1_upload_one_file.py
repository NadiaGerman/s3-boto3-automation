import boto3
import os

# Replace with your actual name
bucket_name = 'student-nadiagerman-bucket'

# Step 1: Connect to S3
s3 = boto3.client('s3')

# Step 2: Create a bucket (only if it doesn't already exist)
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' already exists.")

# Step 3: Upload the file
filename = 'team_image.png'
if os.path.exists(filename):
    s3.upload_file(filename, bucket_name, filename)
    print(f" File '{filename}' uploaded successfully to '{bucket_name}'.")
else:
    print(f" File '{filename}' does not exist.")

# Step 4: List and print the files in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
print("\n Files in bucket:")
if 'Contents' in response:
    for obj in response['Contents']:
        print(" -", obj['Key'])
else:
    print("Bucket is empty.")
