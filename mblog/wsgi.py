"""
WSGI config for mblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from os.path import join, dirname, abspath
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')

PROJECT_DIR = dirname(dirname(abspath(__file__)))#3
sys.path.insert(0, PROJECT_DIR)

#os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

application = get_wsgi_application()


