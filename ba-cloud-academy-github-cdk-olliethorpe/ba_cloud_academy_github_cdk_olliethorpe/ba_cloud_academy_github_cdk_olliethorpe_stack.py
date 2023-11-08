from aws_cdk import (
    Stack,
    aws_s3 as s3, 
    RemovalPolicy
)
from constructs import Construct

class BaCloudAcademyGithubCdkOlliethorpeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket( 
            self, 
            'ollies-bucket-object', 
            bucket_name='ollies-github-workflow-bucket', 
            removal_policy=RemovalPolicy.DESTROY 
        )
