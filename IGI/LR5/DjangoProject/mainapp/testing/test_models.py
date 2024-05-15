# from datetime import date
# from ..models import *
# from django.test import TestCase

# class PickupPointTestCase(TestCase):
#     def setUp(self):
#         self.pickup_point = PickupPoint.objects.create(
#             name='Test Pickup Point',
#             address='Test Address',
#             phone_number='Test Phone Number'
#         )

#     def test_pickup_point_name(self):
#         self.assertEqual(self.pickup_point.name, 'Test Pickup Point')

#     def test_pickup_point_address(self):
#         self.assertEqual(self.pickup_point.address, 'Test Address')

#     def test_pickup_point_phone_number(self):
#         self.assertEqual(self.pickup_point.phone_number, 'Test Phone Number')

#     def test_pickup_point_absolute_url(self):
#         expected_url = f'/pickup_point/{self.pickup_point.id}/'
#         self.assertEqual(self.pickup_point.get_absolute_url(), expected_url)

#     def test_pickup_point_string_representation(self):
#         self.assertEqual(str(self.pickup_point), 'Test Pickup Point')

# class ManufacturerTestCase(TestCase):
#     def setUp(self):
#         self.manufacturer = Manufacturer.objects.create(
#             name='Test Manufacturer',
#             address='Test Address',
#             phone='Test Phone'
#         )

#     def test_manufacturer_name(self):
#         self.assertEqual(self.manufacturer.name, 'Test Manufacturer')

#     def test_manufacturer_address(self):
#         self.assertEqual(self.manufacturer.address, 'Test Address')

#     def test_manufacturer_phone(self):
#         self.assertEqual(self.manufacturer.phone, 'Test Phone')

#     def test_manufacturer_absolute_url(self):
#         expected_url = f'/manufacturer/{self.manufacturer.id}/'
#         self.assertEqual(self.manufacturer.get_absolute_url(), expected_url)

#     def test_manufacturer_string_representation(self):
#         self.assertEqual(str(self.manufacturer), 'Test Manufacturer')

# class SupplierTestCase(TestCase):
#     def setUp(self):
#         self.manufacturer = Manufacturer.objects.create(
#             name='Test Manufacturer',
#             address='Test Address',
#             phone='Test Phone'
#         )
#         self.supplier = Supplier.objects.create(
#             name='Test Supplier',
#             address='Test Address',
#             phone='Test Phone'
#         )
#         self.supplier.manufacturers.add(self.manufacturer)

#     def test_supplier_name(self):
#         self.assertEqual(self.supplier.name, 'Test Supplier')

#     def test_supplier_address(self):
#         self.assertEqual(self.supplier.address, 'Test Address')

#     def test_supplier_phone(self):
#         self.assertEqual(self.supplier.phone, 'Test Phone')

#     def test_supplier_manufacturers(self):
#         self.assertIn(self.manufacturer, self.supplier.manufacturers.all())

#     def test_supplier_absolute_url(self):
#         expected_url = f'/supplier/{self.supplier.id}/'
#         self.assertEqual(self.supplier.get_absolute_url(), expected_url)

#     def test_supplier_string_representation(self):
#         self.assertEqual(str(self.supplier), 'Test Supplier')

# class CategoryTestCase(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(
#             name='Test Category',
#             description='Test Description'
#         )

#     def test_category_name(self):
#         self.assertEqual(self.category.name, 'Test Category')

#     def test_category_description(self):
#         self.assertEqual(self.category.description, 'Test Description')

#     def test_category_absolute_url(self):
#         expected_url = f'/category/{self.category.id}/'
#         self.assertEqual(self.category.get_absolute_url(), expected_url)

#     def test_category_string_representation(self):
#         self.assertEqual(str(self.category), 'Test Category')

