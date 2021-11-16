from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string
from django.conf import settings

from .models import Contact
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save()

            messages.success(request, "Great! We received your email and \
                we'll be intouch with you shortly.")
        else:
            messages.error(request, 'Oh No! We did not receive your email. Please \
                make sure the form is filled out correctly.')
            return redirect(reverse('contact', args=[contact_form.id]))

    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
