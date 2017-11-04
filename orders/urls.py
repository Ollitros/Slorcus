import patterns as patterns
from django.conf.urls import url, include
from django.contrib import admin
from orders import views


urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^ordering/(?P<book_id>\w+)/$', views.ordering, name='ordering'),
]