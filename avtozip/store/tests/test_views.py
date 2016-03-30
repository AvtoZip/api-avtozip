"""Testing module for views of Store application."""

from autofixture import AutoFixture

from django import test
from django.core.urlresolvers import reverse

from tastypie import http

from ..models import Product


class ProductListViewTestCase(test.TestCase):
    """Product List page of Store application."""

    @classmethod
    def setUpTestData(cls):  # NOQA
        """Class based setup."""
        cls.product = AutoFixture(Product, generate_fk=True).create_one()

    def test_get(self):
        """Test GET method."""
        response = self.client.get(reverse('store:index'))
        self.assertEqual(response.status_code, http.HttpResponse.status_code)

    def test_post_no_changes(self):
        """Test POST without changes."""
        data = {
            'form-0-id': self.product.pk,
            'form-0-article': self.product.article,
            'form-0-name': self.product.name,
            'form-0-category': self.product.category_id,
            'form-0-cost': self.product.cost,
            'form-0-price': self.product.price,
            'form-0-count': self.product.count,
            'form-0-store': self.product.store_id,
            'form-1-id': '',
            'form-1-article': '',
            'form-1-name': '',
            'form-1-category': '',
            'form-1-cost': '',
            'form-1-price': '',
            'form-1-count': '',
            'form-1-store': '',
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '1',
        }
        response = self.client.post(reverse('store:index'), data)
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertEqual(Product.objects.count(), 1)

    def test_post_changed(self):
        """Test POST with changes."""
        new_product = AutoFixture(Product, generate_fk=True).create_one(commit=False)
        self.assertEqual(Product.objects.count(), 1)
        data = {
            'form-0-id': self.product.pk,
            'form-0-article': new_product.article,
            'form-0-name': new_product.name,
            'form-0-category': new_product.category_id,
            'form-0-cost': new_product.cost,
            'form-0-price': new_product.price,
            'form-0-count': new_product.count,
            'form-0-store': new_product.store_id,
            'form-1-id': '',
            'form-1-article': '',
            'form-1-name': '',
            'form-1-category': '',
            'form-1-cost': '',
            'form-1-price': '',
            'form-1-count': '',
            'form-1-store': '',
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '1',
        }
        response = self.client.post(reverse('store:index'), data)
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertEqual(Product.objects.count(), 1)
        new_product.id = self.product.id
        prod = Product.objects.first()
        self.assertNotEqual(str(self.product), str(prod))

    def test_post_new(self):
        """Test POST with new object creation."""
        new_product = AutoFixture(Product, generate_fk=True).create_one(commit=False)
        self.assertEqual(Product.objects.count(), 1)
        data = {
            'form-0-id': self.product.pk,
            'form-0-article': self.product.article,
            'form-0-name': self.product.name,
            'form-0-category': self.product.category_id,
            'form-0-cost': self.product.cost,
            'form-0-price': self.product.price,
            'form-0-count': self.product.count,
            'form-0-store': self.product.store_id,
            'form-1-id': '',
            'form-1-article': new_product.article,
            'form-1-name': new_product.name,
            'form-1-category': new_product.category_id,
            'form-1-cost': new_product.cost,
            'form-1-price': new_product.price,
            'form-1-count': new_product.count,
            'form-1-store': new_product.store_id,
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '1',
        }
        response = self.client.post(reverse('store:index'), data)
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertEqual(Product.objects.count(), 2)
        prod1, prod2 = Product.objects.order_by('id')
        self.assertEqual(str(self.product), str(prod1))
        new_product.id = prod2.id
        self.assertAlmostEqual(str(new_product), str(prod2))

    def test_post_invalid(self):
        """Test POST with invalid data."""
        new_product = AutoFixture(Product, generate_fk=True).create_one(commit=False)
        self.assertEqual(Product.objects.count(), 1)
        data = {
            'form-0-id': self.product.pk,
            'form-0-article': '',
            'form-0-name': new_product.name,
            'form-0-category': new_product.category_id,
            'form-0-cost': new_product.cost,
            'form-0-price': new_product.price,
            'form-0-count': new_product.count,
            'form-0-store': new_product.store_id,
            'form-1-id': '',
            'form-1-article': '',
            'form-1-name': '',
            'form-1-category': '',
            'form-1-cost': '',
            'form-1-price': '',
            'form-1-count': '',
            'form-1-store': '',
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '1',
        }
        response = self.client.post(reverse('store:index'), data)
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        self.assertEqual(Product.objects.count(), 1)
        new_product.id = self.product.id
        prod = Product.objects.first()
        self.assertEqual(str(self.product), str(prod))
