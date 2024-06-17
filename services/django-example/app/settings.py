from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 't!z4wdw8_4#yfkt&d!$ne6*30g^he)s6rx8o9s)nb5hdj)@4)z'

DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'app'
]

MIDDLEWARE = []

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
