from .base import *

import authkey
DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = authkey.EMAIL_HOST
EMAIL_HOST_USER = authkey.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = authkey.EMAIL_HOST_PASSWORD
EMAIL_PORT = authkey.EMAIL_PORT
EMAIL_USE_TLS = authkey.EMAIL_USE_TLS
DEFAULT_FROM_EMAIL = authkey.DEFAULT_FROM_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = INSTALLED_APPS +[
    'storages',
]

DATABASES['default']['ATOMIC_REQUESTS'] = True

INTERNAL_IPS = ('127.0.0.1', 'localhost',)

AWS_STORAGE_BUCKET_NAME = authkey.BUCKET_NAME
AWS_ACCESS_KEY_ID = authkey.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = authkey.AWS_SECRET_ACCESS_KEY
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST = authkey.AWS_S3_HOST
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'djangostarter.storage.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'djangostarter.storage.MediaStorage'