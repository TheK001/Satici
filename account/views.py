from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_user(request):
    form = RegisterForm()
    context = {
        "form" : form
    }
    return render(request, "register.html", context)

def login_user(request):   
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email") 
            password = form.cleaned_data.get("password")
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.error("email ve ya sifreni dogru daxil edin")
                return redirect("login")
    else:
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request,"login.html",context)

def logout_user(request):
    logout(request)
    return redirect('login')