"""Testing module for views of Store application."""

from django.template.exceptions import TemplateDoesNotExist
from django.test import TestCase

from ..views import index_view


class IndexViewTestCase(TestCase):
    """Index page tests of Store application."""

    def test_direct_access(self):
        """Test direct access of the view."""
        self.assertRaises(TemplateDoesNotExist, *(index_view, self.client.request))
