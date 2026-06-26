from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurants'),
    path('chefs/', views.chef_list, name='chefs'),
    path('book-table/', views.book_table, name='book_table'),
    path('book-chef/<int:chef_id>/', views.book_chef, name='book_chef'),
    path('success/', views.booking_success, name='booking_success'),
    path('staff-login/', views.staff_login, name='staff_login'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]
