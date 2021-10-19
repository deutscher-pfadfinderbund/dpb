"""
Django settings for dpb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")
DEBUG = os.getenv("DEBUG", "").lower() != "false"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ALLOWED_HOSTS = ['.deutscher-pfadfinderbund.de', 'deutscher-pfadfinderbund.de', '.jungenbund.de', '.maedchenbund.de',
#                  '127.0.0.1']
ALLOWED_HOSTS = ['*']

SITE_ID = 1
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = 'index'

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # 3rd party
    'dpb.apps.MyFilerConfig',  # Use Django-Filer with own config for verbose name
    'easy_thumbnails',
    'django_forms_bootstrap',
    'autoslug',
    'pagedown',
    'markdownify',

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
    'adressverzeichnis'
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MIDDLEWARE_CLASSES = MIDDLEWARE

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
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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
    ("bootstrap", os.path.join(BASE_DIR, 'node_modules/bootstrap/dist/js')),
    ("jquery", os.path.join(BASE_DIR, 'node_modules/jquery/dist')),
    ("styles", os.path.join(BASE_DIR, 'styles')),
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

# Configure Easy Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'pages': {'size': (350, 350), 'crop': "scale", 'quality': 100},
    },
}
MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            'table',
            'thead',
            'tbody',
            'th',
            'tr',
            'td',
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'em',
            'i',
            'li',
            'ol',
            'p',
            'strong',
            'ul',
            'img',
            'style',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
            'br',
            'div',
            'span'
        ],
        "MARKDOWN_EXTENSIONS": [
            'markdown.extensions.fenced_code',
            'markdown.extensions.extra',
            'markdown.extensions.md_in_html'
        ],
        "WHITELIST_ATTRS": [
            'href',
            'src',
            'alt',
            'class',
            'id',
        ]
    }
}
