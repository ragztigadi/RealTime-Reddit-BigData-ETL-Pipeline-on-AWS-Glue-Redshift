import s3fs
import boto3

from utils.constants import AWS_ACCESS_KEY_ID
from utils.constants import AWS_SECRET_ACCESS_KEY
from utils.constants import AWS_REGION

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False,
            key = AWS_ACCESS_KEY_ID,
            secret = AWS_SECRET_ACCESS_KEY,
            client_kwargs={"region_name": AWS_REGION})
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3_client, bucket, region):
    if not bucket_exists(s3_client, bucket):
        s3_client.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={"LocationConstraint": region} if region != "us-east-1" else {}
        )

def bucket_exists(s3_client, bucket):
    try:
        s3_client.head_bucket(Bucket=bucket)
        return True
    except Exception:
        return False

# Upload to S3

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket:str, s3_file_name: str):
    try:
        s3.put(file_path, f"{bucket}/raw/{s3_file_name}")
        print('File uploaded to s3')
    except FileNotFoundError:
        print('The file was not found')