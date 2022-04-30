from django.shortcuts import render, HttpResponse
from store import models

def home(request):
    products = models.Store.objects.all()
    products_dic = {
        'products':products
    }
    
    response=render (request, 'home.html', products_dic)
    response.set_cookie(key='user_id', value= 1, max_age=7)
    return response

