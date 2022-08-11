from .base import *


DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd4gr7q38j7el0o',
        'USER': 'ilagjelqhzcodz',
        'PASSWORD': '453819f31319cbf4a6739cf9b496af818dd05b8e3a23b5bf5db34f50442de442',
        'HOST': 'ec2-34-203-182-65.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')