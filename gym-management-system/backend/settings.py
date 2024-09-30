# gym_backend/settings.py

import os
from pathlib import Path

# Path to the project's base directory, used for constructing absolute paths.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for cryptographic signing. Should be changed to a unique, secure key in production.
SECRET_KEY = 'your-secret-key'  # Replace with a secure secret key

# Debug mode is enabled for development. This should be set to False in production for security reasons.
DEBUG = True

# List of allowed hosts. In production, you should add the domain names that are allowed to access the app.
ALLOWED_HOSTS = []

# Installed apps in the Django project, including:
# - Core Django apps (admin, auth, etc.)
# - Third-party apps: 'rest_framework' for building APIs, 'corsheaders' for handling Cross-Origin Resource Sharing (CORS).
# - Custom apps: 'api' and 'users', likely to manage API endpoints and user-related functionalities.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',  # Custom app for API management
    'users',  # Custom app for user-related functionalities
]

# Middleware that processes requests and responses. It includes security-related middlewares and session management.
# 'corsheaders.middleware.CorsMiddleware' is added to handle CORS requests.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Enable CORS (Cross-Origin Resource Sharing)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# The root URL configuration for the project. Defines where to look for URL patterns.
ROOT_URLCONF = 'gym_backend.urls'

# Template configuration for rendering HTML views. It uses the default Django template engine.
# 'APP_DIRS' being True means that the template engine will search for templates in app directories.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Directory list for custom templates can be added here.
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

# Entry point for WSGI (Web Server Gateway Interface) to serve the application.
WSGI_APPLICATION = 'gym_backend.wsgi.application'

# Database configuration using Djongo, a MongoDB connector for Django.
# MongoDB will be running on 'localhost' at port '27017', and the database is named 'gym_management_db'.
DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # Djongo allows Django to interact with MongoDB.
        'NAME': 'gym_management_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Validators for user passwords to ensure security. Various rules are enforced:
# - 'UserAttributeSimilarityValidator': Prevents passwords similar to user attributes (e.g., username).
# - 'MinimumLengthValidator': Ensures a minimum password length.
# - 'CommonPasswordValidator': Prevents using common, easily guessed passwords.
# - 'NumericPasswordValidator': Prevents entirely numeric passwords.
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

# Localization settings. The default language is English (en-us), and the time zone is set to UTC.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True  # Enables Django’s internationalization system.
USE_TZ = True  # Enables timezone support.

# URL for serving static files (CSS, JavaScript, images). In production, this would typically point to a static file server.
STATIC_URL = '/static/'

# Default field type for automatically generated model primary keys (IDs).
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings: Allows requests from any origin during development.
# In production, this should be restricted to trusted domains for security.
CORS_ALLOW_ALL_ORIGINS = True  # For development only. Configure properly for production.