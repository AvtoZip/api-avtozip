"""URLs module for Store REST API."""

from tastypie.api import Api

from . import resources


store_api = Api(api_name='store_v1')
store_api.register(resources.ProductResource())
store_api.register(resources.ProductCategoryResource())
store_api.register(resources.StoreResource())
store_api.register(resources.StoreAddressResource())
