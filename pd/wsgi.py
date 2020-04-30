"""
WSGI config for pd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import DjnagoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pd.settings')

application = get_wsgi_application()
application = DjnagoWhiteNoise(application)
