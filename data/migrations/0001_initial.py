# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(choices=[('unknown', 'u'), ('hygrometry', 'h'), ('rain', 'r'), ('temperature', 't'), ('wind_direction', 'wd'), ('wind_strength', 'ws'), ('snow', 's'), ('pressure', 'p')], default='unknown', help_text='type of the sensor', max_length=100)),
                ('value', models.CharField(default='N/A', help_text='Floating number or wind direction', max_length=100)),
                ('date', models.DateField(auto_now_add=True, help_text='Field automatically fill with current date')),
                ('time', models.TimeField(auto_now_add=True, help_text='Field automatically fill with current time')),
                ('station_id', models.IntegerField(default=-1, help_text='Station identifier where the data comes from')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', help_text='Station name', max_length=100)),
                ('description', models.CharField(default='N/A', help_text='Station details', max_length=400)),
                ('latitude', models.FloatField(default=500)),
                ('longitude', models.FloatField(default=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
