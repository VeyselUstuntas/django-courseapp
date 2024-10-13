from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import AccountLoginForm, AccountRegisterForm, LoginUserForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            repassword = form.cleaned_data.get("repassword")
            if User.objects.filter(Q(username=username) | Q(email=email)).exists(): # kullanıcı varlığı sorgulama
                form = AccountRegisterForm(initial={"username":username,"email":email})
                messages.add_message(request,messages.ERROR,"User Account Available with Entered Username/Email")
                return render(request,"account/register.html",{"form":form,})

            if password == repassword:
                user = User.objects.create_user(username=username,email=email,password=password,is_staff=True, is_active=True, is_superuser=True)
                user.save()
                messages.add_message(request,messages.WARNING,"Hesap Oluşturuldu Giriş Yapabilirsiniz.")
            else:
                form = AccountRegisterForm(initial={"username":username,"email":email})
                messages.add_message(request,messages.ERROR,"Passwords Do Not Match" )
                return render(request,"account/register.html",{"form":form})
            return redirect("user_login")
    else:
        form = AccountRegisterForm()
    return render(request,"account/register.html",{"form":form})


def user_logout(request):
    logout(request)
    messages.add_message(request,messages.INFO,"Çıkış Yapıldı.")
    return redirect("courses")