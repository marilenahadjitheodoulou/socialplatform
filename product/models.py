from django.db import models
from django.contrib.auth.models import User

STATE_TYPE_CHOICES = (
    ('USED', 'Used'),
    ('NEW', 'New'),
    ('BROKEN', 'Broken'),
)

class ProductCategory(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="")
    slug = models.SlugField(default="")
    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, default="", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state_type = models.CharField(
        max_length=50, blank=False, default="", choices=STATE_TYPE_CHOICES)
    
    def __str__(self):
        return self.user.username

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]