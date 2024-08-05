#!/bin/bash

# Install dependencies
python install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
