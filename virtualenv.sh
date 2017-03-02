#!/bin/sh
## virtualenv.sh for  in /home/spare/capgemini/meteo_server_git/meteo_api
## 
## Made by root
## Login   <spare@epitech.net>
## 
## Started on  Wed Mar  1 15:42:32 2017 root
## Last update Wed Mar  1 17:34:14 2017 root
##

virtualenv env
source env/bin/activate

pip install django
pip install djangorestframework
pip install pygments
pip install docutils
pip install middleware

python manage.py runserver 0.0.0.0:8000
