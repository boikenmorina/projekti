from django.urls import path

from . import views

urlpatterns = [
  
    path('', views.home, name='home'),
    path('contract/', views.contract, name='contract'),
    path('about/', views.about, name='about'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('pricelist/', views.pricelist, name='pricelist'),
    path('search_services/', views.search_services, name='search_services'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]