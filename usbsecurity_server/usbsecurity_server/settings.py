"""
Django settings for usbsecurity_server project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

#  This module belongs to the usbsecurity-server project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Contact: alexis89.dev@gmail.com

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z)r7xjaklk6c2x)hcjz_f)n0(4_x4oq!k)b0%fk1wvw)xr*n2u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa',
    'usbsecurity_server.usbsecurity_server_app.apps.UsbsecurityServerAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'usbsecurity_server.usbsecurity_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'usbsecurity_server.usbsecurity_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#######################################################################################

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Espa??ol'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_URL = '/login/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'usbsecurity-server.log',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# PWA ########################################################################################

PWA_APP_NAME = 'USBSecurity'
PWA_APP_DESCRIPTION = _('Server program to control access to USB ports.')
PWA_APP_THEME_COLOR = '#fff'
PWA_APP_BACKGROUND_COLOR = '#fff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = '#fff'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/icon-72x72.png',
        'type': 'image/png',
        'sizes': '72x72',
    },
    {
        'src': '/static/images/icons/icon-96x96.png',
        'type': 'image/png',
        'sizes': '96x96',
    },
    {
        'src': '/static/images/icons/icon-128x128.png',
        'type': 'image/png',
        'sizes': '128x128',
    },
    {
        'src': '/static/images/icons/icon-144x144.png',
        'type': 'image/png',
        'sizes': '144x144',
    },
    {
        'src': '/static/images/icons/icon-152x152.png',
        'type': 'image/png',
        'sizes': '152x152',
    },
    {
        'src': '/static/images/icons/icon-192x192.png',
        'type': 'image/png',
        'sizes': '192x192',
    },
    {
        'src': '/static/images/icons/icon-384x384.png',
        'type': 'image/png',
        'sizes': '384x384',
    },
    {
        'src': '/static/images/icons/icon-512x512.png',
        'type': 'image/png',
        'sizes': '512x512',
    },
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 640px) and (device-height: 1136px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-750x1334.png',
        'media': '(device-width: 750px) and (device-height: 1334px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-828x1792.png',
        'media': '(device-width: 828px) and (device-height: 1792px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-1125x2436.png',
        'media': '(device-width: 1125px) and (device-height: 2436px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-1242x2208.png',
        'media': '(device-width: 1242px) and (device-height: 2208px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-1242x2688.png',
        'media': '(device-width: 1242px) and (device-height: 2688px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-1536x2048.png',
        'media': '(device-width: 1536px) and (device-height: 2048px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-1668x2224.png',
        'media': '(device-width: 1668px) and (device-height: 2224px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-1668x2388.png',
        'media': '(device-width: 1668px) and (device-height: 2388px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/splash-2048x2732.png',
        'media': '(device-width: 20480px) and (device-height: 27326px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
    },
]
# PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static', 'js', 'pwa-sw.js')

######################################################################################################

ACTION_ADD = 'add'
ACTION_REMOVE = 'remove'

STATICS_VERSION = 11
