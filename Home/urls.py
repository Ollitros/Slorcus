from django.conf.urls import url, include
from django.contrib import admin
from Home import views
from templates import *


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
]