from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from account.forms import AccountLoginForm


def user_login(request):
    if request.method == "POST":
        form = AccountLoginForm(request.POST)

        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("courses")
            else:
                form = AccountLoginForm(initial={"username":username})
                return render(request,"account/login.html",{"form":form,"error":"Username ya da Parola Yanlış"})
    else:
        form = AccountLoginForm()
    return render(request,"account/login.html",{"form":form})


def user_register(request):
    return render(request,"account/register.html")


def user_logout(register):
    return redirect("courses")