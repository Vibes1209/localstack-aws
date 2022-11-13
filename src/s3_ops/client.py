import boto3
from typing import Optional

class AwsResource(object):
    def __init__(self, session: boto3.Session, service_name: str, endpoint_url:Optional[str] ):
        self.resource = session.resource(service_name, endpoint_url=endpoint_url)

class AwsS3Resource(AwsResource):
    def __init__(self, session: boto3.Session,endpoint_url: Optional[str] = None, service_name: str ='s3'):
        super().__init__(session, service_name, endpoint_url)


    def create_bucket(self, bucket_name: str):
        return self.resource.create_bucket(Bucket=bucket_name)

    def list_bucket_contents(self,bucket_name):
        return [obj.key for obj in self.resource.Bucket(bucket_name).objects.all()]

    def delete_bucket(self, Bucket):
        return self.resource.Bucket(Bucket).delete()

    def upload_file(self, Filename_local:str, Bucket:str, Filename_S3:str):
        return self.resource.Object(Bucket,Filename_S3).upload_file(Filename=Filename_local)

    def download_file(self, Filename_local:str, Bucket:str, Filename_S3:str):
        return self.resource.Object(Bucket,Filename_S3).download_file(Filename=Filename_local)

    def delete_file(self, Bucket:str, Filename_S3:str):
        return self.resource.Bucket(Bucket).Object(Filename_S3).delete()