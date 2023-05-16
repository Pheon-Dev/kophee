from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddItemForm
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

def login_user(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # Authenticate and login
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password1']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         messages.success(request, "You have successfully registered! Welcome")
    #         return redirect('home')
    # else:
    #     form = SignUpForm()
    #     return render(request, 'register.html', {'form': form})
    return render(request, 'login.html', {})

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
        # messages.error(request, 'You are not logged in')
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

def add_item(request):
    form = AddItemForm(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                a = form.save()
                messages.success(request, "Item added successfully")
                return redirect('home')
        return render(request, 'add_item.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add and item ...")
        return redirect('home')

def update_item(request, pk):
    if request.user.is_authenticated:
        current_item = Menu.objects.get(id=pk)
        form = AddItemForm(request.POST or None, request.FILES or None, instance=current_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully")
            return redirect('home')
        return render(request, 'update_item.html', {'form': form, 'current_item': current_item})
    else:
        messages.success(request, "You must be logged in to update an item ...")
        return redirect('home')

def order_item(request, pk):
    pass
    # if request.user.is_authenticated:
    #     item = Menu.objects.get(id=pk)
    #     return render(request, 'order.html', {'item':item})
    # else:
    #     messages.success(request, "You must be logged in to update an item ...")
    #     return redirect('home')
