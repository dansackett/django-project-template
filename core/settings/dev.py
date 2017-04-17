# development-specific settings
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

ROOT_URLCONF = 'core.urls.dev'

INSTALLED_APPS = [
    'debug_toolbar',
    'whitenoise.runserver_nostatic',
] + INSTALLED_APPS

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ('127.0.0.1',)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}

# cache config
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# send emails to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# logging config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'static/bundles/',
        'STATS_FILE': os.path.join(ROOT_DIR, 'webpack-stats.json'),
    }
}
