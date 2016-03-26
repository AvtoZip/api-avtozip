"""Store models."""

from django.db import models


class Product(models.Model):
    """Class for any product in the store."""

    article = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.DecimalField(max_digits=10, decimal_places=2)
