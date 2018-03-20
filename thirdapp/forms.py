from django import forms
from thirdapp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password','email']

class UserProfile(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=['profile_site','profile_pic']

class Login(forms.Form):
    username=forms.CharField(max_length=100,required=True)
    password=forms.CharField(widget=forms.PasswordInput())

