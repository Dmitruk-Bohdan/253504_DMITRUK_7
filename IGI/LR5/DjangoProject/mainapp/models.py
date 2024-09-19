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
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default= 9.99)
    suppliers = models.ManyToManyField(Supplier, related_name ='products')
    image = models.ImageField(upload_to='images/products/', default='images/products/default.png')
    category = models.ForeignKey(Category, related_name ='products', on_delete=models.DO_NOTHING)
    pickup_points = models.ManyToManyField(PickupPoint, related_name ='products')
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default=5)
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
    
class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart',on_delete=models.CASCADE)

    @property
    def total_items(self):
        return self.orders.count()

    @property
    def total_price(self):
        return sum(order.total_price for order in self.orders.all())

    def add_order(self, order):
        if not self.orders.filter(id=order.id).exists():
            order.cart = self  # Устанавливаем связь с корзиной
            order.save()      # Сохраняем заказ

    def remove_order(self, order):
        if self.orders.filter(id=order.id).exists():
            order.cart = None  # Удаляем связь с корзиной
            order.save()      # Сохраняем заказ

    def __str__(self):
        return f"Cart of {self.user.username} with {self.total_items} items"


class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=5)
    expiration_date = models.DateField(default=datetime.now() + timedelta(days=30))

    def is_valid(self):
        return self.expiration_date >= datetime.now().date()

    def __str__(self):
        return self.code   

    def get_absolute_url(self):
        return reverse('promocode_detail', args=[str(self.id)])
    

class Order(models.Model):
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    customer = models.CharField(max_length=100)
    cart = models.ForeignKey(Cart, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.DO_NOTHING, default=None)
    promocode = models.ForeignKey(PromoCode, on_delete=models.DO_NOTHING,  blank=True, null=True, default=None)

    paginate_by = 10

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

    @property
    def price_per_unit(self):
        return self.product.price_per_unit

    @property
    def total_price(self):
        if self.promocode:
            return self.quantity * self.price_per_unit * self.promocode.discount / 100
        else:
            return self.quantity * self.price_per_unit * 100

    def __str__(self):
        return f"Order: {self.product.name} - {self.quantity} units"
    


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='images/employees/', default='images/employees/default_employee.png')
    job_description = models.TextField(null=True)
    non_secretive = models.BooleanField(default=False)
    
    @property
    def age(self):
        if self.birth_date:
            from datetime import date
            today = date.today()
            age = today.year - self.birth_date.year
            if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
                age -= 1
            return age
        else:
            return 0
        
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Vacancy(models.Model):
    title = models.CharField(max_length=100, default='not definded')
    description = models.TextField(default='not definded')
    requirements = models.TextField(default='not definded')
    responsibilities = models.TextField(default='not definded')
    location = models.CharField(max_length=100, default='not definded')
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=500)
    image = models.ImageField(upload_to='images/vacancies/', default='images/vacancies/default.png')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def get_absolute_url(self):
        return reverse('vacancy_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=100, default='not definded')
    text = models.TextField(default='not definded')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
class AboutArticle(Article):
    photo = models.ImageField(upload_to='images/about_articles/', default='default_image.png')
    
class NewsArticle(Article):
    photo = models.ImageField(upload_to='images/news_articles/', default='default_image.png')
    
    def get_absolute_url(self):
        return reverse('news_article_detail', args=[str(self.id)])
    
class FAQ(Article):
    question = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/faq/', default='default_image.png')
    
    def get_absolute_url(self):
        return reverse('faq_detail', args=[str(self.id)])
    
class Review(models.Model):
    title = models.CharField(max_length=100, default='not definded')
    rating = models.PositiveIntegerField(default=0)
    text = models.TextField(null=True, default='not definded')
    created_at = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    
    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
     
class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/partners/', default='images/partners/default.png')
    website = models.URLField(default="https://minsk-lada.by")

    def __str__(self):
        return self.name
    
