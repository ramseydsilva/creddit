"""
Django settings for sprddit project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'served/media/')  # Uploaded content
STATIC_ROOT = os.path.join(PROJECT_PATH, 'served/static/')  # Static files: css, js, images, etc.
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ("creddit", os.path.join(PROJECT_PATH, 'static')),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4dsm+tz^9uwnh7rlhvy-tj3lh@kwl(d=^^y8k6bmj*zpx8r^b#'

DEBUG = True
THUMBNAIL_DEBUG = True
TEMPLATE_DEBUG = True
    
if os.environ.get('DATABASE_URL', False):
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  
            'NAME': 'creddit',
            'USER': 'ramsey',
            'PASSWORD': 'ramseypostgres..', 
            'HOST': 'localhost',
            'PORT': '',  
        }
    }

ALLOWED_HOSTS = ["*"]
APPEND_SLASH = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_pagination',
    'markdown_deux',
    'sorl.thumbnail',
    'tastypie',
    'api',
    'posts',
    'users'
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
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'posts.context_processors.site_settings',
                'posts.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

SETTINGS = {
    "title": "Creddit",
    "tagline": "Building internet credibility"
}

API_LIMIT_PER_PAGE = 10
TASTYPIE_DEFAULT_FORMATS = ['json']

LOGIN_URL = '/login/'
