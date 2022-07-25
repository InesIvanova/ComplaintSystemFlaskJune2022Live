import boto3
from botocore.exceptions import ClientError
from decouple import config
from werkzeug.exceptions import InternalServerError


class S3Service:
    def __init__(self):
        key = config("AWS_KEY")
        secret = config("AWS_SECRET_KEY")
        self.region = config("S3_REGION")
        self.bucket = config("S3_BUCKET_NAME")
        self.s3 = boto3.client('s3', region_name=self.region, aws_access_key_id=key, aws_secret_access_key=secret)

    def upload_photo(self, path, key):
        try:
            self.s3.upload_file(path, self.bucket, key)
            return f"https://{self.bucket}.s3.{self.region}.amazonaws.com/{key}"
        except ClientError as ex:
            raise InternalServerError("S3 is not available at the moment")

    def delete_photo(self, key):
        # TODO implement
        pass