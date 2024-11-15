from django.test import TestCase
from mainapp.models import PickupPoint
from mainapp.factories import *

class PickupPointModelTest(TestCase):
    def test_get_absolute_url(self):
        pickup_point = PickupPointFactory()

        expected_url = f'/mainapp/pickup_point/{pickup_point.id}'
        self.assertEqual(pickup_point.get_absolute_url(), expected_url)

    def test_str_representation(self):
        pickup_point = PickupPointFactory(name='Test Pickup Point')
        self.assertEqual(str(pickup_point), 'Test Pickup Point')

class ManufacturerModelTest(TestCase):
    def test_get_absolute_url(self):
        manufacturer = ManufacturerFactory()

        expected_url = f'/mainapp/manufacturer/{manufacturer.id}'
        self.assertEqual(manufacturer.get_absolute_url(), expected_url)

    def test_str_representation(self):
        manufacturer = ManufacturerFactory(name='Test Manufacturer')
        self.assertEqual(str(manufacturer), 'Test Manufacturer')

class SupplierModelTest(TestCase):
    def test_get_absolute_url(self):
        supplier = SupplierFactory()

        expected_url = f'/mainapp/supplier/{supplier.id}/'
        self.assertEqual(supplier.get_absolute_url(), expected_url)

    def test_str_representation(self):
        supplier = SupplierFactory(name='Test Supplier')
        self.assertEqual(str(supplier), 'Test Supplier')

class FAQModelTest(TestCase):
    def test_get_absolute_url(self):
        faq = FAQFactory()

        expected_url = f'/mainapp/faq/{faq.id}'
        self.assertEqual(faq.get_absolute_url(), expected_url)


class ReviewModelTest(TestCase):
    def test_get_absolute_url(self):
        review = ReviewFactory()

        expected_url = f'/mainapp/review/{review.id}'
        self.assertEqual(review.get_absolute_url(), expected_url)

    def test_str_representation(self):
        review = ReviewFactory(title='Test Review')
        self.assertEqual(str(review), 'Test Review')

class PromoCodeModelTest(TestCase):
    def test_is_valid(self):
        promo_code = PromoCodeFactory(used_count=2, max_usage=3, expiration_date=datetime.now().date() + timedelta(days=10))
        self.assertTrue(promo_code.is_valid())

        promo_code.used_count = 3
        self.assertFalse(promo_code.is_valid())

        promo_code.used_count = 2
        promo_code.max_usage = 2
        self.assertFalse(promo_code.is_valid())

        promo_code.expiration_date = datetime.now().date() - timedelta(days=10)
        self.assertFalse(promo_code.is_valid())

    def test_str_representation(self):
        promo_code = PromoCodeFactory(code='TESTCODE')
        self.assertEqual(str(promo_code), 'TESTCODE')

    def test_get_absolute_url(self):
        promo_code = PromoCodeFactory()

        expected_url = f'/mainapp/promocode/{promo_code.id}'
        self.assertEqual(promo_code.get_absolute_url(), expected_url)