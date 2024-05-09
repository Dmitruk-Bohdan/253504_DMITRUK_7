from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth.models import User
from django.forms import FloatField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class PickupPoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('pickup_point_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('manufacturer_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    manufacturers = models.ManyToManyField(Manufacturer)
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('supplier_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="category description", max_length=200)
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    article_number = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name ='products')
    category = models.ForeignKey(Category, related_name ='products', on_delete=models.DO_NOTHING)
    pickup_points = models.ManyToManyField(PickupPoint, related_name ='pickup_points')
    # manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.DO_NOTHING, null=True)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField()
    paginate_by = 10

    @property
    def total_price(self):
        return self.count * self.price_per_unit
    
    def display_suppliers(self):
        return ', '.join([ supplier.name for supplier in self.suppliers.all()[:3]])
    
    display_suppliers.short_description = 'Suppliers'

    def display_pickup_points(self):
        return ', '.join([ pickup_point.name for pickup_point in self.pickup_points.all()[:3]])
    
    display_pickup_points.short_description = 'Pickup points'

    def get_absolute_url(self):

        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name, self.article_number, self.price_per_unit}'
    
    class Meta:
        ordering = ['name']
    

class Order(models.Model):
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    customer = models.CharField(max_length=100)
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.DO_NOTHING, default=None)


    paginate_by = 10

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

    @property
    def price_per_unit(self):
        return self.product.price_per_unit

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"Order: {self.product.name} - {self.quantity} units"
    
    
class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    expiration_date = models.DateField(default=datetime.now() + timedelta(days=30))
    max_usage = models.PositiveIntegerField(default=3)
    used_count = models.PositiveIntegerField(default=0)

    def is_valid(self):
        return self.used_count < self.max_usage and self.expiration_date >= datetime.now().date()

    def __str__(self):
        return self.code   

    def get_absolute_url(self):
        return reverse('promocode_detail', args=[str(self.id)])

class Vacancy(models.Model):
    duties = models.JSONField()
    salary = FloatField()

    def get_absolute_url(self):
        return reverse('vacancy_detail', args=[str(self.id)])
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    def get_age(self):
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        else:
            return None
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
