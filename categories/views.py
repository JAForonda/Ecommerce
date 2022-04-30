from django.shortcuts import render, get_object_or_404
from . import models
from store import models
from django.core.paginator import Paginator

# Create your views here.
def categoriesApp(request):
    return render (request, 'includes/navbar.html')
def byCategoryApp (request, pk):
    products = models.Store.objects.all()
    mylist = list()
    
    for p in products:
        if p.category_id == pk:
            mylist.append(p)
    return render (request, 'store/store.html', {'products':mylist})
def Search (request):
    if request.method=='POST':
        mySearch = request.POST.get('mySearch')
        products = list(models.Store.objects.filter(product_name__icontains=mySearch))
        
        return render(request, 'store/store.html', {'products':products})
    
 