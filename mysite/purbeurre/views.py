from django.shortcuts import render, HttpResponse
from . import views
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def test_page(request):
    return render(request, 'purbeurre/test_page.html')

def account(request):
    return render(request, 'purbeurre/account.html')

def creation_successful(request):
    return render(request, 'purbeurre/creation_successful.html')

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Votre compte a bien été enregistré.')
            return redirect('purbeurre:creation_successful')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'purbeurre/signup.html', {'form': f})

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Votre compte a bien été enregistré. Cliquez sur "se connecter" pour vous connecter.')
            return redirect('purbeurre:register')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'purbeurre/register.html', {'form': f})