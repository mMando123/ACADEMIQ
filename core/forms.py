"""
Forms for ACADEMIQ - Contact and Order forms.
Fully internationalized for bilingual support.
"""

from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage, OrderRequest


class ContactForm(forms.ModelForm):
    """Contact form for general inquiries."""
    
    phone = forms.CharField(
        max_length=20,
        required=False,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', _('Enter a valid phone number.'))],
        widget=forms.TextInput(attrs={
            'placeholder': '+1234567890',
            'class': 'form-control',
        })
    )
    
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'subject', 'service_type', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': _('Your full name'),
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': _('your.email@example.com'),
                'class': 'form-control',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': _('What is this about?'),
                'class': 'form-control',
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': _('Tell us more about your inquiry...'),
                'class': 'form-control',
                'rows': 5,
            }),
        }


class OrderForm(forms.ModelForm):
    """Order form for service requests with file upload."""
    
    phone = forms.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', _('Enter a valid phone number.'))],
        widget=forms.TextInput(attrs={
            'placeholder': '+1234567890',
            'class': 'form-control',
        })
    )
    
    class Meta:
        model = OrderRequest
        fields = ['full_name', 'email', 'phone', 'service_type', 'message', 'attachment']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': _('Your full name'),
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': _('your.email@example.com'),
                'class': 'form-control',
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': _('Describe your project requirements, deadline, and any specific details...'),
                'class': 'form-control',
                'rows': 6,
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': '.pdf,.doc,.docx,.txt,.zip,.rar',
            }),
        }
