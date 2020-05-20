from django.db import models
from django.contrib.auth.models import User
import os

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.user.id, "product_%s" % instance.user, filename)

STATE_TYPE_CHOICES = (
    ('USED', 'Used'),
    ('NEW', 'New'),
    ('BROKEN', 'Broken'),
)
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'productcategory'
        verbose_name_plural = 'productscategories'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    state_type = models.CharField(max_length=10, choices=STATE_TYPE_CHOICES)
    image = models.ImageField(upload_to=get_upload_path, blank=False)
    extra_image = models.ImageField(upload_to=get_upload_path, blank=True)

    def __str__(self):
        return self.title