# class ProductTestCase(TestCase):
#     def setUp(self):
#         self.supplier = Supplier.objects.create(
#             name='Test Supplier',
#             address='Test Address',
#             phone='Test Phone'
#         )
#         self.category = Category.objects.create(
#             name='Test Category',
#             description='Test Description'
#         )
#         self.pickup_point = PickupPoint.objects.create(
#             name='Test Pickup Point',
#             address='Test Address',
#             phone_number='Test Phone Number'
#         )
#         self.manufacturer = Manufacturer.objects.create(
#             name='Test Manufacturer',
#             address='Test Address',
#             phone='Test Phone'
#         )
#         self.product = Product.objects.create(
#             name='Test Product',
#             article_number='Test Article Number',
#             description='Test Description',
#             price_per_unit=10.99,
#             category=self.category,
#             manufacturer=self.manufacturer,
#             count=10
#         )
#         self.product.suppliers.add(self.supplier)
#         self.product.pickup_points.add(self.pickup_point)

#     def test_product_name(self):
#         self.assertEqual(self.product.name, 'Test Product')

#     def test_product_article_number(self):
#         self.assertEqual(self.product.article_number, 'Test Article Number')

#     def test_product_description(self):
#         self.assertEqual(self.product.description, 'Test Description')

#     def test_product_price_per_unit(self):
#         self.assertEqual(self.product.price_per_unit, 10.99)

#     def test_product_suppliers(self):
#         self.assertIn(self.supplier, self.product.suppliers.all())

#     def test_product_category(self):
#         self.assertEqual(self.product.category, self.category)

#     def test_product_pickup_points(self):
#         self.assertIn(self.pickup_point, self.product.pickup_points.all())

#     def test_product_manufacturer(self):
#         self.assertEqual(self.product.manufacturer, self.manufacturer)

#     def test_product_count(self):
#         self.assertEqual(self.product.count, 10)

#     def test_product_total_price(self):
#         expected_total_price = 10 * 10.99
#         self.assertEqual(self.product.total_price, expected_total_price)

#     def test_product_display_suppliers(self):
#         expected_display = 'Test Supplier'
#         self.assertEqual(self.product.display_suppliers(), expected_display)

#     def test_product_display_pickup_points(self):
#         expected_display = 'Test Pickup Point'
#         self.assertEqual(self.product.display_pickup_points(), expected_display)

#     def test_product_absolute_url(self):
#         expected_url = f'/product/{self.product.id}/'
#         self.assertEqual(self.product.get_absolute_url(), expected_url)

#     def test_product_string_representation(self):
#         expected_str = "('Test Product', 'Test Article Number', Decimal('10.99'))"
#         self.assertEqual(str(self.product), expected_str)

#     def test_product_meta_ordering(self):
#         self.assertEqual(Product._meta.ordering, ['name'])

# class OrderTestCase(TestCase):
#     def setUp(self):
#         self.product = Product.objects.create(
#             name='Test Product',
#             article_number='Test Article Number',
#             description='Test Description',
#             price_per_unit=10.99,
#             count=10
#         )
#         self.pickup_point = PickupPoint.objects.create(
#             name='Test Pickup Point',
#             address='Test Address',
#             phone_number='Test Phone Number'
#         )
#         self.order = Order.objects.create(
#             date='2021-01-01',
#             quantity=5,
#             product=self.product,
#             customer='Test Customer',
#             pickup_point=self.pickup_point
#         )
#         self.product.category = Category.objects.create(
#             name = 'test name',
#             description = 'test description',   
#         )

#     def test_order_date(self):
#         self.assertEqual(str(self.order.date), '2021-01-01')

#     def test_order_quantity(self):
#         self.assertEqual(self.order.quantity, 5)

#     def test_order_product(self):
#         self.assertEqual(self.order.product, self.product)

#     def test_order_customer(self):
#         self.assertEqual(self.order.customer, 'Test Customer')

#     def test_order_pickup_point(self):
#         self.assertEqual(self.order.pickup_point, self.pickup_point)

#     def test_order_absolute_url(self):
#         expected_url = f'/order/{self.order.id}/'
#         self.assertEqual(self.order.get_absolute_url(), expected_url)

