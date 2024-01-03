#!/bin/sh
set -e

python manage.py migrate --no-input

gunicorn -b 0.0.0.0:8000 dpb.wsgi
