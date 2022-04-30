from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from checkout.models import order
from cart.models import Cart, CartItem
from store.models import Store
from verify_email.email_handler import send_verification_email


from accounts.models import userProfile, account
from . import forms
# Create your views here.
def signin (request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Email or password incorrect. Also remeber to verify your email')
            
    return render(request, 'accounts/signin.html')
def register (request):
    if request.user.username != None:
        logout(request)

    form = forms.createAccount()
    
    if request.method == 'POST':
        form = forms.createAccount(request.POST)
        if form.is_valid():
            form.save() 
            inactive_user = send_verification_email(request, form) 
            yourUsername = form.cleaned_data['username']
            yourAddress = form.cleaned_data['address']
            yourCity = form.cleaned_data['city']
            yourCountry = form.cleaned_data['country']
            yourFName = form.cleaned_data['first_name']
            yourLName = form.cleaned_data['last_name']
            yourPassword = form.cleaned_data['password1']
            yourEmail = yourUsername
            yourNick = yourEmail.split('@')[0]
            if userProfile.objects.filter(userId=yourUsername).exists():
                myUser = userProfile.objects.filter(userId=yourUsername).update(userId=yourUsername, address = yourAddress, city = yourCity, country = yourCountry)
                myAccount = account.objects.filter(userId=yourUsername).update(userId= yourUsername, password = yourPassword, firstName = yourFName, lastName = yourLName, userName=yourNick, email = yourEmail)
            else:
                myUser = userProfile.objects.create(userId=yourUsername, address = yourAddress, city = yourCity, country = yourCountry)
                myAccount = account.objects.create(userId= yourUsername, password = yourPassword, firstName = yourFName, lastName = yourLName, userName=yourNick, email = yourEmail)
                myUser.save()
                myAccount.save()
            messages.success(request, 'Account created! Please verify your email before signing in or continue as guest')
            return redirect ('signin')      
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def signout (request):
    if request.user.username != None:
        logout(request)
        return redirect ('signin')
    else:
        return redirect ('signin')
def dashboard (request):
    if request.user != None:
        myOrders = list(order.objects.filter(user_id=request.user.username))
        uId= request.user.username
    else:
        return redirect('signin')
        
    if len(myOrders)==0:
        return render(request, 'accounts/dashboard.html', {'msg':'No orders found on your history'})
    else:
        myOrder = myOrders[-1]
        items = []
        myItems = list(CartItem.objects.filter(user=uId, cart=myOrder.cart))
        for i in myItems:
            product= Store.objects.get(id=i.product)
            image = product.images
            name = product.product_name
            price= product.price
            id = product.id
            item={
                'image':image,
                'name':name,
                'price':price,
                'id':id,
            }
            items.append(item)


        context = {
            'order': myOrders[-1], 
            'items' : items
        }
    return render(request, 'accounts/dashboard.html', context)
