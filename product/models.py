from django.db import models
from django.contrib.auth.models import User

STATE_TYPE_CHOICES = (
    ('USED', 'Used'),
    ('NEW', 'New'),
    ('BROKEN', 'Broken'),
)
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'products categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    state_type = models.CharField(max_length=10, choices=STATE_TYPE_CHOICES)
    #image = models.ImageField(upload_to='media/', default="")

    def __str__(self):
        return self.title


