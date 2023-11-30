from django.contrib import admin
from django.urls import path
from .views import sayHello, index,Bookingview, MenuItemsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', sayHello,name='sayHello'),
    path('index/', index,name='index'),
    path('booking/', Bookingview.as_view(),name='booking'),
    path('menu/', MenuItemsView.as_view(),name='menu'),
    path('api-token-auth/', obtain_auth_token)

]