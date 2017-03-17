#!/bin/sh
## virtualenv.sh for  in /home/spare/capgemini/meteo_server_git/meteo_api
## 
## Made by root
## Login   <spare@epitech.net>
## 
## Started on  Wed Mar  1 15:42:32 2017 root
## Last update Thu Mar  2 14:36:22 2017 root
##

virtualenv env
source env/bin/activate

pip install django
pip install djangorestframework
pip install pygments
pip install admindocs
pip install middleware

python manage.py runserver 0.0.0.0:8000
