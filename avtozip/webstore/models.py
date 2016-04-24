"""WebStore application models."""

from django.db import models
from django.utils.translation import ugettext_lazy as _ul

from . import fields as custom_fields


class StoreAddress(models.Model):
    """Model for address of the store."""

    line1 = models.CharField(max_length=100, verbose_name=_ul('Line1'))
    line2 = models.CharField(max_length=100, null=True, blank=True, verbose_name=_ul('Line2'))
    street = models.CharField(max_length=40, verbose_name=_ul('Street'))
    city = models.CharField(max_length=40, verbose_name=_ul('City'))
    state = models.CharField(max_length=40, null=True, blank=True, verbose_name=_ul('State'))
    zip = models.CharField(max_length=20, verbose_name=_ul('ZIP'))
    country = models.CharField(max_length=20, verbose_name=_ul('Country'))

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

    name = models.CharField(max_length=200, verbose_name=_ul('Name'))
    address = models.ForeignKey('webstore.StoreAddress', verbose_name=_ul('Address'))

    def __str__(self):
        """String representation of store model."""
        return '<{model_name}#{id}: {name}>'.format(
            model_name=self.__class__.__name__, id=self.id, name=self.name,
        )


class ProductCategory(models.Model):
    """Model for category of the product."""

    class Meta:
        verbose_name_plural = 'ProductCategories'

    name = models.CharField(max_length=50, verbose_name=_ul('Name'))
    parent = models.ForeignKey('webstore.ProductCategory', null=True, blank=True, verbose_name=_ul('Category'))

    def __str__(self):
        """String representation of product category model."""
        return '<{model_name}#{id}: {name}>'.format(
            model_name=self.__class__.__name__, id=self.id, name=self.name,
        )


class Product(models.Model):
    """Model for product in the store."""

    article = custom_fields.ArticleField(verbose_name=_ul('Article'))
    name = models.CharField(max_length=200, verbose_name=_ul('Name'))
    category = models.ForeignKey(ProductCategory, verbose_name=_ul('Category'))
    cost = custom_fields.PositiveDecimalField(verbose_name=_ul('Cost'))
    price = custom_fields.PositiveDecimalField(verbose_name=_ul('Price'))
    count = custom_fields.PositiveDecimalField(verbose_name=_ul('Count'))
    is_active = models.BooleanField(default=True, verbose_name=_ul('Active'))
    store = models.ForeignKey(Store, verbose_name=_ul('Store'))

    def __str__(self):
        """String representation of product model."""
        return '<{model_name}#{id} ({article}): {name}>'.format(
            model_name=self.__class__.__name__, id=self.id, article=self.article, name=self.name,
        )
