from django.db import models
from django.contrib.auth.models import User

STATE_TYPE_CHOICES = (
    ('USED', 'Used'),
    ('NEW', 'New'),
    ('BROKEN', 'Broken'),
)

CATEGORIES_TYPE_CHOICE = (
    ('FOOD', 'Food'),
    ('TEGNOLOGY', 'Tegnology'),
    ('HOUSEHOLDS_ITEMS', 'Households_Items'),
    ('CLOTHING', 'Clothing'),
    ('HYGIENE', 'Hygiene'),
    ('GAMES', 'Games'),
    ('MATERNITY', 'Maternity'),
    ('MEDICINE', 'Medicine'),
    ('STATIONERY', 'Stationery'),
)

SUBCATEGORIES_TYPE_CHOICE = (
    ('CEREALS', 'Cereals'),
)


class Product(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    state_type = models.CharField(
        max_length=50, blank=False, choices=STATE_TYPE_CHOICES)
    categories_type = models.CharField(
        max_length=50, blank=False, choices=CATEGORIES_TYPE_CHOICE)
    subcategories_type = models.CharField(
        max_length=50, blank=False, choices=SUBCATEGORIES_TYPE_CHOICE)

    def __str__(self):
        return self.user.username
