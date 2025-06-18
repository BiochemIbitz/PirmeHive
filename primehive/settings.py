"""
Django settings for primehive project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env.development for local development
load_dotenv(os.path.join(Path(__file__).resolve().parent.parent, '.env.development'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-development-only-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.FirebaseAuthMiddleware',  # Add Firebase middleware
]

ROOT_URLCONF = 'primehive.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'primehive.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Messages configuration
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Firebase Configuration
FIREBASE_CONFIG = {
    "apiKey": os.getenv('FIREBASE_API_KEY', 'AIzaSyD1z25MWrimY5Mfj2nHvoj3yTMgkSZMj68'),
    "authDomain": os.getenv('FIREBASE_AUTH_DOMAIN', 'primehive-a6e2c.firebaseapp.com'),
    "projectId": os.getenv('FIREBASE_PROJECT_ID', 'primehive-a6e2c'),
    "storageBucket": os.getenv('FIREBASE_STORAGE_BUCKET', 'primehive-a6e2c.firebasestorage.app'),
    "messagingSenderId": os.getenv('FIREBASE_MESSAGING_SENDER_ID', '799270848700'),
    "appId": os.getenv('FIREBASE_APP_ID', '1:799270848700:web:cffa5316a9343d9388a8b9'),
    "measurementId": os.getenv('FIREBASE_MEASUREMENT_ID', 'G-9ZG5Z01G5Q'),
    "databaseURL": os.getenv('FIREBASE_DATABASE_URL', '')
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
