from django import forms

class AccountLoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={"class":"form-control"}),
        error_messages = {"required":"User Name must be entered"},
    )

    password = forms.CharField(
        label = "Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Password must be entered"},
    )


class AccountRegisterForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={"class":"form-control"}),
        error_messages = {"required":"User Name must be entered"},
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        error_messages={"required": "Email must be entered", "invalid": "Enter a valid email address."},
    )


    password = forms.CharField(
        label = "Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Password must be entered"},
    )

    repassword = forms.CharField(
        label = "Re-Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Password must be entered"},
    )