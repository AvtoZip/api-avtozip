"""Store application models."""

from django.db import models


class ProductCategory(models.Model):
    """Model for category of the product."""

    class Meta:
        verbose_name_plural = 'ProductCategories'

    name = models.CharField(max_length=50)
    parent = models.ForeignKey('ProductCategory', null=True, blank=True)

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
