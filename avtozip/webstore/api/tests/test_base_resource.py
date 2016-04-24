"""Tests for StoreBaseResource functionality."""

from django.core.urlresolvers import reverse
from django.test import TestCase

from tastypie import http


class GetSchemaTestCase(TestCase):
    """Forbidden schema access for any resource."""

    def test_product(self):
        """Test ProductResource."""
        response = self.client.get(
            reverse('api_get_schema', kwargs={'resource_name': 'product', 'api_name': 'webstore_v1'}),
        )
        self.assertEqual(response.status_code, http.HttpForbidden.status_code)

    def test_product_category(self):
        """Test ProductCategoryResource."""
        response = self.client.get(
            reverse('api_get_schema', kwargs={'resource_name': 'productcategory', 'api_name': 'webstore_v1'}),
        )
        self.assertEqual(response.status_code, http.HttpForbidden.status_code)

    def test_store(self):
        """Test StoreResource."""
        response = self.client.get(
            reverse('api_get_schema', kwargs={'resource_name': 'store', 'api_name': 'webstore_v1'}),
        )
        self.assertEqual(response.status_code, http.HttpForbidden.status_code)

    def test_store_address(self):
        """Test StoreAddressResource."""
        response = self.client.get(
            reverse('api_get_schema', kwargs={'resource_name': 'storeaddress', 'api_name': 'webstore_v1'}),
        )
        self.assertEqual(response.status_code, http.HttpForbidden.status_code)
