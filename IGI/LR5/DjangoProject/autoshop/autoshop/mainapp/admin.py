from django.contrib import admin
from .models import *

admin.site.register(Manufacturer)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale)

