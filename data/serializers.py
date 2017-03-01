from rest_framework import serializers
from data.models import Sensor, Station

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'sensor', 'value', 'date', 'time', 'station_id')

        
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'name', 'description', 'latitude', 'longitude')
