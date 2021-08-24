from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

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
