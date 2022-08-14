from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5vvba4srtckot',
        'USER': 'dacvjmdahtilcg',
        'PASSWORD': 'dac5f2bc9afc5d496201749f51c6ae37d78559943ba136444484988998912ddd',
        'HOST': 'ec2-34-193-44-192.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')