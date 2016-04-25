"""WebStore API resources."""

from django.conf.urls import url
from django.db.models import Q

from tastypie import fields
from tastypie.http import HttpForbidden
from tastypie.resources import ModelResource

from ..models import (
    Product,
    ProductCategory,
    Store,
    StoreAddress,
)


class WebStoreBaseResource(ModelResource):
    """Base Resource API for WebStore application."""

    class Meta:
        allowed_methods = ('post', 'put', 'get', 'patch', 'delete')

    def prepend_urls(self):
        """
        Return a URL scheme based on the default scheme to specify the response format as a file extension.

        E.g. /api/webstore_v1/resource.json.
        """
        return [
            url(
                regex=r'^(?P<resource_name>{})\.(?P<format>\w+)$'.format(self._meta.resource_name),
                view=self.wrap_view('dispatch_list'),
                name='api_dispatch_list',
            ),
            url(
                regex=r'^(?P<resource_name>{})/schema\.(?P<format>\w+)$'.format(self._meta.resource_name),
                view=self.wrap_view('get_schema'),
                name='api_get_schema',
            ),
            url(
                regex=r'^(?P<resource_name>{})/set/(?P<pk_list>\w[\w/;-]*)\.(?P<format>\w+)$'.format(
                    self._meta.resource_name,
                ),
                view=self.wrap_view('get_multiple'),
                name='api_get_multiple',
            ),
            url(
                regex=r'^(?P<resource_name>{})/(?P<pk>\w[\w/-]*)\.(?P<format>\w+)$'.format(self._meta.resource_name),
                view=self.wrap_view('dispatch_detail'),
                name='api_dispatch_detail',
            ),
            ]

    def determine_format(self, request):
        """Used to determine the desired format from the request.format attribute."""
        if hasattr(request, 'format') and request.format in self._meta.serializer.formats:
            return self._meta.serializer.get_mime_for_format(request.format)
        return super(WebStoreBaseResource, self).determine_format(request)

    def wrap_view(self, view):
        """Outer view wrapper."""
        def wrapper(request, *args, **kwargs):
            """Inner view wrapper."""
            request.format = kwargs.pop('format', None)
            wrapped_view = super(WebStoreBaseResource, self).wrap_view(view)
            return wrapped_view(request, *args, **kwargs)
        return wrapper

    def get_schema(self, request, **kwargs):
        """Forbidden schema request."""
        bundle = self.build_bundle(request=request)
        return self.create_response(request, bundle, response_class=HttpForbidden)


class StoreAddressResource(WebStoreBaseResource):
    """Resource API for the store address."""

    class Meta(WebStoreBaseResource.Meta):
        queryset = StoreAddress.objects.all()


class StoreResource(WebStoreBaseResource):
    """Resource API for the store."""

    address = fields.ForeignKey('webstore.api.resources.StoreAddressResource', 'address')

    class Meta(WebStoreBaseResource.Meta):
        queryset = Store.objects.all()


class ProductCategoryResource(WebStoreBaseResource):
    """Resource API for category of the product."""

    parent = fields.ForeignKey('webstore.api.resources.ProductCategoryResource', 'parent', null=True)

    class Meta(WebStoreBaseResource.Meta):
        queryset = ProductCategory.objects.all()


class ProductResource(WebStoreBaseResource):
    """Resource API for product in the store."""

    category = fields.ForeignKey('webstore.api.resources.ProductCategoryResource', 'category')
    store = fields.ForeignKey('webstore.api.resources.StoreResource', 'store')

    QUERY_KEY = 'query'

    class Meta(WebStoreBaseResource.Meta):
        queryset = Product.objects.all()
        # TODO need to implement correct handling of custom_filters
        filtering = {}
        # TODO END

    def build_filters(self, filters=None, ignore_bad_filters=False):
        """Build required filters. Expanded by filter `query`."""
        orm_filters = super(ProductResource, self).build_filters(filters, ignore_bad_filters)

        # Append orm_filter `query`
        if self.QUERY_KEY in filters:
            query = filters[self.QUERY_KEY]
            qset = Q(article__icontains=query) | Q(name__icontains=query)
            orm_filters.update({self.QUERY_KEY: qset})

        return orm_filters

    def apply_filters(self, request, applicable_filters):
        """Apply applicable filters. Expanded by filter `query`."""
        if self.QUERY_KEY in applicable_filters:
            custom = applicable_filters.pop(self.QUERY_KEY)
        else:
            custom = None

        semi_filtered = super(ProductResource, self).apply_filters(request, applicable_filters)
        return semi_filtered.filter(custom) if custom else semi_filtered
