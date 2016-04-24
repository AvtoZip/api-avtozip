"""Testing module for WebStore application models."""

from autofixture import AutoFixture

from django import test

from ..models import (
    Product,
    ProductCategory,
    Store,
    StoreAddress,
)


class ModelRepresentationTestCase(test.TestCase):
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

    def test_store_representation(self):
        """Test for store representation."""
        store = Store.objects.first()
        result = '{0}'.format(store)
        self.assertIn(store.__class__.__name__, result)
        self.assertIn(str(store.id), result)
        self.assertIn(store.name, result)

    def test_store_address_representation(self):
        """Test for store address representation."""
        store_address = StoreAddress.objects.first()
        result = '{0}'.format(store_address)
        self.assertIn(store_address.__class__.__name__, result)
        self.assertIn(str(store_address.id), result)
        self.assertIn(store_address.line1, result)
        self.assertIn(store_address.line2, result)
        self.assertIn(store_address.street, result)
        self.assertIn(store_address.city, result)
        self.assertIn(store_address.state, result)
        self.assertIn(store_address.zip, result)
        self.assertIn(store_address.country, result)
