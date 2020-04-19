from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from userprofiles import views as userprofiles_views
from templates import registration

urlpatterns = [
    path('', userprofiles_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),  
    path('oauth/', include('social_django.urls', namespace='social')),  
    path('register/', userprofiles_views.register, name='register'),
    path('profile/', userprofiles_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout')   
  #  path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change-password'),

]

