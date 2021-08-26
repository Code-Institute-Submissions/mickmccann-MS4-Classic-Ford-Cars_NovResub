from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to return the cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Sends a car to the cart """

    car = request.POST.get('car')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = car

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
