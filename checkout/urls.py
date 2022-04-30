from django.urls import path
from . import views

urlpatterns = [
   path('store/cart/place-order/', views.placeOrder, name='place-order'),
   path('store/cart/place-order/final/', views.final, name='final/'),
]