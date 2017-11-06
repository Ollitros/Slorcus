from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Home.urls')),
    url(r'^', include('Library.urls')),
    url(r'^', include('orders.urls')),

] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)