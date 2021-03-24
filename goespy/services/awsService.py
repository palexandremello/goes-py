import boto3
import botocore


class BucketAcessService:
    def __init__(self):
        self.__s3 = boto3.resource(
            "s3", config=botocore.client.Config(signature_version=botocore.UNSIGNED)
        )

    def get_public_bucket(self, bucket):
        return self.__s3.Bucket(bucket)
