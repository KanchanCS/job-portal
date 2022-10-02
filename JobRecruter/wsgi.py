"""
WSGI config for JobRecruter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JobRecruter.settings")
sys.path.append('/media/')
sys.path.append('/media/')

application = get_wsgi_application()
