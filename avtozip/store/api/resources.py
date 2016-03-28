"""Store API resources."""

from tastypie import fields
from tastypie.http import HttpForbidden
from tastypie.resources import ModelResource

from store.models import (
    Product,
    ProductCategory,
)


class StoreBaseResource(ModelResource):
    """Base Resource API for Store application."""

    def get_schema(self, request, **kwargs):
        """Forbidden schema request."""
        bundle = self.build_bundle(request=request)
        return self.create_response(request, bundle, response_class=HttpForbidden)


class ProductCategoryResource(StoreBaseResource):
    """Resource API for category of the product."""

    parent = fields.ForeignKey('store.api.resources.ProductCategoryResource', 'parent', null=True)

    class Meta:
        queryset = ProductCategory.objects.all()
        allowed_methods = ('post', 'put', 'get', 'patch', 'delete')


class ProductResource(StoreBaseResource):
    """Resource API for any product in the store."""

    category = fields.ForeignKey(ProductCategoryResource, 'category')

    class Meta:
        queryset = Product.objects.all()
        allowed_methods = ['post', 'put', 'get', 'patch', 'delete']
        filtering = {
            'name': ('exact',),
        }
