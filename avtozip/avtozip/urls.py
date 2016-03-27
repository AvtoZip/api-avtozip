"""avtozip URL Configuration."""

from django.conf.urls import include, url
from django.contrib import admin

from tastypie.api import Api

from store.api.resources import ProductResource


v1_api = Api(api_name='v1')
v1_api.register(ProductResource())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]
