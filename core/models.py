"""
Core models for ACADEMIQ - Contact and Order management.
Fully internationalized for English and Arabic support.
"""

from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    """Model for contact form submissions."""
    
    SERVICE_CHOICES = [
        ('general', _('General Inquiry')),
        ('thesis', _('Thesis Preparation')),
        ('review', _('Research Paper Review')),
        ('statistics', _('Statistical Analysis')),
        ('translation', _('Scientific Translation')),
        ('formatting', _('Academic Formatting')),
    ]
    
    full_name = models.CharField(max_length=100, verbose_name=_('Full Name'))
    email = models.EmailField(validators=[EmailValidator()], verbose_name=_('Email Address'))
    phone = models.CharField(
        max_length=20, 
        blank=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', _('Enter a valid phone number.'))],
        verbose_name=_('Phone Number')
    )
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    service_type = models.CharField(
        max_length=20, 
        choices=SERVICE_CHOICES,
        default='general',
        verbose_name=_('Service Type')
    )
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Submitted At'))
    is_read = models.BooleanField(default=False, verbose_name=_('Read'))
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')
    
    def __str__(self):
        return f"{self.full_name} - {self.subject}"


class OrderRequest(models.Model):
    """Model for order form submissions."""
    
    SERVICE_CHOICES = [
        ('thesis', _("Master's & PhD Thesis Preparation")),
        ('review', _('Research Paper Reviewing')),
        ('statistics', _('Statistical Analysis')),
        ('translation', _('Scientific Translation')),
        ('formatting', _('Academic Formatting')),
    ]
    
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('in_progress', _('In Progress')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ]
    
    full_name = models.CharField(max_length=100, verbose_name=_('Full Name'))
    email = models.EmailField(validators=[EmailValidator()], verbose_name=_('Email Address'))
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', _('Enter a valid phone number.'))],
        verbose_name=_('Phone Number')
    )
    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        verbose_name=_('Service Type')
    )
    message = models.TextField(verbose_name=_('Project Details / Message'))
    attachment = models.FileField(
        upload_to='order_attachments/%Y/%m/',
        blank=True,
        null=True,
        verbose_name=_('Attachment')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_('Order Status')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Submitted At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Order Request')
        verbose_name_plural = _('Order Requests')
    
    def __str__(self):
        return f"Order #{self.id} - {self.full_name} ({self.get_service_type_display()})"
    
    @property
    def order_number(self):
        return f"ACD-{self.created_at.year}-{self.id:05d}"


class Testimonial(models.Model):
    """Model for customer testimonials."""
    
    name = models.CharField(max_length=100, verbose_name=_('Customer Name'))
    title = models.CharField(max_length=200, verbose_name=_('Title / Position'))
    institution = models.CharField(max_length=200, blank=True, verbose_name=_('Institution'))
    content = models.TextField(verbose_name=_('Testimonial Content'))
    image = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True,
        verbose_name=_('Photo')
    )
    rating = models.PositiveSmallIntegerField(
        default=5,
        choices=[(i, i) for i in range(1, 6)],
        verbose_name=_('Rating (1-5)')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
    
    def __str__(self):
        return f"{self.name} - {self.rating} stars"


class Service(models.Model):
    """Model for services that can be managed via admin."""
    
    title = models.CharField(max_length=100, verbose_name=_('Service Title'))
    slug = models.SlugField(unique=True, verbose_name=_('URL Slug'))
    short_description = models.CharField(max_length=200, verbose_name=_('Short Description'))
    description = models.TextField(verbose_name=_('Full Description'))
    icon = models.CharField(
        max_length=50,
        default='fas fa-graduation-cap',
        help_text=_('Font Awesome icon class'),
        verbose_name=_('Icon Class')
    )
    price_starting_at = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Starting Price')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    display_order = models.PositiveSmallIntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
    
    def __str__(self):
        return self.title
