#!/bin/bash

python manage.py migrate issues zero
rm -rf /var/www/django/hr3dcms/media/docs/*
python manage.py migrate issues 
python manage.py loaddata --app issues issues_initial.json
