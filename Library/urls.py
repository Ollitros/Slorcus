import patterns as patterns
from django.conf.urls import url, include
from django.contrib import admin
from Library import views


urlpatterns = [
    url(r'^library/$', views.library, name='library'),
    url(r'^library/about_book/(?P<product_id>\w+)/$', views.about_book, name='about_book'),
]

