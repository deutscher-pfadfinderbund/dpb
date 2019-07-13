"""
Django settings for dpb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
import sys

import django.contrib.auth

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")
# DEBUG = os.getenv("DEBUG", "").lower() == "true"
DEBUG = True
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ALLOWED_HOSTS = ['.deutscher-pfadfinderbund.de', 'deutscher-pfadfinderbund.de', '.jungenbund.de', '.maedchenbund.de',
#                  '127.0.0.1']
ALLOWED_HOSTS = ['*']

SITE_ID = 1
LOGOUT_REDIRECT_URL = 'index'

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party
    'dpb.apps.MyFilerConfig',  # Use Django-Filer with own config for verbose name
    'easy_thumbnails',
    'django_forms_bootstrap',
    'autoslug',
    'pagedown',
    'markdown_deux',

    # Own apps
    'pages',
    'archive',
    'contact',
    'feedback',
    'intern',
    'blog',
    'links',
    'evening_program',
    'maps',
    'maedchenbund',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dpb.urls'

WSGI_APPLICATION = 'dpb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRES_DB", "dpb"),
        'USER': os.getenv("POSTGRES_USER", "dpb"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "razupaltuff"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
FILE_UPLOAD_PERMISSIONS = 0o777
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'templates/dpb'),
    os.path.join(BASE_DIR, 'contact/templates/contact'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Configure Templates
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'debug': DEBUG,
    },
},
]

# Filer Settings
FILER_CANONICAL_URL = 'filer/'

# Markdown Deux Settings
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": False,
    },
    "nohtml": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": "escape",
    },
}
# END MARKDOWN DEUX

# Configure Easy Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'pages': {'size': (350, 350), 'crop': "scale", 'quality': 100},
    },
}

# Needed for login
django.contrib.auth.LOGIN_URL = '/'
