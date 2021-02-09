from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('/about',views.about,name='about'),
    path('/contact',views.contact1,name='contact'),
    path('/tracker',views.tracker,name='tracker'),
    path('/search',views.search,name='search'),
    path('/products/<int:myid>',views.products,name='products'),
    path('/checkout',views.checkout,name='checkout'),
]
