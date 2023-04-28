#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
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
'''
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyNTE3OTUxLCJpYXQiOjE2ODI1MTQzNTEsImp0aSI6IjlhNjYxYTExOTdmYTQ2OTE4ZTBiYWU1NWEyY2M4ZGE1IiwidXNlcl9pZCI6MX0.urSVe5Vtitj5cSeJCSmdHIPxlWIBNICVhjZrg293PAs
'''
