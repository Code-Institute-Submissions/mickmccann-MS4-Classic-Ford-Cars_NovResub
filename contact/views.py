from django.shortcuts import render, redirect, reverse
from django.conf import settings

from .models import Contact
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
