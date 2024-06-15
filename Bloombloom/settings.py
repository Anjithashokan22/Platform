"""
Django settings for Bloombloom project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-urqqa4r5a*q9i&i+%n8jt!dq1%)-f_4ugkif357xfj3ol9hit-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'credentials',
    'course_app',
    'event_app',
    'category',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'Bloombloom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Bloombloom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bloom_database',
        'USER':'root',
        'PASSWORD':'',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'credentials.CustomUser'

#django all-auth setting
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
SITE_ID=1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#login through email using django all-auth documentation
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_UNIQUE_EMAIL=True




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'anjithas@bloombloom.co'
EMAIL_HOST_PASSWORD = 'nfyj clfn cpjv clva'

# Password reset via email
PASSWORD_RESET_TIMEOUT_DAYS = 1

TWILIO_ACCOUNT_SID="AC156fe3a99be16476a2f7f371bd404137"
TWILIO_AUTH_TOKEN='fceb05d9d81ca10ba0c6cec7ee7c8d3e'
TWILIO_PHONE_NUMBER='+1 843 603 1132'




SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
            'https://www.googleapis.com/auth/user.birthday.read',  # To access the user's date of birth
            'https://www.googleapis.com/auth/user.addresses.read',  # To access the user's location
            'https://www.googleapis.com/auth/user.phonenumbers.read',  # To access the user's phone number
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'LOGIN_CALLBACK_URL': '/accounts/google/login/callback/',
        'OAUTH_PKCE_ENABLED': True,
    }
}

# Add the django-allauth settings, including client ID and client secret
SOCIALACCOUNT_PROVIDERS.update({
    'google': {
        'APP': {
            'client_id': '623358219774-s5f893j0ehd9qb06a1k9flqs4ubuqqt6.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
})

# Add other necessary django-allauth settings
LOGIN_REDIRECT_URL = reverse_lazy('save_top_purposes_view')  # Redirect URL after successful login
LOGOUT_REDIRECT_URL = reverse_lazy('login')  # Redirect URL after logout
SOCIALACCOUNT_QUERY_EMAIL=True
# LOGIN_REDIRECR_URL='home'

AUTH_USER_MODEL = 'credentials.customuser'

# crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"
# for facebook

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',  # Set to 'js_sdk' to use the Facebook connect SDK
        # 'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',
    }
}

# For apple

SOCIALACCOUNT_PROVIDERS = {
    "apple": {
        "APP": {
            # Your service identifier.
            "client_id": "your.service.id",

            # The Key ID (visible in the "View Key Details" page).
            "secret": "KEYID",

             # Member ID/App ID Prefix -- you can find it below your name
             # at the top right corner of the page, or it’s your App ID
             # Prefix in your App ID.
            "key": "MEMAPPIDPREFIX",

            "settings": {
                # The certificate you downloaded when generating the key.
                "certificate_key": """-----BEGIN PRIVATE KEY-----
s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
c3ts3cr3t
-----END PRIVATE KEY-----
"""
            }
        }
    }
}

# Social providers

SOCIALACCOUNT_ENABLED=True

ACCOUNT_FORMS = {
    'signup':'credentials.forms.CustomUserCreationForm',
}