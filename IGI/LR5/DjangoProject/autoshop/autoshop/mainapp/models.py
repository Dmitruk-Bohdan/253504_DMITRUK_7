from django.db import models
from django.contrib.auth.models import User
from django.forms import FloatField
from django.urls import reverse

class Manufacturer(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
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

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    article_number = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name ='products')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    paginate_by = 10

    @property
    def total_price(self):
        return self.count * self.price_per_unit
    
    def display_suppliers(self):
        return ', '.join([ supplier.name for supplier in self.suppliers.all()[:3]])
    
    display_suppliers.short_description = 'Suppliers'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name, self.article_number, self.price_per_unit}'
    
    class Meta:
        ordering = ['name']
    
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    paginate_by = 10
    
class Sale(models.Model):
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    paginate_by = 10

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
    
class PickupPoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('pickup_point_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    
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