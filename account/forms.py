from django.contrib import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


# Oluşturulan Kullanıcı giriş ve kayıt formları
class AccountLoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={"class":"form-control"}),
        error_messages = {"required":"User Name must be entered"},
    )

    password = forms.CharField(
        label = "Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}) ,
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


class AuthenticationPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label="Old Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Enter Your Old Password"}
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Enter your new password"}
    )
    new_password2 = forms.CharField(
        label="New Password Again",
        widget= forms.PasswordInput(attrs={"class":"form-control"}),
        error_messages={"required":"Re-enter your new password"}
    )
    def __init__(self,user,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.user = user
    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Your old password was entered incorrectly.")
        return old_password
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two new password fields didn't match.")
        return cleaned_data
    def save(self):
        new_password = self.cleaned_data["new_password1"]
        self.user.set_password(new_password)
        self.user.save()


# Django tarafından hazır olarak sunulan kayıt, giriş ve sıfırlama form sınıfları
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


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["old_password"] = forms.CharField(
            label="Old Password",
            widget= forms.PasswordInput(attrs={"class":"form-control"}),
            error_messages={"required":"Enter Your Old Password"}
        )

        self.fields["new_password1"] = forms.CharField(
            label="New Password",
            widget= forms.PasswordInput(attrs={"class":"form-control"}),
            error_messages={"required":"Enter your new password"}
        )

        self.fields["new_password2"] = forms.CharField(
            label="New Password Again",
            widget= forms.PasswordInput(attrs={"class":"form-control"}),
            error_messages={"required":"Re-enter your new password"}
        )
