#!/bin/sh
## virtualenv.sh for  in /home/spare/capgemini/meteo_server_git/meteo_api
## 
## Made by root
## Login   <spare@epitech.net>
## 
## Started on  Wed Mar  1 15:42:32 2017 root
## Last update Wed Apr  5 14:40:11 2017 root
##

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

