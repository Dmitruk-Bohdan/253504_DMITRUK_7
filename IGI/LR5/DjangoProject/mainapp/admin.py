from django.contrib import admin
from .models import *


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number']
    list_filter = ['name', 'address', 'phone_number']

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['code']
    list_filter = ['code']

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    list_filter = ['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    list_filter = ['name']

class SupplierInline(admin.StackedInline):
    model = Supplier.products.through
    extra = 0
    verbose_name = 'Supplier'
    verbose_name_plural = 'Suppliers'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'article_number',
                    'description',
                    'price_per_unit',
                    'category',
                    'display_suppliers',
                    'display_pickup_points',
                    'count'
                    ]
    inlines = [SupplierInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'quantity', 'product', 'customer', 'pickup_point']
    list_filter = ['date', 'quantity']