#     def test_order_price_per_unit(self):
#         self.assertEqual(self.order.price_per_unit, 10.99)

#     def test_order_total_price(self):
#         expected_total_price = 5 * 10.99
#         self.assertEqual(self.order.total_price, expected_total_price)

#     def test_order_string_representation(self):
#         expected_str = 'Order: Test Product - 5 units'
#         self.assertEqual(str(self.order), expected_str)

# class PromoCodeTestCase(TestCase):
#     def setUp(self):
#         self.promo_code = PromoCode.objects.create(
#             code='TESTCODE',
#             discount=10,
#             expiration_date=datetime.now().date() + timedelta(days=30),
#             max_usage=5,
#             used_count=2
#         )

#     def test_promo_code_code(self):
#         self.assertEqual(self.promo_code.code, 'TESTCODE')

#     def test_promo_code_discount(self):
#         self.assertEqual(self.promo_code.discount, 10)

#     def test_promo_code_expiration_date(self):
#         expected_date = datetime.now().date() + timedelta(days=30)
#         self.assertEqual(self.promo_code.expiration_date, expected_date)

#     def test_promo_code_max_usage(self):
#         self.assertEqual(self.promo_code.max_usage, 5)

#     def test_promo_code_used_count(self):
#         self.assertEqual(self.promo_code.used_count, 2)

#     def test_promo_code_is_valid(self):
#         self.assertTrue(self.promo_code.is_valid())

#     def test_promo_code_string_representation(self):
#         self.assertEqual(str(self.promo_code), 'TESTCODE')

#     def test_promo_code_absolute_url(self):
#         expected_url = f'/promocode/{self.promo_code.id}/'
#         self.assertEqual(self.promo_code.get_absolute_url(), expected_url)

# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )
#         self.profile = Profile.objects.create(
#             user=self.user,
#             birth_date=date(1990, 1, 1),
#             phone_number='1234567890',
#             job_description='Test job description',
#             non_secretive=True
#         )

#     def test_profile_user(self):
#         self.assertEqual(self.profile.user, self.user)

#     def test_profile_birth_date(self):
#         self.assertEqual(self.profile.birth_date, date(1990, 1, 1))

#     def test_profile_phone_number(self):
#         self.assertEqual(self.profile.phone_number, '1234567890')

#     def test_profile_photo(self):
#         self.assertEqual(self.profile.photo.name, 'images/employees/default_employee.png')

#     def test_profile_job_description(self):
#         self.assertEqual(self.profile.job_description, 'Test job description')

#     def test_profile_non_secretive(self):
#         self.assertTrue(self.profile.non_secretive)

#     def test_profile_age(self):
#         self.assertEqual(self.profile.age, 31)

#     def test_profile_age_no_birth_date(self):
#         self.profile.birth_date = None
#         self.assertEqual(self.profile.age, 0)

# class UpdateProfileSignalTestCase(TestCase):
#     def test_update_profile_signal(self):
#         @receiver(post_save, sender=User)
#         def update_profile_signal(sender, instance, created, **kwargs):
#             if created:
#                 Profile.objects.create(user=instance)
#             instance.profile.save()

#         user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )

#         update_profile_signal(sender=User, instance=user, created=True)

#         profile = Profile.objects.get(user=user)
#         self.assertEqual(profile.user, user)

# class VacancyTestCase(TestCase):
#     def setUp(self):
#         self.vacancy = Vacancy.objects.create(
#             title='Test Vacancy',
#             description='Test Description',
#             requirements='Test Requirements',
#             responsibilities='Test Responsibilities',
#             location='Test Location',
#             salary=1000
#         )

#     def test_vacancy_title(self):
#         self.assertEqual(self.vacancy.title, 'Test Vacancy')

#     def test_vacancy_description(self):
#         self.assertEqual(self.vacancy.description, 'Test Description')

