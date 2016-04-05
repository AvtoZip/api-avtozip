"""Testing module for views of Store application."""

from django import test
from django.core.urlresolvers import reverse

from tastypie import http


class IndexViewTestCase(test.TestCase):
    """Index page tests of Store application."""

    def test_index_page(self):
        """Test index page of Store application."""
        response = self.client.get(reverse('store:index'))
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
