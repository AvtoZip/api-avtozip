"""Store API resources."""

from tastypie.http import HttpForbidden
from tastypie.resources import ModelResource

from store.models import Product


class ProductResource(ModelResource):
    """Resource API for any product in the store."""

    class Meta:
        queryset = Product.objects.all()
        allowed_methods = ['post', 'put', 'get', 'patch', 'delete']
        filtering = {
            'name': ('exact',),
        }

    def get_schema(self, request, **kwargs):
        """Forbidden schema request."""
        bundle = self.build_bundle(request=request)
        return self.create_response(request, bundle, response_class=HttpForbidden)
