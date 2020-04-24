from django.db import models
from django.contrib.auth.models import User

STATE_TYPE_CHOICES = (
    ('USED', 'Used'),
    ('NEW', 'New'),
    ('BROKEN', 'Broken'),
)

class ProductCategory(models.Model):
    category_type = models.CharField(
        max_length=50, blank=False, default="")

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.category_type

class ProductSubcategory(models.Model):
    category = models.ForeignKey(ProductCategory, default="", on_delete=models.CASCADE)
    subcategory_type = models.CharField(
        max_length=50, blank=False, default="")
    class Meta:
        verbose_name = 'product subcategory'
        verbose_name_plural = 'product subcategories'

    def __str__(self):
        return self.subcategory_type
class Product(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, default="", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(ProductSubcategory, default="", on_delete=models.CASCADE)

    state_type = models.CharField(
        max_length=50, blank=False, default="", choices=STATE_TYPE_CHOICES)
    
    def __str__(self):
        return self.user.username
