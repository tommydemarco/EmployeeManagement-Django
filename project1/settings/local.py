#LOCAL SETTINGS FILE

#importing the base settings to merge the two files
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #name of the database that you created with postgresql
        'NAME': 'dbproject1',
        #all the other settings created with postgresql
        'USER': 'tommy',
        'PASSWORD': 'Ch1tarra',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
