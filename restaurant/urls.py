from django.contrib import admin
from django.urls import path
from .views import sayHello, index

urlpatterns = [
    path('hello/', sayHello,name='sayHello'),
    path('index/', index,name='index'),
]