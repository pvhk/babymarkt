from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class StaticRootS3BotoStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_DIR

class MediaRootS3BotoStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_DIR