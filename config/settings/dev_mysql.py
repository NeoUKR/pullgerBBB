from .common import *
from pullgerSquirrel.settings import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MY_SQL_DEFAULT_NAME', 'bbb'),
        'USER': os.getenv('MY_SQL_DEFAULT_USER', 'bbb'),
        'PASSWORD': os.getenv('MY_SQL_DEFAULT_PASSWORD', 'password'),
        'HOST': os.getenv('MY_SQL_DEFAULT_HOST', '127.0.0.1'),
        'PORT': os.getenv('MY_SQL_DEFAULT_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
