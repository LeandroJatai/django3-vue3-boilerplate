from . import ambiente

from .apps import *
from .auth import *
from .drf import *
from .email import *
from .frontend import *
from .languages import *
from .logs import *
from .medias import *
from .middleware import *


env = ambiente.env
BASE_DIR = ambiente.BASE_DIR
PROJECT_ROOT = ambiente.PROJECT_ROOT

SECRET_KEY = env.str('SECRET_KEY', default='Env')

DEBUG = env.bool('DEBUG', True)

SHELL_PLUS = "ipython"

ALLOWED_HOSTS = []

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
