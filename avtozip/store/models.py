"""Store application models."""

from django.db import models


class StoreAddress(models.Model):
    """Model for address of the store."""

    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, null=True, blank=True)
    zip = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        """String representation of store address model."""
        address_line = ', '.join(
            [token for token in [
                self.zip, self.country, self.state, self.city, self.street, self.line1, self.line2,
            ] if token],
        )
        return '<{model_name}#{id}: {address_line}>'.format(
            model_name=self.__class__.__name__, id=self.id, address_line=address_line,
        )


class Store(models.Model):
    """Model for store."""

    name = models.CharField(max_length=200)
    address = models.ForeignKey('store.StoreAddress')

    def __str__(self):
        """String representation of store model."""
        return '<{model_name}#{id}: {name}>'.format(
            model_name=self.__class__.__name__, id=self.id, name=self.name,
        )


class ProductCategory(models.Model):
    """Model for category of the product."""

    class Meta:
        verbose_name_plural = 'ProductCategories'

    name = models.CharField(max_length=50)
    parent = models.ForeignKey('store.ProductCategory', null=True, blank=True)

    def __str__(self):
        """String representation of product category model."""
        return '<{model_name}#{id}: {name}>'.format(
            model_name=self.__class__.__name__, id=self.id, name=self.name,
        )


class Product(models.Model):
    """Model for any product in the store."""

    article = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store)

    def __str__(self):
        """String representation of product model."""
        return '<{model_name}#{id} ({article}): {name}>'.format(
            model_name=self.__class__.__name__, id=self.id, article=self.article, name=self.name,
        )
