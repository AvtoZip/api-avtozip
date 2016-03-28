"""Testing module for Store application models."""

from autofixture import AutoFixture

from django.test import TestCase

from ..models import (
    Product,
    ProductCategory,
)


class ModelRepresentationTestCase(TestCase):
    """Representation check for different models."""

    @classmethod
    def setUpTestData(cls):  # NOQA
        """Class based setup."""
        AutoFixture(Product, generate_fk=True).create()

    def test_product_representation(self):
        """Test for product representation."""
        product = Product.objects.first()
        result = '{0}'.format(product)
        self.assertIn(product.__class__.__name__, result)
        self.assertIn(str(product.id), result)
        self.assertIn(product.article, result)
        self.assertIn(product.name, result)

    def test_product_category_representation(self):
        """Test for product category representation."""
        product_category = ProductCategory.objects.first()
        result = '{0}'.format(product_category)
        self.assertIn(product_category.__class__.__name__, result)
        self.assertIn(str(product_category.id), result)
        self.assertIn(product_category.name, result)
