"""
WSGI config for quantified_self_py project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
# ADDED PER TUTORIAL-----^

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quantified_self_py.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
# ADDED PER TUTORIAL-----^
