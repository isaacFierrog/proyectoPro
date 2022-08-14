from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dqthvvpvlih04',
        'USER': 'pkcmvxueqsgnfq',
        'PASSWORD': '238bde66551b0fe4939ae87eddaedf077b428432f4495de5973a551a441e46d4',
        'HOST': 'ec2-44-195-100-240.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')