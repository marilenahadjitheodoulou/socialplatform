from django.db import models
from django.contrib.auth.models import User


USER_TYPE_CHOICES = (
    ('CIVILIAN', 'Civilian'),
    ('NGO', 'N.G.O.')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30)
    number = models.IntegerField()
    user_type = models.CharField(
        max_length=50, blank=False, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username
