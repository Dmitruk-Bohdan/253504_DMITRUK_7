from django.test import TestCase
from django.urls import reverse, resolve
from mainapp import views

class UrlsTestCase(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_about_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about)

    def test_privacy_policy_url(self):
        url = reverse('privacy_policy')
        self.assertEqual(resolve(url).func, views.index)

    def test_products_url(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func.view_class, views.ProductsListView)

    def test_categories_url(self):
        url = reverse('categories')
        self.assertEqual(resolve(url).func.view_class, views.CategoryListView)

    def test_orders_url(self):
        url = reverse('orders')
        self.assertEqual(resolve(url).func.view_class, views.OrderListView)

    def test_pickup_points_url(self):
        url = reverse('pickup_points')
        self.assertEqual(resolve(url).func.view_class, views.PickupPointListView)

    def test_promocodes_url(self):
        url = reverse('promocodes')
        self.assertEqual(resolve(url).func.view_class, views.PromoCodeListView)

    def test_manufacturers_url(self):
        url = reverse('manufacturers')
        self.assertEqual(resolve(url).func.view_class, views.ManufacturerListView)

    def test_suppliers_url(self):
        url = reverse('suppliers')
        self.assertEqual(resolve(url).func.view_class, views.SupplierListView)

    def test_faqs_url(self):
        url = reverse('faqs')
        self.assertEqual(resolve(url).func.view_class, views.FAQListView)

    def test_news_articles_url(self):
        url = reverse('news_articles')
        self.assertEqual(resolve(url).func.view_class, views.NewsArticleListView)

    def test_reviews_url(self):
        url = reverse('reviews')
        self.assertEqual(resolve(url).func.view_class, views.ReviewListView)

    def test_vacancies_url(self):
        url = reverse('vacancies')
        self.assertEqual(resolve(url).func.view_class, views.VacancyListView)

    def test_employees_url(self):
        url = reverse('employees')
        self.assertEqual(resolve(url).func.view_class, views.EmployeeListView)

    def test_about_us_url(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func.view_class, views.AboutArticleListView)

    def test_product_detail_url(self):
        url = reverse('product_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.ProductDetailView)

    def test_category_detail_url(self):
        url = reverse('category_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.CategoryDetailView)

    def test_order_detail_url(self):
        url = reverse('order_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.OrderDetailView)

    def test_promocode_detail_url(self):
        url = reverse('promocode_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.PromoCodeDetailView)

    def test_pickup_point_detail_url(self):
        url = reverse('pickup_point_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.PickupPointDetailView)

    def test_manufacturer_detail_url(self):
        url = reverse('manufacturer_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.ManufacturerDetailView)

    def test_faq_detail_url(self):
        url = reverse('faq_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.FAQDetailView)

    def test_news_article_detail_url(self):
        url = reverse('news_article_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.NewsArticleDetailView)

    def test_review_detail_url(self):
        url = reverse('review_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.ReviewDetailView)

    def test_vacancy_detail_url(self):
        url = reverse('vacancy_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.VacancyDetailView)

    def test_about_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register_view)

    def test_supplier_detail_url(self):
        url = reverse('supplier_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.SupplierDetailView)

    def test_order_create_url(self):
        url = reverse('order_create', kwargs={'product_id': 1})
        self.assertEqual(resolve(url).func.view_class, views.OrderCreateView)

    def test_pickup_point_create_url(self):
        url = reverse('pickup_point_create')
        self.assertEqual(resolve(url).func.view_class, views.PickupPointCreateView)

    def test_pickup_point_update_url(self):
        url = reverse('pickup_point_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.PickupPointUpdateView)

    def test_pickup_point_delete_url(self):
        url = reverse('pickup_point_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, views.PickupPointDeleteView)

    def test_review_create_url(self):
        url = reverse('review_create')
        self.assertEqual(resolve(url).func.view_class, views.ReviewCreateView)

    def test_redirect_to_previous_url(self):
        url = reverse('redirect_to_previous')
        self.assertEqual(resolve(url).func, views.redirect_to_previous)
