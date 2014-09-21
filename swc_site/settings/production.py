from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': "swconsulting",
        'USER': 'swconsulting',
        'PASSWORD': get_env("DJANGO_DATABASES_PASSWORD"),
    }
}

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [".swconsulting.se", ]
