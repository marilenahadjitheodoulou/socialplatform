from django.contrib import admin
from .models import Product, ProductCategory

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        model = ProductCategory
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'category', 'title', 'description', 'state_type')
    class Meta:
        model = Product

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
