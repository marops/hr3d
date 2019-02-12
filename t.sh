#!/bin/bash

python manage.py migrate issues zero
python manage.py migrate issues 
python manage.py loaddata --app issues issues_initial.json
