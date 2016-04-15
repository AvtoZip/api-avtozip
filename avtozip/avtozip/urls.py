"""avtozip URL Configuration."""

from django.conf.urls import include, url
from django.contrib import admin

from store.api.urls import store_api

from . import views


urlpatterns = [
    url(r'^$', views.dashboard_view, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(store_api.urls)),
    url(r'^store/', include('store.urls', namespace='store')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
