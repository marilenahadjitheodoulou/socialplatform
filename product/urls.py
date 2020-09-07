from django.urls import path
from . import views
from product import views as product_views

app_name='product'
urlpatterns = [
    path('upload/', product_views.upload, name='upload'),
    path('myproducts/', product_views.UploadView.as_view(), name='myproducts'),
    path('products/', product_views.ProductView.as_view(), name='products'),
    path('load_subcategories/', product_views.load_subcategories, name='load_subcategories'),
    path('interest/<str:pk>/', product_views.createInterest, name='interest'),
    path('wishlist/', product_views.wishlist, name='wishlist'),
    path('delete_interest/<str:pk>/', product_views.deleteInterest, name='delete_interest'),
    path('productdone/<str:pk>/', product_views.productdone, name='productdone'),
]
