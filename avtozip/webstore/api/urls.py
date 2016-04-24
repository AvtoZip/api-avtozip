"""URLs module for WebStore REST API."""

from tastypie.api import Api

from . import resources


webstore_api = Api(api_name='webstore_v1')
webstore_api.register(resources.ProductResource())
webstore_api.register(resources.ProductCategoryResource())
webstore_api.register(resources.StoreResource())
webstore_api.register(resources.StoreAddressResource())
