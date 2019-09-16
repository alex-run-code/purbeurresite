from django.shortcuts import render, HttpResponse
from . import views
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return render(request, 'index.html')

def test_page(request):
    return render(request, 'purbeurre/test_page.html')

def account(request):
    return render(request, 'purbeurre/account.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'