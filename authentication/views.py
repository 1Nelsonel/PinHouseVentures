from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from base.models import User
from .forms import UserForm
from django.contrib import messages

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User registered')
            return redirect("dashboard")
        else:
            messages.error(request, 'Failed, Please Try Again.')
            
        
    return render(request, 'authentication/register.html', {'form': form})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'authentication/login.html', {"message": "Invalid credentials"})
    return render(request, "authentication/login.html")

def Logout(request):
    logout(request)
    return redirect("login")