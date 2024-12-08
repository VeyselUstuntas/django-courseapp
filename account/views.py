from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User
from account.forms import AccountLoginForm, AccountRegisterForm, AuthenticationPasswordChangeForm, ChangePasswordForm, LoginUserForm, RegisterUserForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    # form = AccountLoginForm()
    form = LoginUserForm()
    if request.user.is_authenticated and "next" in request.GET:
        messages.add_message(request, messages.ERROR, "Yetkiniz Yok!!!")
        return render(request,"account/login.html",{"form":form})
    elif request.user.is_authenticated and request.method == "GET":
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


def change_password(request):
    if request.method == "POST":
        # form = AuthenticationPasswordChangeForm(user = request.user, data = request.POST) # kenmdi yazdığım form 
        form = ChangePasswordForm(user=request.user, data=request.POST) #djangonun kendi formu
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.add_message(request,messages.SUCCESS,"Şifre Değişikliği Başarılı")
            return redirect("change_password")
        else:
            return render(request, "account/change-password.html",{"form":form})
    form = ChangePasswordForm(user=request.user)
    # form = AuthenticationPasswordChangeForm(user=request.user)
    return render(request, "account/change-password.html",{"form":form})

def user_logout(request):
    logout(request)
    messages.add_message(request,messages.INFO,"Çıkış Yapıldı.")
    return redirect("courses")