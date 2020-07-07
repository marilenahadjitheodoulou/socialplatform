from django.contrib import admin
from .models import Product, ProductCategory, Subcategory, ProductInterest

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

class ProductInterestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'title', 'status', 'date_created')

    class Meta:
        model = ProductInterest

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ProductInterest, ProductInterestAdmin)
admin.site.register(Product, ProductAdmin)
