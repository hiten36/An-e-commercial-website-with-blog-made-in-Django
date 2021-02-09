from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.index,name='home'),
    path('/about',views.about,name='about'),
    path('/contact',views.contact1,name='contact'),
    path('/blogpost/<int:myid>',views.blogpost1,name='blogpost1'),
    path('/fblog1/<int:myid>',views.blogpost2,name='blogpost1'),
    path('/fblog2/<int:myid>',views.blogpost3,name='blogpost1'),
    path('/search',views.search,name='search'),
    path('/signin',views.handlesignin,name='signin'),
    path('/login',views.handlelogin,name='login'),
    path('/logout',views.handlelogout,name='logout')
]
