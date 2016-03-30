"""Testing module for views of AvtoZip project."""

from django.template.exceptions import TemplateDoesNotExist
from django.test import TestCase

from ..views import dashboard_view


class DashboardViewTestCase(TestCase):
    """Dashboard page tests of AvtoZip project."""

    def test_direct_access(self):
        """Test direct access of the view."""
        self.assertRaises(TemplateDoesNotExist, *(dashboard_view, self.client.request))
