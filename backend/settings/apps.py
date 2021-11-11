
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'webpack_loader',

    'rest_framework',
    'corsheaders',

    'channels'

]

BACKEND_APPS = [
    'backend.core'
]

INSTALLED_APPS += BACKEND_APPS
