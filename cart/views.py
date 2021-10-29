from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a car to the cart. It also displays an
    error message and redirects to the homepage if a user
    tries to type the url into the browser """

    product = get_object_or_404(Product, pk=item_id)
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
    """ Remove car from the cart. It also displays
    an error message if a user tries to type
    the url into the browser """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed { product.name } from your cart')
        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
