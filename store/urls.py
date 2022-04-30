from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.storeApp, name ='store'),
    path('store/filter', views.filtered, name='filter'),
    path('store/product_detail/<int:pk>', views.productDApp, name='product-detail'),
    path('store/addToCart/<int:pk>', views.addToCart, name = 'add'),
]