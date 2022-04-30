from django.urls import path
from . import views

urlpatterns = [
   path ('store/searchResults/', views.Search, name = 'search'),
   path('store/<int:pk>/', views.byCategoryApp, name='by-category'),
]