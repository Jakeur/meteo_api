from django.db import models

SENSOR_CHOICES = (
    ('u', 'unknown'),
    ('h', 'hygrometry'),
    ('r', 'rain'),
    ('t', 'temperature'),
    ('wd', 'wind_direction'),
    ('ws', 'wind_strength'),
    ('s', 'snow'),
)

class Sensor(models.Model):
    """
    Sensor is an atomic data pushed from a meteo station
    """
    sensor = models.CharField(choices=SENSOR_CHOICES, default=SENSOR_CHOICES[0][1], max_length=100, help_text="type of the sensor")
    value = models.CharField(default='N/A', max_length=100, help_text="Floating number or wind direction")
    date = models.DateField(auto_now_add=True, help_text="Field automatically fill with current date")
    time = models.TimeField(auto_now_add=True, help_text="Field automatically fill with current time")
    station_id = models.IntegerField(default=-1, help_text="Station identifier where the data comes from")


class Station(models.Model):
    """
    Station is a physical device that push datas from his different sensors
    """
    name = models.CharField(default='N/A', max_length=100, help_text="Station name")
    description = models.CharField(default='N/A', max_length=400, help_text="Station details")
    latitude = models.FloatField(default=500)
    longitude = models.FloatField(default=500)
