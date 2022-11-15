from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbregistro',
        'USER' : 'sofiafer',
        'PASSWORD': 'sofia016',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field