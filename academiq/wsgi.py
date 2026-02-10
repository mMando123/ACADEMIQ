"""
WSGI config for academiq project.
This is used for PythonAnywhere deployment.
"""

import os
import sys

# Add project path for PythonAnywhere
path = '/home/yourusername/academiq'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academiq.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
