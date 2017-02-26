from rest_framework import generics
from data.models import Data
from data.serializers import DataSerializer

class DataList(generics.ListCreateAPIView):
    
    queryset = Data.objects.all()
    serializer_class = DataSerializer

        
class DataDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Data.objects.all()
    serializer_class = DataSerializer
