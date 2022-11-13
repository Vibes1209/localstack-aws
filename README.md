# localstack-aws
This repository uses localstack to run/test AWS services locally without an actual AWS account using boto3/CLI client


## Pre-requisites:
1. Python
2. Docker

Set Up Instructions

1. Install Dependencies in a virtual environment

python -m venv venv
source ./venv/Scripts/activate
pip install -r requirements.txt

2. Configure awscli with a local profile
    ```aws configure --profile local-profile```

    Enter any string for AWS ACCESS Key and SECTRET KEY when prompted eg. 'test123'
    Enter 'us-east-1' for region and 'json' for format when prompted

3. Start localstack server in a seperate terminal
    ```localstack start```

4. Set these env variables

    S3_BUCKET_NAME="mymockbucket"
    S3_FILE_NAME="s3file.txt"
    LOCAL_FILE_NAME_1="./data/local_file_1.txt"
    LOCAL_FILE_NAME_2="./data/local_file_2.txt"
    LOCALSTACK_ENDPOINT_URL="http://localhost:4566"

4. Run ``` python main.py ```
    It will run a series of S3 operations using boto3 SDK but all its requests will be directed to localstack server instead of actual AWS services

    The sequence of operation includes
    1. Creating a bucket
    2. Adding a file to the Bucket
    3. Downloading a file from the bucket
    4. Deleting the file in S3
    5. Deleting the bucket itself

### Note:
We can also execute the same sequence using awscli
Since we are mocking the S3 service, we need to pass "endpoint" and "profile" parameters for all cli commands

Eg. To list the objects in a bucket, 

instead of this
```aws s3 ls s3://<your_bucket_name> ```
use this 
```aws s3 ls s3://<your_bucket_name> --endpoint=http://localhost:4566 --profile local-profile```



