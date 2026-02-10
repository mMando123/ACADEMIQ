"""
Admin configuration for ACADEMIQ core models.
"""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage, OrderRequest, Testimonial, Service


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'service_type', 'created_at', 'is_read']
    list_filter = ['service_type', 'is_read', 'created_at']
    search_fields = ['full_name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, _('%(count)d message(s) marked as read.') % {'count': updated})
    mark_as_read.short_description = _("Mark selected messages as read")

    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, _('%(count)d message(s) marked as unread.') % {'count': updated})
    mark_as_unread.short_description = _("Mark selected messages as unread")

    actions = ['mark_as_read', 'mark_as_unread']


@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ['get_order_number', 'full_name', 'email', 'service_type', 'status', 'created_at']
    list_filter = ['service_type', 'status', 'created_at']
    search_fields = ['full_name', 'email', 'message', 'id']
    readonly_fields = ['get_order_number', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    list_per_page = 25

    @admin.display(description=_('Order #'), ordering='id')
    def get_order_number(self, obj):
        return obj.order_number

    fieldsets = (
        (_('Customer Information'), {
            'fields': ('full_name', 'email', 'phone')
        }),
        (_('Order Details'), {
            'fields': ('service_type', 'message', 'attachment')
        }),
        (_('Status'), {
            'fields': ('status',)
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'rating', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['name', 'title', 'content']
    list_editable = ['is_active', 'rating']
    list_per_page = 25


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price_starting_at', 'is_active', 'display_order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'short_description']
    list_editable = ['is_active', 'display_order']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25
