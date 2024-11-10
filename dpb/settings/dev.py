import os
from .defaults import *

DEBUG = True

SECRET_KEY = "CHANGE_ME"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "dpb"),
        'USER': os.getenv("POSTGRES_USER", "dpb"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "razupaltuff"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}


SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "EMAIL_AUTHENTICATION": True,
        "APPS": [
            {
                "provider_id": "keycloak",
                "name": "DPB Login",
                "client_id": "website",
                "secret": "",
                "settings": {
                    "server_url": ""
                },
            }
        ]
    }
}
