from django.shortcuts import render, HttpResponse
from . import views

# Create your views here.

def index(request):
    return render(request, 'index.html')

def test_page(request):
    return render(request, 'purbeurre/test_page.html')

def account(request):
    return render(request, 'purbeurre/account.html')