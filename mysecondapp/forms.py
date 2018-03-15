from django import forms
from mysecondapp.models import User
from django.core import validators
from django.forms import Widget
class Details(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"


