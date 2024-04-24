import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse

class Manufacturer(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    manufacturers = models.ManyToManyField(Manufacturer)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    article_number = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name ='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.IntegerField()

    @property
    def total_price(self):
        return self.count * self.price_per_unit

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Sale(models.Model):
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    @property
    def price_per_unit(self):
        return self.product.price_per_unit

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"Sale: {self.product.name} - {self.quantity} units"
    
    
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     class Meta:
#         # Используйте related_name для избежания конфликтов обратного доступа
#         # с полями groups и user_permissions модели User
#         # встроенной модели пользователя Django.
#         # Назовите related_name с учетом вашего проекта и логики доступа.
#         # Например, 'custom_user_groups' и 'custom_user_permissions'.
#         # Или выберите другие подходящие имена.
#         related_query_name = 'custom_user_%(class)s'

#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     def get_short_name(self):
#         return self.first_name


# class Moderator(CustomUser):
#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         self.is_staff = True
#         super().save(*args, **kwargs)


# class SuperUser(CustomUser):
#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         self.is_staff = True
#         self.is_superuser = True
#         super().save(*args, **kwargs)
