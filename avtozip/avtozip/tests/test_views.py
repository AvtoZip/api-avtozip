"""Testing module for views of AvtoZip project."""

from django import test
from django.core.urlresolvers import reverse

from tastypie import http


class DashboardViewTestCase(test.TestCase):
    """Dashboard page tests of AvtoZip project."""

    def test_index_page(self):
        """Test index page of AvtoZip project."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
