from . import models
from cart.models import CartItem, Cart
from accounts.models import account

def context (request):
    categories = models.Category.objects.all()
    
    NoI=0
    if request.user != None:
        myUser = request.user.username
  
    else:
        myUser = request.session._get_or_create_session_key()


    carts = list(Cart.objects.filter(user_id=myUser, active = True))
    if len(carts) != 0:
        myCart = carts[-1]
        cartItems = list(CartItem.objects.filter(cart=myCart.cart_id))
        if len(cartItems)==0:
            NoI = 0
        else:
            for i in cartItems:
                NoI +=1
    else:
        NoI=0
    cart_dir={
        'username': myUser,
        'NoI':NoI,
        'categories':categories,
        }
    return (cart_dir)
