from django.urls import path
from . import views
from userprofiles import views as userprofiles_views

app_name='userprofiles'
urlpatterns = [
    path('', userprofiles_views.home, name='home'),
    path('register/', userprofiles_views.register, name='register'),
    path('profile/', userprofiles_views.ProfileView.as_view(), name='profile'),
    path('user_profile/<str:pk>/', userprofiles_views.user_profile, name='user_profile'),
    path('edit_profile/', userprofiles_views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('create_profile/', userprofiles_views.ProfileCreateView.as_view(), name='create_profile'),
    path('ngodetails/', userprofiles_views.ngodetails, name='ngodetails'),
    path('allngo/', userprofiles_views.allngo, name='allngo'),
]