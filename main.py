from src.s3_ops.config import AwsSessionConfig
from src.s3_ops.client import AwsS3Resource
import os
from dotenv import load_dotenv
import boto3
from typing import Optional

aws_envs = {
    'local' : 'local-profile',
    'dev' : 'dev-profile',
    'prod': 'prod-profile'
}

def get_aws_session(env_name:str) -> boto3.Session:
    aws_profile_name = None
    if env_name in aws_envs:
        aws_profile_name = aws_envs[env_name]
    return boto3.Session(profile_name=aws_profile_name)


def main(environment:Optional[str]=None):
    
    print("Creating AWS session")
    config = AwsSessionConfig(environment)
    session = config.create_session()

    print("Creating S3 Resource")
    s3_resource = AwsS3Resource(session=session,endpoint_url=config.endpoint_url)

    # Create a new bucket
    my_bucket = s3_resource.create_bucket(os.getenv("S3_BUCKET_NAME"))
    print(f"New bucket {my_bucket.name} is created")

    # Add a local file (file_1.txt) to the bucket and store it as s3_file.txt
    _ = s3_resource.upload_file(
            Filename_local=os.getenv("LOCAL_FILE_NAME_1"),
            Bucket=os.getenv("S3_BUCKET_NAME"),
            Filename_S3=os.getenv("S3_FILE_NAME")
    )
    print("File uploaded to S3 bucket")
    print(s3_resource.list_bucket_contents(os.getenv("S3_BUCKET_NAME")))

    # Retrieve a S3 file (s3_file.txt) from the bucket and store it locally (file_2.txt)
    _ = s3_resource.download_file(
            Filename_local=os.getenv("LOCAL_FILE_NAME_2"),
            Bucket=os.getenv("S3_BUCKET_NAME"),
            Filename_S3=os.getenv("S3_FILE_NAME")
    )
    print("File Downloaded from S3 bucket")


    # Delete S3 file
    _ = s3_resource.delete_file(Bucket=os.getenv("S3_BUCKET_NAME"), Filename_S3=os.getenv("S3_FILE_NAME"))
    print("File deleted in S3 bucket")
    print(s3_resource.list_bucket_contents(os.getenv("S3_BUCKET_NAME")))

    # Delete Bucket
    _ = s3_resource.delete_bucket(Bucket=os.getenv("S3_BUCKET_NAME"))
    print("S3 Bucket deleted")


if __name__=='__main__':
    load_dotenv(".env")
    execution_env = 'local'
    main(execution_env)