#     def test_vacancy_requirements(self):
#         self.assertEqual(self.vacancy.requirements, 'Test Requirements')

#     def test_vacancy_responsibilities(self):
#         self.assertEqual(self.vacancy.responsibilities, 'Test Responsibilities')

#     def test_vacancy_location(self):
#         self.assertEqual(self.vacancy.location, 'Test Location')

#     def test_vacancy_salary(self):
#         self.assertEqual(self.vacancy.salary, 1000)

#     def test_vacancy_created_at(self):
#         self.assertIsNotNone(self.vacancy.created_at)

#     def test_vacancy_absolute_url(self):
#         expected_url = f'/vacancy/{self.vacancy.id}/'
#         self.assertEqual(self.vacancy.get_absolute_url(), expected_url)

#     def test_vacancy_string_representation(self):
#         self.assertEqual(str(self.vacancy), 'Test Vacancy')

# class ArticleTestCase(TestCase):
#     def setUp(self):
#         self.article = Article.objects.create(
#             title='Test Article',
#             text='Test Text'
#         )

#     def test_article_title(self):
#         self.assertEqual(self.article.title, 'Test Article')

#     def test_article_text(self):
#         self.assertEqual(self.article.text, 'Test Text')

#     def test_article_created_at(self):
#         self.assertIsNotNone(self.article.created_at)

#     def test_article_string_representation(self):
#         self.assertEqual(str(self.article), 'Test Article')


# class AboutArticleTestCase(TestCase):
#     def setUp(self):
#         self.about_article = AboutArticle.objects.create(
#             title='Test About Article',
#             text='Test About Text',
#             photo='images/about_articles/test_image.png'
#         )

#     def test_about_article_title(self):
#         self.assertEqual(self.about_article.title, 'Test About Article')

#     def test_about_article_text(self):
#         self.assertEqual(self.about_article.text, 'Test About Text')

#     def test_about_article_created_at(self):
#         self.assertIsNotNone(self.about_article.created_at)

#     def test_about_article_string_representation(self):
#         self.assertEqual(str(self.about_article), 'Test About Article')

#     def test_about_article_photo(self):
#         self.assertEqual(self.about_article.photo.name, 'images/about_articles/test_image.png')

# class NewsArticleTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )
#         self.news_article = NewsArticle.objects.create(
#             title='Test News Article',
#             text='Test News Text',
#             photo='images/news_articles/test_image.png',
#             author=self.user
#         )

#     def test_news_article_title(self):
#         self.assertEqual(self.news_article.title, 'Test News Article')

#     def test_news_article_text(self):
#         self.assertEqual(self.news_article.text, 'Test News Text')

#     def test_news_article_photo(self):
#         self.assertEqual(self.news_article.photo.name, 'images/news_articles/test_image.png')

#     def test_news_article_author(self):
#         self.assertEqual(self.news_article.author, self.user)

#     def test_news_article_created_at(self):
#         self.assertIsNotNone(self.news_article.created_at)

#     def test_news_article_absolute_url(self):
#         expected_url = reverse('news_article_detail', args=[str(self.news_article.id)])
#         self.assertEqual(self.news_article.get_absolute_url(), expected_url)

# class ReviewTestCase(TestCase):
#     def setUp(self):
#         self.review = Review.objects.create(
#             title='Test Review',
#             rating=4,
#             text='Test Text'
#         )

#     def test_review_title(self):
#         self.assertEqual(self.review.title, 'Test Review')

#     def test_review_rating(self):
#         self.assertEqual(self.review.rating, 4)

#     def test_review_text(self):
#         self.assertEqual(self.review.text, 'Test Text')

#     def test_review_created_at(self):
#         self.assertIsNotNone(self.review.created_at)

#     def test_review_absolute_url(self):
#         expected_url = reverse('review_detail', args=[str(self.review.id)])
#         self.assertEqual(self.review.get_absolute_url(), expected_url)

#     def test_review_string_representation(self):
#         self.assertEqual(str(self.review), 'Test Review')
