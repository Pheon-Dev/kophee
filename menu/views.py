from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Menu

def home(request):
    menu = Menu.objects.all()
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
        return render(request, 'home.html', {'menu': menu})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form':form})

def menu_item(request, pk):
    if request.user.is_authenticated:
        menu_item = Menu.objects.get(pk=pk)
        return render(request, 'menu_item.html', {'menu_item': menu_item})
    else:
        messages.error(request, 'You are not logged in')
        return redirect('home')

def delete_item(request, pk):
    if request.user.is_authenticated:
        delete_item = Menu.objects.get(id=pk)
        delete_item.delete()
        messages.success(request, "Item deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete an item")
        return redirect('home')
