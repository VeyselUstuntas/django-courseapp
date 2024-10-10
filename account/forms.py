from django import forms

class AccountLoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={"class":"form-control"}),
        error_messages = {"required":"Kullanıcı Adı Girilmelidir"},
    )

    password = forms.CharField(
        label = "Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Şifre Girilmelidir"},
    )