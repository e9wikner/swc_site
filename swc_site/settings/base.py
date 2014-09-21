"""
Django settings for swcblog project.

These settings are loaded from environment variables:
BASE_DIR = DJANGO_BASE_DIR
SECRET_KEY = DJANGO_SECRET_KEY
DATABASES: 'PASSWORD': DJANGO_DATABASES_PASSWORD

This settings file should be inherited by e.g. production.py where these
variables should be set:
DEBUG, TEMPLATE_DEBUG, ALLOWED_HOSTS, DATABASES

The environment variable DJANGO_SETTINGS_MODULE should point to the settings
file to be used.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.exceptions import ImproperlyConfigured

def get_env(var_name):
    """
    Loads the var_name environment variable.
    :param var_name:
    :return: :raise ImproperlyConfigured: If the var_name is not defined
    """
    env = os.environ.get(var_name)
    if env:
        return env
    else:
        raise ImproperlyConfigured("Set the {} environment variable"
                                   .format(var_name))

BASE_DIR = get_env("DJANGO_BASE_DIR")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env("DJANGO_SECRET_KEY")

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_markdown',
    'blog',
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

ROOT_URLCONF = 'swc_site.urls'

WSGI_APPLICATION = 'swc_site.wsgi.application'

LANGUAGE_CODE = 'sv_SE'

TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

# if USE_L10N is set to True, then the locale-dictated format has higher
# precedence and will be applied instead
USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
