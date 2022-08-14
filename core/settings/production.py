from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2d8q0mpatkf2s',
        'USER': 'xfodvptcljrojx',
        'PASSWORD': '8a3c5c80d0e8b37ca3e93f49b0be005aa9b92d63d8359078e2b6a631e1790e78',
        'HOST': 'ec2-50-19-255-190.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')