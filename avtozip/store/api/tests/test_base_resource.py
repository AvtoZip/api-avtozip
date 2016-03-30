"""Tests for StoreBaseResource functionality."""

from django.test import TestCase

from tastypie import http


class GetSchemaTestCase(TestCase):
    """Forbidden schema access for any resource."""

    def test_product(self):
        """Test ProductResource."""
        response = self.client.get('/api/store_v1/product/schema/')
        self.assertEqual(response.status_code, http.HttpForbidden.status_code)

    def test_product_category(self):
        """Test ProductCategoryResource."""
        response = self.client.get('/api/store_v1/productcategory/schema/')
        self.assertEqual(response.status_code, http.HttpForbidden.status_code)
