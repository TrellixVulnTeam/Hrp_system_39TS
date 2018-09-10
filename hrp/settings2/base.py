"""
Django settings for hrp project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iq3k8(iki_a=m4evl+z60tjqd0!d_!j@e+(g^uu2)ab2crem-j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
#    'django.contrib.sites',
    'django_extensions',
    
##    'djcelery',
    'django_celery_beat',
    'django_celery_results',
    'djcelery_email',
    'easy_pdf',
    'auditlog',
    
    'payroll',
    'leave',
    'appraisal',
    'recruitment',
    'asset',

    'session_security',
#    'pinax.notifications'
    'notify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
#    'middleware.Updated110EnforceLoginMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
]

ROOT_URLCONF = 'hrp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/../templates/',
            BASE_DIR + '/../templates/auth/',
            BASE_DIR + '/../payroll/templates/payroll/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'hrp.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Kampala' #'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

SERIALIZATION_MODULES = {
    'yml': "django.core.serializers.pyyaml"
}
#SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'
#STATIC_ROOT = BASE_DIR + '/payroll/static/'

AUTH_PROFILE_MODULE="payroll.EmployeeProfile"
LOGIN_URL='/login/'
LOGIN_REDIRECT_URL= '/home/'
PUBLIC_URLS=['.*login.*', '.*sendslips.*', '.*pdfdetail.*', '.*ext.*']

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
#BROKER_URL = 'http://localhost:15672'

#SESSION_EXPIRE_AT_BROWSER_CLOSE=True
#SESSION_SECURITY_WARN_AFTER=300
#SESSION_SECURITY_EXPIRE_AFTER=420

CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
#CELERY_RESULT_BACKEND = "database"#  'pgsql://steve:@localhost:5432/hrp2'
#CELERY_RESULT_BACKEND='djcelery.backends.database.DatabaseBackend'
CELERY_RESULT_BACKEND = 'amqp' # 'django-db'
#CELERY_RESULT_BACKEND = 'django-cache'
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_IMPORTS = ("payroll.tasks", )

LOGO_PATH = BASE_DIR + '/../payroll/static/img/hrp-logo-4pdf.png'
EMAIL_NOTIFICATION_SUBJECT_TEXT = 'HRP Notification'
HRP_SERVER_URL = 'http://localhost:7001'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s %(funcName)s() %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'hrp.log'),
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'payroll': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

