"""
WSGI config for books project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

// defining that this application will use books.settings for default 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')

application = get_wsgi_application()
