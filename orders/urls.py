import patterns as patterns
from django.conf.urls import url, include
from django.contrib import admin
from orders import views


urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^ordering/(?P<book_id>\w+)/$', views.ordering, name='ordering'),
    url(r'^product_in_order/$', views.product_in_order, name='product_in_order'),
    url(r'^done_ordering/$', views.done_ordering, name='done_ordering'),
    url(r'^check_on_exist/$', views.check_on_exist, name='check_on_exist'),
]
