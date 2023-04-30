from rest_framework.test import APIClient
from unittest import TestCase


class TestProductsView(TestCase):
    def test_products(self):
        client = APIClient()
        response = client.get('/api/v1/products/')
        assert response.status_code == 200
