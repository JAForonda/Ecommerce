from django.shortcuts import render, redirect
from .models import CartItem, Cart
from store.models import Store
from django.db.models import F
from datetime import date
# Create your views here.
def cartView(request):
    items = []
    if request.user.is_authenticated:
        idU = request.user.username
    else:
        return redirect ('signin')
    myCarts = list(Cart.objects.filter(user_id=idU, active=True))
    if len(myCarts)==0:
        myCart = Cart()
    else:
        myCart = myCarts[-1]
    cartItems = list(CartItem.objects.filter(cart=myCart.cart_id))
    tPrice=0
    tax=0
    
    
    for i in cartItems:
        product= Store.objects.get(id=i.product)
        image = product.images
        name = product.product_name
        desc = product.description
        ItemId=product.id
        price= product.price
        sTotal=round(price*i.quantity, 2)
        tPrice=round(tPrice+sTotal, 2)
        tax=round(tPrice*0.12, 2 )
        
        item={
            'image':image,
            'name':name,
            'desc':desc,
            'id':ItemId,
            'price':price,
            'sTotal':sTotal,
            'quantity':i.quantity,
        }
        items.append(item)

    myProducts_dic={
        'items': items,
        'tPrice':tPrice,
        'tax': tax,
        'total': tax+tPrice,

    }    
    
    return render (request, 'store/cart.html', myProducts_dic)


def addQ(request, pk):
    if request.user.is_authenticated:
        idU = request.user.username
    else:
        idU = request.session._get_or_create_session_key()
    myCart = Cart.objects.get(user_id=idU, active=True)
    if CartItem.objects.filter(cart=myCart.cart_id, product=pk).exists():
        myCartItem =  CartItem.objects.filter(cart= myCart.cart_id, product=pk)
        myCartItem.update(quantity=F('quantity')+1)
    return redirect("cart")

def decQ(request, pk):
    if request.user.is_authenticated:
        idU = request.user.username
    else:
        idU = request.session._get_or_create_session_key()
    myCart = Cart.objects.get(user_id=idU, active=True)
    if CartItem.objects.filter(cart=myCart.cart_id, product=pk).exists():
        myCartItem =  CartItem.objects.filter(cart=myCart.cart_id, product=pk)
        myCartItem.update(quantity=F('quantity')-1)
    return redirect("cart")

def delete(request, pk):
    if request.user.is_authenticated:
        idU = request.user.username
    else:
        idU = request.session._get_or_create_session_key()
    myCarts = list(Cart.objects.filter(user_id=idU, active=True))
    myCart = myCarts[-1]
    if CartItem.objects.filter(cart=myCart.cart_id, product=pk).exists():
        myCartItem =  CartItem.objects.filter(cart=myCart.cart_id, product=pk)
        myCartItem.delete()
    
    if len(list(CartItem.objects.filter(cart = myCart.cart_id )))==0:
        Cart.objects.filter(cart_id= myCart.cart_id).delete()
    return redirect("store")