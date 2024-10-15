from django.contrib import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


###--- LOGIN
## kendi oluşturduğum form class'ı
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


# djangoda hazır olarak gelen auth class'ı
class LoginUserForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields["username"] = forms.CharField(
            label = "Username",
            widget = forms.TextInput(attrs={"class":"form-control"}),
            error_messages = {"required":"User Name must be entered"},
        )

        self.fields["password"] = forms.CharField(
            label = "Password",
            widget= forms.PasswordInput(attrs={"class":"form-control"}),
            error_messages={"required":"Password must be entered"},
        )

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.add_message(self.request, messages.SUCCESS, "HOŞGELDİN ADMİN")
        return username
    
    def confirm_login_allowed(self, user):
        if user.username.startswith("v"):
            raise forms.ValidationError("Bu kullanıcı adi ile login olamazsınız")
    


###--- REGISTER
## kendi oluşturduğum form class'ı
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


#dJANGODA HAZIR OLARAK GELEN auth Class'ı

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email",)
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields["username"] = forms.CharField(
            label = "Username",
            widget = forms.TextInput(attrs={"class":"form-control"}),
            error_messages = {"required":"User Name must be entered"},
        )

        self.fields["email"] = forms.EmailField(
            label="Email",
            widget=forms.EmailInput(attrs={"class": "form-control"}),
            error_messages={"required": "Email must be entered", "invalid": "Enter a valid email address."},
        )


        self.fields["password1"] = forms.CharField(
            label = "Password",
            widget= forms.PasswordInput(attrs={"class":"form-control"}),
            error_messages={"required":"Password must be entered"},
        )

        self.fields["password2"] = forms.CharField(
            label = "Re-Password",
            widget= forms.PasswordInput(attrs={"class":"form-control"}),
            error_messages={"required":"Password must be entered"},
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error("email","Email Daha Önceden Kullanılmıştır")
        return email

