"""
WSGI config for django_rest_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

"""
WSGI config for django_rest_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.management import call_command
from django.contrib.auth.models import User

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_main.settings')

# Initialize Django application
django.setup()

# Create superuser if it doesn't exist
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpass123")

# Apply migrations
try:
    call_command('migrate')
except Exception as e:
    print(f"Migration failed: {e}")

application = get_wsgi_application()

