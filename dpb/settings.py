"""
Django settings for dpb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fy5#xmxaf&@-30c_nm)0te&@=-g9y+45i6r03+%2(1q@vfztr_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['christian-meter.de', 'localhost', 'deutscher-pfadfinderbund.de']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'django.contrib.pages',

    # 3rd party
    'filer',
    'mptt',
    'easy_thumbnails',
    'tinymce',
    'captcha',
    'django_forms_bootstrap',

    # Own apps
    'polls',
    'pages',
    'login',
    'archive',
    'contact',
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
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = "/var/www/dpbstatic/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'media'),
    os.path.join(BASE_DIR, 'templates/dpb'),
    os.path.join(BASE_DIR, 'contact/templates/contact'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Configure TinyMCE
# Find the TinyMCE configuration in /templates/admin/base_site.html

TINYMCE_JS_URL = STATIC_URL + 'assets/tinymce/tinymce.min.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "code,directionality,paste,searchreplace,bootstrap",
    'theme': "modern",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'language': "de",
    'directionality': "de",
    'spellchecker_languages': "de",
    'spellchecker_rpc_url': STATIC_URL + 'assets/tinymce/langs/de.js',
    'bootstrapConfig': {
        'imagesPath': MEDIA_URL + 'img/filer_public',
    },
    'toolbar': "bootstrap",
    'fullpage_default_encoding': "UTF-8",
    'entity_encoding': "raw",
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False


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
            ],
        },
    },
]

# Needed for login
import django.contrib.auth
django.contrib.auth.LOGIN_URL = '/'


### E-MAIL SETTINGS ###
EMAIL_HOST = "smtp.strato.de"
EMAIL_HOST_PASSWORD = "6w25Y@Zf$Sj!"
EMAIL_HOST_USER = "noreply@deutscher-pfadfinderbund.de"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = 465
EMAIL_SUBJECT_PREFIX = "[Deutscher-Pfadfinderbund.de]"
EMAIL_USE_SSL = True
### END E-MAIL ###

### Google Recaptcha Support ###
RECAPTCHA_PUBLIC_KEY = "6LdOm_cSAAAAAMAn4otF5sCysq0TGz0eJtjK38CO"
RECAPTCHA_PRIVATE_KEY = "6LdOm_cSAAAAAI6FJ1vC5iR589Me1lLSUjilpzun"
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True

### END Recaptcha ###