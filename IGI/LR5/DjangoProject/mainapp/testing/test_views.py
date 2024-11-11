from django.test import Client, RequestFactory, TestCase
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

class AboutViewTest(TestCase):
    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class PrivacyPolicyViewTest(TestCase):
    def test_privacy_policy_view(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy_policy.html')

class RegisterViewTest(TestCase):
    def test_register_view_post_valid_form(self):
        client = Client()
        response = client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com',
            'phone_number': '+375297717940',
            'birth_date': '2000-01-01'
        })
        
        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('index'))

class OrderDetailViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.order = OrderFactory()

    def test_get_object(self):
        request = self.factory.get(reverse('order_detail', args=[self.order.id]))
        request.user = self.user

        view = OrderDetailView.as_view()
        response = view(request, pk=self.order.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['object'], self.order)

    def test_template_used(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('order_detail', args=[self.order.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')

    def test_order_detail(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('order_detail', args=[self.order.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.order)

class OrderListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.staff_user = User.objects.create_user(username='staff', password='staff', is_staff=True)
        self.order = OrderFactory(customer=self.user.username)
        self.product = ProductFactory(name='Test Product')

    def test_get_queryset(self):
        view = OrderListView()
        queryset = view.get_queryset()

        self.assertQuerysetEqual(queryset, Order.objects.all(), transform=lambda x: x)

    def test_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_list.html')
        self.assertIsInstance(response.context['form'], OrderSearchForm)
        self.assertQuerysetEqual(response.context['orders'], Order.objects.filter(customer=self.user.username), transform=lambda x: x)

    def test_get_staff_user(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_list.html')
        self.assertIsInstance(response.context['form'], OrderSearchForm)
        self.assertQuerysetEqual(response.context['orders'], Order.objects.all(), transform=lambda x: x)

    def test_post_sort(self):
        self.client.force_login(self.user)
        sort_data = {
            'search_term': '',
            'sort_by': 'customer',
            'reverse': False
        }
        response = self.client.post(reverse('orders'), data=sort_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_list.html')
        self.assertIsInstance(response.context['form'], OrderSearchForm)
        self.assertQuerysetEqual(response.context['orders'], Order.objects.order_by('customer'), transform=lambda x: x)

    def test_post_invalid_form(self):
        self.client.force_login(self.user)
        invalid_form_data = {
            'search_term': '',
            'sort_by': '',
            'reverse': False
        }
        response = self.client.post(reverse('orders'), data=invalid_form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_list.html')
        self.assertIsInstance(response.context['form'], OrderSearchForm)
        self.assertQuerysetEqual(response.context['orders'], Order.objects.filter(customer=self.user.username), transform=lambda x: x)