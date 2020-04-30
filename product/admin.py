from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Product, ProductCategory


#class ProductCategoryAdmin(admin.ModelAdmin):
#class ProductSubcategoryAdmin(admin.ModelAdmin):
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'state_type')

    class Meta:
        model = Product




admin.site.register(ProductCategory)#, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)

