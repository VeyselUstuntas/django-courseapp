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


class AccountRegisterForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={"class":"form-control"}),
        error_messages = {"required":"Kullanıcı Adı Girilmelidir"},
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        error_messages={"required": "Email Girilmelidir", "invalid": "Geçerli bir email adresi giriniz."},
    )


    password = forms.CharField(
        label = "Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Şifre Girilmelidir"},
    )

    repassword = forms.CharField(
        label = "Re-Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Şifre Girilmelidir"},
    )