from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import AccountLoginForm, AccountRegisterForm
from django.db.models import Q


def user_login(request):
    form = AccountLoginForm()

    if request.user.is_authenticated and "next" in request.GET:
        return render(request,"account/login.html",{"form":form,"error":"Yetkiniz Yok!"})
    elif request.user.is_authenticated:
        return redirect("courses")

    if request.method == "POST":
        form = AccountLoginForm(request.POST)
        next_url = request.POST.get("next", None)  # POST'dan next parametresini alıyoruz
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return redirect("courses")
            return render(request,"account/login.html",{"form":form,"error":"Username or Password Incorrect"})
        
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
                return render(request,"account/register.html",{"form":form,"error":"User Account Available with Entered Username/Email"})

            if password == repassword:
                user = User.objects.create_user(username=username,email=email,password=password,is_staff=True, is_active=True, is_superuser=True)
                user.save()
            else:
                form = AccountRegisterForm(initial={"username":username,"email":email})
                return render(request,"account/register.html",{"form":form,"error":"Passwords Do Not Match"})
            return redirect("user_login")
    else:
        form = AccountRegisterForm()
    return render(request,"account/register.html",{"form":form})


def user_logout(request):
    logout(request)
    return redirect("courses")