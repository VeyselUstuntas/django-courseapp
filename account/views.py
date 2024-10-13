from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import AccountLoginForm, AccountRegisterForm, LoginUserForm, RegisterUserForm
from django.db.models import Q
from django.contrib import messages


def user_login(request):
    # form = AccountLoginForm()
    form = LoginUserForm()
    if request.user.is_authenticated and "next" in request.GET:
        return render(request,"account/login.html",{"form":form,"error":"Yetkiniz Yok!"})
    elif request.user.is_authenticated:
        return redirect("courses")

    if request.method == "POST":
        # form = AccountLoginForm(request.POST)
        form = LoginUserForm(request,data=request.POST)
        next_url = request.POST.get("next", None)  # POST'dan next parametresini alıyoruz

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"Welcome, {request.user.username}")
                if next_url:
                    return redirect(next_url)
                return redirect("courses")
            return render(request,"account/login.html",{"form":form})
        
    return render(request,"account/login.html",{"form":form})


def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
       
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get("username")
           password = form.cleaned_data.get("password1")
           user = authenticate(request, username=username, password = password,is_active=True)
           login(request,user)
           return redirect("courses")
        else:
            return render(request, "account/register.html",{"form":form})
    else:
        form = RegisterUserForm()
        return render(request,"account/register.html",{"form":form})


def user_logout(request):
    logout(request)
    messages.add_message(request,messages.INFO,"Çıkış Yapıldı.")
    return redirect("courses")