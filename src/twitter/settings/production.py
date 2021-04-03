import os

ALLOWED_HOSTS = [*]

# AWS FILES LOCATION
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADADA = True
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'finder-assets')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'

STATIC_URL = (
    "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
)

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'iadental.storage_backends.MediaStorage'

AWS_HEADERS = {
    'x-amz-acl': 'public-read',
    'Cache-Control': 'public, max-age=31556926'
}
