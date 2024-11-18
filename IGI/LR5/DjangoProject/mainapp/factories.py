import factory
from factory.django import DjangoModelFactory
from .models import *

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    title = factory.Faker('sentence', nb_words=3)
    rating = factory.Faker('random_int', min=1, max=5)
    text = factory.Faker('text')

class AboutArticleFactory(DjangoModelFactory):
    class Meta:
        model = AboutArticle

    title = factory.Faker('sentence', nb_words=3)
    text = factory.Faker('text')
    photo = factory.django.ImageField()

class NewsArticleFactory(DjangoModelFactory):
    class Meta:
        model = NewsArticle

    title = factory.Faker('sentence', nb_words=3)
    text = factory.Faker('text')
    photo = factory.django.ImageField()

    @factory.post_generation
    def created_at(self, create, extracted, **kwargs):
        if not create:
            return

        self.created_at = factory.Faker('date_time_this_year')

class FAQFactory(DjangoModelFactory):
    class Meta:
        model = FAQ

    title = factory.Faker('sentence', nb_words=3)
    text = factory.Faker('text')
    question = factory.Faker('sentence', nb_words=5)
    photo = factory.django.ImageField()

class VacancyFactory(DjangoModelFactory):
    class Meta:
        model = Vacancy

    title = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('text')
    requirements = factory.Faker('text')
    responsibilities = factory.Faker('text')
    location = factory.Faker('city')
    salary = factory.Faker('pydecimal', left_digits=4, right_digits=2, min_value=500, max_value=10000)

    @factory.post_generation
    def created_at(self, create, extracted, **kwargs):
        if not create:
            return

        self.created_at = factory.Faker('date_time_this_year')

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')

    @factory.post_generation
    def profile(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            ProfileFactory(user=self, **extracted)
        else:
            ProfileFactory(user=self)

class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    birth_date = factory.Faker('date_of_birth')
    phone_number = factory.Faker('phone_number')
    photo = factory.django.ImageField()
    job_description = factory.Faker('text')
    non_secretive = factory.Faker('boolean')

    @classmethod
    def create(cls, **kwargs):
        user = kwargs.pop('user', None)
        profile = super().create(**kwargs)
        if user:
            user.profile = profile
            user.save()
        return profile
    
class PromoCodeFactory(DjangoModelFactory):
    class Meta:
        model = PromoCode

    code = factory.Faker('bothify', text='????-####')
    discount = factory.Faker('pydecimal', left_digits=2, right_digits=2, min_value=0, max_value=100)
    expiration_date = factory.LazyFunction(lambda: datetime.now().date() + timedelta(days=30))
    max_usage = factory.Faker('random_int', min=1, max=10)
    used_count = factory.Faker('random_int', min=0, max=2)

    @classmethod
    def create(cls, **kwargs):
        promo_code = super().create(**kwargs)
        return promo_code
    
class PickupPointFactory(DjangoModelFactory):
    class Meta:
        model = PickupPoint

    name = factory.Faker('company')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')

    @classmethod
    def create(cls, **kwargs):
        pickup_point = super().create(**kwargs)
        return pickup_point
    
class ManufacturerFactory(DjangoModelFactory):
    class Meta:
        model = Manufacturer

    name = factory.Faker('company')
    address = factory.Faker('address')
    phone = factory.Faker('phone_number')

    @classmethod
    def create(cls, **kwargs):
        manufacturer = super().create(**kwargs)
        return manufacturer
    
class SupplierFactory(DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker('company')
    address = factory.Faker('address')
    phone = factory.Faker('phone_number')

    @factory.post_generation
    def manufacturers(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for manufacturer in extracted:
                self.manufacturers.add(manufacturer)
        else:
            manufacturers = ManufacturerFactory.create_batch(3)
            for manufacturer in manufacturers:
                self.manufacturers.add(manufacturer)

    @classmethod
    def create(cls, **kwargs):
        supplier = super().create(**kwargs)
        return supplier
    
class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=200)

    @classmethod
    def create(cls, **kwargs):
        category = super().create(**kwargs)
        return category

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    article_number = factory.Faker('ean13')
    description = factory.Faker('text', max_nb_chars=100)
    price_per_unit = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)
    manufacturer = factory.SubFactory(ManufacturerFactory)

    @factory.post_generation
    def suppliers(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for supplier in extracted:
                self.suppliers.add(supplier)
        else:
            suppliers = SupplierFactory.create_batch(2)
            for supplier in suppliers:
                self.suppliers.add(supplier)

    @factory.post_generation
    def pickup_points(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for pickup_point in extracted:
                self.pickup_points.add(pickup_point)

    @classmethod
    def create(cls, **kwargs):
        product = super().create(**kwargs)
        return product
    
class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    date = factory.Faker('date')
    quantity = factory.Faker('pyint', min_value=1, max_value=100)
    product = factory.SubFactory(ProductFactory)
    customer = factory.Faker('name')
    pickup_point = factory.SubFactory(PickupPointFactory)

    @classmethod
    def create(cls, **kwargs):
        order = super().create(**kwargs)
        return order

