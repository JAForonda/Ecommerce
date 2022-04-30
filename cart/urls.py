from django.urls import path
from .views import cartView, addQ, decQ, delete
urlpatterns = [
    path('store/cart/', cartView, name = 'cart'),
    path('store/cart/add/<int:pk>', addQ, name='add-1'),
    path('store/cart/dec/<int:pk>', decQ, name='dec-1'),
    path('store/cart/delete/<int:pk>', delete, name='del'),
]