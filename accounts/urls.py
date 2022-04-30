from django.urls import path
from . import views

urlpatterns = [
   path('signin/', views.signin, name='signin'),
   path('register/', views.register, name='register'), 
   path('singout/', views.signout, name='signout'),
   path('dashboard/', views.dashboard, name='dashboard'),

]