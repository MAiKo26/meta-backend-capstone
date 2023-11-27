from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.

def sayHello(request):
    return JsonResponse({"message":"Hello, World!"})

def index(request):
    return render(request, 'index.html',{})