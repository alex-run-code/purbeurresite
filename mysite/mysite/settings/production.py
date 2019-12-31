from . import *

SECRET_KEY = '-~aO;| F;rE[??/w^zcumh(9'
DEBUG = False
ALLOWED_HOSTS = ['51.91.253.245']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'purbeurredb', # le nom de notre base de données créée précédemment
        'USER': 'alexandre', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': '123456',
        'HOST': '',
        'PORT': '5432',
    }
}

