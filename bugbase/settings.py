import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()
print("🔎 DATABASE_URL:", os.getenv("DATABASE_URL"))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-y88%ec3qo_rs9yy1$aq-c*0!^)*d$29i347+f3mn-02u%#qf0p'
DEBUG = True  # Turn off after testing

ALLOWED_HOSTS = ['*']  # Simplified for Render

# === Installed Apps ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tracker',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

# === Middleware ===
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # CSRF middleware can stay — we're not using SessionAuth
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === URLConf & WSGI ===
ROOT_URLCONF = 'bugbase.urls'
WSGI_APPLICATION = 'bugbase.wsgi.application'

# === REST Framework Settings ===
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}

# === Database ===
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# === CORS ===
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    "https://bugbase-collaborative-bug-tracking.vercel.app",
]

# === Templates ===
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

# === Password Validators ===
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# === Static Files ===
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# === Other ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
