from rest_framework import generics
from data.models import Sensor, Station
from data.serializers import SensorSerializer, StationSerializer
from datetime import datetime
from pytz import timezone
import pytz

from rest_framework.decorators import api_view
from rest_framework.response import Response

"""    
GET request

**Context**

Webservice to list all :model:`data.Sensor` from a specific :model:`data.Station`.

**URL**

server_url/sensor/{id}/
"""
@api_view(['GET'])
def from_station(request, station_id):
    sensors = Sensor.objects.filter(station_id=station_id)
    serializer_class = SensorSerializer(sensors, many=True)
    return Response(serializer_class.data)

"""    
GET request

**Context**

Webservice to list a specific type of :model:`data.Sensor` from a specific :model:`data.Station`.

**URL**

server_url/sensor/{id}/{sensor_type}/
"""
@api_view(['GET'])
def from_station_and_type(request, station_id, sensor_type):
    sensors = Sensor.objects.filter(station_id=station_id, sensor=sensor_type)
    serializer_class = SensorSerializer(sensors, many=True)
    return Response(serializer_class.data)

"""    
GET request

**Context**

Webservice to list all :model:`data.Sensor` from a specific :model:`data.Station` in a given datetime range.
Datetime format request : YYYYMMDD-HHMMSS

**URL**

server_url/sensor/{id}/{begin_datetime}/{end_datetime}
"""
@api_view(['GET'])
def from_station_and_range(request, station_id, begin_datetime, end_datetime):
    tmp = begin_datetime.split("-")
    begin = datetime((int)(tmp[0][0:4]), (int)(tmp[0][4:6]), (int)(tmp[0][6:8]), (int)(tmp[1][0:2]), (int)(tmp[1][2:4]), (int)(tmp[1][4:6]), tzinfo=pytz.utc)
    tmp = end_datetime.split("-")
    end = datetime((int)(tmp[0][0:4]), (int)(tmp[0][4:6]), (int)(tmp[0][6:8]), (int)(tmp[1][0:2]), (int)(tmp[1][2:4]), (int)(tmp[1][4:6]), tzinfo=pytz.utc)
        
    sensors = Sensor.objects.filter(station_id=station_id, datetime__range=[begin, end])
    serializer_class = SensorSerializer(sensors, many=True)
    return Response(serializer_class.data)

"""    
GET request

**Context**

Webservice to list a specific type of :model:`data.Sensor` from a specific :model:`data.Station` in a given datetime range.
Datetime format request : YYYYMMDD-HHMMSS

**URL**

server_url/sensor/{id}/{sensor_type}/{begin_datetime}/{end_datetime}
"""
@api_view(['GET'])
def from_station_and_type_and_range(request, station_id, sensor_type, begin_datetime, end_datetime):
    tmp = begin_datetime.split("-")
    begin = datetime((int)(tmp[0][0:4]), (int)(tmp[0][4:6]), (int)(tmp[0][6:8]), (int)(tmp[1][0:2]), (int)(tmp[1][2:4]), (int)(tmp[1][4:6]), tzinfo=pytz.utc)
    tmp = end_datetime.split("-")
    end = datetime((int)(tmp[0][0:4]), (int)(tmp[0][4:6]), (int)(tmp[0][6:8]), (int)(tmp[1][0:2]), (int)(tmp[1][2:4]), (int)(tmp[1][4:6]), tzinfo=pytz.utc)

    sensors = Sensor.objects.filter(station_id=station_id, sensor=sensor_type, datetime__range=[begin, end])
    serializer_class = SensorSerializer(sensors, many=True)
    return Response(serializer_class.data)

class SensorList(generics.ListCreateAPIView):
    """    
    GET request

    **Context**
    
    Webservice to list all :model:`data.Sensor` from all :model:`data.Station`.
   
    **URL**

    server_url/sensor/
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
class StationList(generics.ListCreateAPIView):
    """    
    GET request

    **Context**
    
    Webservice to list all :model:`data.Station`.
   
    **URL**

    server_url/station/
    """
    
    queryset = Station.objects.all()
    serializer_class = StationSerializer

        
class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    """    
    GET / POST / DELETE requests

    **Context**
    
    Webservices to interact with a specific :model:`data.Station`.
   
    **URL**

    GET / DELETE -> server_url/station/{id}/

    POST -> server_url/sensor/ with form :model:`data.Station` filled.
    """
        
    queryset = Station.objects.all()
    serializer_class = StationSerializer
