from xml.etree.ElementInclude import include
from django.urls import path
from django.contrib import *
from citylocations import views


urlpatterns = [
    path('loc-nyc', views.loc_nyc, name='loc-nyc'), 
    path('', include('citylocations.urls')),
]