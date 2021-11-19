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
            email_context = Contact.objects.get(id=contact_form.id)

            customer_email_message = email_context.email
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'email_context': email_context})
            body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'email_context': email_context,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [customer_email_message],
                fail_silently=False,
            )
            messages.success(request, f"Great! We received your email, {email_context.name}. \
                We'll be in touch with you shortly.")
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Oh No! We did not receive your email. Please \
                make sure the form is filled out correctly.')
            return redirect(reverse('contact'))

    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
