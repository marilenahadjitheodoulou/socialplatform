from django.urls import path
from . import views
from product import views as product_views

app_name='product'
urlpatterns = [
    path('upload/', product_views.upload, name='upload'),
    path('myproducts/', product_views.UploadView.as_view(), name='myproducts'),
    path('products/', product_views.ProductView.as_view(), name='products'),
    path('load_subcategories/', product_views.load_subcategories, name='load_subcategories'),
]
