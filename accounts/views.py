from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_view(request): 
    form = AuthenticationForm(request,data=request.POST or None)
    if form.is_valid(): 
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {"form": form, "title":"Login", "btn_label": "Login","username": request.user.username}
    return render(request, "accounts/login.html",context)

def register_view(request): 
    form = UserCreationForm(request.POST or None)
    if form.is_valid(): 
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request,user)
        return redirect("/")
    context = {"form": form, "title":"Register", "btn_label": "Register","username": request.user.username}
    return render(request, "accounts/auth.html",context)

def logout_view(request): 
    if(request.method == "POST"):
        logout(request)
        return redirect("/login")
    context = {"form": None, "title":"Logout", "btn_label": "Click to Confirm Logout", "description":"Are you sure you want to logout?","username": request.user.username}
    return render(request, "accounts/auth.html",context)