"""Test ProductResource functionality."""

from django.core.urlresolvers import reverse
from django.test import TestCase

from tastypie import http

from ...autofixtures import ProductAutoFixture
from ...models import Product


class ProductListTestCase(TestCase):
    """Product List resource."""

    @classmethod
    def setUpTestData(cls):  # NOQA
        """Initialize Product for Product Resource."""
        cls.fullProduct = ProductAutoFixture(
            model=Product, generate_fk=True, field_values={'article': 'testArticle', 'name': 'testName'},
        ).create_one()
        cls.articleProduct = ProductAutoFixture(
            model=Product, generate_fk=True, field_values={'article': 'testArticle'},
        ).create_one()
        cls.nameProduct = ProductAutoFixture(
            model=Product, generate_fk=True, field_values={'name': 'testName'},
        ).create_one()
        cls.fakeArticleProduct = ProductAutoFixture(
            model=Product, generate_fk=True, field_values={'article': 'fakeArticle'},
        ).create_one()
        cls.fakeNameProduct = ProductAutoFixture(
            model=Product, generate_fk=True, field_values={'name': 'fakeName'},
        ).create_one()

        cls.url = reverse('api_dispatch_list', kwargs={'resource_name': 'product', 'api_name': 'store_v1'})

    def test_list(self):
        """Complete list of products."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 5)

    def test_full_article(self):
        """List of products by full article."""
        response = self.client.get(self.url, data={'query': 'testArticle'})
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 2)
        self.assertIn(objects[0]['id'], (self.fullProduct.id, self.articleProduct.id))
        self.assertIn(objects[1]['id'], (self.fullProduct.id, self.articleProduct.id))

    def test_full_name(self):
        """List of products by full name."""
        response = self.client.get(self.url, data={'query': 'testName'})
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 2)
        self.assertIn(objects[0]['id'], (self.fullProduct.id, self.nameProduct.id))
        self.assertIn(objects[1]['id'], (self.fullProduct.id, self.nameProduct.id))

    def test_partial_article(self):
        """List of products by partial article."""
        response = self.client.get(self.url, data={'query': 'Article'})
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 3)
        self.assertIn(objects[0]['id'], (self.fullProduct.id, self.articleProduct.id, self.fakeArticleProduct.id))
        self.assertIn(objects[1]['id'], (self.fullProduct.id, self.articleProduct.id, self.fakeArticleProduct.id))
        self.assertIn(objects[2]['id'], (self.fullProduct.id, self.articleProduct.id, self.fakeArticleProduct.id))

    def test_partial_name(self):
        """List of products by partial name."""
        response = self.client.get(self.url, data={'query': 'Name'})
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 3)
        self.assertIn(objects[0]['id'], (self.fullProduct.id, self.nameProduct.id, self.fakeNameProduct.id))
        self.assertIn(objects[1]['id'], (self.fullProduct.id, self.nameProduct.id, self.fakeNameProduct.id))
        self.assertIn(objects[2]['id'], (self.fullProduct.id, self.nameProduct.id, self.fakeNameProduct.id))

    def test_partial_fake(self):
        """List of products by partial fake."""
        response = self.client.get(self.url, data={'query': 'fake'})
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 2)
        self.assertIn(objects[0]['id'], (self.fakeArticleProduct.id, self.fakeNameProduct.id))
        self.assertIn(objects[1]['id'], (self.fakeArticleProduct.id, self.fakeNameProduct.id))

    def test_no_matches(self):
        """List of products with no matches."""
        response = self.client.get(self.url, data={'query': 'unknown'})
        self.assertEqual(response.status_code, http.HttpResponse.status_code)
        objects = response.json()['objects']
        self.assertEqual(len(objects), 0)
