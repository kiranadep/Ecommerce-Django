#!/bin/bash

# Install dependencies
python3.10 -m pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput
