from django.test import TestCase
import datetime
from django.urls import reverse, resolve
from mainapp.views import *
from mainapp.models import *
from mainapp.factories import *


class GetMedianTestCase(TestCase):
    def test_get_median_odd_number_of_sales(self):
        sales = [1, 2, 3, 4, 5]
        expected_median = 3

        result = get_median(sales)

        self.assertEqual(result, expected_median)

class GetModeTestCase(TestCase):
    def test_get_mode(self):
        sales = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        expected_mode = 4

        result = get_mode(sales)

        self.assertEqual(result, expected_mode)

    def test_get_mode_empty_sales(self):
        sales = []
        expected_mode = None

        result = get_mode(sales)

        self.assertEqual(result, expected_mode)

class GetMostPopularProductTest(TestCase):
    def test_get_most_popular_product(self):
        
        product1 = ProductFactory(name='Product 1')
        product2 = ProductFactory(name='Product 2')
        product3 = ProductFactory(name='Product 3')

        
        order1 = OrderFactory(product=product1)
        order2 = OrderFactory(product=product2)
        order3 = OrderFactory(product=product2)
        order4 = OrderFactory(product=product3)
        order5 = OrderFactory(product=product3)
        order6 = OrderFactory(product=product3)

        
        result = get_most_popular_product([order1, order2, order3, order4, order5, order6])
        self.assertEqual(result, 'Product 3')

class GetMostProfitableProductTest(TestCase):
    def test_get_most_profitable_product(self):
        product1 = ProductFactory(name='Product 1', price_per_unit=10.0)
        product2 = ProductFactory(name='Product 2', price_per_unit=20.0)
        product3 = ProductFactory(name='Product 3', price_per_unit=5.0)

        order1 = OrderFactory(product=product1, quantity=1)
        order2 = OrderFactory(product=product2, quantity=2)
        order3 = OrderFactory(product=product2, quantity=3)
        order4 = OrderFactory(product=product3, quantity=1)
        order5 = OrderFactory(product=product3, quantity=2)
        order6 = OrderFactory(product=product3, quantity=3)

        result = get_most_profitable_product([order1, order2, order3, order4, order5, order6])
        self.assertEqual(result, 'Product 2')