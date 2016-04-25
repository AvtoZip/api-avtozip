"""Tests for StoreBaseResource functionality."""

from django.core.urlresolvers import reverse
from django.test import TestCase

from tastypie import http


class ResponseFormatTestCase(TestCase):
    """JSON/XML format with different request structure."""

    def test_no_format(self):
        """No format provided, JSON by default."""
        response = self.client.get(
            reverse('api_dispatch_list', kwargs={'resource_name': 'product', 'api_name': 'webstore_v1'}),
        )
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertIn('application/json', response.get('Content-Type'))

    def test_json_format_keyword(self):
        """JSON format provided using `?format=json`."""
        response = self.client.get(
            '{}?format={}'.format(
                reverse('api_dispatch_list', kwargs={'resource_name': 'product', 'api_name': 'webstore_v1'}),
                'json',
            ),
        )
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertIn('application/json', response.get('Content-Type'))

    def test_xml_format_keyword(self):
        """XML format provided using `?format=xml`."""
        response = self.client.get(
            '{}?format={}'.format(
                reverse('api_dispatch_list', kwargs={'resource_name': 'product', 'api_name': 'webstore_v1'}),
                'xml',
            ),
        )
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertIn('application/xml', response.get('Content-Type'))

    def test_json_format_appendix(self):
        """JSON format provided using `<resource>.json`."""
        response = self.client.get(
            reverse(
                viewname='api_dispatch_list',
                kwargs={'resource_name': 'product', 'api_name': 'webstore_v1', 'format': 'json'},
            ),
        )
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertIn('application/json', response.get('Content-Type'))

    def test_xml_format_appendix(self):
        """XML format provided using `<resource>.xml`."""
        response = self.client.get(
            reverse(
                viewname='api_dispatch_list',
                kwargs={'resource_name': 'product', 'api_name': 'webstore_v1', 'format': 'xml'},
            ),
        )
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertIn('application/xml', response.get('Content-Type'))


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
