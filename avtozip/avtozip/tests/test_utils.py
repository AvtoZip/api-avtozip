"""Testing module for Store application models."""

from django.test import TestCase

from ..utils import inject_settings


class InjectorTestCase(TestCase):
    """Inject settings testcases."""

    @classmethod
    def setUpTestData(cls):  # NOQA
        """Setup class based test data."""
        cls.context = {'DEBUG': None}

    def test_inject_production_success(self):
        """Success for production settings."""
        context = self.context.copy()
        inject_settings('avtozip.settings.production', context)
        self.assertEqual(context['DEBUG'], False)

    def test_inject_development_success(self):
        """Success for development settings."""
        context = self.context.copy()
        inject_settings('avtozip.settings.development', context)
        self.assertEqual(context['DEBUG'], True)

    def test_inject_local_failure(self):
        """Failure for local settings."""
        context = self.context.copy()
        self.assertRaises(ImportError, *(inject_settings, 'avtozip.settings.local', context))

    def test_inject_local_failure_silent(self):
        """Failure for local settings with silent error handling."""
        context = self.context.copy()
        inject_settings('avtozip.settings.local', context, fail_silently=True)
        self.assertEqual(context['DEBUG'], None)
