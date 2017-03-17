from rest_framework import serializers
from data.models import Sensor, Station
#from django.contrib.auth.models import User

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'sensor', 'value', 'date', 'time', 'station_id')

        
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'name', 'description', 'latitude', 'longitude')

# Work in progress on authentication system
#class UserSerializer(serializers.ModelSerializer):
#    station = serializers.PrimaryKeyRelatedField(many=True, queryset=Station.objects.all())
#    sensor = serializers.PrimaryKeyRelatedField(many=True, queryset=Sensor.objects.all())
#    
#    class Meta:
#        model = User
#        fields = ('id', 'username', 'station', 'sensor')
