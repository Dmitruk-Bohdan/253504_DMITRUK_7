from django.db import models
from django.contrib.auth.models import User
from django.forms import FloatField
from django.urls import reverse

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
<<<<<<< HEAD
    pickup_points = models.ManyToManyField(PickupPoint, related_name ='pickup_points')
=======
>>>>>>> 0acec09b6871441dca20dd0bd1a8120f30836b67
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
<<<<<<< HEAD
=======
    
class PickupPoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('pickup_point_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
>>>>>>> 0acec09b6871441dca20dd0bd1a8120f30836b67

class Order(models.Model):
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
<<<<<<< HEAD
    pickup_point = models.ManyToManyField(PickupPoint, related_name ='pickup_point')
=======
    pickup_points = models.ManyToManyField(PickupPoint, related_name ='pickup_points')
>>>>>>> 0acec09b6871441dca20dd0bd1a8120f30836b67

    paginate_by = 10

    def display_pickup_points(self):
        return ', '.join([ pickup_point.name for pickup_point in self.pickup_points.all()[:3]])
    
    display_pickup_points.short_description = 'Pickup point'

    def get_absolute_url(self):
        return reverse('sale_detail', args=[str(self.id)])

    @property
    def price_per_unit(self):
        return self.product.price_per_unit

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"Sale: {self.product.name} - {self.quantity} units"
    
    
class PromoCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    users = models.ManyToManyField(User)    

    def get_absolute_url(self):
        return reverse('promo_code_detail', args=[str(self.id)])

class Vacancy(models.Model):
    duties = models.JSONField()
    salary = FloatField()

    def get_absolute_url(self):
        return reverse('vacancy_detail', args=[str(self.id)])