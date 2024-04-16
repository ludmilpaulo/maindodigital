
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dk=wa$(!d5kyeu)y-cu6vt*&71hykop5uik@nncr#n8s7rq$1z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['www.maindodigital.com',
                    'maindodigital.com']


DEFAULT_FROM_EMAIL = 'info@maindodigital.com'

ADMINS = [('Maindo Digital Agency', 'info@maindodigital.com')]
MANAGERS = ADMINS

SERVER_EMAIL = 'info@maindodigital.com' # this is for to send 500 mail to admins


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
    'django.contrib.postgres',
    'widget_tweaks',
    'easy_thumbnails',
    'team',

    'allauth',
    #'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

   # 'bootstrap4',
    'bootstrapform',
    'django_extensions',
    'memcache_status',
    'bootstrap5',
    'chat',
    'social_django',
    'oauth2_provider',
    'markdown_deux',

    'blog',
    'taggit',
    'courses',
    'students',
    'embed_video',
    'home_page',
    'account',
    'channels',
    'columns',
    'shop',
    'orders',
    'rosetta',
    'parler',
    'localflavor',
    'studentPreferences',
    'questions',

]

LOGIN_REDIRECT_URL = '/account/'
LOGIN_URL = 'account:login'
LOGOUT_URL = '/'

#FACEBOOK_STORE_LOCAL_IMAGE = False

CART_SESSION_ID = 'cart'

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION= False

# allow upload big file
# DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 95  # 15M
# FILE_UPLOAD_MAX_MEMORY_SIZE = DATA_UPLOAD_MAX_MEMORY_SIZE

CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'maindodigital.urls'

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
                'cart.context_processors.cart',
                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]

WSGI_APPLICATION = 'maindodigital.wsgi.application'

ASGI_APPLICATION = 'maindodigital.routing.application'

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

from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('pt', _('Portuguese')),
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'pt'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statics"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")


ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
DEFAULT_HTTP_PROTOCOL           = "https"
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_HOST_USER='info@maindodigital.com'
EMAIL_HOST_PASSWORD='Maindo@2021'
EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_USE_TLS=False

from django.urls import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('students:student_course_list')

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'www.maindodigital.com',
#     }
# }

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'maindodigital'


ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail',
                                        args=[u.username])
}

#SOCIAL_AUTH_LOGIN_URL = ""
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = "dashboard"
#SOCIAL_AUTH_LOGIN_ERROR_URL = "error"


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend',

]

SOCIAL_AUTH_FACEBOOK_KEY = '' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']



SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]

SOCIAL_AUTH_TWITTER_KEY = '' # Twitter API Key
SOCIAL_AUTH_TWITTER_SECRET = '' # Twitter API Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' # Google Consumer Secret

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('www.maindodigital.com', 6379)],
#         },
#     },
# }

SOCIAL_AUTH_PIPELINE = [  # Note: Sequence of functions matters here.
    'social.pipeline.social_auth.social_details',  # 0
    'social.pipeline.social_auth.social_uid',  # 1
    'social.pipeline.social_auth.auth_allowed',  # 2
    'social.pipeline.social_auth.social_user',  # 3
    'social.pipeline.user.get_username',  # 4
    'social.pipeline.social_auth.associate_by_email',  # 5
    'social.pipeline.social_auth.associate_user',  # 6
    'social.pipeline.social_auth.load_extra_data',  # 7
    'social.pipeline.user.user_details',  # 8
]



BRAINTREE_MERCHANT_ID = ''  # Merchant ID
BRAINTREE_PUBLIC_KEY = ''   # Public Key
BRAINTREE_PRIVATE_KEY = ''  # Private key

import braintree

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)



REDIS_HOST = 'maindodigital.com'
REDIS_PORT = 6379
REDIS_DB = 1


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('35.173.69.207', 6379)],
        },
    },
}



SITE_ID = 1
