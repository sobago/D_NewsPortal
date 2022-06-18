"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

EMAIL_HOST = 'smtp.beget.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'django_test123@sobago.ru'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_SSL = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

ALLOWED_HOSTS = ['*']
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'news.forms.CommonSignupForm'}
DEFAULT_FROM_EMAIL = 'django_test123@sobago.ru'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 1,
    }
}

# Application definition
INSTALLED_APPS = [
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'basic.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'news/templates/news')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Localization
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('ru', 'Русский'),
    ('en-us', 'English'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'style': '{',
#     'formatters': {
#         'console_debug': {
#             'format': '%(asctime)s %(levelname)s %(message)s'
#         },
#         'console_warning': {
#             'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
#         },
#         'console_error': {
#             'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
#         },
#         'file_general': {
#             'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
#         },
#         'file_errors': {
#             'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
#         },
#         'file_security': {
#             'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
#         },
#         'mail_admins': {
#             'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console_debug': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_debug'
#         },
#         'console_warning': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_warning'
#         },
#         'console_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_error'
#         },
#         'console_critical': {
#             'level': 'CRITICAL',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_error'
#         },
#         'file_general': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/general.log'),
#             'formatter': 'file_general'
#         },
#         'file_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/errors.log'),
#             'formatter': 'file_errors'
#         },
#         'file_critical': {
#             'level': 'CRITICAL',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/errors.log'),
#             'formatter': 'file_errors'
#         },
#         'file_security': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/security.log'),
#             'formatter': 'file_security'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'mail_admins'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console_debug', 'console_warning', 'console_error', 'console_critical', 'file_general',
#                          'file_critical'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins', 'file_error', 'file_critical'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.server': {
#             'handlers': ['mail_admins', 'file_error', 'file_critical'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.template': {
#             'handlers': ['file_error', 'file_critical'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.db_backends': {
#             'handlers': ['file_error', 'file_critical'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.security': {
#             'handlers': ['file_security'],
#             'level': 'ERROR',
#             'propagate': True,
#         }
#     }
# }
