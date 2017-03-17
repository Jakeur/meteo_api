from django.db import models

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
    sensor = models.CharField(choices=SENSOR_CHOICES, default=SENSOR_CHOICES[0][0], max_length=100, help_text="type of the sensor")
    value = models.CharField(default='N/A', max_length=100, help_text="Floating number or wind direction")
    date = models.DateField(help_text="Date format: YYYY-MM-DD", blank=False)
    time = models.TimeField(help_text="Time format: HH:MM:SS", blank=False)
    station_id = models.IntegerField(default=-1, help_text="Station identifier where the data comes from")
    #owner = models.ForeignKey('auth.User', related_name='sensor', on_delete=models.CASCADE)
    

class Station(models.Model):
    """
    Station is a physical device that push datas from his different sensors
    """
    name = models.CharField(default='N/A', max_length=100, help_text="Station name")
    description = models.CharField(default='N/A', max_length=400, help_text="Station details")
    latitude = models.FloatField(default=500)
    longitude = models.FloatField(default=500)
    #owner = models.ForeignKey('auth.User', related_name='station', on_delete=models.CASCADE)
