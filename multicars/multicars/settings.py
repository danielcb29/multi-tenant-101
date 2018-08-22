"""
Django settings for multicars project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u1g62$u6owa6s9jo7d(#sji7^@q^i=%v64pj8c1ew5(wm67bf*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.localhost'] ## Important


# Application definition

SHARED_APPS = (
    'django_tenants',  # mandatory
    'companies', # you must list the app where your tenant model resides in

    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

TENANT_APPS = (
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',

    # your tenant-specific apps
    'cars',
)

INSTALLED_APPS = list(set(SHARED_APPS + TENANT_APPS))


MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware', ## Important
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASE_ROUTERS = [
    'django_tenants.routers.TenantSyncRouter', ## Important
]

ROOT_URLCONF = 'multicars.tenant_urls' ## Important 
PUBLIC_SCHEMA_URLCONF = 'multicars.public_urls' ## Important

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'multicars.context_processors.company', ## Important
                'django.template.context_processors.debug',                
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TENANT_MODEL = "companies.Company" 
TENANT_DOMAIN_MODEL = "companies.Domain"

WSGI_APPLICATION = 'multicars.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend', ## Important
        'NAME': 'multicars',
        'USER': 'multicars',
        'PASSWORD': 'multicars',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
