"""avtozip URL Configuration."""

from django.conf.urls import include, url
from django.contrib import admin

from tastypie.api import Api

from store.api.resources import ProductResource

from . import views


v1_api = Api(api_name='v1')
v1_api.register(ProductResource())


urlpatterns = [
    url(r'^$', views.dashboard_view, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url(r'^store/', include('store.urls', namespace='store')),
]
