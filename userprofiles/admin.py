from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Ngodetails

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'location', 'number', 'user_type')
    class Meta:
        model = UserProfile

class NgodetailsAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'pdf')
    class Meta:
        model= Ngodetails

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Ngodetails,NgodetailsAdmin)

