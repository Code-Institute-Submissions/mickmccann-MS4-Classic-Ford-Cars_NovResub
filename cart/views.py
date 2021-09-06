from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a car to the cart """

    product = Product.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove car from the cart """

    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart

    return HttpResponse(status=200)  
