from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

admin.site.register(Profile)

class SupplierInline(admin.StackedInline):
    model = Supplier.products.through
    extra = 0
    verbose_name = 'Supplier'
    verbose_name_plural = 'Suppliers'
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    
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
                    'manufacturer',
                    'count',
                    ]
    inlines = [SupplierInline]
    
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'quantity', 'product', 'customer', 'pickup_point']
    list_filter = ['date', 'quantity']
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['title', 'question', 'text', 'created_at', 'photo']
    list_filter = ['title', 'created_at']
    
@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at', 'photo']
    list_filter = ['title', 'created_at']
    
@admin.register(AboutArticle)
class AboutArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at', 'photo']
    list_filter = ['title', 'created_at']
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'text', 'date']
    list_filter = ['name', 'rating']
    
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'requirements',
                    'responsibilities', 'location', 'salary', 'created_at']
    list_filter = ['title', 'salary', 'created_at']