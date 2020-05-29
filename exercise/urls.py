from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from userprofiles import views as userprofiles_views
from templates import registration
from product import views as product_views

urlpatterns = [
    path('', userprofiles_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('register/', userprofiles_views.register, name='register'),
    path('profile/', userprofiles_views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', userprofiles_views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('create_profile/', userprofiles_views.ProfileCreateView.as_view(), name='create_profile'),
    path('ngodetails/', userprofiles_views.ngodetails, name='ngodetails'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('upload/', product_views.upload, name='upload'),
    path('myproducts/', product_views.UploadView.as_view(), name='myproducts'),
    path('products/', product_views.ProductView.as_view(), name='products'),
    path('load_subcategories/', product_views.load_subcategories, name='load_subcategories')
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
