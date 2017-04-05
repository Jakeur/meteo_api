from django.db import models
from datetime import datetime
from django.utils import timezone

SENSOR_CHOICES = (
    ('unknown', 'u'),
    ('hygrometry', 'h'),
    ('rain', 'r'),
    ('temperature', 't'),
    ('wind_direction', 'wd'),
    ('wind_strength', 'ws'),
    ('snow', 's'),
    ('pressure', 'p'),
)

class Sensor(models.Model):
    """
    Sensor is an atomic data pushed from a meteo station
    """
    sensor = models.CharField(choices=SENSOR_CHOICES, default=SENSOR_CHOICES[0][0], max_length=100, help_text="type of the sensor = hygrometry | rain | temperature | wind_direction | wind_strength | snow | pressure")
    value = models.CharField(default='N/A', max_length=100, help_text="Floating number or wind direction - string parameter")
    datetime = models.DateTimeField(default=timezone.now, blank=True, help_text="Datetime format: YYYY-MM-DD HH:MM:SS")
    station_id = models.IntegerField(default=-1, help_text="Station identifier where the data comes from - integer parameter")
    #owner = models.ForeignKey('auth.User', related_name='sensor', on_delete=models.CASCADE)
    

class Station(models.Model):
    """
    Station is a physical device that push datas from his different sensors
    """
    name = models.CharField(default='N/A', max_length=100, help_text="Station name - string parameter")
    description = models.CharField(default='N/A', max_length=400, help_text="Station details - string parameter")
    latitude = models.FloatField(default=500, help_text="floating parameter")
    longitude = models.FloatField(default=500, help_text="floating parameter")
    #owner = models.ForeignKey('auth.User', related_name='station', on_delete=models.CASCADE)
