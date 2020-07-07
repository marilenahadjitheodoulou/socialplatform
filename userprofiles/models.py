from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse 
from django.db.models.signals import post_save
from django.conf import settings
import os

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.user.id, "detail_%s" % instance.user, filename)

class UserProfileManager(models.Manager):
    pass

USER_TYPE_CHOICES = (
    ('CIVILIAN', 'Civilian'),
    ('NGO', 'N.G.O.')
)


class UserProfile(models.Model):
    user = models.OneToOneField(
                User, 
                on_delete=models.CASCADE, 
                unique=True,
                related_name='userprofile'
        )
    location = models.CharField(max_length=30, default=None)
    number = models.IntegerField(default=None)
    user_type = models.CharField(default=None,
        max_length=50, blank=False, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('userprofiles:profile')#, kwargs={'slug':self.slug})

class Ngodetails(models.Model):
    user = models.OneToOneField(
                User, 
                on_delete=models.CASCADE, 
        )
    pdf = models.FileField(upload_to=get_upload_path, blank=False)

    def __str__(self):
        return self.user.username