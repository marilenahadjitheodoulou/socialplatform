from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from userprofiles import views as userprofiles_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),  
    path('oauth/', include('social_django.urls', namespace='social')),  
    path('register/', userprofiles_views.register, name='register'),
    path('profile/', userprofiles_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userprofiles/logout.html'), name='logout')   
    
]

