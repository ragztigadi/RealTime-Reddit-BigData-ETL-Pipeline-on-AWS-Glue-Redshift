# pipelines/aws_s3_pipeline.py
from utils.constants import AWS_REGION, AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import boto3
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    s3 = connect_to_s3()

    s3_client = boto3.client(
        "s3",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    create_bucket_if_not_exist(s3_client, AWS_BUCKET_NAME, AWS_REGION)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])
