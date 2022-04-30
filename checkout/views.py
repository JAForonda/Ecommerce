from argparse import MetavarTypeHelpFormatter
from types import CoroutineType
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import order
from cart.models import CartItem, Cart
from store.models import Store
from datetime import date
import json

# Create your views here.
def placeOrder(request):
    if request.user.is_authenticated:
        idU = request.user.username
    else:
        idU = request.session._get_or_create_session_key()

    myCarts = list(Cart.objects.filter(user_id=idU, active=True))
    myCart = myCarts[-1]
    myItems = list(CartItem.objects.filter(cart=myCart.cart_id))
    products = []
    itemInfo={}
    tax=0.12
    total=0
    
    for i in myItems:
        myItem = Store.objects.get(id=i.product)
        sTotal = i.quantity*myItem.price
        total = total+sTotal
        
        itemInfo = {
            'image':myItem.images,
            'name':myItem.product_name,
            'quantity': i.quantity,
            'sTotal':round(sTotal,2),
        }
        products.append(itemInfo)
    
    tTax = tax * total
    tTax = round(tTax, 2)
    tTotal = round(tTax + total, 2)
    myCart_dic = {
        'cart': products,
        'total':total,
        'tax':tTax,
        'tTotal':tTotal,
    }
    return render (request, 'store/place-order.html', myCart_dic)
def final (request):
    if request.user != None:
        sessionId = request.user.username
    else: 
        sessionId= request.session._get_or_create_session_key()
    myCarts = list(Cart.objects.filter(user_id=sessionId, active=True))
    myCart = myCarts[-1]
    
    Cart.objects.filter(user_id=sessionId, active=True).update(active=False)
   
    orderData = json.loads(request.body)
    myId= orderData['id']
    myPaymentId = orderData['purchase_units'][0]['payments']['captures'][0]['id']
    myFirstName = orderData['payer']['name']['given_name']
    myLastName = orderData['payer']['name']['surname']
    myEmail = orderData['payer']['email_address']
    myAddress = orderData['purchase_units'][0]['shipping']['address']['address_line_1']
    myCountry = orderData['purchase_units'][0]['shipping']['address']['country_code']
    myState = orderData['purchase_units'][0]['shipping']['address']['admin_area_1']
    myCity = orderData['purchase_units'][0]['shipping']['address']['admin_area_2']
    myTotal = orderData['purchase_units'][0]['amount']['value']
    myStatus = orderData['status']
    if myStatus=='COMPLETED':
        myIsOrdered=True
    else:
        myIsOrdered=False
    myCreatedDate = date.today()
    myUpdatedDate = date.today()

    myOrder = order.objects.create(
        id = myId,
        cart = myCart.cart_id,
        payment_id = myPaymentId,
        user_id = sessionId,
        first_name = myFirstName,
        last_name = myLastName,
        email = myEmail,
        address = myAddress,
        country = myCountry,
        state = myState,
        city = myCity,
        total = myTotal, 
        status = myStatus, 
        is_ordered = myIsOrdered,
        created_date = myCreatedDate,
        updatd_date = myUpdatedDate

    )
    myOrder.save()
