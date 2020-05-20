from django.contrib import admin
from .models import Product, ProductCategory, Subcategory

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    class Meta:
        model = ProductCategory

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    
    class Meta:
        model = Subcategory

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'category', 'subcategory', 'title', 'description', 'state_type', 'image', 'extra_image')
    class Meta:
        model = Product

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
