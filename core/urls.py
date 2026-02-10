"""
URL configuration for the core app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('order/', views.order, name='order'),
    path('order/success/', views.order_success, name='order_success'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
