from genericpath import exists
from django.shortcuts import get_object_or_404, render, redirect
from datetime import date
from cart.models import Cart, CartItem
from . import models
from django.db.models import F
from categories.models import Category
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def storeApp(request ):
    products = list(models.Store.objects.all())
  
    products_dic = {
        'products':products
    }
    return render (request, 'store/store.html', products_dic)


def productDApp (request, pk):
    
    list = models.Store.objects.get(id=pk)
    
    if models.variations.objects.filter(product=pk).exists():
        sizes = models.variations.objects.get(product=pk)
    else:
        sizes = None
    context = {'list':list,
                'size':sizes}
    return render (request, 'store/product-detail.html/', context)

def filtered (request):
    if request.method == 'POST':
        category = int(request.POST.get('category')) if request.POST.get('category')!=None else 0
        size = request.POST.get('size') if request.POST.get('size')!= None else 'N'
        min = request.POST.get('min')
        max = request.POST.get('max')
        if min > max:
            max = min
        elif max<min:
            min = max
        else:
            min = min
            max = max
        if category == 0:
            if size=='S':
                products = list(models.Store.objects.filter(price__range=(min, max), 
                    variations__small=True))
            elif size=='M':
                products = list(models.Store.objects.filter(price__range=(min, max), 
                    variations__medium=True))
            elif size=='L':
                products = list(models.Store.objects.filter(price__range=(min, max), 
                    variations__large=True)) 
            elif size=='XL':
                products = list(models.Store.objects.filter(price__range=(min, max), 
                    variations__extraL=True)) 
            else:
                products = list(models.Store.objects.filter(price__range=(min, max)))     
        else:
            if size=='S':
                products = list(models.Store.objects.filter(category_id = category, price__range=(min, max), 
                    variations__small=True))
            elif size=='M':
                products = list(models.Store.objects.filter(category_id = category, price__range=(min, max), 
                    variations__medium=True))
            elif size=='L':
                products = list(models.Store.objects.filter(category_id = category, price__range=(min, max), 
                    variations__large=True)) 
            elif size=='XL':
                products = list(models.Store.objects.filter(category_id = category, price__range=(min, max), 
                    variations__extraL=True)) 
            else:
                products = list(models.Store.objects.filter(category_id = category, price__range=(min, max)))
    
    return render(request, 'store/store.html', {'products':products, 'ItemsFound':len(products)})
def addToCart (request, pk):

    products = models.Store.objects.all()
    item = get_object_or_404(products, id=pk)
    if request.user.is_authenticated:
        myUser = request.user.username
    else:
        return redirect ('signin')
    myCarts = list(Cart.objects.filter(user_id=myUser, active=True))
    myCart = Cart()
 
    if len(myCarts)==0:
        myCart= Cart.objects.create(user_id = myUser, active=True, date_added=date.today())
        myCart.save()
    else: 
        myCart = myCarts[-1]
    myCartItem = CartItem.objects.filter(product=item.id, cart=myCart.cart_id)
    if myCartItem.exists():
        myCartItem.update(quantity=F('quantity')+1)
        
    else:
        myCartItem= CartItem.objects.create(user= myUser, product=item.id, cart = myCart.cart_id, quantity=1, is_active=True)
        myCartItem.save()
    return redirect("store")