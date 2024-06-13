from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65,widget=forms.TextInput(
        attrs={"class": "form-control",
                "label": "Username",
                "placeholder": "Username...",}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
                "class": "form-control",
                "label": "Password",
                "placeholder": "Password...",
            }))

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','password1','password2']

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=65,widget=forms.TextInput(
        attrs={"class": "form-control",
                "label": "First Name",
                "placeholder": "First Name...",}))
    last_name = forms.CharField(max_length=65, widget=forms.TextInput(attrs={
                "class": "form-control",
                "label": "Last Name",
                "placeholder": "Last Name...",
            }))
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
                "class": "form-control",
                "label": "Phone Number",
                "placeholder": "Phone Number",
            }))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
                "class": "form-control",
                "label": "Address",
                "placeholder": "Address...",
            }))
    profile_picture = forms.ImageField()

    # class Meta:
    #     model = Profile
    #     fields = ['phone_number', 'address', 'profile_picture', 'bio']