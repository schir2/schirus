import os
from pathlib import Path
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env()
env = environ.Env(
    DEBUG=(bool, False)
)

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'main.apps.MainConfig',
    'blog.apps.BlogConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    'dal',
    'dal_select2',
    'tinymce',
    'sorl.thumbnail',
    'users',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

ROOT_URLCONF = 'schirus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'schirus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'users.User'

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_ADAPTER = 'users.adapters.CustomAccountAdapter'
SOCIAL_ACCOUNT_ADAPTER = 'users.adapters.CustomSocialAccountAdapter'
LOGIN_REDIRECT_URL = '/'

TINYMCE_JS_URL = os.path.join(STATIC_URL, 'tinymce/tinymce.min.js')
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, 'tinymce')
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "max-width": "768",
    "menubar": "file edit view insert table help",
    "plugins": "advlist autolink lists link charmap print preview anchor searchreplace visualblocks"
               "fullscreen insertdatetime table paste help",
    "toolbar": "bold italic underline strikethrough | formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | "
    "casechange permanentpen formatpainter removeformat"
    "fullscreen  preview print"
    "a11ycheck ltr rtl | showcomments addcomment",
}