from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': "swconsulting",
        'USER': 'swconsulting',
        'PASSWORD': get_env("DJANGO_DATABASES_PASSWORD"),
    }
}

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
