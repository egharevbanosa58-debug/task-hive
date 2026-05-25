#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv  # 1. Import django-dotenv

def main():
    """Run administrative tasks."""
    dotenv.load_dotenv()  # 2. Load the .env file before anything else
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ttProject.settings') # Keep your original line here
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()