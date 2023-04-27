from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass
