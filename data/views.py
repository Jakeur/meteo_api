from rest_framework import generics
from data.models import Sensor, Station
from data.serializers import SensorSerializer, StationSerializer

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

        
class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """    
    GET / POST / DELETE requests

    **Context**
    
    Webservices to interact with a specific :model:`data.Sensor`.
   
    **URL**

    GET / DELETE -> server_url/sensor/{id}/

    POST -> server_url/sensor/ with form :model:`data.Sensor` filled.
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
