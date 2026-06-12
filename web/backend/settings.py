
DEBUG=True
SECURE=True
ANDROID = False
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
VERSION = '0.260106'
SECRET_KEY = os.environ.get('DJANGO_SECRET')

ALLOWED_HOSTS = ['melodify.ddns.net',]
CSRF_TRUSTED_ORIGINS = [ 'https://melodify.ddns.net', 'https://cpanel.iskarion.ddns.net' ]
CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS = [
    'main',
    'pwa',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fontawesome_5',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates' if not ANDROID else os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'melodify'),
        'USER': os.environ.get('POSTGRES_USER', 'iskarion'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'Iskarion777!'),
        'HOST': 'postgres',  # Debe coincidir exactamente con el nombre del servicio en tu docker-compose.yml
        'PORT': '5432', # Puerto por defecto de PostgreSQL
    }
}

LOG_FILE = '/var/log/melodify.log'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 
    'main.auth_backends.NostrAuthBackend',     
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"
USE_X_FORWARDED_HOST = True
CSRF_TRUSTED_ORIGINS = ['https://melodify.ddns.net']
STATIC_ROOT = '/static/melodify'
STATIC_FILES = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [ STATIC_FILES ]
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/melodify'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SPOTIFY_CLIENT_ID  = 'dc75272b15354119b9df60392848cc6a'
SPOTIFY_CLIENT_SECRET = '76d4dfef594f4625bd68b8068a574289' 

PWA_APP_NAME = 'Melodify'
PWA_APP_DESCRIPTION = "Melodify"
PWA_APP_THEME_COLOR = '#0A0000'
PWA_APP_BACKGROUND_COLOR = '#202020'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'

# Ruta a los iconos obligatorios para que sea instalable
PWA_APP_ICONS = [
    {
        'src': '/static/images/icon-160x160.png',
        'sizes': '160x160'
    },
    {
        'src': '/static/images/icon-512x512.png',
        'sizes': '512x512'
    }
]

# Ubicación del archivo de Service Worker personalizado (opcional)
# Si no lo defines, Django usará el Service Worker básico por defecto
PWA_SERVICE_WORKER_PATH = 'static/js/serviceworker.js'
