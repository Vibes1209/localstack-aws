import boto3
from typing import Optional
import os


class AwsSessionConfig(object):

    execution_env_to_aws_profile = {
    'local' : 'local-profile',
    'dev' : 'dev-profile',
    'prod': 'prod-profile'
    }

    def __init__(self,execution_env_name:Optional[str]=None):
        self.execution_env_name = execution_env_name.lower() if execution_env_name else None
        self.endpoint_url = os.getenv('LOCALSTACK_ENDPOINT_URL') if self.execution_env_name == 'local' else None
        self.aws_profile = self.__execution_env_to_aws_profile_mapping()

    def __execution_env_to_aws_profile_mapping(self):
        return AwsSessionConfig.execution_env_to_aws_profile[self.execution_env_name] if self.execution_env_name in AwsSessionConfig.execution_env_to_aws_profile else 'default'

    def create_session(self) -> boto3.Session:
        return boto3.Session(profile_name=self.aws_profile)



