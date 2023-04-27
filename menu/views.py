from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def register_user(request):
    pass



