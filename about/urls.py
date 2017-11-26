from django.conf.urls import url, include
from django.contrib import admin
from about import views
from about.views import AboutView
from templates import *


urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    # url(r'^about/$', views.about, name='about'),
]