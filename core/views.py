"""
Views for ACADEMIQ - All page views and form handling.
"""

import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _

from .forms import ContactForm, OrderForm
from .models import Testimonial, Service


def home(request):
    """Home page view with testimonials and services."""
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    services_list = Service.objects.filter(is_active=True)[:6]

    context = {
        'testimonials': testimonials,
        'services': services_list,
    }
    return render(request, 'home.html', context)


def about(request):
    """About Us page view."""
    return render(request, 'about.html')


def services(request):
    """Services page view."""
    all_services = Service.objects.filter(is_active=True)
    context = {
        'services': all_services,
    }
    return render(request, 'services.html', context)


def contact(request):
    """Contact page view with form handling."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Send email notification
            try:
                send_mail(
                    subject=f'New Contact Message: {contact_message.subject}',
                    message=(
                        f'New contact message received:\n\n'
                        f'Name: {contact_message.full_name}\n'
                        f'Email: {contact_message.email}\n'
                        f'Phone: {contact_message.phone or "Not provided"}\n'
                        f'Service Type: {contact_message.get_service_type_display()}\n\n'
                        f'Message:\n{contact_message.message}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, _('Thank you! Your message has been sent successfully. We will get back to you soon.'))
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


ALLOWED_UPLOAD_EXTENSIONS = {'.pdf', '.doc', '.docx', '.txt', '.zip', '.rar'}
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50 MB


def order(request):
    """Order page view with form handling and file validation."""
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            # Validate the uploaded file before saving
            attachment = request.FILES.get('attachment')
            if attachment:
                ext = os.path.splitext(attachment.name)[1].lower()
                if ext not in ALLOWED_UPLOAD_EXTENSIONS:
                    form.add_error('attachment', _('Invalid file type. Allowed: PDF, DOC, DOCX, TXT, ZIP, RAR.'))
                elif attachment.size > MAX_UPLOAD_SIZE:
                    form.add_error('attachment', _('File size exceeds the 50 MB limit.'))

            if form.errors:
                return render(request, 'order.html', {'form': form})

            order_request = form.save()

            # Send email notification
            try:
                send_mail(
                    subject=f'New Order Request #{order_request.order_number}',
                    message=(
                        f'New order received:\n\n'
                        f'Order Number: {order_request.order_number}\n'
                        f'Name: {order_request.full_name}\n'
                        f'Email: {order_request.email}\n'
                        f'Phone: {order_request.phone}\n'
                        f'Service: {order_request.get_service_type_display()}\n\n'
                        f'Project Details:\n{order_request.message}\n\n'
                        f'Attachment: {"Yes" if order_request.attachment else "No"}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, _('Thank you! Your order has been submitted successfully. We will contact you shortly.'))
            return redirect('order_success')
    else:
        form = OrderForm()

    context = {
        'form': form,
    }
    return render(request, 'order.html', context)


def privacy_policy(request):
    """Privacy Policy page view."""
    return render(request, 'privacy.html')


def contact_success(request):
    """Contact form success page."""
    return render(request, 'success.html')


def order_success(request):
    """Order form success page."""
    context = {
        'order_type': 'order',
    }
    return render(request, 'success.html', context)


def custom_404(request, exception=None):
    """Custom 404 error handler."""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error handler."""
    return render(request, '500.html', status=500)
