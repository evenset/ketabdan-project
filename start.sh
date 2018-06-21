#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec python manage.py collectstatic --noinput & python manage.py migrate --noinput & gunicorn ketabdan.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

