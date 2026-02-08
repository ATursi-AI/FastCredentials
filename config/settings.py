"""
Django settings for config project.
PRODUCTION SECURE MODE
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY: PRODUCTION SETTINGS ---
# 1. Disable Debug Mode (Hides errors from public)
DEBUG = False

# 2. Keep Secret Key Secret
SECRET_KEY = 'django-insecure-n_hd2d8^!472+adc1#x7_7@n31xe08_5$u^%c%%7c$^s&fgu+!'

# 3. Allow only your domain
ALLOWED_HOSTS = ['fastcredentials.com', 'www.fastcredentials.com', '127.0.0.1', 'localhost']

# 4. HTTPS Security Settings (Essential for Login)
CSRF_TRUSTED_ORIGINS = ['https://fastcredentials.com', 'https://www.fastcredentials.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False  # Set to False if Nginx handles SSL (safer to avoid loops)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# --- STRIPE SETTINGS ---
STRIPE_PUBLISHABLE_KEY = 'pk_test_51Suy40Q4Xmiwb7fPUzrhDBkS4TGwJ2ipsHJsEjGw486J1d9WiE90AYloIhQ50yf6V1O9VzTYWEZrL1i3TZdRER1T00YV6UGD7v' 
STRIPE_SECRET_KEY = 'sk_test_51Suy40Q4Xmiwb7fPpJIzhhYbF860cpZ8XKuohXSpB9VnP0C1hr41n60UMxYhdcplYTau1ml4tdr82lBlXeqpHMS900ZvKF2bqM'

# --- EMAIL SETTINGS (STILL IN CONSOLE MODE) ---
# We will fix this after your break to make emails actually send.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'FastCredentials <admin@fastcredentials.com>'

SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
X_FRAME_OPTIONS = 'ALLOWALL'
SECURE_CROSS_ORIGIN_EMBEDDER_POLICY = None
SITE_ID = 1
