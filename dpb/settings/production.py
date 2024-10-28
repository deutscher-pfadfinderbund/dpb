import os
from .defaults import *

DEBUG = False


### SECURITY ###

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['deutscher-pfadfinderbund.de', '.deutscher-pfadfinderbund.de', '.jungenbund.de', '.maedchenbund.de']

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://deutscher-pfadfinderbund.de']

SESSION_COOKIE_SECURE = True

# NGINX <-> Django is using HTTP
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ADMINS = [("BBI", "bbi@deutscher-pfadfinderbund.de")]


### DATABASE ###

DB_NAME = os.environ["POSTGRES_DB"]
DB_USER = os.environ["POSTGRES_USER"]
DB_PASS = os.environ["POSTGRES_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT or "5432",
    }
}


### E-MAIL ###

DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_EMAIL_HOST_USERUSER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]

EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_TIMEOUT = 10  # seconds