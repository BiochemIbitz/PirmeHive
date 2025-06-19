"""
Production settings for primehive project.
"""

from .settings import *
import os
from dotenv import load_dotenv

# Load environment variables from .env.production
load_dotenv(os.path.join(BASE_DIR, '.env.production'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Secret key
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Allowed hosts
# Include Netlify domains and any domains from environment variables
netlify_domains = ['netlify.app', '.netlify.app']
env_hosts = os.getenv('ALLOWED_HOSTS', '').split(',')
ALLOWED_HOSTS = env_hosts + netlify_domains if env_hosts != [''] else netlify_domains

# Database settings
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Email settings
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# Static files
STATIC_URL = os.getenv('STATIC_URL', '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = os.getenv('MEDIA_URL', '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Add whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings
if os.getenv('SECURE_SSL_REDIRECT', 'False') == 'True':
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
    },
}

# Firebase Configuration from environment variables
FIREBASE_CONFIG = {
    "apiKey": os.getenv('FIREBASE_API_KEY', FIREBASE_CONFIG['apiKey']),
    "authDomain": os.getenv('FIREBASE_AUTH_DOMAIN', FIREBASE_CONFIG['authDomain']),
    "projectId": os.getenv('FIREBASE_PROJECT_ID', FIREBASE_CONFIG['projectId']),
    "storageBucket": os.getenv('FIREBASE_STORAGE_BUCKET', FIREBASE_CONFIG['storageBucket']),
    "messagingSenderId": os.getenv('FIREBASE_MESSAGING_SENDER_ID', FIREBASE_CONFIG['messagingSenderId']),
    "appId": os.getenv('FIREBASE_APP_ID', FIREBASE_CONFIG['appId']),
    "measurementId": os.getenv('FIREBASE_MEASUREMENT_ID', FIREBASE_CONFIG['measurementId']),
    "databaseURL": os.getenv('FIREBASE_DATABASE_URL', FIREBASE_CONFIG['databaseURL'])
}

# Admin email for notifications
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@primehive.com')
