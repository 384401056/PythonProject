#!/usr/bin/env python
import os,django
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrazyMonitor.settings")
    django.setup()
    from app01.backend.management import execute_from_command_line
    execute_from_command_line(sys.argv)
