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

class Data(models.Model):
    sensor = models.CharField(choices=SENSOR_CHOICES, default=SENSOR_CHOICES[0][1], max_length=100)
    value = models.CharField(default='N/A', max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    station_id = models.IntegerField(default=-1)

# Create your models here.
