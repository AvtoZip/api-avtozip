"""Store API resources."""

from django.db.models import Q

from tastypie import fields
from tastypie.http import HttpForbidden
from tastypie.resources import ModelResource

from store.models import (
    Product,
    ProductCategory,
    Store,
    StoreAddress,
)


class StoreBaseResource(ModelResource):
    """Base Resource API for Store application."""

    class Meta:
        allowed_methods = ('post', 'put', 'get', 'patch', 'delete')

    def get_schema(self, request, **kwargs):
        """Forbidden schema request."""
        bundle = self.build_bundle(request=request)
        return self.create_response(request, bundle, response_class=HttpForbidden)


class StoreAddressResource(StoreBaseResource):
    """Resource API for the store address."""

    class Meta(StoreBaseResource.Meta):
        queryset = StoreAddress.objects.all()


class StoreResource(StoreBaseResource):
    """Resource API for the store."""

    address = fields.ForeignKey('store.api.resources.StoreAddressResource', 'address')

    class Meta(StoreBaseResource.Meta):
        queryset = Store.objects.all()


class ProductCategoryResource(StoreBaseResource):
    """Resource API for category of the product."""

    parent = fields.ForeignKey('store.api.resources.ProductCategoryResource', 'parent', null=True)

    class Meta(StoreBaseResource.Meta):
        queryset = ProductCategory.objects.all()


class ProductResource(StoreBaseResource):
    """Resource API for product in the store."""

    category = fields.ForeignKey('store.api.resources.ProductCategoryResource', 'category')
    store = fields.ForeignKey('store.api.resources.StoreResource', 'store')

    QUERY_KEY = 'query'

    class Meta(StoreBaseResource.Meta):
        queryset = Product.objects.all()
        # TODO need to implement correct handling of custom_filters
        filtering = {}
        # TODO END

    def build_filters(self, filters=None, ignore_bad_filters=False):
        """Build required filters. Expanded by filter `query`."""
        if filters is None:
            filters = {}

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
