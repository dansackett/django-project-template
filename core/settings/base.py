"""
Django settings for my_project project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# easy paths for finding directories
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.dirname(SETTINGS_DIR)
ROOT_DIR = os.path.dirname(CORE_DIR)

# useful paths
APPS_DIR = os.path.join(CORE_DIR, 'apps')
LOGS_DIR = os.path.join(CORE_DIR, 'logs')
MEDIA_DIR = os.path.join(ROOT_DIR, 'media')
DIST_DIR = os.path.join(ROOT_DIR, 'dist')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')

# add the apps directory to the PATH
sys.path.insert(0, os.path.join(APPS_DIR))

# set the name of the website here
SITE_NAME = 'Django Project Template'

ADMINS = [
    ('Dwight Shrute', 'dwight@dundermiflin.com'),
]

MANAGERS = ADMINS

# application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'crispy_forms',
    'registration',
]

LOCAL_APPS = [
    'accounts',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THIRD_PARTY_MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

LOCAL_MIDDLEWARE = []

MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.settings_file_constants',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
AUTH_USER_MODEL = 'accounts.User'

# internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DIST_DIR)

STATICFILES_DIRS = (
    os.path.join(STATIC_DIR),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(MEDIA_DIR)

# Django app config
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
DEFAULT_FROM_EMAIL = 'dwight@dundermiflin.com'

# third party setup
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_DEFAULT_FROM_EMAIL = 'noreply@example.com'
INCLUDE_REGISTER_URL = True
INCLUDE_AUTH_URLS = True
