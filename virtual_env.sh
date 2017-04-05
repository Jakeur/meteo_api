#!/bin/sh
## virtualenv.sh for  in /home/spare/capgemini/meteo_server_git/meteo_api
## 
## Made by root
## Login   <spare@epitech.net>
## 
## Started on  Wed Mar  1 15:42:32 2017 root
## Last update Wed Apr  5 14:39:40 2017 root
##

virtualenv env				# Launch virtualenv
source env/bin/activate

pip install django
pip install djangorestframework
pip install pygments
pip install admindocs
pip install middleware

easy_install --upgrade pytz		# Python Timezone manager

python manage.py runserver 0.0.0.0:8000	# Run server according to settings.py parameters
