from django.conf.urls import url, include
from django.contrib import admin
from Library import views


urlpatterns = [
    url(r'^library/', views.library, name='library'),
]