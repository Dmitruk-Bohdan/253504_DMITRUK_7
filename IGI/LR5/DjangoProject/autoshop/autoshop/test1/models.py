from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    """Типичный класс модели, производный от класса Model."""

    # Поля
    my_field_name = models.CharField(max_length=20, help_text='Введите описание поля')
    # …

    # Метаданные
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return self.my_field_name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Добавьте дополнительные поля, если необходимо

    def __str__(self):
        return self.name
    
class Sale(models.Model):
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"Sale: {self.product.name} - {self.quantity} units"
    
