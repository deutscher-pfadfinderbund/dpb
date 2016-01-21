"""
Django settings for dpb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
SECRET_KEY = "CHANGE_ME"
import django.contrib.auth
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# Import SECRET_KEY and check it
try:
    from dpb.settings_secret import *
except ImportError:
    print("[ERROR] dpb/settings_secret.py not found. Please create it according to the template settings_secret.py.template")
    sys.exit()

if SECRET_KEY == "CHANGE_ME":
    print("[ERROR] Please change your secret key, stored in dpb/settings_secret.py")
    print("More information: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY")
    sys.exit()
elif len(SECRET_KEY) < 50:
    print("[WARNING] Your SECRET_KEY is too short. Please consider changing it.")


ALLOWED_HOSTS = ['christian-meter.de', 'localhost', 'deutscher-pfadfinderbund.de', 'jungenbund.de']

SITE_ID = 1

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
    'dpb.apps.MyFilerConfig',       # Use Django-Filer with own config for verbose name
    'mptt',
    'easy_thumbnails',
    'captcha',
    'django_forms_bootstrap',
    'autoslug',
    'pagedown',
    'markdown_deux',

    # Own apps
    'pages',
    'login',
    'archive',
    'contact',
    'feedback',
    'intern',
    'blog',
    'links',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dpb.urls'

WSGI_APPLICATION = 'dpb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
            ]
        },
    },
]

# Filer Settings
FILER_CANONICAL_URL = 's/'

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

# Needed for login
django.contrib.auth.LOGIN_URL = '/'


### E-MAIL SETTINGS ###
EMAIL_HOST = "smtp.strato.de"
EMAIL_HOST_PASSWORD = "5kFYS4Svh5WF"
EMAIL_HOST_USER = "noreply@deutscher-pfadfinderbund.de"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = 465
EMAIL_SUBJECT_PREFIX = "[Deutscher-Pfadfinderbund.de]"
EMAIL_USE_SSL = True
### END E-MAIL ###

### Google Recaptcha Support ###
RECAPTCHA_PUBLIC_KEY = "6Ld9OBQTAAAAAFY3w4kc029PUVvFupckwo5PfR25"
RECAPTCHA_PRIVATE_KEY = "6Ld9OBQTAAAAAP7HT6Lu6IppZEOFD3LXjg2nrWSA"
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True
### END Recaptcha ###

### Haystack+Solr Search Engine ###
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
