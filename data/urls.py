from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from data import views

urlpatterns = [

    # Get all sensors
    url(r'^sensor/$', views.SensorList.as_view()),

    # Get sensors from a specific station
    url(r'^sensor/(?P<station_id>[0-9]+)/$', views.from_station),

    # Get last sensors value from a specific station 
    url(r'^sensor/(?P<station_id>[0-9]+)/last_values/$', views.last_values_from_station),

    # Get a specific sensor from a specific station
    url(r'^sensor/(?P<station_id>[0-9]+)/(?P<sensor_type>[a-z]+)/$', views.from_station_and_type),

    # Get sensors from a specific station in a given datetime range
    url(r'^sensor/(?P<station_id>[0-9]+)/(?P<begin_datetime>(((?:19|20|21)\d{2})(0?\d|1[012])(0?\d|[12]\d|3[01])-([0-9]|0[0-9]|1[0-9]|2[0-3])([0-5][0-9])([0-5][0-9])))/(?P<end_datetime>(((?:19|20|21)\d{2})(0?\d|1[012])(0?\d|[12]\d|3[01])-([0-9]|0[0-9]|1[0-9]|2[0-3])([0-5][0-9])([0-5][0-9])))/$', views.from_station_and_range), # Regex to check YYYYMMDD-HHMMSS. Unreadable but that works...

    # Get a specific sensor from a specific station in a given datetime range
    url(r'^sensor/(?P<station_id>[0-9]+)/(?P<sensor_type>[a-z]+)/(?P<begin_datetime>(((?:19|20|21)\d{2})(0?\d|1[012])(0?\d|[12]\d|3[01])-([0-9]|0[0-9]|1[0-9]|2[0-3])([0-5][0-9])([0-5][0-9])))/(?P<end_datetime>(((?:19|20|21)\d{2})(0?\d|1[012])(0?\d|[12]\d|3[01])-([0-9]|0[0-9]|1[0-9]|2[0-3])([0-5][0-9])([0-5][0-9])))/$', views.from_station_and_type_and_range),

    # Get all stations
    url(r'^station/$', views.StationList.as_view()),

    # Get a specific station
    url(r'^station/(?P<pk>[0-9]+)/$', views.StationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

