from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        print(f"PRICE: {product.price}")
        print(f"QUANTITY: {quantity}")
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_MECHANICAL_SERVICES_THRESHOLD:
        mech_services = total * Decimal(settings.STANDARD_MECHANICAL_SERVICES_PRECENTAGE / 100)
        free_services_delta = settings.FREE_MECHANICAL_SERVICES_THRESHOLD - total
    else:
        mech_services = 0
        free_services_delta = 0

    grand_total = mech_services + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'mech_services': mech_services,
        'free_services_delta': free_services_delta,
        'free_mechanical_services_threshold': settings.FREE_MECHANICAL_SERVICES_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
