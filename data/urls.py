from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from data import views

urlpatterns = [
    url(r'^sensor/$', views.SensorList.as_view()),
    url(r'^sensor/(?P<pk>[0-9]+)/$', views.SensorDetail.as_view()),
    url(r'^station/$', views.StationList.as_view()),
    url(r'^station/(?P<pk>[0-9]+)/$', views.StationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
