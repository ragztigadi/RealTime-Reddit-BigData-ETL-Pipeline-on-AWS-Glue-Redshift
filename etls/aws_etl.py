import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION


def connect_to_s3():
    """
    Establishes a connection to AWS S3 using s3fs.
    Returns an authenticated S3FileSystem object.
    """
    try:
        s3 = s3fs.S3FileSystem(
            anon=False,
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_SECRET_ACCESS_KEY,
            client_kwargs={'region_name': AWS_REGION}
        )
        print(" Connected to S3")
        return s3
    except Exception as e:
        print(f" Failed to connect to S3: {e}")
        return None


def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket: str):
    """
    Creates the S3 bucket if it doesn't already exist.
    """
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f" Bucket '{bucket}' created")
        else:
            print(f" Bucket '{bucket}' already exists")
    except Exception as e:
        print(f" Failed to check/create bucket: {e}")


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str):
    """
    Uploads a file to the specified S3 bucket inside the 'raw' folder.
    """
    try:
        s3.put(file_path, f"{bucket}/raw/{s3_file_name}")
        print(f"File '{s3_file_name}' uploaded to bucket '{bucket}/raw/'")
    except FileNotFoundError:
        print(f" The file '{file_path}' was not found")
    except Exception as e:
        print(f" Failed to upload file to S3: {e}")
