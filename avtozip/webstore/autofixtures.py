"""Custom AutoFixtures."""

import string

from autofixture import AutoFixture, generators, register

from .models import Product


class ProductAutoFixture(AutoFixture):
    """Fixture for Product generation."""

    field_values = {
        'article': generators.StringGenerator(
            chars=string.ascii_letters + string.digits + ' -',
            max_length=Product._meta.get_field('article').max_length,
        ),
        'cost': generators.PositiveDecimalGenerator(
            max_digits=Product._meta.get_field('cost').max_digits,
            decimal_places=Product._meta.get_field('cost').decimal_places,
        ),
        'price': generators.PositiveDecimalGenerator(
            max_digits=Product._meta.get_field('price').max_digits,
            decimal_places=Product._meta.get_field('price').decimal_places,
        ),
        'count': generators.PositiveDecimalGenerator(
            max_digits=Product._meta.get_field('count').max_digits,
            decimal_places=Product._meta.get_field('count').decimal_places,
        ),
    }


register(Product, ProductAutoFixture)
