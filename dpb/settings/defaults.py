"""
Django settings for dpb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# ALLOWED_HOSTS = ['.deutscher-pfadfinderbund.de', 'deutscher-pfadfinderbund.de', '.jungenbund.de', '.maedchenbund.de',
#                  '127.0.0.1']
ALLOWED_HOSTS = ['*']

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://deutscher-pfadfinderbund.de']

SESSION_COOKIE_SECURE = True

# NGINX <-> Django is using HTTP
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SITE_ID = 1
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
SERVER_EMAIL = 'website@deutscher-pfadfinderbund.de'

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
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.openid_connect',

    # Own apps
    'dpb',
    'pages',
    'archive',
    'contact',
    'intern',
    'blog',
    'links',
    'evening_program',
    'adressverzeichnis',
    'permalink',
    'vorfreude'
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
)

MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'dpb.urls'

WSGI_APPLICATION = 'dpb.wsgi.application'


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


ACCOUNT_ADAPTER = 'dpb.account_adapter.NoNewUsersAccountAdapter'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

# Static files (CSS, JavaScript, Images)
FILE_UPLOAD_PERMISSIONS = 0o644
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    ("leaflet", os.path.join(BASE_DIR, 'node_modules/leaflet/dist')),
    ("leaflet-fullscreen", os.path.join(BASE_DIR, 'node_modules/leaflet-fullscreen/dist')),
    ("bootstrap", os.path.join(BASE_DIR, 'node_modules/bootstrap/dist/js')),
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
THUMBNAIL_DEFAULT_STORAGE_ALIAS = "default"
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
            'span',
            'section',
            'article',
            'details',
            'summary'
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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
