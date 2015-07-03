"""Django Settings File."""

import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    'devf.mx',
    'www.devf.mx',
    'devfmx.herokuapp.com',
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages',
    'django_markdown',

    'home',
    'mentors',
    'programs',
    'senseis',
    'testimonials',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'devf.middlewares.SSLMiddleware',
)

ROOT_URLCONF = 'devf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'devf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if ENVIRONMENT != 'development':
    DATABASES['default'] = dj_database_url.config()

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static and Media Files
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'

MEDIAFILES_LOCATION = 'development_media'

if not DEBUG:
    STATIC_URL = 'https://%s.s3.amazonaws.com/' % os.getenv('AWS_S3_BUCKET')
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    MEDIAFILES_LOCATION = 'media'

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_S3_BUCKET')
AWS_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_QUERYSTRING_AUTH = False

MEDIA_URL = 'https://{0}.s3.amazonaws.com' +\
            '/{1}/'.format(os.getenv('AWS_S3_BUCKET'), MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'devf.custom_storages.MediaStorage'
# Static and Media Files
